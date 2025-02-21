# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Literal

from pydantic import Field

from .base_model import BaseModel


class DatasetReady(BaseModel):
    dataset: "DatasetReadyDataset"


class DatasetReadyDataset(BaseModel):
    id: str
    is_anndata_up_to_date: bool = Field(alias="isAnnDataUpToDate")
    is_embeddings_up_to_date: bool = Field(alias="isEmbeddingsUpToDate")
    typename__: Literal["Dataset"] = Field(alias="__typename")


DatasetReady.model_rebuild()
