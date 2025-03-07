# Generated by ariadne-codegen
# Source: queries.graphql

from typing import List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class CreateSession(BaseModel):
    save_embedding_session: "CreateSessionSaveEmbeddingSession" = Field(
        alias="saveEmbeddingSession"
    )


class CreateSessionSaveEmbeddingSession(BaseModel):
    id: Optional[str]
    name: Optional[str]
    dataset_type: Optional[str] = Field(alias="datasetType")
    description: Optional[str]
    cell_count: Optional[float] = Field(alias="cellCount")
    labelsets: Optional[List["CreateSessionSaveEmbeddingSessionLabelsets"]]
    typename__: Literal["DatasetModel"] = Field(alias="__typename")


class CreateSessionSaveEmbeddingSessionLabelsets(BaseModel):
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
    labels: Optional[List["CreateSessionSaveEmbeddingSessionLabelsetsLabels"]]
    typename__: Literal["LabelsetModel"] = Field(alias="__typename")


class CreateSessionSaveEmbeddingSessionLabelsetsLabels(BaseModel):
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
    typename__: Literal["LabelModel"] = Field(alias="__typename")


CreateSession.model_rebuild()
CreateSessionSaveEmbeddingSession.model_rebuild()
CreateSessionSaveEmbeddingSessionLabelsets.model_rebuild()
