from pydantic import BaseModel


class ComputeInstance(BaseModel):
    id: int
    name: str
    cpu: int
    memory: int
    region: str
    status: str