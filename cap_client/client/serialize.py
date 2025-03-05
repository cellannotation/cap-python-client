from .lookup_cells import (
    LookupCells,
    LookupCellsLookupCells,
)
from .fragments import (
    CellLabelResultLabelset,
    CellLabelResultLabelsetDataset,
    CellLabelResultLabelsetDatasetProject,
    CellLabelResult,
    DatasetResult,
    DatasetResultLabelsets,
    DatasetResultLabelsetsLabels,
    DatasetResultProject,
)
from .search_datasets import (
    SearchDatasets,
    SearchDatasetsResults,
)


def serialize_lookup_cells(self):
    return {
        "lookup_cells": [c.serialize() for c in self.lookup_cells],
    }

LookupCells.serialize = serialize_lookup_cells


def serialize_lookup_cells_lookup_cells(self):
    return {
        "id": self.id,
        "full_name": self.full_name,
        "name": self.name,
    }

LookupCellsLookupCells.serialize = serialize_lookup_cells_lookup_cells


def serialize_cell_label_result_labelset(self):
    return {
        "id": self.id,
        "name": self.name,
        "dataset": self.dataset.serialize(),
    }

CellLabelResultLabelset.serialize = serialize_cell_label_result_labelset


def serialize_cell_label_result_labelset_datasett(self):
    return {
        "id": self.id,
        "name": self.name,
        "labelsets": [l.serialize() for l in self.labelsets] if self.labelsets is not None else [],
        "project": self.project.serialize(),
    }

CellLabelResultLabelsetDataset.serialize = serialize_cell_label_result_labelset_datasett


def serialize_cell_label_result_labelset_dataset_project(self):
    return {
        "id": self.id,
        "name": self.name,
    }
CellLabelResultLabelsetDatasetProject.serialize = serialize_cell_label_result_labelset_dataset_project


def serialize_cell_label_result(self):
    return {
        "id": self.id,
        "full_name": self.full_name,
        "name": self.name,
        "ontology_term_exists": self.ontology_term_exists,
        "ontology_term_id": self.ontology_term_id,
        "ontology_term": self.ontology_term,
        "synonyms": self.synonyms,
        "category_ontology_term_exists": self.category_ontology_term_exists,
        "category_ontology_term_id": self.category_ontology_term_id,
        "category_ontology_term": self.category_ontology_term,
        "category_full_name": self.category_full_name,
        "marker_genes": self.marker_genes,
        "canonical_marker_genes": self.canonical_marker_genes,
        "count": self.count,
        "labelset": self.labelset.serialize(),
    }

CellLabelResult.serialize = serialize_cell_label_result


def serialize_dataset_result(self):
    return {
        "id": self.id,
        "name": self.name,
        "cell_count": self.cell_count,
        "labelsets": [l.serialize() for l in self.labelsets] if self.labelsets is not None else [],
        "project": self.project,
    }

DatasetResult.serialize = serialize_dataset_result


def serialize_dataset_result_labelsets(self):
    return {
        "id": self.id,
        "name": self.name,
        "labels": [l.serialize() for l in self.labels] if self.labels is not None else [],
    }

DatasetResultLabelsets.serialize = serialize_dataset_result_labelsets


def serialize_dataset_result_labelsets_labels(self):
    return {
        "id": self.id,
        "name": self.name,
        "count": self.count,
    }

DatasetResultLabelsetsLabels.serialize = serialize_dataset_result_labelsets_labels


def serialize_dataset_result_project(self):
    return {
        "id": self.id,
        "name": self.name,
    }

DatasetResultProject.serialize = serialize_dataset_result_project


def serialize_search_datasets(self):
    return {
        "results": [r.serialize() for r in self.results],
    }

SearchDatasets.serialize = serialize_search_datasets


def serialize_search_datasets_results(self):
    return {
        "id": self.id,
        "name": self.name,
    }

SearchDatasetsResults.serialize = serialize_search_datasets_results
