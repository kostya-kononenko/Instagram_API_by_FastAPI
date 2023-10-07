from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Instagram API"

    DATABASE_URL: str | None = "sqlite:///./instagram_api.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
