from litestar import Request
from litestar.datastructures import State

from litestar.controller import Controller
from litestar.handlers import get, post
from litestar.response import Template


class HomeController(Controller):
    path = "/"

    @get(path="", name="homepage", exclude_from_auth=True)
    async def homepage(self, scope: dict, state: State, request: Request) -> Template:
        return Template(template_name="jinja/home/home.html.jinja2")
