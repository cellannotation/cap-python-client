# Generated by ariadne-codegen
# Source: https://celltype.info/graphql

from typing import Annotated, Any, List, Optional, Union

from pydantic import Field, PlainSerializer

from .base_model import BaseModel, Upload


class GetDatasetEmbeddingDataInput(BaseModel):
    embedding: str
    selection_gene: Optional[str] = Field(alias="selectionGene", default=None)
    scale_max_plan: float = Field(alias="scaleMaxPlan")
    selection_key_major: Optional[str] = Field(alias="selectionKeyMajor", default=None)
    selection_key_minor: Optional[str] = Field(alias="selectionKeyMinor", default=None)
    session_id: Optional[str] = Field(alias="sessionId", default=None)
    labelsets: Optional[List[str]] = None


class GetDatasetClustersDataInput(BaseModel):
    cluster_type: str = Field(alias="clusterType")


class PostHeatmapInput(BaseModel):
    diff_key: str = Field(alias="diffKey")
    n_genes: Optional[int] = Field(alias="nGenes", default=None)
    scale_max_plan: Optional[float] = Field(alias="scaleMaxPlan", default=None)
    genes_filter: Optional[List[str]] = Field(alias="genesFilter", default=None)
    use_genes_pattern: Optional[bool] = Field(alias="useGenesPattern", default=None)
    session_id: Optional[str] = Field(alias="sessionId", default=None)
    include_reference_selection: Optional[bool] = Field(
        alias="includeReferenceSelection", default=None
    )
    selection_key: Optional[str] = Field(alias="selectionKey", default=None)


class GetHighlyVariableGenesInput(BaseModel):
    offset: float
    limit: float
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    use_genes_pattern: Optional[bool] = Field(alias="useGenesPattern", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetGeneralDiffInput(BaseModel):
    labelset_id: str = Field(alias="labelsetId")
    session_id: str = Field(alias="sessionId")
    random_seed: float = Field(alias="randomSeed")


class CellLabelsSearchOptions(BaseModel):
    offset: Optional[int] = None
    limit: Optional[int] = None
    sort: Optional[List["CellLabelsSearchSort"]] = None


class CellLabelsSearchSort(BaseModel):
    field: str
    order: str


class LookupLabelsFilters(BaseModel):
    metadata: Optional[List["SearchLabelByMetadataArgs"]] = None


class SearchLabelByMetadataArgs(BaseModel):
    field: str
    values: List[str]


class LookupCellsSearch(BaseModel):
    name: Optional[str] = None
    fields: Optional[List[str]] = None


class DatasetSearchOptions(BaseModel):
    offset: Optional[int] = None
    limit: Optional[int] = None
    sort: Optional[List["DatasetSearchSort"]] = None


class DatasetSearchSort(BaseModel):
    field: str
    order: str


class LookupDatasetsFiltersInput(BaseModel):
    metadata: Optional[List["SearchByMetadataArgs"]] = None
    labelset: Optional[List[str]] = None


class SearchByMetadataArgs(BaseModel):
    field: str
    values: List[str]


class LookupDatasetsSearchInput(BaseModel):
    cell_types: Optional[List[str]] = Field(alias="cellTypes", default=None)
    name: Optional[str] = None
    project_name: Optional[str] = Field(alias="projectName", default=None)
    project_description: Optional[str] = Field(alias="projectDescription", default=None)


class PostSaveEmbeddingSessionInput(BaseModel):
    session_id: str = Field(alias="sessionId")
    dataset: "DatasetObjectInput"


class DatasetObjectInput(BaseModel):
    id: Optional[str] = None
    dataset_type: Optional[str] = Field(alias="datasetType", default=None)
    cell_count: Optional[float] = Field(alias="cellCount", default=None)
    description: Optional[str] = None
    labelsets_count: Optional[float] = Field(alias="labelsetsCount", default=None)
    name: Optional[str] = None
    labelsets: Optional[List["LabelsetWithLabelsObjectInput"]] = None


class LabelsetWithLabelsObjectInput(BaseModel):
    id: Optional[str] = None
    algorithm_name: Optional[str] = Field(alias="algorithmName", default=None)
    algorithm_repo_url: Optional[str] = Field(alias="algorithmRepoUrl", default=None)
    algorithm_version: Optional[str] = Field(alias="algorithmVersion", default=None)
    annotation_method: Optional[str] = Field(alias="annotationMethod", default=None)
    description: Optional[str] = None
    mode: Optional[str] = None
    name: Optional[str] = None
    reference_description: Optional[str] = Field(
        alias="referenceDescription", default=None
    )
    reference_url: Optional[str] = Field(alias="referenceUrl", default=None)
    embedding: Optional[str] = None
    labels: Optional[List["LabelObjectInput"]] = None


class LabelObjectInput(BaseModel):
    id: Optional[str] = None
    canonical_marker_genes: Optional[List[str]] = Field(
        alias="canonicalMarkerGenes", default=None
    )
    category_full_name: Optional[str] = Field(alias="categoryFullName", default=None)
    category_ontology_term_exists: Optional[bool] = Field(
        alias="categoryOntologyTermExists", default=None
    )
    ontology_term_exists: Optional[bool] = Field(
        alias="ontologyTermExists", default=None
    )
    category: Optional[str] = None
    category_ontology_exists: Optional[bool] = Field(
        alias="categoryOntologyExists", default=None
    )
    category_ontology_term: Optional[str] = Field(
        alias="categoryOntologyTerm", default=None
    )
    category_ontology_term_id: Optional[str] = Field(
        alias="categoryOntologyTermId", default=None
    )
    color: Optional[str] = None
    count: Optional[float] = None
    full_name: Optional[str] = Field(alias="fullName", default=None)
    name: Optional[str] = None
    ontology_assessment: Optional[str] = Field(alias="ontologyAssessment", default=None)
    ontology_exists: Optional[bool] = Field(alias="ontologyExists", default=None)
    ontology_term: Optional[str] = Field(alias="ontologyTerm", default=None)
    ontology_term_id: Optional[str] = Field(alias="ontologyTermId", default=None)
    rationale: Optional[str] = None
    canonical_genes: Optional[List[str]] = Field(alias="canonicalGenes", default=None)
    marker_genes: Optional[List[str]] = Field(alias="markerGenes", default=None)
    rationale_dois: Optional[List[str]] = Field(alias="rationaleDois", default=None)
    synonyms: Optional[List[str]] = None


CellLabelsSearchOptions.model_rebuild()
LookupLabelsFilters.model_rebuild()
DatasetSearchOptions.model_rebuild()
LookupDatasetsFiltersInput.model_rebuild()
PostSaveEmbeddingSessionInput.model_rebuild()
DatasetObjectInput.model_rebuild()
LabelsetWithLabelsObjectInput.model_rebuild()
