from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    time_zone: Optional[int] = None
    gpt_api_key: Optional[str] = None
    mail: Optional[str] = None
    post_auto_send: Optional[bool] = None
    created: Optional[datetime] = None
    parsing_stopped: Optional[bool] = None
    lang: Optional[str] = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class GetUsersWithSpecificSubscription(BaseModel):
    channel_for_parsing_id: Optional[int] = None
    subscription_id: Optional[int] = None