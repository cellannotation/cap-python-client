from typing import List, cast

from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLEnumType,
    GraphQLEnumValue,
    GraphQLField,
    GraphQLFloat,
    GraphQLID,
    GraphQLInputField,
    GraphQLInputObjectType,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLScalarType,
    GraphQLSchema,
    GraphQLString,
    GraphQLUnionType,
    Undefined,
)
from graphql.type.schema import TypeMap

type_map: TypeMap = {
    "Query": GraphQLObjectType(
        name="Query",
        description=None,
        interfaces=[],
        fields=lambda: {
            "user": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={
                    "uid": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "lookupUsers": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"]))
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["SearchOptionsInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType, type_map["LookupUsersSearchInput"]
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "label": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"])),
                args={
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetLabelInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "lookupSynonyms": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["LabelSynonym"])
                        )
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["SearchOptionsInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["LookupSynonymsSearch"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "lookupCells": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"]))
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["CellLabelsSearchOptions"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "filter": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["LookupLabelsFilters"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["LookupCellsSearch"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "listMetadataTypes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["GroupedMetadataResponse"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "uploadList": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["UploadResponse"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "pendingUploads": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["UploadResponse"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "upload": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["UploadResponse"])),
                args={
                    "upload": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["UploadIdentifier"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "dataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "datasetId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "lookupDatasets": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["DatasetLookupResponse"])
                        )
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["DatasetSearchOptions"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "filter": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType,
                            type_map["LookupDatasetsFiltersInput"],
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType,
                            type_map["LookupDatasetsSearchInput"],
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "downloadUrls": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DatasetDownloadUrlsResponse"])
                ),
                args={
                    "datasetId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "validateDataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetValidation"])),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType, type_map["ValidateDatasetInput"]
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "isLastUpdate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={
                    "updateJob": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetUpdateJobIdentifier"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingsSessionSnapshot": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetModel"])),
                args={
                    "data": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetEmbeddingSessionSnapshotInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "projectPermissions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["ProjectPermission"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "homepageStatistics": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["HomepageStatisticsResponse"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lookupLabelCategories": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["LabelCategory"])
                        )
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["SearchOptionsInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType,
                            type_map["LookupLabelCategoriesSearch"],
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "lookupTissueTerms": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["TissueTerm"]))
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType, type_map["LookupTissueTermsOptions"]
                        ),
                        default_value={"offset": 0.0, "limit": 100.0},
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType, type_map["LookupTissueTermsSearch"]
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "project": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "projectId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CapUser": GraphQLObjectType(
        name="CapUser",
        description=None,
        interfaces=[],
        fields=lambda: {
            "uid": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "displayName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "tempDisplayName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "avatarUrl": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "bio": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "location": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "firstName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lastName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "institution": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labUrl": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "orcidId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "username": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason="Will be removed soon",
            ),
            "projects": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isSuperUser": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Project": GraphQLObjectType(
        name="Project",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "version": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isPlaceholder": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "contactEmail": GraphQLField(
                GraphQLString,
                args={},
                description=None,
                deprecation_reason="Will be replaced with 'contactEmails'",
            ),
            "contactEmails": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "externalUrl": GraphQLField(
                GraphQLString,
                args={},
                description=None,
                deprecation_reason="Will be replaced with 'externalUrls'",
            ),
            "externalUrls": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "contactName": GraphQLField(
                GraphQLString,
                args={},
                description=None,
                deprecation_reason="Will be replaced with 'contactNames'",
            ),
            "contactNames": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "journalDoi": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rawDataUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "lastUpdatedByUid": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedBy": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ownerUid": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "doi": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "owner": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "capAuthors": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "datasets": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "versions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "permissions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["ProjectPermission"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "canPublish": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DateTime": GraphQLScalarType(
        name="DateTime", description=None, specified_by_url=None
    ),
    "Dataset": GraphQLObjectType(
        name="Dataset",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "projectId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "isAnnDataUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUrlUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isEmbeddingsUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "geneCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "defaultEmbedding": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "errors": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetErrorGQL"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "project": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lastUpdateJob": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetUpdateJob"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["Labelset"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "seuratStatus": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DatasetSeuratStatusResponse"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embeddingsCellCount": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embeddings": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["EmbeddingGroup"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embeddingData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["EmbeddingData"])),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetDatasetEmbeddingDataInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingSelectionObs": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLInt))),
                args={
                    "selection": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetDatasetEmbeddingSelectionObsInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingClusters": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["EmbeddingClusters"])
                        )
                    )
                ),
                args={
                    "cluster": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetDatasetClustersDataInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingClusterTypes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["EmbeddingClusterType"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embeddingClustersObs": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLInt))),
                args={
                    "cluster": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetDatasetClustersObsInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiff": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetEmbeddingDiffInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingSingleSelectionKey": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["PostSingleSelectionKeyInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiffHeatMap": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Heatmap"])),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["PostHeatmapInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingClusteredHeatMap": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ClusteredHeatmap"])),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["PostClusteredHeatmapInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingHighlyVariableGenesCsv": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetHighlyVariableGenesCsvInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingObsDetails": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ObsDetails"])),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetObsDetailsInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiffGenesBySelectionCsv": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetGenesBySelectionCsvInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiffGenes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["GeneRow"]))
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetGenesInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingHighlyVariableGenes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["HighlyVariableGeneRow"])
                        )
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetHighlyVariableGenesInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiffGenesBySelection": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["GenesRows"]))
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetGenesBySelectionInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingDiffKeygen": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetEmbeddingDiffKeygenInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingValidateSelection": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ComplexSelection"])),
                args={
                    "selection": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["ValidateSelectionInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingsObsCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={
                    "selection": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetEmbeddingsObsCountInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingsSankeyDiagram": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Sankey"])),
                args={
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["GetSankeyDiagramInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "embeddingsMolecularData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StandardResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetErrorGQL": GraphQLObjectType(
        name="DatasetErrorGQL",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "type": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "message": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "info": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSONScalar"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "JSONScalar": GraphQLScalarType(
        name="JSONScalar", description=None, specified_by_url=None
    ),
    "DatasetUpdateJob": GraphQLObjectType(
        name="DatasetUpdateJob",
        description=None,
        interfaces=[],
        fields=lambda: {
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "reason": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rolledBackAt": GraphQLField(
                cast(GraphQLScalarType, type_map["DateTime"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "processedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["DateTime"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Labelset": GraphQLObjectType(
        name="Labelset",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "datasetId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "mode": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "annotationMethod": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmVersion": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmRepoUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceLocation": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceDescription": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "version": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "labels": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "dataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Label": GraphQLObjectType(
        name="Label",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelsetId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "count": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isActive": GraphQLField(
                GraphQLBoolean,
                args={},
                description=None,
                deprecation_reason="Unused property, will be removed soon",
            ),
            "color": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "deletedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["DateTime"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "polygon": GraphQLField(
                cast(GraphQLObjectType, type_map["PolygonCoord"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermExists": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermExists": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyAssessment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "fullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationale": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationaleDois": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "canonicalMarkerGenes": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "relations": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["LabelRelation"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Labelset"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "feedbacks": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["LabelFeedback"])
                        )
                    )
                ),
                args={
                    "options": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType, type_map["ListLabelFeedbackOptions"]
                        ),
                        default_value={"limit": 50.0, "offset": 0.0, "sortDir": "desc"},
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "scores": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["LabelScores"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "PolygonCoord": GraphQLObjectType(
        name="PolygonCoord",
        description=None,
        interfaces=[],
        fields=lambda: {
            "x": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "y": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelRelation": GraphQLObjectType(
        name="LabelRelation",
        description=None,
        interfaces=[],
        fields=lambda: {
            "label": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelFeedback": GraphQLObjectType(
        name="LabelFeedback",
        description=None,
        interfaces=[],
        fields=lambda: {
            "score": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "explanation": GraphQLField(
                cast(GraphQLObjectType, type_map["LabelFeedbackExplanation"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isUpdated": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "user": GraphQLField(
                cast(GraphQLObjectType, type_map["CapUser"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "label": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelFeedbackExplanation": GraphQLObjectType(
        name="LabelFeedbackExplanation",
        description=None,
        interfaces=[],
        fields=lambda: {
            "type": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "data": GraphQLField(
                cast(GraphQLUnionType, type_map["ExplanationData"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ExplanationData": GraphQLUnionType(
        name="ExplanationData",
        description=None,
        types=lambda: cast(
            List[GraphQLObjectType],
            [
                type_map["FeedbackExplanationDataMerge"],
                type_map["FeedbackExplanationDataRefine"],
                type_map["FeedbackExplanationDataComment"],
                type_map["FeedbackExplanationDataSplit"],
            ],
        ),
    ),
    "FeedbackExplanationDataMerge": GraphQLObjectType(
        name="FeedbackExplanationDataMerge",
        description=None,
        interfaces=[],
        fields=lambda: {
            "comment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "labelIds": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackExplanationDataRefine": GraphQLObjectType(
        name="FeedbackExplanationDataRefine",
        description=None,
        interfaces=[],
        fields=lambda: {
            "changes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(
                                GraphQLObjectType,
                                type_map["FeedbackExplanationDataRefineChanges"],
                            )
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "FeedbackExplanationDataRefineChanges": GraphQLObjectType(
        name="FeedbackExplanationDataRefineChanges",
        description=None,
        interfaces=[],
        fields=lambda: {
            "attribute": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "newValue": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["AnyScalar"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "originalValue": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["AnyScalar"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AnyScalar": GraphQLScalarType(
        name="AnyScalar", description=None, specified_by_url=None
    ),
    "FeedbackExplanationDataComment": GraphQLObjectType(
        name="FeedbackExplanationDataComment",
        description=None,
        interfaces=[],
        fields=lambda: {
            "comment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            )
        },
    ),
    "FeedbackExplanationDataSplit": GraphQLObjectType(
        name="FeedbackExplanationDataSplit",
        description=None,
        interfaces=[],
        fields=lambda: {
            "comment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "labelsNumber": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLObjectType,
                            type_map["FeedbackExplanationDataSplitLabels"],
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackExplanationDataSplitLabels": GraphQLObjectType(
        name="FeedbackExplanationDataSplitLabels",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ListLabelFeedbackOptions": GraphQLInputObjectType(
        name="ListLabelFeedbackOptions",
        description=None,
        fields=lambda: {
            "limit": GraphQLInputField(
                GraphQLFloat,
                default_value=50.0,
                description=None,
                deprecation_reason=None,
            ),
            "offset": GraphQLInputField(
                GraphQLFloat,
                default_value=0.0,
                description=None,
                deprecation_reason=None,
            ),
            "sortDir": GraphQLInputField(
                GraphQLString,
                default_value="desc",
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelScores": GraphQLObjectType(
        name="LabelScores",
        description=None,
        interfaces=[],
        fields=lambda: {
            "average": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "agree": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "disagree": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idk": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "total": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetSeuratStatusResponse": GraphQLObjectType(
        name="DatasetSeuratStatusResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "failedReason": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "processedOn": GraphQLField(
                cast(GraphQLScalarType, type_map["DateTime"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "timestamp": GraphQLField(
                cast(GraphQLScalarType, type_map["DateTime"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EmbeddingGroup": GraphQLObjectType(
        name="EmbeddingGroup",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cellCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EmbeddingData": GraphQLObjectType(
        name="EmbeddingData",
        description=None,
        interfaces=[],
        fields=lambda: {
            "obsIds": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLInt))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "embeddings": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["EmbeddingMap"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "geneExpression": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLFloat))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "inSelectionMajor": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLBoolean))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "inSelectionMinor": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLBoolean))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "annotations": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(
                                GraphQLObjectType,
                                type_map["EmbeddingDataAnnotationItem"],
                            )
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EmbeddingMap": GraphQLObjectType(
        name="EmbeddingMap",
        description=None,
        interfaces=[],
        fields=lambda: {
            "x": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "y": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EmbeddingDataAnnotationItem": GraphQLObjectType(
        name="EmbeddingDataAnnotationItem",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "items": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelIds": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetDatasetEmbeddingDataInput": GraphQLInputObjectType(
        name="GetDatasetEmbeddingDataInput",
        description=None,
        fields=lambda: {
            "embedding": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionGene": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "scaleMaxPlan": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionKeyMajor": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionKeyMinor": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetDatasetEmbeddingSelectionObsInput": GraphQLInputObjectType(
        name="GetDatasetEmbeddingSelectionObsInput",
        description=None,
        fields=lambda: {
            "selectionKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "EmbeddingClusters": GraphQLObjectType(
        name="EmbeddingClusters",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cellCount": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "color": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "clusterId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetDatasetClustersDataInput": GraphQLInputObjectType(
        name="GetDatasetClustersDataInput",
        description=None,
        fields=lambda: {
            "clusterType": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "EmbeddingClusterType": GraphQLObjectType(
        name="EmbeddingClusterType",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "groupsCount": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetDatasetClustersObsInput": GraphQLInputObjectType(
        name="GetDatasetClustersObsInput",
        description=None,
        fields=lambda: {
            "clusterType": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "clusterIds": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetEmbeddingDiffInput": GraphQLInputObjectType(
        name="GetEmbeddingDiffInput",
        description=None,
        fields=lambda: {
            "currentSelectionKey": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "backgroundSelectionsKey": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "cancel": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "downsamplingAllowed": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "randomSeed": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "PostSingleSelectionKeyInput": GraphQLInputObjectType(
        name="PostSingleSelectionKeyInput",
        description=None,
        fields=lambda: {
            "selection": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["SelectionType"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "SelectionType": GraphQLInputObjectType(
        name="SelectionType",
        description=None,
        fields=lambda: {
            "multiPolygon": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["MultiPolygonSelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotation": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["AnnotationSelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "hcSelection": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["HCSelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelIdSelection": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["LabelIdSelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "remainingSelection": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["RemainingSelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "keySelection": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["KeySelection"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "MultiPolygonSelection": GraphQLInputObjectType(
        name="MultiPolygonSelection",
        description=None,
        fields=lambda: {
            "coordinates": GraphQLInputField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GeoCoordinates"])
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GeoCoordinates": GraphQLInputObjectType(
        name="GeoCoordinates",
        description=None,
        fields=lambda: {
            "coords": GraphQLInputField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            GraphQLList(
                                GraphQLNonNull(
                                    GraphQLList(GraphQLNonNull(GraphQLFloat))
                                )
                            )
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "AnnotationSelection": GraphQLInputObjectType(
        name="AnnotationSelection",
        description=None,
        fields=lambda: {
            "column": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selection": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "HCSelection": GraphQLInputObjectType(
        name="HCSelection",
        description=None,
        fields=lambda: {
            "parentSelectionKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "obsPerPixel": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "genesPerPixel": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "left": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "right": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelIdSelection": GraphQLInputObjectType(
        name="LabelIdSelection",
        description=None,
        fields=lambda: {
            "labelId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "RemainingSelection": GraphQLInputObjectType(
        name="RemainingSelection",
        description=None,
        fields=lambda: {
            "labelset": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "KeySelection": GraphQLInputObjectType(
        name="KeySelection",
        description=None,
        fields=lambda: {
            "selectionKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "Heatmap": GraphQLObjectType(
        name="Heatmap",
        description=None,
        interfaces=[],
        fields=lambda: {
            "annotations": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["AnnotationsObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "genes": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["GenesObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "obsIds": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ObsIDSObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "scores": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ScoresObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isInSelections": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["IsInSelectionsObject"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "topGenesBySelection": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(
                                GraphQLObjectType,
                                type_map["HeatmapTopGenesBySelection"],
                            )
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AnnotationsObject": GraphQLObjectType(
        name="AnnotationsObject",
        description=None,
        interfaces=[],
        fields=lambda: {
            "data": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "GenesObject": GraphQLObjectType(
        name="GenesObject",
        description=None,
        interfaces=[],
        fields=lambda: {
            "data": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ObsIDSObject": GraphQLObjectType(
        name="ObsIDSObject",
        description=None,
        interfaces=[],
        fields=lambda: {
            "data": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLInt))),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ScoresObject": GraphQLObjectType(
        name="ScoresObject",
        description=None,
        interfaces=[],
        fields=lambda: {
            "data": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLFloat))),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "IsInSelectionsObject": GraphQLObjectType(
        name="IsInSelectionsObject",
        description=None,
        interfaces=[],
        fields=lambda: {
            "data": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLBoolean))),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "HeatmapTopGenesBySelection": GraphQLObjectType(
        name="HeatmapTopGenesBySelection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "selectionName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "genes": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "PostHeatmapInput": GraphQLInputObjectType(
        name="PostHeatmapInput",
        description=None,
        fields=lambda: {
            "diffKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "nGenes": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "scaleMaxPlan": GraphQLInputField(
                GraphQLFloat,
                default_value=500.0,
                description=None,
                deprecation_reason=None,
            ),
            "genesFilter": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "useGenesPattern": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "includeReferenceSelection": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionKey": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ClusteredHeatmap": GraphQLObjectType(
        name="ClusteredHeatmap",
        description=None,
        interfaces=[],
        fields=lambda: {
            "annotations": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["AnnotationsObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "genes": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["GenesObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "obsIds": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ObsIDSObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "scores": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ScoresObject"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "PostClusteredHeatmapInput": GraphQLInputObjectType(
        name="PostClusteredHeatmapInput",
        description=None,
        fields=lambda: {
            "obsPerPixel": GraphQLInputField(
                GraphQLFloat,
                default_value=100.0,
                description=None,
                deprecation_reason=None,
            ),
            "genesPerPixel": GraphQLInputField(
                GraphQLFloat,
                default_value=100.0,
                description=None,
                deprecation_reason=None,
            ),
            "selectionKey": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelset": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "cancel": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetHighlyVariableGenesCsvInput": GraphQLInputObjectType(
        name="GetHighlyVariableGenesCsvInput",
        description=None,
        fields=lambda: {
            "geneNameFilter": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortBy": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortOrder": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ObsDetails": GraphQLObjectType(
        name="ObsDetails",
        description=None,
        interfaces=[],
        fields=lambda: {
            "point": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["ObsDetailsResponsePoint"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ObsDetailsResponsePoint": GraphQLObjectType(
        name="ObsDetailsResponsePoint",
        description=None,
        interfaces=[],
        fields=lambda: {
            "x": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "y": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetObsDetailsInput": GraphQLInputObjectType(
        name="GetObsDetailsInput",
        description=None,
        fields=lambda: {
            "obsId": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetGenesBySelectionCsvInput": GraphQLInputObjectType(
        name="GetGenesBySelectionCsvInput",
        description=None,
        fields=lambda: {
            "diffKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "geneNameFilter": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionNames": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortBy": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortOrder": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GeneRow": GraphQLObjectType(
        name="GeneRow",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "score": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "logFoldChange": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "pValue": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "dispersion": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "highlyVariable": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "GetGenesInput": GraphQLInputObjectType(
        name="GetGenesInput",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "diffKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "geneNameFilter": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortBy": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortOrder": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "HighlyVariableGeneRow": GraphQLObjectType(
        name="HighlyVariableGeneRow",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "dispersion": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "highlyVariable": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "GetHighlyVariableGenesInput": GraphQLInputObjectType(
        name="GetHighlyVariableGenesInput",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "geneNameFilter": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortBy": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortOrder": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GenesRows": GraphQLObjectType(
        name="GenesRows",
        description=None,
        interfaces=[],
        fields=lambda: {
            "selection": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "genes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["GeneRow"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetGenesBySelectionInput": GraphQLInputObjectType(
        name="GetGenesBySelectionInput",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "diffKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "geneNameFilter": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selectionNames": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortBy": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sortOrder": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetEmbeddingDiffKeygenInput": GraphQLInputObjectType(
        name="GetEmbeddingDiffKeygenInput",
        description=None,
        fields=lambda: {
            "selectionType": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "downsamplingAllowed": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "randomSeed": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ComplexSelection": GraphQLObjectType(
        name="ComplexSelection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "msg": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "selectionKey": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "pointsCount": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ValidateSelectionInput": GraphQLInputObjectType(
        name="ValidateSelectionInput",
        description=None,
        fields=lambda: {
            "currentSelectionKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "previousSelectionsKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetEmbeddingsObsCountInput": GraphQLInputObjectType(
        name="GetEmbeddingsObsCountInput",
        description=None,
        fields=lambda: {
            "selectionKey": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "Sankey": GraphQLObjectType(
        name="Sankey",
        description=None,
        interfaces=[],
        fields=lambda: {
            "links": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["SankeyDataLink"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "nodes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["SankeyDataNode"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "SankeyDataLink": GraphQLObjectType(
        name="SankeyDataLink",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "count": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "source": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "source_id": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "target": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "target_id": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "SankeyDataNode": GraphQLObjectType(
        name="SankeyDataNode",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "title": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetSankeyDiagramInput": GraphQLInputObjectType(
        name="GetSankeyDiagramInput",
        description=None,
        fields=lambda: {
            "columns": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "StandardResponse": GraphQLObjectType(
        name="StandardResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "msg": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "error": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "ProjectPermission": GraphQLObjectType(
        name="ProjectPermission",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "userUid": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "role": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["ApiClientRole"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isActive": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "project": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "user": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ApiClientRole": GraphQLScalarType(
        name="ApiClientRole", description=None, specified_by_url=None
    ),
    "SearchOptionsInput": GraphQLInputObjectType(
        name="SearchOptionsInput",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupUsersSearchInput": GraphQLInputObjectType(
        name="LookupUsersSearchInput",
        description=None,
        fields=lambda: {
            "displayName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "GetLabelInput": GraphQLInputObjectType(
        name="GetLabelInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "LabelSynonym": GraphQLObjectType(
        name="LabelSynonym",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "originalName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupSynonymsSearch": GraphQLInputObjectType(
        name="LookupSynonymsSearch",
        description=None,
        fields=lambda: {
            "originalName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "CellLabelsSearchOptions": GraphQLInputObjectType(
        name="CellLabelsSearchOptions",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sort": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["CellLabelsSearchSort"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CellLabelsSearchSort": GraphQLInputObjectType(
        name="CellLabelsSearchSort",
        description=None,
        fields=lambda: {
            "field": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "order": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupLabelsFilters": GraphQLInputObjectType(
        name="LookupLabelsFilters",
        description=None,
        fields=lambda: {
            "metadata": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["SearchLabelByMetadataArgs"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "SearchLabelByMetadataArgs": GraphQLInputObjectType(
        name="SearchLabelByMetadataArgs",
        description=None,
        fields=lambda: {
            "field": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "values": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupCellsSearch": GraphQLInputObjectType(
        name="LookupCellsSearch",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fields": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GroupedMetadataResponse": GraphQLObjectType(
        name="GroupedMetadataResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "group": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "metadata": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(
                                GraphQLObjectType,
                                type_map["DatasetMetadataCountResponse"],
                            )
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetMetadataCountResponse": GraphQLObjectType(
        name="DatasetMetadataCountResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "count": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "fieldValue": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UploadResponse": GraphQLObjectType(
        name="UploadResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "fileName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "error": GraphQLField(
                GraphQLString,
                args={},
                description=None,
                deprecation_reason="Will be removed after FE implementation of multiple uploads",
            ),
            "projectId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "uploaderUid": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "uploader": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "project": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "errors": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["UploadErrorItem"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UploadErrorItem": GraphQLObjectType(
        name="UploadErrorItem",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "error": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "message": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "meta": GraphQLField(
                cast(GraphQLScalarType, type_map["JSONScalar"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UploadIdentifier": GraphQLInputObjectType(
        name="UploadIdentifier",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DatasetLookupResponse": GraphQLObjectType(
        name="DatasetLookupResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "projectId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["DateTime"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUrlUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isEmbeddingsUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rawDataUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "annDataUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "errors": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetErrorGQL"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "geneCount": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "highlight": GraphQLField(
                cast(GraphQLObjectType, type_map["DatasetsHighlight"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "project": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["Labelset"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lastUpdateJob": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetUpdateJob"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetsHighlight": GraphQLObjectType(
        name="DatasetsHighlight",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "projectName": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "projectDescription": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetSearchOptions": GraphQLInputObjectType(
        name="DatasetSearchOptions",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sort": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["DatasetSearchSort"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetSearchSort": GraphQLInputObjectType(
        name="DatasetSearchSort",
        description=None,
        fields=lambda: {
            "field": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "order": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupDatasetsFiltersInput": GraphQLInputObjectType(
        name="LookupDatasetsFiltersInput",
        description=None,
        fields=lambda: {
            "metadata": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["SearchByMetadataArgs"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelset": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "SearchByMetadataArgs": GraphQLInputObjectType(
        name="SearchByMetadataArgs",
        description=None,
        fields=lambda: {
            "field": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "values": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupDatasetsSearchInput": GraphQLInputObjectType(
        name="LookupDatasetsSearchInput",
        description=None,
        fields=lambda: {
            "cellTypes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "projectName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "projectDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetDownloadUrlsResponse": GraphQLObjectType(
        name="DatasetDownloadUrlsResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "seuratUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "annDataUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "capJsonUrlZip": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "capJsonUrlTar": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "isAnnDataUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUrlUpToDate": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetValidation": GraphQLObjectType(
        name="DatasetValidation",
        description=None,
        interfaces=[],
        fields=lambda: {
            "msg": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "error": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "data": GraphQLField(
                cast(GraphQLObjectType, type_map["DatasetValidationResult"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetValidationResult": GraphQLObjectType(
        name="DatasetValidationResult",
        description=None,
        interfaces=[],
        fields=lambda: {
            "dataset": GraphQLField(
                cast(GraphQLObjectType, type_map["DatasetValidationResultData"]),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DatasetValidationResultData": GraphQLObjectType(
        name="DatasetValidationResultData",
        description=None,
        interfaces=[],
        fields=lambda: {
            "errors": GraphQLField(
                cast(GraphQLObjectType, type_map["DatasetValidatioNResultErrors"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["LabelsetValidationResult"])
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetValidatioNResultErrors": GraphQLObjectType(
        name="DatasetValidatioNResultErrors",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "labelsetsCount": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "LabelsetValidationResult": GraphQLObjectType(
        name="LabelsetValidationResult",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "errors": GraphQLField(
                cast(GraphQLObjectType, type_map["LabelsetValidationResultErrors"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["LabelValidationResult"])
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelsetValidationResultErrors": GraphQLObjectType(
        name="LabelsetValidationResultErrors",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "cellCount": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "emptyValues": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "annotationMethod": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmVersion": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmRepoUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceLocation": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceDescription": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "LabelValidationResult": GraphQLObjectType(
        name="LabelValidationResult",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "errors": GraphQLField(
                cast(GraphQLObjectType, type_map["LabelValidationResultErrors"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelValidationResultErrors": GraphQLObjectType(
        name="LabelValidationResultErrors",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "fullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermExists": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationale": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "markerGenes": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "synonyms": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryFullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermExists": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyAssessment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "canonicalMarkerGenes": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationaleDois": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "count": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "ValidateDatasetInput": GraphQLInputObjectType(
        name="ValidateDatasetInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "defaultEmbedding": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType, type_map["EditNestedLabelsetInput"]
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditNestedLabelsetInput": GraphQLInputObjectType(
        name="EditNestedLabelsetInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotationMethod": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmVersion": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmRepoUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceLocation": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "version": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["EditNestedLabelInput"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditNestedLabelInput": GraphQLInputObjectType(
        name="EditNestedLabelInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "color": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "count": GraphQLInputField(
                GraphQLInt,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isActive": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "polygon": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["NestedLabelMultiPolygonInput"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyAssessment": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationale": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationaleDois": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalMarkerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "NestedLabelMultiPolygonInput": GraphQLInputObjectType(
        name="NestedLabelMultiPolygonInput",
        description=None,
        fields=lambda: {
            "selections": GraphQLInputField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["NestedLabelMultiPolygonSelectionInput"],
                            )
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "NestedLabelMultiPolygonSelectionInput": GraphQLInputObjectType(
        name="NestedLabelMultiPolygonSelectionInput",
        description=None,
        fields=lambda: {
            "type": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "polygonCoord": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["PolygonCoordInput"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "column": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "selection": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "PolygonCoordInput": GraphQLInputObjectType(
        name="PolygonCoordInput",
        description=None,
        fields=lambda: {
            "x": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "y": GraphQLInputField(
                GraphQLNonNull(GraphQLFloat),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetUpdateJobIdentifier": GraphQLInputObjectType(
        name="DatasetUpdateJobIdentifier",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DatasetModel": GraphQLObjectType(
        name="DatasetModel",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cellCount": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "datasetType": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "labelsets": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["LabelsetModel"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "LabelsetModel": GraphQLObjectType(
        name="LabelsetModel",
        description=None,
        interfaces=[],
        fields=lambda: {
            "algorithmName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmRepoUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "algorithmVersion": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "annotationMethod": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "embedding": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "labels": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["LabelModel"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceDescription": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "referenceLocation": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "LabelModel": GraphQLObjectType(
        name="LabelModel",
        description=None,
        interfaces=[],
        fields=lambda: {
            "canonicalMarkerGenes": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermExists": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "count": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "fullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "markerGenes": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyAssessment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermExists": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "ontologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationale": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "rationaleDois": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "GetEmbeddingSessionSnapshotInput": GraphQLInputObjectType(
        name="GetEmbeddingSessionSnapshotInput",
        description=None,
        fields=lambda: {
            "datasetId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "HomepageStatisticsResponse": GraphQLObjectType(
        name="HomepageStatisticsResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cells": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "datasets": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "organisms": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "projects": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "tissues": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["StateResponse"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "StateResponse": GraphQLObjectType(
        name="StateResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "total": GraphQLField(
                GraphQLNonNull(GraphQLInt),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "LabelCategory": GraphQLObjectType(
        name="LabelCategory",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermExists": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTerm": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "categoryOntologyTermId": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "LookupLabelCategoriesSearch": GraphQLInputObjectType(
        name="LookupLabelCategoriesSearch",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "TissueTerm": GraphQLObjectType(
        name="TissueTerm",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lowerTerms": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["TissueLowerTerm"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "TissueLowerTerm": GraphQLObjectType(
        name="TissueLowerTerm",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupTissueTermsOptions": GraphQLInputObjectType(
        name="LookupTissueTermsOptions",
        description=None,
        fields=lambda: {
            "offset": GraphQLInputField(
                GraphQLFloat,
                default_value=0.0,
                description=None,
                deprecation_reason=None,
            ),
            "limit": GraphQLInputField(
                GraphQLFloat,
                default_value=100.0,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LookupTissueTermsSearch": GraphQLInputObjectType(
        name="LookupTissueTermsSearch",
        description=None,
        fields=lambda: {
            "value": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fields": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Mutation": GraphQLObjectType(
        name="Mutation",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createUser": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={
                    "user": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["CreateUserArg"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "editUser": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={
                    "user": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["EditUserArg"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "updateAvatarUploadStatus": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["OperationResultResponse"])
                ),
                args={
                    "objectId": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "uid": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "ok": GraphQLArgument(
                        GraphQLNonNull(GraphQLBoolean),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "url": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "status": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "deleteCapUser": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["OperationResultResponse"])
                ),
                args={
                    "uid": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "resetPassword": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["OperationResultResponse"])
                ),
                args={
                    "params": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["ResetCapUserPasswordInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "editLabel": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Label"])),
                args={
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["EditLabelInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "saveFeedback": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["LabelFeedback"])
                        )
                    )
                ),
                args={
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetLabelInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "feedbacks": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["CreateLabelFeedbackInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "deleteFeedback": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["OperationResult"])),
                args={
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetLabelInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "deleteRefinement": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["OperationResult"])),
                args={
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["GetLabelInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "editLabelset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Labelset"])),
                args={
                    "info": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["EditLabelsetInfoInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "labelset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["EditLabelsetInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "createLabelsets": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Labelset"]))
                    )
                ),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "labelsets": GraphQLArgument(
                        GraphQLNonNull(
                            GraphQLList(
                                GraphQLNonNull(
                                    cast(
                                        GraphQLInputObjectType,
                                        type_map["CreateNestedLabelsetInput"],
                                    )
                                )
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "createUpload": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["UploadResponse"])),
                args={
                    "uploader": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["UploadUploader"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "upload": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["UploadPayload"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "updateUpload": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["UploadResponse"])),
                args={
                    "upload": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType, type_map["UpdateUploadPayload"]
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "createDataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "info": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType, type_map["CreateDatasetInfoInput"]
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["CreateDatasetInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "editDataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "info": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["EditDatasetInfoInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["EditDatasetInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "editDatasetCore": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "info": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["EditDatasetInfoInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["EditDatasetCoreFieldsInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "reportProcessingStarted": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["OperationResultResponse"])
                ),
                args={
                    "job": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["ReportDatasetUpdateInProgressInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "reportUpdateFailure": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["OperationResultResponse"])
                ),
                args={
                    "failure": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["ReportDatasetUpdateFailureInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "editDatasetEmbeddings": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "embeddings": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["EditDatasetEmbeddingsInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason="Use editDatasetCore mutation instead",
            ),
            "deleteDataset": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DeleteResultResponse"])
                ),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["DeleteDatasetInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "saveCorteges": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["OperationResult"])),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["SaveDatasetLabelCortegesInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "datasetClusteredHeatmapResult": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["OperationResult"])),
                args={
                    "error": GraphQLArgument(
                        cast(
                            GraphQLInputObjectType,
                            type_map["ClusteredHeatmapErrorInput"],
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "heatmap": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["ClusteredHeatmapInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "saveEmbeddingSession": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetModel"])),
                args={
                    "data": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["PostSaveEmbeddingSessionInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "modifyLabelsetSessionData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetModel"])),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "action": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "sessionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "labelset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType, type_map["LabelsetObjectInput"]
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "modifyLabelSessionData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["DatasetModel"])),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "action": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "sessionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "label": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["LabelObjectInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "selectionKey": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "labelsetId": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "startAsyncHC": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DatasetAsyncHCStartResponse"])
                ),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["PostClusteredHeatmapInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "cancelAsyncHC": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DatasetAsyncHCStartResponse"])
                ),
                args={
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "options": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["CancelClusteredHeatmapInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "configureDebugger": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["OperationResult"])),
                args={
                    "levels": GraphQLArgument(
                        GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "createProject": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["CreateProjectInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "editProject": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["EditProjectInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "addRole": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ProjectPermission"])),
                args={
                    "permission": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["AddPermissionInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "inviteByEmail": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ProjectPermission"])),
                args={
                    "permission": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["InviteByEmailInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "deleteRole": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DeleteResultResponse"])
                ),
                args={
                    "permission": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["RemovePermissionInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "deleteProject": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["DeleteProjectResponse"])
                ),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["DeleteProjectInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "approveInvitation": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["ApproveInvitationResponse"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createPublication": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["CreatePublicationInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "reviewProjectRequest": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["ReviewProjectRequestInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "declineProjectReview": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DeclineProjectReviewInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "cancelProjectReview": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["CancelProjectReviewInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateUserArg": GraphQLInputObjectType(
        name="CreateUserArg",
        description=None,
        fields=lambda: {
            "uid": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "displayName": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "bio": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "location": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "avatarUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isTempDisplayName": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "firstName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "lastName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "institution": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "orcidId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditUserArg": GraphQLInputObjectType(
        name="EditUserArg",
        description=None,
        fields=lambda: {
            "uid": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "displayName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "bio": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "location": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "avatarUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isTempDisplayName": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "firstName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "lastName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "institution": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "orcidId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "OperationResultResponse": GraphQLObjectType(
        name="OperationResultResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "ok": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ResetCapUserPasswordInput": GraphQLInputObjectType(
        name="ResetCapUserPasswordInput",
        description=None,
        fields=lambda: {
            "resetLink": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "newPassword": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "uid": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditLabelInput": GraphQLInputObjectType(
        name="EditLabelInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationale": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationaleDois": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalMarkerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyAssessment": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateLabelFeedbackInput": GraphQLInputObjectType(
        name="CreateLabelFeedbackInput",
        description=None,
        fields=lambda: {
            "score": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "explanation": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["LabelFeedbackExplanationInput"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelFeedbackExplanationInput": GraphQLInputObjectType(
        name="LabelFeedbackExplanationInput",
        description=None,
        fields=lambda: {
            "type": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLEnumType, type_map["FeedbackExplanationType"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "data": GraphQLInputField(
                cast(GraphQLInputObjectType, type_map["FeedbackExplanationDataInput"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackExplanationType": GraphQLEnumType(
        name="FeedbackExplanationType",
        description=None,
        values={
            "agree": GraphQLEnumValue(
                value="agree", description=None, deprecation_reason=None
            ),
            "disagree": GraphQLEnumValue(
                value="disagree", description=None, deprecation_reason=None
            ),
            "split": GraphQLEnumValue(
                value="split", description=None, deprecation_reason=None
            ),
            "merge": GraphQLEnumValue(
                value="merge", description=None, deprecation_reason=None
            ),
            "refine": GraphQLEnumValue(
                value="refine", description=None, deprecation_reason=None
            ),
            "idk": GraphQLEnumValue(
                value="idk", description=None, deprecation_reason=None
            ),
        },
    ),
    "FeedbackExplanationDataInput": GraphQLInputObjectType(
        name="FeedbackExplanationDataInput",
        description=None,
        fields=lambda: {
            "changes": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["FeedbackExplanationDataRefineChangesInput"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "comment": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelIds": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsNumber": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["FeedbackExplanationSplitLabels"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackExplanationDataRefineChangesInput": GraphQLInputObjectType(
        name="FeedbackExplanationDataRefineChangesInput",
        description=None,
        fields=lambda: {
            "attribute": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "newValue": GraphQLInputField(
                cast(GraphQLScalarType, type_map["AnyScalar"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "originalValue": GraphQLInputField(
                cast(GraphQLScalarType, type_map["AnyScalar"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackExplanationSplitLabels": GraphQLInputObjectType(
        name="FeedbackExplanationSplitLabels",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "OperationResult": GraphQLObjectType(
        name="OperationResult",
        description=None,
        interfaces=[],
        fields=lambda: {
            "ok": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "msg": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "EditLabelsetInfoInput": GraphQLInputObjectType(
        name="EditLabelsetInfoInput",
        description=None,
        fields=lambda: {
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "EditLabelsetInput": GraphQLInputObjectType(
        name="EditLabelsetInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotationMethod": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmVersion": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmRepoUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceLocation": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "version": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetIdentifierInput": GraphQLInputObjectType(
        name="DatasetIdentifierInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "CreateNestedLabelsetInput": GraphQLInputObjectType(
        name="CreateNestedLabelsetInput",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotationMethod": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmVersion": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmRepoUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceLocation": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLInputField(
                GraphQLString,
                default_value="cell-labels",
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelCount": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "version": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["CreateNestedLabelInput"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateNestedLabelInput": GraphQLInputObjectType(
        name="CreateNestedLabelInput",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "color": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "count": GraphQLInputField(
                GraphQLNonNull(GraphQLInt),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationale": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationaleDois": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyAssessment": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalMarkerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UploadUploader": GraphQLInputObjectType(
        name="UploadUploader",
        description=None,
        fields=lambda: {
            "uid": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "UploadPayload": GraphQLInputObjectType(
        name="UploadPayload",
        description=None,
        fields=lambda: {
            "fileName": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "projectId": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UpdateUploadPayload": GraphQLInputObjectType(
        name="UpdateUploadPayload",
        description=None,
        fields=lambda: {
            "status": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "errors": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["UpdateUploadErrorItemPayload"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "UpdateUploadErrorItemPayload": GraphQLInputObjectType(
        name="UpdateUploadErrorItemPayload",
        description=None,
        fields=lambda: {
            "message": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "error": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "meta": GraphQLInputField(
                cast(GraphQLScalarType, type_map["JSONScalar"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateDatasetInfoInput": GraphQLInputObjectType(
        name="CreateDatasetInfoInput",
        description=None,
        fields=lambda: {
            "userUid": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "uploadId": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "overwrite": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateDatasetInput": GraphQLInputObjectType(
        name="CreateDatasetInput",
        description=None,
        fields=lambda: {
            "projectId": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annDataUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrlZip": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrlTar": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLInputField(
                GraphQLNonNull(GraphQLInt),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "geneCount": GraphQLInputField(
                GraphQLNonNull(GraphQLInt),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["CreateNestedLabelsetInput"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditDatasetInfoInput": GraphQLInputObjectType(
        name="EditDatasetInfoInput",
        description=None,
        fields=lambda: {
            "jobId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditDatasetInput": GraphQLInputObjectType(
        name="EditDatasetInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "defaultEmbedding": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType, type_map["EditNestedLabelsetInput"]
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditDatasetCoreFieldsInput": GraphQLInputObjectType(
        name="EditDatasetCoreFieldsInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrlZip": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrlTar": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annDataUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "seuratUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUpToDate": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isAnnDataUrlUpToDate": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "isEmbeddingsUpToDate": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ReportDatasetUpdateInProgressInput": GraphQLInputObjectType(
        name="ReportDatasetUpdateInProgressInput",
        description=None,
        fields=lambda: {
            "jobId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ReportDatasetUpdateFailureInput": GraphQLInputObjectType(
        name="ReportDatasetUpdateFailureInput",
        description=None,
        fields=lambda: {
            "reason": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "jobId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "retry": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditDatasetEmbeddingsInput": GraphQLInputObjectType(
        name="EditDatasetEmbeddingsInput",
        description=None,
        fields=lambda: {
            "annDataUrl": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DeleteResultResponse": GraphQLObjectType(
        name="DeleteResultResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "msg": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DeleteDatasetInput": GraphQLInputObjectType(
        name="DeleteDatasetInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "SaveDatasetLabelCortegesInput": GraphQLInputObjectType(
        name="SaveDatasetLabelCortegesInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "corteges": GraphQLInputField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLScalarType, type_map["KeyValue"]))
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "KeyValue": GraphQLScalarType(
        name="KeyValue", description=None, specified_by_url=None
    ),
    "ClusteredHeatmapErrorInput": GraphQLInputObjectType(
        name="ClusteredHeatmapErrorInput",
        description=None,
        fields=lambda: {
            "message": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ClusteredHeatmapInput": GraphQLInputObjectType(
        name="ClusteredHeatmapInput",
        description=None,
        fields=lambda: {
            "annotations": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLInputObjectType, type_map["AnnotationsObjectResponse"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "genes": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLInputObjectType, type_map["GenesObjectResponse"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "obs_ids": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLInputObjectType, type_map["ObsIDSObjectResponse"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "scores": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLInputObjectType, type_map["ScoresObjectResponse"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AnnotationsObjectResponse": GraphQLInputObjectType(
        name="AnnotationsObjectResponse",
        description=None,
        fields=lambda: {
            "data": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "GenesObjectResponse": GraphQLInputObjectType(
        name="GenesObjectResponse",
        description=None,
        fields=lambda: {
            "data": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ObsIDSObjectResponse": GraphQLInputObjectType(
        name="ObsIDSObjectResponse",
        description=None,
        fields=lambda: {
            "data": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLInt))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ScoresObjectResponse": GraphQLInputObjectType(
        name="ScoresObjectResponse",
        description=None,
        fields=lambda: {
            "data": GraphQLInputField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLFloat))),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "PostSaveEmbeddingSessionInput": GraphQLInputObjectType(
        name="PostSaveEmbeddingSessionInput",
        description=None,
        fields=lambda: {
            "sessionId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "dataset": GraphQLInputField(
                GraphQLNonNull(
                    cast(GraphQLInputObjectType, type_map["DatasetObjectInput"])
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetObjectInput": GraphQLInputObjectType(
        name="DatasetObjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "datasetType": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "cellCount": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsetsCount": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labelsets": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(
                            GraphQLInputObjectType,
                            type_map["LabelsetWithLabelsObjectInput"],
                        )
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelsetWithLabelsObjectInput": GraphQLInputObjectType(
        name="LabelsetWithLabelsObjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmRepoUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmVersion": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotationMethod": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "labels": GraphQLInputField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLInputObjectType, type_map["LabelObjectInput"])
                    )
                ),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelObjectInput": GraphQLInputObjectType(
        name="LabelObjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalMarkerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryFullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "category": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "categoryOntologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "color": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "count": GraphQLInputField(
                GraphQLFloat,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fullName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyAssessment": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyExists": GraphQLInputField(
                GraphQLBoolean,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTerm": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "ontologyTermId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationale": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "canonicalGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "markerGenes": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rationaleDois": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "synonyms": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "LabelsetObjectInput": GraphQLInputObjectType(
        name="LabelsetObjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmRepoUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "algorithmVersion": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "annotationMethod": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "mode": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceDescription": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "referenceUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "embedding": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "DatasetAsyncHCStartResponse": GraphQLObjectType(
        name="DatasetAsyncHCStartResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "error": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "message": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "taskId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "requestId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CancelClusteredHeatmapInput": GraphQLInputObjectType(
        name="CancelClusteredHeatmapInput",
        description=None,
        fields=lambda: {
            "taskId": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "sessionId": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreateProjectInput": GraphQLInputObjectType(
        name="CreateProjectInput",
        description=None,
        fields=lambda: {
            "name": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmail": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmails": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrls": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactNames": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "journalDoi": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EditProjectInput": GraphQLInputObjectType(
        name="EditProjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmail": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmails": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrls": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactNames": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "journalDoi": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AddPermissionInput": GraphQLInputObjectType(
        name="AddPermissionInput",
        description=None,
        fields=lambda: {
            "projectId": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "uid": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "role": GraphQLInputField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["ApiClientRole"])),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "InviteByEmailInput": GraphQLInputObjectType(
        name="InviteByEmailInput",
        description=None,
        fields=lambda: {
            "projectId": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLInputField(
                GraphQLNonNull(GraphQLString),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "role": GraphQLInputField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["ApiClientRole"])),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "RemovePermissionInput": GraphQLInputObjectType(
        name="RemovePermissionInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DeleteProjectResponse": GraphQLObjectType(
        name="DeleteProjectResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "projectId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DeleteProjectInput": GraphQLInputObjectType(
        name="DeleteProjectInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "ApproveInvitationResponse": GraphQLObjectType(
        name="ApproveInvitationResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "msg": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "CreatePublicationInput": GraphQLInputObjectType(
        name="CreatePublicationInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmail": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactEmails": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "externalUrls": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactName": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "contactNames": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "journalDoi": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "rawDataUrl": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "capAuthors": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLString)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ReviewProjectRequestInput": GraphQLInputObjectType(
        name="ReviewProjectRequestInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "DeclineProjectReviewInput": GraphQLInputObjectType(
        name="DeclineProjectReviewInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "CancelProjectReviewInput": GraphQLInputObjectType(
        name="CancelProjectReviewInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "Subscription": GraphQLObjectType(
        name="Subscription",
        description=None,
        interfaces=[],
        fields=lambda: {
            "profile": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CapUser"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "avatarStatus": GraphQLField(
                GraphQLNonNull(
                    cast(GraphQLObjectType, type_map["AvatarUploadStatusResponse"])
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "uploadStatusChange": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["UploadResponse"])),
                args={
                    "upload": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["UploadIdentifier"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "uploads": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["UploadResponse"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "dataset": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Dataset"])),
                args={
                    "datasetId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "datasetClusteredHeatmap": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["ClusteredHeatmap"])),
                args={
                    "requestId": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "dataset": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType,
                                type_map["DatasetIdentifierInput"],
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "onProjectChange": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Project"])),
                args={
                    "project": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["ProjectIdentifier"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AvatarUploadStatusResponse": GraphQLObjectType(
        name="AvatarUploadStatusResponse",
        description=None,
        interfaces=[],
        fields=lambda: {
            "objectId": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ok": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "url": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "ProjectIdentifier": GraphQLInputObjectType(
        name="ProjectIdentifier",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
}
schema: GraphQLSchema = GraphQLSchema(
    query=cast(GraphQLObjectType, type_map["Query"]),
    mutation=cast(GraphQLObjectType, type_map["Mutation"]),
    subscription=cast(GraphQLObjectType, type_map["Subscription"]),
    types=type_map.values(),
    directives=[
        GraphQLDirective(
            name="skip",
            description=None,
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD,
                DirectiveLocation.FRAGMENT_SPREAD,
                DirectiveLocation.INLINE_FRAGMENT,
            ),
            args={
                "if": GraphQLArgument(
                    GraphQLNonNull(GraphQLBoolean),
                    default_value=Undefined,
                    description=None,
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="include",
            description=None,
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD,
                DirectiveLocation.FRAGMENT_SPREAD,
                DirectiveLocation.INLINE_FRAGMENT,
            ),
            args={
                "if": GraphQLArgument(
                    GraphQLNonNull(GraphQLBoolean),
                    default_value=Undefined,
                    description=None,
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="deprecated",
            description=None,
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD_DEFINITION,
                DirectiveLocation.ENUM_VALUE,
            ),
            args={
                "reason": GraphQLArgument(
                    GraphQLString,
                    default_value="No longer supported",
                    description=None,
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="specifiedBy",
            description=None,
            is_repeatable=False,
            locations=(DirectiveLocation.SCALAR,),
            args={
                "url": GraphQLArgument(
                    GraphQLNonNull(GraphQLString),
                    default_value=Undefined,
                    description=None,
                    deprecation_reason=None,
                )
            },
        ),
    ],
    description=None,
)
