# Generated by ariadne-codegen

from io import IOBase

from pydantic import BaseModel as PydanticBaseModel, ConfigDict, Field
from typing import Optional, List, Literal


class UnsetType:
    def __bool__(self) -> bool:
        return False


UNSET = UnsetType()


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        protected_namespaces=(),
    )


class Upload:
    def __init__(self, filename: str, content: IOBase, content_type: str):
        self.filename = filename
        self.content = content
        self.content_type = content_type


class Label(BaseModel):
    id: Optional[str]
    name: Optional[str]
    count: Optional[float]
    color: Optional[str]
    full_name: Optional[str] = Field(alias="fullName")
    ontology_term_exists: Optional[bool] = Field(alias="ontologyTermExists")
    ontology_term: Optional[str] = Field(alias="ontologyTerm")
    ontology_term_id: Optional[str] = Field(alias="ontologyTermId")
    category_full_name: Optional[str] = Field(alias="categoryFullName")
    category_ontology_term_exists: Optional[bool] = Field(
        alias="categoryOntologyTermExists"
    )
    category_ontology_term: Optional[str] = Field(alias="categoryOntologyTerm")
    category_ontology_term_id: Optional[str] = Field(alias="categoryOntologyTermId")
    marker_genes: Optional[List[str]] = Field(alias="markerGenes")
    canonical_marker_genes: Optional[List[str]] = Field(alias="canonicalMarkerGenes")
    synonyms: Optional[List[str]]
    rationale: Optional[str]
    rationale_dois: Optional[List[str]] = Field(alias="rationaleDois")
    ontology_assessment: Optional[str] = Field(alias="ontologyAssessment")


class LabelSet(BaseModel):
    id: Optional[str]
    name: Optional[str]
    mode: Optional[str]
    description: Optional[str]
    annotation_method: Optional[str] = Field(alias="annotationMethod")
    algorithm_name: Optional[str] = Field(alias="algorithmName")
    algorithm_version: Optional[str] = Field(alias="algorithmVersion")
    algorithm_repo_url: Optional[str] = Field(alias="algorithmRepoUrl")
    reference_location: Optional[str] = Field(alias="referenceLocation")
    reference_description: Optional[str] = Field(alias="referenceDescription")
    labels: Optional[List[Label]]


class Dataset(BaseModel):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    cell_count: Optional[float] = Field(alias="cellCount")
    labelsets: Optional[List[LabelSet]]
