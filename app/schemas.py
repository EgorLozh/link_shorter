from pydantic import BaseModel

class RedirectLinkPostSchema(BaseModel):
    link: str