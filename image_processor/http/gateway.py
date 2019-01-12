import asyncio
import aiohttp

from .route import Route
from .functions import ImageFunctions
from .exceptions import InvalidFormat


class HttpImageClient(ImageFunctions):

    def __init__(self, uri: str = None, loop=None):
        self.session: aiohttp.ClientSession = None
        self.loop = loop or asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=self.loop)
        Route.BASE_URL = uri or Route.BASE_URL
        self._route = Route

    def route(self, path, method: str = "POST", **params):
        return self._route(path, method, **params)

    async def request(self, route: Route, read=True, **kwargs):
        method = route.method
        url = route.url
        async with self.session.request(method, url, **kwargs) as response:
            if response.status == 400:
                raise InvalidFormat
            if read:
                response.read_data = await response.read()
                return response
            else:
                response.read_data = None
                return response
