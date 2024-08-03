from pydantic import BaseModel
from typing import Optional


class EnvVar(BaseModel):
    name: str
    value: str


class ContainerPort(BaseModel):
    containerPort: int


class ResourceLimits(BaseModel):
    cpu: str


class Resources(BaseModel):
    limits: ResourceLimits


class VolumeMount(BaseModel):
    mountPath: str
    name: str


class Container(BaseModel):
    name: str
    image: str
    command: list[str]
    env: list[EnvVar]
    ports: list[ContainerPort]
    resources: Resources
    volumeMounts: list[VolumeMount]


class EmptyDir(BaseModel):
    pass


class ConfigMapItem(BaseModel):
    key: str
    path: str


class ConfigMap(BaseModel):
    name: str
    items: list[ConfigMapItem]


class Volume(BaseModel):
    name: str
    emptyDir: Optional[EmptyDir] = None
    configMap: Optional[ConfigMap] = None


class PodSpec(BaseModel):
    containers: list[Container]
    volumes: list[Volume]


class PodMetadata(BaseModel):
    name: str


class PodConfig(BaseModel):
    apiVersion: str
    kind: str
    metadata: PodMetadata
    spec: PodSpec
