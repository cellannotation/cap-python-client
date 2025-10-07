
# Python client for Cell-Annotation-Platform GraphQL API
[![PyPI version](https://img.shields.io/pypi/v/cap-sc-client)](https://pypi.org/project/cap-sc-client/)

The Python package provides a simple interface to interact with the [Cell Annotation Platform](https://celltype.info/) (CAP) GraphQL API. The package allows to search for datasets, cell labels metadata and get molecular profiles of cell types published on CAP.

## Installation

```bash
pip install -U cap-sc-client
```

## Basic usage

The main goal of this package is to provide an interace to access CAP datasets and cell annotation metadata (including marker genes, synonyms, rationales, etc.) via standard python tooling. The outputs are in the format [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), which could be converted to other formats (csv, JSON, etc.) if the user desires.


```
>>> from cap_sc_client import CapClient
>>> cp = CapClient()
>>> datasets = cp.search_datasets(limit=5, offset=0, organism=["Homo sapiens"])
>>> datasets.head()
     id                           name  cell_count                        project
0  1427  Skin fibroblasts   - Pan-d...    337376.0  {'id': '613', 'name': 'Pan...
1  1426  Skin fibroblast scRNA-seq ...    153546.0  {'id': '613', 'name': 'Pan...
2  1157  Single cell atlas of the h...     72788.0  {'id': '544', 'name': 'Sin...
3  1156  snRNA-seq of human retina ...   3177310.0  {'id': '544', 'name': 'Sin...
4  1154  snRNA-seq of human retina ...    691008.0  {'id': '544', 'name': 'Sin...
>>> labels = cp.search_cell_labels(limit=10, offset=0)
>>> labels[["full_name", "ontology_term_exists", "marker_genes"]]
             full_name  ontology_term_exists         marker_genes
0  cycling stromal ...                 True   [MKI67, TOP2A, C...
1  alveolar type 1 ...                 True          [PDPN, HOPX]
2    mesoderm 2 (ZEB2)                False                [ZEB2]
3          acinar cell                 True               [PRSS1]
4               neuron                 True               [STMN2]
5   smooth muscle cell                 True   [DES, CNN1, ACTA...
6        ciliated cell                 True               [FOXJ1]
7         Schwann cell                 True                 [MPZ]
8     pancreatic cells                False                [PDX1]
9            club cell                 True             [SCGB1A1]
```

There is also an `MDSession` class that allows users to interact with the molecular profiles of cell types within a specific dataset. However, this class requires users to be familiar with the CAP MD page.

For more examples, please refer to ["examples"](https://github.com/cellannotation/cap-python-client/tree/main/examples) and the [GitHub wiki](https://github.com/cellannotation/cap-python-client/wiki) for detailed documentation.

## Documentation

Detailed documentation is available on [GitHub Wiki](https://github.com/cellannotation/cap-python-client/wiki).
