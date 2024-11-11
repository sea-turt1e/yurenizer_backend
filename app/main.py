# from api.api import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from yurenizer import SynonymNormalizer

app = FastAPI()
# CORS設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # フロントエンドのオリジン
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(api_router)

synonym_normalizer = SynonymNormalizer(synonym_file_path="synonyms.txt")


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.get("/normalize")
def normalize(text: str):
    try:
        normalized_text = synonym_normalizer.normalize(text)
        return {"status": "ok", "message": normalized_text}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
