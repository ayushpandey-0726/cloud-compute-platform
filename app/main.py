from fastapi import FastAPI, status

from app.schemas import InstanceCreate, InstanceResponse


app = FastAPI(
    title="Cloud Compute Platform",
    description="A simple cloud compute management API",
    version="1.0.0",
)


instances = []


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "service": "cloud-compute-platform",
    }


@app.post(
    "/instances",
    response_model=InstanceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_instance(instance: InstanceCreate):
    new_instance = {
        "id": len(instances) + 1,
        "name": instance.name,
        "cpu": instance.cpu,
        "memory": instance.memory,
        "region": instance.region,
        "status": "RUNNING",
    }

    instances.append(new_instance)

    return new_instance
