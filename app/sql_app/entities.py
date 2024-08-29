from pydantic import BaseModel, Field
from app.sql_app import services
from app.sql_app.models import RedirectLink as RedirectLinkModel

class RedirectLink(BaseModel):
    id: int | None = None
    link: str
    redirect_endpoint: str | None = None

    
    def to_model(self):
        return RedirectLinkModel(**self.dict())
    
    @classmethod
    def from_model(self, model: RedirectLinkModel):
        return RedirectLink(
            id=model.id,
            link=model.link,
            redirect_endpoint=model.redirect_endpoint
        )
