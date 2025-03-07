# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Literal

from pydantic import Field

from .base_model import BaseModel


class GeneralDE(BaseModel):
    dataset: "GeneralDEDataset"


class GeneralDEDataset(BaseModel):
    id: str
    general_diff: str = Field(alias="generalDiff")
    typename__: Literal["Dataset"] = Field(alias="__typename")


GeneralDE.model_rebuild()
