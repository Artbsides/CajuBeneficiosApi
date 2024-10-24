import jwt

from fastapi import Request
from fastapi.security import HTTPBearer

from api.confs.settings import settings
from api.exceptions.errors.unauthorized_token import UnauthorizedTokenError


class Authorization(HTTPBearer):
    async def __call__(self, request: Request) -> None:
        try:
            authorization = await super().__call__(request)

            jwt.decode(
                authorization.credentials, settings.JWT_SECRET, [settings.JWT_ALGORITHM]
            )
        except Exception as exception:
            raise UnauthorizedTokenError from exception
