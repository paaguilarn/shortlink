from pydantic import Field, PostgresDsn

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = True

    project_name: str = "ShortLink App"
    project_prefix: str = "shortlink"
    api_v1_route: str = f"/api/v1/{project_prefix}"
    openapi_route: str = f"/api/v1/{project_prefix}/openapi.json"
    docs_url: str = f'/docs/{project_prefix}'
    redoc_url: str = f'/redoc/{project_prefix}'

    short_url_len: int = Field(8, alias="SHORT_URL_LEN")

    db_uri: PostgresDsn = Field("postgresql://postgres:@db/shortlink", alias="DB_URI")


settings = Settings()
