from typing import Annotated
from fastapi import FastAPI, Body, Depends, status
from fastapi.responses import JSONResponse
from app.workers.api.models import *
from app.db.models import Notification, User
from datetime import datetime
import mongoengine
from app.workers.api.smtp import send_mail


app = FastAPI()


@app.post("/create", status_code=status.HTTP_201_CREATED)
async def create_notif(notif_data: Annotated[NotifRequestModel, Body()]) -> NotifResponceModel:
    try:
        user = User.objects(id=notif_data.user_id)[0]
    except:
        return JSONResponse(status_code=403, content={"message": f"Oops! There is no user with this id."})

    if notif_data.key in ['new_message', 'new_post', 'new_login']:
        notif_db = Notification()
        notif_db.timestamp = datetime.utcnow()
        notif_db.is_new = True
        notif_db.user_id = notif_data.user_id
        notif_db.key = notif_data.key
        notif_db.target_id = notif_data.target_id
        notif_db.data = notif_data.data

        try:
            user.notif_list.append(notif_db)
            user.save()
        except mongoengine.errors.ValidationError as e:
            return JSONResponse(status_code=403, content={"message": f"Oops! {e.message}"})

    if notif_data.key in ['registration', 'new_login']:
        send_mail(email=user.email, message=notif_data.key)

    return NotifResponceModel()


@app.get("/list")
async def list_notif(list_params: Annotated[ListNotifRequestModel, Depends()]) -> ListNotifResponceModel:
    try:
        user = User.objects(id=list_params.user_id)[0]
    except:
        return JSONResponse(status_code=403, content={"message": f"Oops! There is no user with this id."})

    notif_list = [ob.to_mongo().to_dict() for ob in user.notif_list]
    for d in notif_list:
        d.update({'id': str(d['id'])})
    new_els = sum(1 for ob in notif_list if ob['is_new'] is True)
    responce = ListNotifResponceModel(
        success=True,
        data=NotifData(
            elements=len(notif_list),
            new=new_els,
            request=list_params,
            list=notif_list[list_params.skip:list_params.limit]
        )
    )

    return responce


@app.get("/read")
async def read_notif(read_params: Annotated[ReadNotifRequestModel, Depends()]) -> NotifResponceModel:
    try:
        user = User.objects(id=read_params.user_id)[0]
    except:
        return JSONResponse(status_code=403, content={"message": f"Oops! There is no user with this id."})

    doc = User.objects(id=read_params.user_id, notif_list__id=read_params.notification_id)
    doc.update(set__notif_list__S__is_new=False)

    return NotifResponceModel()
