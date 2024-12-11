# Generated by ariadne-codegen
# Source: queries.graphql

from typing import List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .fragments import CellLabelResult


class LookupCells(BaseModel):
    lookup_cells: List["LookupCellsLookupCells"] = Field(alias="lookupCells")


class LookupCellsLookupCells(CellLabelResult):
    id: str
    full_name: Optional[str] = Field(alias="fullName")
    name: str
    typename__: Literal["Label"] = Field(alias="__typename")


LookupCells.model_rebuild()