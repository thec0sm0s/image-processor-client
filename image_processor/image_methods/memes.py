from abc import ABC, abstractmethod

from image_processor.http import HttpImageClient


class MemesMethods(ABC):

    @property
    @abstractmethod
    def http(self) -> HttpImageClient:
        raise NotImplementedError

    async def rip_meme(self, text: str, avatar_url: str) -> bytes:
        data = await self.http.rip_meme(text, avatar_url)
        return data.read_data
