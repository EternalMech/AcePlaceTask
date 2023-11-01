from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    email: str
    port: int
    db_uri: str
    smtp_host: str
    smtp_port: int
    smtp_login: str
    smtp_password: str
    smtp_email: str
    smtp_name: str


settings = Settings()
