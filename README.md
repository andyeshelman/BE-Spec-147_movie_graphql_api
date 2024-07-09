# GraphQL Flask Example

This repository contains a simple example of how to use GraphQL with Flask. GraphQL is a query language for your API and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.

## Quick Explanation of GraphQL

GraphQL is a powerful tool that allows clients to request exactly the data they need, and nothing more. It enables declarative data fetching, where a client can specify not only the data they want but also the format of the response. This can lead to more efficient data retrieval and reduce the amount of data transferred over the network.

Key benefits of GraphQL:
- **Declarative Data Fetching:** Clients can specify exactly what data they need.
- **Single Endpoint:** Unlike REST, which often requires multiple endpoints, GraphQL typically uses a single endpoint.
- **Strongly Typed:** GraphQL schemas are strongly typed, which makes it easier to validate and understand the data.

## Required Pip Installs

To set up the environment for this project, you need to install several Python packages. Here is a list of the required pip installs:

```sh
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install graphene
pip install --pre graphene-sqlalchemy
pip install "graphql-server[flask]"
```

# Movie Database GraphQL Schema

## Objective:
Create a GraphQL schema for a movie database using `graphene` and `graphene-sqlalchemy`. The schema should include queries to retrieve all movies, retrieve a movie by its ID, and search for movies by title. Additionally, include mutations to create, update, and delete movies.

## Database Model:

**Movie**
- `id: ID!`
- `title: String!`
- `genre: String!`
- `releaseYear: Int!`
- `director: String!`
- `rating: Float`

## Requirements:

### Queries:

- `allMovies`: Retrieve all movies.
- `movieById(id: ID!): Movie`: Retrieve a movie by its ID.
- `searchMovies(title: String!): [Movie]`: Search for movies by title.

### Mutations:

- `createMovie(title: String!, genre: String!, releaseYear: Int!, director: String!, rating: Float): Movie`: Create a new movie.
- `updateMovie(id: ID!, title: String, genre: String, releaseYear: Int, director: String, rating: Float): Movie`: Update an existing movie.
- `deleteMovie(id: ID!): Boolean`: Delete a movie by its ID.
