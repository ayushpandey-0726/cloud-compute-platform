from pydantic import BaseModel


class InstanceCreate(BaseModel):
    name: str
    cpu: int
    memory: int
    region: str


class InstanceResponse(BaseModel):
    id: int
    name: str
    cpu: int
    memory: int
    region: str
    status: str