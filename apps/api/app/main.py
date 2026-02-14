from fastapi import FastAPI

app = FastAPI(
    title="Vehicle Predictive Maintenance API"
)

@app.get("/health")
def health():
    return {"status": "ok"}
