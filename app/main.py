from fastapi import Depends, FastAPI, HTTPException, status

from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models
from app.schemas import InstanceCreate, InstanceResponse


app = FastAPI(
    title="Cloud Compute Platform",
    description="A simple cloud compute management API",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)


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
def create_instance(
    instance: InstanceCreate,
    db: Session = Depends(get_db),
):
    new_instance = models.Instance(
        name=instance.name,
        cpu=instance.cpu,
        memory=instance.memory,
        region=instance.region,
        status="RUNNING",
    )

    db.add(new_instance)
    db.commit()
    db.refresh(new_instance)

    return new_instance


@app.get(
    "/instances",
    response_model=list[InstanceResponse],
)
def get_instances(db: Session = Depends(get_db)):
    return db.query(models.Instance).all()


@app.get(
    "/instances/{instance_id}",
    response_model=InstanceResponse,
)
def get_instance(
    instance_id: int,
    db: Session = Depends(get_db),
):
    instance = (
        db.query(models.Instance)
        .filter(models.Instance.id == instance_id)
        .first()
    )

    if instance is None:
        raise HTTPException(
            status_code=404,
            detail="Instance not found",
        )

    return instance
