from typing import Union
from enum import Enum
from pydantic import BaseModel, Field


class KeyEnum(str, Enum):
    registration: str = 'registration'
    new_message: str = 'new_message'
    new_post: str = 'new_post'
    new_login: str = 'new_login'


class NotifRequestModel(BaseModel):
    user_id: str = Field(max_length=24, min_length=24)
    target_id: Union[str, None] = Field(max_length=24, min_length=24, default=None)
    key: KeyEnum
    data: Union[dict, None] = None


class NotifResponceModel(BaseModel):
    success: bool = True


class ListNotifRequestModel(BaseModel):
    user_id: str = Field(max_length=24, min_length=24)
    skip: int
    limit: int


class NotifData(BaseModel):
    elements: int
    new: int
    request: ListNotifRequestModel
    list: Union[list, None]


class ListNotifResponceModel(BaseModel):
    success: bool
    data: NotifData


class ReadNotifRequestModel(BaseModel):
    user_id: str = Field(max_length=24, min_length=24)
    notification_id: str = Field(max_length=24, min_length=24)