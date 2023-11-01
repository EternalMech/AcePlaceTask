from mongoengine import connect
import logging
import sys
from app.conf import settings
from app.db.models import User
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def connect_to_db() -> None:
    connect(host=settings.db_uri)
    logger.info('Connection to db has been initialized')


def create_test_user() -> None:
    if not User.objects():
        logger.info('No users found. Creating a test user.')
        test_user = User()
        test_user.username = 'TestUser'
        test_user.email = settings.email
        test_user.notif_list = []
        test_user.save()
        logger.info(f'User_id is {test_user.id}')