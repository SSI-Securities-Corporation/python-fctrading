from dataclasses import dataclass

@dataclass
class Response():
    status: int = 500
    message: str = ''
    data: object = None

@dataclass
class AccessToken(object):
    accessToken: str