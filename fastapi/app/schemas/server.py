import datetime as dt

from app.schemas.base import BaseModel


class ServerDetail(BaseModel):
    datetime: dt.datetime = dt.datetime.utcnow()
