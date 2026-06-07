from fastapi import FastAPI

app = FastAPI(
    title="EventMesh",
    version="0.1.0"
)


@app.get("/")
async def health():
    return {
        "service": "eventmesh",
        "status": "healthy"
    }