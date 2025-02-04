from litestar import Request
from litestar.datastructures import State
import random

from litestar.controller import Controller
from litestar.handlers import get, post
from litestar.response import Template
from litestar.plugins.htmx import HTMXRequest, HTMXTemplate


class FlagCardController(Controller):
    path = "flag"

    @get(path="{flag_id:int}", name="card")
    async def get_card(self, flag_id: int, request: HTMXRequest) -> Template:

        flags_list = {1: "FLAG ONE", 2: "FLAG TWO", 3: "FLAG THREE", 4: "FLAG FOUR"}
        flag_status = random.choice([True, False])
        flag_name = flags_list.get(flag_id, "FLAG ZERO")

        return HTMXTemplate(template_name="htmx/card/card.html.jinja2", context={"flag_name": flag_name, "flag_status": flag_status})
