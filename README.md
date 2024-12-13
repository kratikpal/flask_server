# Bank Branches GraphQL API

This project creates a GraphQL API for querying bank branch data from a PostgreSQL database. The API uses Flask as the web framework, SQLAlchemy for database interaction, and Graphene for handling GraphQL queries.

### Deploved URL

[PythonAnyWhere](https://patanahi.pythonanywhere.com/)

## Project Structure

```
.
├── app.py            # Entry point for the Flask application
├── config.py         # Configuration file for Flask and database settings
├── models.py         # Contains SQLAlchemy models
├── schema.py         # GraphQL schema definitions using Graphene
├── requirements.txt  # List of required Python packages
```

## Screenshots

<img src="https://github.com/user-attachments/assets/f75b02c1-5aca-4d43-bc0c-5a5468a70ee4">

## Features

- **GraphQL API** at the `/gql` endpoint to query bank branch data.
- Ability to query:
  - Branch details (branch name, IFSC, and address).
  - Bank name associated with each branch.

## Requirements

Before running the project, ensure that you have the following installed:

- Python 3.7+
- PostgreSQL
- `pip` for Python package management

### Dependencies

- Flask: Web framework
- Graphene: For GraphQL integration with Flask
- SQLAlchemy: ORM for database interactions
- psycopg2: PostgreSQL adapter for Python
- Flask-SQLAlchemy: Integrates SQLAlchemy with Flask

Install dependencies using:

```
pip install -r requirements.txt
```

## Running the Application

1. Clone the repository:

```bash
git clone https://github.com/kratikpal/flask_server.git
cd flask_server
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

By default, the API will be available at `http://localhost:5000/gql`.

### GraphQL Query Example

You can query the GraphQL API with the following example:

```graphql
query {
  branches {
    edges {
      node {
        branch
        bank {
          name
        }
        ifsc
      }
    }
  }
}
```

This query will return all the bank branches with their names and IFSC codes.
