from config.domain import (
    PodConfig,
    PodMetadata,
    PodSpec,
    Container,
    EnvVar,
    ContainerPort,
    Resources,
    ResourceLimits,
    Volume,
    VolumeMount,
    ConfigMap,
    ConfigMapItem,
    EmptyDir,
)

pod_config = PodConfig(
    apiVersion="v1",
    kind="Pod",
    metadata=PodMetadata(name="redis"),
    spec=PodSpec(
        containers=[
            Container(
                name="redis",
                image="redis:5.0.4",
                command=["redis-server", "/redis-master/redis.conf"],
                env=[EnvVar(name="MASTER", value="true")],
                ports=[ContainerPort(containerPort=6379)],
                resources=Resources(limits=ResourceLimits(cpu="0.1")),
                volumeMounts=[
                    VolumeMount(mountPath="/redis-master-data", name="data"),
                    VolumeMount(mountPath="/redis-master", name="config"),
                ],
            )
        ],
        volumes=[
            Volume(name="data", emptyDir=EmptyDir()),
            Volume(
                name="config",
                configMap=ConfigMap(
                    name="example-redis-config",
                    items=[ConfigMapItem(key="redis-config", path="redis.conf")],
                ),
            ),
        ],
    ),
)
