from functools import reduce
from sqlalchemy import and_, select
from app.sql_app.engine import get_session
from app.sql_app.base import AsyncAbstractRedirectLinkRepo
from app.sql_app.models import RedirectLink as RedirectLinkModel
from app.sql_app.entities import RedirectLink as RedirectLinkEnity

from sqlalchemy.ext.asyncio import AsyncSession

from app.sql_app.services import generate_redirect_link


class RedirectLinkRepo(AsyncAbstractRedirectLinkRepo):

    async def get(self, **kwargs):
        session: AsyncSession = get_session()

        query = select(RedirectLinkModel).where(
            and_(*[eval(f"RedirectLinkModel.{key} == '{value}'") for key, value in kwargs.items()]))

        response = await session.execute(query)
        result = response.first()
        if not result:
            return None
        
        return RedirectLinkEnity(id=result[0].id, link=result[0].link, redirect_endpoint=result[0].redirect_endpoint)
               
    

    async def create(self, redirect_link: RedirectLinkEnity, **kwargs):
        session = get_session()

        try_get_redirect_link = await self.get(link=redirect_link.link)
        
        if try_get_redirect_link:
            return try_get_redirect_link

        if not redirect_link.redirect_endpoint:
            redirect_link.redirect_endpoint = await generate_redirect_link()

        model_redirect_link = redirect_link.to_model()
        session.add(model_redirect_link)
        await session.commit()
        await session.refresh(model_redirect_link)

        return RedirectLinkEnity.from_model(model_redirect_link)
     