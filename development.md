# Development

This project uses [Ariadne code generation](https://ariadnegraphql.org/blog/2023/02/02/ariadne-codegen) to generate pydantic models and graphQL client. In case of need to update or add new queries please follow the steps below:

1. Add new queries to [queries.graphql](./queries.graphql)
2. Run `ariadne-codegen`
