# Generated by ariadne-codegen
# Source: queries.graphql

from typing import Any, Dict, Optional, Union

from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .download_urls import DownloadUrls
from .input_types import (
    CellLabelsSearchOptions,
    DatasetSearchOptions,
    LookupCellsSearch,
    LookupDatasetsFiltersInput,
    LookupDatasetsSearchInput,
    LookupLabelsFilters,
)
from .lookup_cells import LookupCells
from .search_datasets import SearchDatasets


def gql(q: str) -> str:
    return q


class Client(BaseClient):
    def search_datasets(
        self,
        options: Union[Optional[DatasetSearchOptions], UnsetType] = UNSET,
        search: Union[Optional[LookupDatasetsSearchInput], UnsetType] = UNSET,
        filter: Union[Optional[LookupDatasetsFiltersInput], UnsetType] = UNSET,
        **kwargs: Any
    ) -> SearchDatasets:
        query = gql(
            """
            query SearchDatasets($options: DatasetSearchOptions, $search: LookupDatasetsSearchInput, $filter: LookupDatasetsFiltersInput) {
              results: lookupDatasets(options: $options, search: $search, filter: $filter) {
                id
                name
                ...DatasetResult
                __typename
              }
            }

            fragment DatasetResult on Dataset {
              id
              name
              cellCount
              labelsets {
                id
                name
                labels {
                  id
                  name
                  count
                  __typename
                }
                __typename
              }
              project {
                id
                name
                ...ProjectAuthors_project
                __typename
              }
              __typename
            }

            fragment ProjectAuthors_project on Project {
              version
              owner {
                uid
                tempDisplayName
                displayName
                avatarUrl
                __typename
              }
              permissions {
                id
                isActive
                role
                user {
                  uid
                  tempDisplayName
                  displayName
                  avatarUrl
                  __typename
                }
                __typename
              }
              __typename
            }
            """
        )
        variables: Dict[str, object] = {
            "options": options,
            "search": search,
            "filter": filter,
        }
        response = self.execute(
            query=query, operation_name="SearchDatasets", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return SearchDatasets.model_validate(data)

    def lookup_cells(
        self,
        options: CellLabelsSearchOptions,
        filter: Union[Optional[LookupLabelsFilters], UnsetType] = UNSET,
        search: Union[Optional[LookupCellsSearch], UnsetType] = UNSET,
        **kwargs: Any
    ) -> LookupCells:
        query = gql(
            """
            query LookupCells($options: CellLabelsSearchOptions!, $filter: LookupLabelsFilters, $search: LookupCellsSearch) {
              lookupCells(options: $options, filter: $filter, search: $search) {
                id
                fullName
                name
                ...CellLabelResult
                __typename
              }
            }

            fragment CellLabelResult on Label {
              id
              fullName
              name
              ontologyTermExists
              ontologyTermId
              ontologyTerm
              synonyms
              categoryOntologyTermExists
              categoryOntologyTermId
              categoryOntologyTerm
              categoryFullName
              markerGenes
              canonicalMarkerGenes
              count
              labelset {
                id
                name
                dataset {
                  id
                  name
                  labelsets {
                    id
                    name
                    labels {
                      id
                      name
                      count
                      __typename
                    }
                    ...GeneLink_labelset
                    __typename
                  }
                  project {
                    id
                    name
                    ...ProjectAuthors_project
                    __typename
                  }
                  __typename
                }
                __typename
              }
              __typename
            }

            fragment GeneLink_labelset on Labelset {
              id
              labels {
                id
                name
                count
                __typename
              }
              __typename
            }

            fragment ProjectAuthors_project on Project {
              version
              owner {
                uid
                tempDisplayName
                displayName
                avatarUrl
                __typename
              }
              permissions {
                id
                isActive
                role
                user {
                  uid
                  tempDisplayName
                  displayName
                  avatarUrl
                  __typename
                }
                __typename
              }
              __typename
            }
            """
        )
        variables: Dict[str, object] = {
            "options": options,
            "filter": filter,
            "search": search,
        }
        response = self.execute(
            query=query, operation_name="LookupCells", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return LookupCells.model_validate(data)

    def download_urls(self, dataset_id: str, **kwargs: Any) -> DownloadUrls:
        query = gql(
            """
            query DownloadUrls($datasetId: ID!) {
              downloadUrls(datasetId: $datasetId) {
                isAnnDataUrlUpToDate
                annDataUrl
                capJsonUrlZip
                capJsonUrlTar
                __typename
              }
            }
            """
        )
        variables: Dict[str, object] = {"datasetId": dataset_id}
        response = self.execute(
            query=query, operation_name="DownloadUrls", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return  DownloadUrls.model_validate(data)
