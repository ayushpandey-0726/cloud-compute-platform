from fastapi import FastAPI


app = FastAPI(
    title="Cloud Compute Platform",
    description="A cloud compute management platform",
    version="1.0.0",
)



@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "cloud-compute-platform",
    }
