from fastapi import FastAPI

from wgpy.app.router import router


app = FastAPI(
    title="WireGuard management API",
)

app.include_router(router)
