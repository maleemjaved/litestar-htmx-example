from litestar import Litestar
from litestar.template.config import TemplateConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import StaticFilesConfig
from litestar.plugins.htmx import HTMXPlugin


from settings import *
from controllers.home import HomeController
from controllers.card import FlagCardController


# ==================== Imports End ======================= #

# templates configuration
template_config = TemplateConfig(directory=TEMPLATES_DIR, engine=JinjaTemplateEngine)

# static route to serve static files
static_config = StaticFilesConfig(directories=[STATIC_DIR], path="/static", name="static")


def create_app() -> Litestar:
    # main litestar app
    app = Litestar(
        route_handlers=[HomeController, FlagCardController],
        static_files_config=[static_config],
        template_config=template_config,
        plugins=[HTMXPlugin()],
        debug=DEBUG,
    )

    return app
