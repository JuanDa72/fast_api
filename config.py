from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    db_host: str="127.0.0.1"
    db_name: str = Field(validation_alias="MYSQL_DATABASE")
    db_pass: str = Field(validation_alias="MYSQL_ROOT_PASSWORD")

    model_config=SettingsConfigDict(env_file=".env")

settings=Settings()

