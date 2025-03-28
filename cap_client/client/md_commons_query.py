# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Literal

from pydantic import Field

from .base_model import BaseModel
from .fragments import CurrentEmbeddingProviderAvailableEmbeddings


class MDCommonsQuery(BaseModel):
    dataset: "MDCommonsQueryDataset"


class MDCommonsQueryDataset(CurrentEmbeddingProviderAvailableEmbeddings):
    id: str
    typename__: Literal["Dataset"] = Field(alias="__typename")


MDCommonsQuery.model_rebuild()
