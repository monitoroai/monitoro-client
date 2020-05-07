from fastapi import Depends
from fastapi.security import APIKeyHeader


X_API_KEY = APIKeyHeader(name='X-API-Key')


def build_check_authentication_header(api_key: str):
    def check_authentication_header(x_api_key: str = Depends(X_API_KEY)):
        """ takes the X-API-Key header and converts it into
            the matching user object from the database
        """

        if x_api_key == api_key:
            return True
        else:
            return False
    return check_authentication_header