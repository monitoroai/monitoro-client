import uvicorn

from fastapi import HTTPException
from fastapi.responses import PlainTextResponse

from starlette import status

from src.core.config import Settings
from src.core.client import Client
from src.core.security import build_check_authentication_header


settings = Settings()
app = Client(settings.apache_log_file, settings.buffer_size)


@app.post("/")
def parser(authorized: bool = build_check_authentication_header(settings.api_key)):
    if authorized:
        return app.stream.readlines()
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@app.get("/health")
def health(authorized: bool = build_check_authentication_header(settings.api_key)):
    if authorized:
        return PlainTextResponse("ok")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)

