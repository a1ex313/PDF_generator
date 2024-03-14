import uvicorn

from .settings import settings

uvicorn.run(
    'scr.app:app',
    reload=True,
)
