from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.sql_app.container import get_container
from app.sql_app.entities import RedirectLink
from app.sql_app.models import init_models
from app.sql_app.base import AsyncAbstractRedirectLinkRepo
from app.schemas import RedirectLinkPostSchema


app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_models()

@app.get("/{path}")
async def root(path: str):
    redirect_link_repo = get_container().resolve(AsyncAbstractRedirectLinkRepo)
    try:
        redirect_link = await redirect_link_repo.get(redirect_endpoint=path)
        return RedirectResponse(url=redirect_link.link)
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/")
async def create_redirect_link(data: RedirectLinkPostSchema):
    redirect_link_repo = get_container().resolve(AsyncAbstractRedirectLinkRepo)
    redirect_link = RedirectLink(link=data.link)
    redirect_link = await redirect_link_repo.create(redirect_link=redirect_link)

    return {"result": redirect_link.redirect_endpoint}

