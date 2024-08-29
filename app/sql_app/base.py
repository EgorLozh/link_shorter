from abc import ABC, abstractmethod

class AsyncAbstractRedirectLinkRepo(ABC):

    @abstractmethod
    async def get(self, **kwargs):
        ...
    
    @abstractmethod
    async def create(self, **kwargs):
        ...
