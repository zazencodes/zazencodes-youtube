from pydantic import BaseModel, Field


class Resources(BaseModel):
    cpu: float = Field(ge=1, le=2)
    memory_gb: float = Field(le=4)
    disk_size_gb: float = Field(le=20)


class RuntimeConfig(BaseModel):
    operating_system: str = Field(pattern=r"ubuntu\d+")
    python_version: float = Field(ge=3.7)


class AppEngineConfig(BaseModel):
    runtime: str = "python"
    env: str = "flex"
    entrypoint: str
    runtime_config: RuntimeConfig
    manual_scaling: int = 1
    resources: Resources
