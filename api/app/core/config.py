from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    env: str = "dev"
    
    # JWT settings
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
