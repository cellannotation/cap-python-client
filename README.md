# Python client for CAP GraphQL API

Python client uses Ariadne code generation https://ariadnegraphql.org/blog/2023/02/02/ariadne-codegen to generate pydantic models and graphQL client.  

1. Add new queries to `queries.graphql`
2. Run `ariadne-codegen`

# API calls

Create CAP object `cap = Cap()` and use it to access public API endpoints.

If you plan to use CAP API endpoints that require authoriization please set environment variables either `CAP_LOGIN` / `CAP_PWD` or `CAP_TOKEN` with custom token that you can get from CAP UI. CAP will automatically use this information to authenticate you during authorized endpoints requests.

## Search datasets
```Python
cap.search_datasets(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[])
```
returns CAP published datasets searched by a keyword that could be filtered by `organism`, `tissue` or `assay`.
The result could be paginated using `limit`, `offset` and sorted using `sort` and `ASC`, `DESC` keywords

Example:
```Python 
cap.search_datasets(
    search="blood"
    organism=["Homo sapiens"], 
    tissue=["stomach","pyloric antrum"],
    assay=["10x 3' v1"],
    sort=[{'name':'ASC'}]
)
```
Result:
```Python
{
    'results': [
        {
            'id': '420', 
            'name': 'Charting human development ...',
            'description': 'Developing human multi-organ ...',
            'cellCount': 155232,
            'labelsets': [
                {
                    'id': '3714', 
                    'name': 'assay', 
                    'description': None, 
                    'labels': [
                        {
                            'id': '25154', 
                            'name': "10x 3' v2", 
                            'count': 146343,
                            'typename__': 'Label'
                        }
                        ...
                    ],
                    'typename__': 'Labelset'
                }
                ...
            ],
            'project': {
                'version': 1.0,
                'id': '263', 
                'name': 'Charting human ...', 
                'owner': {
                    'displayName': 'CAP Data Upload'
                },
                'typename__': 'Project'
            }            
        }
    ...
    ]
}
```
## Dataset download URLs
```Python
cap.download_urls(id)
```
returns URLs for published dataset files: annData, Seurat, JSON (zip), JSON (tar)

Example:
```Python
cap.download_urls(678)
```
Result:
```Python
{
    'downloadUrls': {
        'annDataUrl': 'https://storage.googleapis.com/...h5ad',
        'seuratUrl': None,
        'capJsonUrlTar': 'https://storage.googleapis.com/...h5ad.json.tar',
        'capJsonUrlZip': 'https://storage.googleapis.com/...h5ad.json.zip',
        'typename__': 'DatasetDownloadUrlsResponse'
    }
}
```

## Search cell labels
```Python
cap.search_cell_labels(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[])
```
returns cell labels from CAP published datasets searched by a keyword that could be filtered by `organism`, `tissue` or `assay`.
The result could be paginated using `limit`, `offset` and sorted using `sort` and `ASC`, `DESC` keywords

Example:
```Python 
cap.search_cell_labels(
    search="blood"
    organism=["Homo sapiens"], 
    tissue=["stomach","pyloric antrum"],
    assay=["10x 3' v1"],
    sort=[{'name':'ASC'}]
)
```
Result:
```Python
{
    'lookupCells': [
        {
            'id': '51853', 
            'fullName': 'progenitor cell', 
            'name': 'progenitor cell', 
            'ontologyTermExists': True, 
            'ontologyTermId': 'CL:0011026', 
            'ontologyTerm': 'progenitor cell', 
            'synonyms': ['unknown'], 
            'categoryOntologyTermExists': True, 
            'categoryOntologyTermId': 'CL:0011115', 
            'categoryOntologyTerm': 'precursor cell', 
            'categoryFullName': 'precursor cell', 
            'markerGenes': ['EOMES'], 
            'canonicalMarkerGenes': ['unknown'], 
            'count': 53089, 
            'ontologyAssessment': None,
            'labelset': {
                'id': '6387', 
                'name': 'cell_type', 
                'description': 'An atlas ...', 
                'dataset': {
                    'id': '532', 
                    'name': 'Second Trimester ...', 
                    'project': {
                        'id': '305', 
                        'name': 'Human developing neocortex by area', 
                        'version': 1,
                        'typename__': 'Project'
                    },
                    'typename__': 'Dataset'
                },
                'typename__': 'Labelset'
            },
            'typename__': 'Label'
        }
        ...
    ]
}
```