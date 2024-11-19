import logging

from api.api import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

logger = logging.getLogger(__name__)

app = FastAPI()

allows_origins = [
    "http://localhost:5173",
]
logger.debug(f"allows_origins: {allows_origins}")

# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=allows_origins,  # フロントエンドのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
handler = Mangum(app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
