from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    db_host: str="127.0.0.1"
    db_name: str = Field(validation_alias="MYSQL_DATABASE")
    db_pass: str = Field(validation_alias="MYSQL_ROOT_PASSWORD")

    secret_key: str = Field(validation_alias="SECRET_KEY")
    algorithm: str = Field(validation_alias="ALGORITHM")
    access_token_expire_minutes: int = Field(validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    model_config=SettingsConfigDict(env_file=".env")

settings=Settings()

