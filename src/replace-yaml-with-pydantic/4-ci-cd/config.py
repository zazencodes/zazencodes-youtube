from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class NodeVersion(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    node_version: str = Field(alias="node-version")


class Step(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(pattern="^[A-Z].*")
    uses: Optional[str] = None
    run: Optional[str] = None
    with_: Optional[NodeVersion] = Field(None, alias="with")


class BuildJob(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    runs_on: str = Field(alias="runs-on")
    steps: list[Step]


class Jobs(BaseModel):
    build: BuildJob


class OnEvent(BaseModel):
    branches: list[str]


class On(BaseModel):
    push: OnEvent
    pull_request: OnEvent


class Workflow(BaseModel):
    name: str = Field(pattern="^[A-Z].*")
    on: On
    jobs: Jobs


workflow = Workflow(
    name="Animal Farm NodeJS CI",
    on=On(push=OnEvent(branches=["main"]), pull_request=OnEvent(branches=["main"])),
    jobs=Jobs(
        build=BuildJob(
            runs_on="ubuntu-latest",  # pyright: ignore
            steps=[
                Step(
                    name="Checkout repository", uses="actions/checkout@v2"
                ),  # pyright: ignore
                Step(
                    name="Use Node.js",
                    uses="actions/setup-node@v1",
                    with_=NodeVersion(node_version="18.x"),  # pyright: ignore
                ),
                Step(name="Run Yarn", run="yarn"),  # pyright: ignore
                Step(name="Run tests", run="yarn test"),  # pyright: ignore
            ],
        )
    ),
)

print(workflow)
