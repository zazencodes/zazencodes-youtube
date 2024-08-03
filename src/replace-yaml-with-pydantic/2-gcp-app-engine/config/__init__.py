from config.domain import AppEngineConfig, RuntimeConfig, Resources

app_config = AppEngineConfig(
    entrypoint="gunicorn -b :$PORT main:app",
    runtime_config=RuntimeConfig(
        operating_system="ubuntu22",
        python_version=3.8,
    ),
    resources=Resources(
        cpu=1,
        memory_gb=0.5,
        disk_size_gb=10,
    ),
)
