from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Config(BaseSettings):
    TABLE_NAME: str = Field(default="")
    DYNAMODB_URL: Optional[str] = Field(default=None)
