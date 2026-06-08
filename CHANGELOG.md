# Changelog

## [Unreleased]

## [v2.9.1] - 2026-06-08

### Fixed

- Handle current CAP API responses that omit embedding selection arrays.
- Handle current CAP API responses that omit the highly variable gene flag.
- Expand live API tests to cover health-check client usage.

## [v2.9.0] - 2026-06-06

### Modified

- Use CAP persisted GraphQL query hashes for API requests.
- Send Apollo client awareness headers as `cap-sc-client`.

## [v2.6.0] - 2026-04-02

### Modified

- GQL schema updated to match the latest CAP API changes. Most of the MD page related endpoints were changes.

...


## [v1.0.1] - 2025-10-07

### Fixed

- Readme file notation in `pyproject.toml`

## [v1.0.0] - 2025-10-07

### First stable release

- **search_datasets** endpoint
- **search_cell_labels** endpoint
- **create_session** endpoint
- **embedding_data** endpoint
- **heatmap** endpoint
- **general_de** endpoint
- **highly_variable_genes** endpoint
- **is_md_cache_ready** endpoint
