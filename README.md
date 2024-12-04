# Python client for CAP GraphQL API

Python client uses Ariadne code generation https://ariadnegraphql.org/blog/2023/02/02/ariadne-codegen to generate pydantic models and graphQL client.  


# API calls

## Search datasets
```Python
search_datasets(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[])
```
returns CAP published datasets searched by a keyword that could be filtered by `organism`, `tissue` or `assay`.
The result could be paginated using `limit`, `offset` and sorted using `sort` and `ASC`, `DESC` keywords

Example:
```Python 
asyncio.run(search_datasets(
    search="blood"
    organism=["Homo sapiens"], 
    tissue=["stomach","pyloric antrum"],
    assay=["10x 3' v1"],
    sort=[{'name':'ASC'}]
))
```
Result:
```Python
{
    'lookupDatasets': [
        {
            'id': '420', 
            'name': 'Charting human development ...',
            'description': 'Developing human multi-organ ...',
            'cellCount': 155232
        }
    ...
    ]
}
```
## Dataset download URLs
```Python
download_urls(id)
```
returns URLs for published dataset files: annData, Seurat, JSON (zip), JSON (tar)

Example:
```Python
asyncio.run(download_urls(678))
```
Result:
```Python
{
    'downloadUrls': {
        'annDataUrl': 'https://storage.googleapis.com/...h5ad',
        'seuratUrl': None,
        'capJsonUrlTar': 'https://storage.googleapis.com/...h5ad.json.tar',
        'capJsonUrlZip': 'https://storage.googleapis.com/...h5ad.json.zip'}}
```

## Search cell labels
```Python
search_cells(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[])
```
returns cell labels from CAP published datasets searched by a keyword that could be filtered by `organism`, `tissue` or `assay`.
The result could be paginated using `limit`, `offset` and sorted using `sort` and `ASC`, `DESC` keywords

Example:
```Python 
asyncio.run(search_cells(
    search="blood"
    organism=["Homo sapiens"], 
    tissue=["stomach","pyloric antrum"],
    assay=["10x 3' v1"],
    sort=[{'name':'ASC'}]
))
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
            'ontologyAssessment': None
        }
        ...
    ]
}
```