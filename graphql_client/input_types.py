# Generated by ariadne-codegen
# Source: https://celltype.info/graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import FeedbackExplanationType


class ListLabelFeedbackOptions(BaseModel):
    limit: Optional[float] = None
    offset: Optional[float] = None
    sort_dir: Optional[str] = Field(alias="sortDir", default=None)


class GetDatasetEmbeddingDataInput(BaseModel):
    embedding: str
    selection_gene: Optional[str] = Field(alias="selectionGene", default=None)
    scale_max_plan: float = Field(alias="scaleMaxPlan")
    selection_key_major: Optional[str] = Field(alias="selectionKeyMajor", default=None)
    selection_key_minor: Optional[str] = Field(alias="selectionKeyMinor", default=None)
    session_id: Optional[str] = Field(alias="sessionId", default=None)
    labelsets: Optional[List[str]] = None


class GetDatasetEmbeddingSelectionObsInput(BaseModel):
    selection_key: str = Field(alias="selectionKey")


class GetDatasetClustersDataInput(BaseModel):
    cluster_type: str = Field(alias="clusterType")


class GetDatasetClustersObsInput(BaseModel):
    cluster_type: str = Field(alias="clusterType")
    cluster_ids: List[str] = Field(alias="clusterIds")


class GetEmbeddingDiffInput(BaseModel):
    current_selection_key: Optional[str] = Field(
        alias="currentSelectionKey", default=None
    )
    background_selections_key: Optional[str] = Field(
        alias="backgroundSelectionsKey", default=None
    )
    cancel: Optional[bool] = None
    downsampling_allowed: Optional[bool] = Field(
        alias="downsamplingAllowed", default=None
    )
    random_seed: Optional[int] = Field(alias="randomSeed", default=None)


class PostSingleSelectionKeyInput(BaseModel):
    selection: Optional[List["SelectionType"]] = None
    session_id: Optional[str] = Field(alias="sessionId", default=None)


class SelectionType(BaseModel):
    multi_polygon: Optional["MultiPolygonSelection"] = Field(
        alias="multiPolygon", default=None
    )
    annotation: Optional["AnnotationSelection"] = None
    hc_selection: Optional["HCSelection"] = Field(alias="hcSelection", default=None)
    label_id_selection: Optional["LabelIdSelection"] = Field(
        alias="labelIdSelection", default=None
    )
    remaining_selection: Optional["RemainingSelection"] = Field(
        alias="remainingSelection", default=None
    )
    key_selection: Optional["KeySelection"] = Field(alias="keySelection", default=None)


class MultiPolygonSelection(BaseModel):
    coordinates: List["GeoCoordinates"]
    embedding: str


class GeoCoordinates(BaseModel):
    coords: List[List[List[float]]]


class AnnotationSelection(BaseModel):
    column: str
    selection: List[str]


class HCSelection(BaseModel):
    parent_selection_key: str = Field(alias="parentSelectionKey")
    obs_per_pixel: Optional[int] = Field(alias="obsPerPixel", default=None)
    genes_per_pixel: Optional[int] = Field(alias="genesPerPixel", default=None)
    left: Optional[int] = None
    right: Optional[int] = None


class LabelIdSelection(BaseModel):
    label_id: str = Field(alias="labelId")


class RemainingSelection(BaseModel):
    labelset: str


class KeySelection(BaseModel):
    selection_key: str = Field(alias="selectionKey")


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


class PostClusteredHeatmapInput(BaseModel):
    obs_per_pixel: Optional[float] = Field(alias="obsPerPixel", default=None)
    genes_per_pixel: Optional[float] = Field(alias="genesPerPixel", default=None)
    selection_key: Optional[str] = Field(alias="selectionKey", default=None)
    labelset: Optional[str] = None
    session_id: Optional[str] = Field(alias="sessionId", default=None)
    cancel: Optional[bool] = None


class GetHighlyVariableGenesCsvInput(BaseModel):
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetObsDetailsInput(BaseModel):
    obs_id: float = Field(alias="obsId")
    embedding: str


class GetGenesBySelectionCsvInput(BaseModel):
    diff_key: str = Field(alias="diffKey")
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    selection_names: Optional[List[str]] = Field(alias="selectionNames", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetGenesInput(BaseModel):
    offset: float
    limit: float
    diff_key: str = Field(alias="diffKey")
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetHighlyVariableGenesInput(BaseModel):
    offset: float
    limit: float
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetGenesBySelectionInput(BaseModel):
    offset: float
    limit: float
    diff_key: str = Field(alias="diffKey")
    gene_name_filter: Optional[str] = Field(alias="geneNameFilter", default=None)
    selection_names: Optional[List[str]] = Field(alias="selectionNames", default=None)
    sort_by: Optional[str] = Field(alias="sortBy", default=None)
    sort_order: Optional[str] = Field(alias="sortOrder", default=None)


class GetEmbeddingDiffKeygenInput(BaseModel):
    selection_type: str = Field(alias="selectionType")
    downsampling_allowed: Optional[bool] = Field(
        alias="downsamplingAllowed", default=None
    )
    random_seed: Optional[int] = Field(alias="randomSeed", default=None)


class ValidateSelectionInput(BaseModel):
    current_selection_key: str = Field(alias="currentSelectionKey")
    previous_selections_key: str = Field(alias="previousSelectionsKey")


class GetEmbeddingsObsCountInput(BaseModel):
    selection_key: str = Field(alias="selectionKey")


class GetSankeyDiagramInput(BaseModel):
    columns: List[str]


class SearchOptionsInput(BaseModel):
    offset: Optional[int] = None
    limit: Optional[int] = None


class LookupUsersSearchInput(BaseModel):
    display_name: Optional[str] = Field(alias="displayName", default=None)


class GetLabelInput(BaseModel):
    id: str


class LookupSynonymsSearch(BaseModel):
    original_name: Optional[str] = Field(alias="originalName", default=None)


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


class UploadIdentifier(BaseModel):
    id: str


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


class ValidateDatasetInput(BaseModel):
    id: str
    name: Optional[str] = None
    default_embedding: Optional[str] = Field(alias="defaultEmbedding", default=None)
    dataset_type: Optional[str] = Field(alias="datasetType", default=None)
    labelsets: Optional[List["EditNestedLabelsetInput"]] = None
    description: Optional[str] = None
    cell_count: float = Field(alias="cellCount")


class EditNestedLabelsetInput(BaseModel):
    id: Optional[str] = None
    embedding: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    annotation_method: Optional[str] = Field(alias="annotationMethod", default=None)
    algorithm_name: Optional[str] = Field(alias="algorithmName", default=None)
    algorithm_version: Optional[str] = Field(alias="algorithmVersion", default=None)
    algorithm_repo_url: Optional[str] = Field(alias="algorithmRepoUrl", default=None)
    reference_location: Optional[str] = Field(alias="referenceLocation", default=None)
    reference_description: Optional[str] = Field(
        alias="referenceDescription", default=None
    )
    version: Optional[str] = None
    mode: Optional[str] = None
    labels: Optional[List["EditNestedLabelInput"]] = None


class EditNestedLabelInput(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    color: Optional[str] = None
    count: Optional[int] = None
    is_active: Optional[bool] = Field(alias="isActive", default=None)
    polygon: Optional["NestedLabelMultiPolygonInput"] = None
    synonyms: Optional[List[str]] = None
    category_full_name: Optional[str] = Field(alias="categoryFullName", default=None)
    category_ontology_term_exists: Optional[bool] = Field(
        alias="categoryOntologyTermExists", default=None
    )
    category_ontology_term: Optional[str] = Field(
        alias="categoryOntologyTerm", default=None
    )
    category_ontology_term_id: Optional[str] = Field(
        alias="categoryOntologyTermId", default=None
    )
    marker_genes: Optional[List[str]] = Field(alias="markerGenes", default=None)
    ontology_term_exists: Optional[bool] = Field(
        alias="ontologyTermExists", default=None
    )
    ontology_term: Optional[str] = Field(alias="ontologyTerm", default=None)
    ontology_term_id: Optional[str] = Field(alias="ontologyTermId", default=None)
    ontology_assessment: Optional[str] = Field(alias="ontologyAssessment", default=None)
    full_name: Optional[str] = Field(alias="fullName", default=None)
    rationale: Optional[str] = None
    rationale_dois: Optional[List[str]] = Field(alias="rationaleDois", default=None)
    canonical_marker_genes: Optional[List[str]] = Field(
        alias="canonicalMarkerGenes", default=None
    )


class NestedLabelMultiPolygonInput(BaseModel):
    selections: List["NestedLabelMultiPolygonSelectionInput"]


class NestedLabelMultiPolygonSelectionInput(BaseModel):
    type: str
    polygon_coord: Optional[List["PolygonCoordInput"]] = Field(
        alias="polygonCoord", default=None
    )
    column: Optional[str] = None
    selection: Optional[List[str]] = None


class PolygonCoordInput(BaseModel):
    x: float
    y: float


class DatasetUpdateJobIdentifier(BaseModel):
    id: str


class GetEmbeddingSessionSnapshotInput(BaseModel):
    dataset_id: str = Field(alias="datasetId")
    session_id: str = Field(alias="sessionId")


class LookupLabelCategoriesSearch(BaseModel):
    name: str


class LookupTissueTermsOptions(BaseModel):
    offset: Optional[float] = None
    limit: Optional[float] = None


class LookupTissueTermsSearch(BaseModel):
    value: str
    fields: List[str]


class CreateUserArg(BaseModel):
    uid: str
    display_name: str = Field(alias="displayName")
    bio: str
    email: str
    location: str
    avatar_url: Optional[str] = Field(alias="avatarUrl", default=None)
    is_temp_display_name: Optional[bool] = Field(
        alias="isTempDisplayName", default=None
    )
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    institution: Optional[str] = None
    lab_name: Optional[str] = Field(alias="labName", default=None)
    lab_url: Optional[str] = Field(alias="labUrl", default=None)
    orcid_id: Optional[str] = Field(alias="orcidId", default=None)


class EditUserArg(BaseModel):
    uid: str
    display_name: Optional[str] = Field(alias="displayName", default=None)
    bio: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None
    avatar_url: Optional[str] = Field(alias="avatarUrl", default=None)
    is_temp_display_name: Optional[bool] = Field(
        alias="isTempDisplayName", default=None
    )
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    institution: Optional[str] = None
    lab_name: Optional[str] = Field(alias="labName", default=None)
    lab_url: Optional[str] = Field(alias="labUrl", default=None)
    orcid_id: Optional[str] = Field(alias="orcidId", default=None)


class ResetCapUserPasswordInput(BaseModel):
    reset_link: str = Field(alias="resetLink")
    new_password: str = Field(alias="newPassword")
    uid: str


class EditLabelInput(BaseModel):
    id: Optional[str] = None
    synonyms: Optional[List[str]] = None
    category_full_name: Optional[str] = Field(alias="categoryFullName", default=None)
    category_ontology_term_exists: Optional[bool] = Field(
        alias="categoryOntologyTermExists", default=None
    )
    category_ontology_term: Optional[str] = Field(
        alias="categoryOntologyTerm", default=None
    )
    category_ontology_term_id: Optional[str] = Field(
        alias="categoryOntologyTermId", default=None
    )
    full_name: Optional[str] = Field(alias="fullName", default=None)
    rationale: Optional[str] = None
    rationale_dois: Optional[List[str]] = Field(alias="rationaleDois", default=None)
    canonical_marker_genes: Optional[List[str]] = Field(
        alias="canonicalMarkerGenes", default=None
    )
    ontology_term_exists: Optional[bool] = Field(
        alias="ontologyTermExists", default=None
    )
    ontology_term: Optional[str] = Field(alias="ontologyTerm", default=None)
    ontology_term_id: Optional[str] = Field(alias="ontologyTermId", default=None)
    ontology_assessment: Optional[str] = Field(alias="ontologyAssessment", default=None)
    marker_genes: Optional[List[str]] = Field(alias="markerGenes", default=None)


class CreateLabelFeedbackInput(BaseModel):
    score: Optional[float] = None
    explanation: Optional["LabelFeedbackExplanationInput"] = None


class LabelFeedbackExplanationInput(BaseModel):
    type: FeedbackExplanationType
    data: Optional["FeedbackExplanationDataInput"] = None


class FeedbackExplanationDataInput(BaseModel):
    changes: Optional[List["FeedbackExplanationDataRefineChangesInput"]] = None
    comment: Optional[str] = None
    label_ids: Optional[List[str]] = Field(alias="labelIds", default=None)
    labels_number: Optional[float] = Field(alias="labelsNumber", default=None)
    labels: Optional[List["FeedbackExplanationSplitLabels"]] = None


class FeedbackExplanationDataRefineChangesInput(BaseModel):
    attribute: str
    new_value: Optional[Any] = Field(alias="newValue", default=None)
    original_value: Optional[Any] = Field(alias="originalValue", default=None)


class FeedbackExplanationSplitLabels(BaseModel):
    name: Optional[str] = None
    marker_genes: List[str] = Field(alias="markerGenes")


class EditLabelsetInfoInput(BaseModel):
    session_id: Optional[str] = Field(alias="sessionId", default=None)


class EditLabelsetInput(BaseModel):
    id: str
    mode: Optional[str] = None
    annotation_method: Optional[str] = Field(alias="annotationMethod", default=None)
    algorithm_name: Optional[str] = Field(alias="algorithmName", default=None)
    algorithm_version: Optional[str] = Field(alias="algorithmVersion", default=None)
    algorithm_repo_url: Optional[str] = Field(alias="algorithmRepoUrl", default=None)
    reference_location: Optional[str] = Field(alias="referenceLocation", default=None)
    reference_description: Optional[str] = Field(
        alias="referenceDescription", default=None
    )
    version: Optional[str] = None


class DatasetIdentifierInput(BaseModel):
    id: str


class CreateNestedLabelsetInput(BaseModel):
    name: str
    description: Optional[str] = None
    annotation_method: Optional[str] = Field(alias="annotationMethod", default=None)
    algorithm_name: Optional[str] = Field(alias="algorithmName", default=None)
    algorithm_version: Optional[str] = Field(alias="algorithmVersion", default=None)
    algorithm_repo_url: Optional[str] = Field(alias="algorithmRepoUrl", default=None)
    reference_location: Optional[str] = Field(alias="referenceLocation", default=None)
    reference_description: Optional[str] = Field(
        alias="referenceDescription", default=None
    )
    mode: Optional[str] = None
    status: Optional[str] = None
    label_count: Optional[float] = Field(alias="labelCount", default=None)
    version: Optional[str] = None
    labels: Optional[List["CreateNestedLabelInput"]] = None


class CreateNestedLabelInput(BaseModel):
    name: str
    color: Optional[str] = None
    count: int
    synonyms: Optional[List[str]] = None
    description: Optional[str] = None
    full_name: Optional[str] = Field(alias="fullName", default=None)
    rationale: Optional[str] = None
    rationale_dois: Optional[List[str]] = Field(alias="rationaleDois", default=None)
    category_full_name: Optional[str] = Field(alias="categoryFullName", default=None)
    category_ontology_term_exists: Optional[bool] = Field(
        alias="categoryOntologyTermExists", default=None
    )
    category_ontology_term: Optional[str] = Field(
        alias="categoryOntologyTerm", default=None
    )
    category_ontology_term_id: Optional[str] = Field(
        alias="categoryOntologyTermId", default=None
    )
    marker_genes: Optional[List[str]] = Field(alias="markerGenes", default=None)
    canonical_genes: Optional[List[str]] = Field(alias="canonicalGenes", default=None)
    ontology_term_exists: Optional[bool] = Field(
        alias="ontologyTermExists", default=None
    )
    ontology_term: Optional[str] = Field(alias="ontologyTerm", default=None)
    ontology_term_id: Optional[str] = Field(alias="ontologyTermId", default=None)
    ontology_assessment: Optional[str] = Field(alias="ontologyAssessment", default=None)
    canonical_marker_genes: Optional[List[str]] = Field(
        alias="canonicalMarkerGenes", default=None
    )


class UploadUploader(BaseModel):
    uid: str


class UploadPayload(BaseModel):
    file_name: str = Field(alias="fileName")
    project_id: str = Field(alias="projectId")


class UpdateUploadPayload(BaseModel):
    status: Optional[str] = None
    errors: Optional[List["UpdateUploadErrorItemPayload"]] = None
    id: str


class UpdateUploadErrorItemPayload(BaseModel):
    message: Optional[str] = None
    error: str
    meta: Optional[Any] = None


class CreateDatasetInfoInput(BaseModel):
    user_uid: Optional[str] = Field(alias="userUid", default=None)
    upload_id: Optional[str] = Field(alias="uploadId", default=None)
    overwrite: Optional[bool] = None


class CreateDatasetInput(BaseModel):
    project_id: str = Field(alias="projectId")
    name: str
    description: Optional[str] = None
    dataset_type: Optional[str] = Field(alias="datasetType", default=None)
    ann_data_url: Optional[str] = Field(alias="annDataUrl", default=None)
    raw_data_url_zip: Optional[str] = Field(alias="rawDataUrlZip", default=None)
    raw_data_url_tar: Optional[str] = Field(alias="rawDataUrlTar", default=None)
    cell_count: int = Field(alias="cellCount")
    gene_count: int = Field(alias="geneCount")
    labelsets: Optional[List["CreateNestedLabelsetInput"]] = None


class EditDatasetInfoInput(BaseModel):
    job_id: Optional[str] = Field(alias="jobId", default=None)
    session_id: Optional[str] = Field(alias="sessionId", default=None)


class EditDatasetInput(BaseModel):
    id: str
    name: Optional[str] = None
    default_embedding: Optional[str] = Field(alias="defaultEmbedding", default=None)
    dataset_type: Optional[str] = Field(alias="datasetType", default=None)
    labelsets: Optional[List["EditNestedLabelsetInput"]] = None
    description: Optional[str] = None


class EditDatasetCoreFieldsInput(BaseModel):
    id: str
    raw_data_url_zip: Optional[str] = Field(alias="rawDataUrlZip", default=None)
    raw_data_url_tar: Optional[str] = Field(alias="rawDataUrlTar", default=None)
    ann_data_url: Optional[str] = Field(alias="annDataUrl", default=None)
    seurat_url: Optional[str] = Field(alias="seuratUrl", default=None)
    is_ann_data_up_to_date: Optional[bool] = Field(
        alias="isAnnDataUpToDate", default=None
    )
    is_ann_data_url_up_to_date: Optional[bool] = Field(
        alias="isAnnDataUrlUpToDate", default=None
    )
    is_embeddings_up_to_date: Optional[bool] = Field(
        alias="isEmbeddingsUpToDate", default=None
    )


class ReportDatasetUpdateInProgressInput(BaseModel):
    job_id: str = Field(alias="jobId")


class ReportDatasetUpdateFailureInput(BaseModel):
    reason: str
    job_id: str = Field(alias="jobId")
    retry: Optional[bool] = None


class EditDatasetEmbeddingsInput(BaseModel):
    ann_data_url: str = Field(alias="annDataUrl")


class DeleteDatasetInput(BaseModel):
    id: str


class SaveDatasetLabelCortegesInput(BaseModel):
    id: str
    corteges: List[Any]


class ClusteredHeatmapErrorInput(BaseModel):
    message: str
    name: str


class ClusteredHeatmapInput(BaseModel):
    annotations: "AnnotationsObjectResponse"
    genes: "GenesObjectResponse"
    obs_ids: "ObsIDSObjectResponse"
    scores: "ScoresObjectResponse"


class AnnotationsObjectResponse(BaseModel):
    data: List[str]


class GenesObjectResponse(BaseModel):
    data: List[str]


class ObsIDSObjectResponse(BaseModel):
    data: List[int]


class ScoresObjectResponse(BaseModel):
    data: List[float]


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


class LabelsetObjectInput(BaseModel):
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


class CancelClusteredHeatmapInput(BaseModel):
    task_id: str = Field(alias="taskId")
    session_id: Optional[str] = Field(alias="sessionId", default=None)


class CreateProjectInput(BaseModel):
    name: str
    description: Optional[str] = None
    contact_email: Optional[str] = Field(alias="contactEmail", default=None)
    contact_emails: Optional[List[str]] = Field(alias="contactEmails", default=None)
    external_url: Optional[str] = Field(alias="externalUrl", default=None)
    external_urls: Optional[List[str]] = Field(alias="externalUrls", default=None)
    contact_name: Optional[str] = Field(alias="contactName", default=None)
    contact_names: Optional[List[str]] = Field(alias="contactNames", default=None)
    journal_doi: Optional[str] = Field(alias="journalDoi", default=None)
    raw_data_url: Optional[str] = Field(alias="rawDataUrl", default=None)


class EditProjectInput(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    contact_email: Optional[str] = Field(alias="contactEmail", default=None)
    contact_emails: Optional[List[str]] = Field(alias="contactEmails", default=None)
    external_url: Optional[str] = Field(alias="externalUrl", default=None)
    external_urls: Optional[List[str]] = Field(alias="externalUrls", default=None)
    contact_name: Optional[str] = Field(alias="contactName", default=None)
    contact_names: Optional[List[str]] = Field(alias="contactNames", default=None)
    journal_doi: Optional[str] = Field(alias="journalDoi", default=None)
    raw_data_url: Optional[str] = Field(alias="rawDataUrl", default=None)


class AddPermissionInput(BaseModel):
    project_id: str = Field(alias="projectId")
    uid: str
    role: Any


class InviteByEmailInput(BaseModel):
    project_id: str = Field(alias="projectId")
    email: str
    role: Any


class RemovePermissionInput(BaseModel):
    id: str


class DeleteProjectInput(BaseModel):
    id: str


class CreatePublicationInput(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    contact_email: Optional[str] = Field(alias="contactEmail", default=None)
    contact_emails: Optional[List[str]] = Field(alias="contactEmails", default=None)
    external_url: Optional[str] = Field(alias="externalUrl", default=None)
    external_urls: Optional[List[str]] = Field(alias="externalUrls", default=None)
    contact_name: Optional[str] = Field(alias="contactName", default=None)
    contact_names: Optional[List[str]] = Field(alias="contactNames", default=None)
    journal_doi: Optional[str] = Field(alias="journalDoi", default=None)
    raw_data_url: Optional[str] = Field(alias="rawDataUrl", default=None)
    cap_authors: Optional[List[str]] = Field(alias="capAuthors", default=None)


class ReviewProjectRequestInput(BaseModel):
    id: str


class DeclineProjectReviewInput(BaseModel):
    id: str


class CancelProjectReviewInput(BaseModel):
    id: str


class ProjectIdentifier(BaseModel):
    id: str


PostSingleSelectionKeyInput.model_rebuild()
SelectionType.model_rebuild()
MultiPolygonSelection.model_rebuild()
CellLabelsSearchOptions.model_rebuild()
LookupLabelsFilters.model_rebuild()
DatasetSearchOptions.model_rebuild()
LookupDatasetsFiltersInput.model_rebuild()
ValidateDatasetInput.model_rebuild()
EditNestedLabelsetInput.model_rebuild()
EditNestedLabelInput.model_rebuild()
NestedLabelMultiPolygonInput.model_rebuild()
NestedLabelMultiPolygonSelectionInput.model_rebuild()
CreateLabelFeedbackInput.model_rebuild()
LabelFeedbackExplanationInput.model_rebuild()
FeedbackExplanationDataInput.model_rebuild()
CreateNestedLabelsetInput.model_rebuild()
UpdateUploadPayload.model_rebuild()
CreateDatasetInput.model_rebuild()
EditDatasetInput.model_rebuild()
ClusteredHeatmapInput.model_rebuild()
PostSaveEmbeddingSessionInput.model_rebuild()
DatasetObjectInput.model_rebuild()
LabelsetWithLabelsObjectInput.model_rebuild()
