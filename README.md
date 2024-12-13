# Bank Branches GraphQL API

This project creates a GraphQL API for querying bank branch data from a PostgreSQL database. The API uses Flask as the web framework, SQLAlchemy for database interaction, and Graphene for handling GraphQL queries.

## Project Structure

```
.
├── app.py            # Entry point for the Flask application
├── config.py         # Configuration file for Flask and database settings
├── models.py         # Contains SQLAlchemy models
├── schema.py         # GraphQL schema definitions using Graphene
├── requirements.txt  # List of required Python packages
```

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
git clone https://github.com/yourusername/bank-graphql-api.git
cd bank-graphql-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the environment variables in `config.py`:

```python
# config.py
SQLALCHEMY_DATABASE_URI = 'postgresql://your_user:your_password@localhost:5432/bank_api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

4. Run the Flask application:

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

## Files Overview

### `app.py`

This is the entry point of the Flask application. It sets up Flask, connects to the database, and initializes GraphQL with the schema.

```python
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from models import db
from schema import Query

app = Flask(__name__)
app.config.from_object('config')

# Set up the database
db.init_app(app)

# Set up the GraphQL schema
schema = Schema(query=Query)

# Create a GraphQL view
app.add_url_rule('/gql', view_func=GraphQLView.as_view('gql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
```

### `config.py`

This file contains the configuration for the Flask application and PostgreSQL connection string.

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/bank_api'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### `models.py`

Contains SQLAlchemy models for interacting with the `banks`, `branches`, and `bank_branches` tables.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(49))

class Branch(db.Model):
    __tablename__ = 'branches'
    ifsc = db.Column(db.String(11), primary_key=True)
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    bank_id = db.Column(db.BigInteger, db.ForeignKey('banks.id'))
    bank = db.relationship('Bank', backref='branches')
```

### `schema.py`

Defines the GraphQL schema using Graphene. The schema enables querying the `branches` and their associated bank data.

```python
import graphene
from models import db, Bank, Branch

class BankType(graphene.ObjectType):
    name = graphene.String()

class BranchType(graphene.ObjectType):
    branch = graphene.String()
    bank = graphene.Field(BankType)
    ifsc = graphene.String()

class Query(graphene.ObjectType):
    branches = graphene.List(BranchType)

    def resolve_branches(self, info):
        # Query the database for all branches
        query = Branch.query.all()
        return query
```

### `requirements.txt`

This file lists the necessary dependencies for the project.

```
Flask==2.1.2
Flask-SQLAlchemy==2.5.1
Flask-GraphQL==2.0.0
Graphene==3.1.1
psycopg2==2.9.3
```

## Bonus Points

1. **Clean Code**: The code is organized into multiple modules (`app.py`, `config.py`, `models.py`, `schema.py`) for maintainability and readability.
2. **Test Cases**: You can write tests using Flask's testing utilities. For example, create a `test_app.py` file to test the GraphQL queries or database interactions.
3. **Deployment**: You can deploy the app on platforms like Heroku. Make sure to add a `Procfile` for Heroku deployment:

```
web: python app.py
```

Ensure the PostgreSQL database is also set up on Heroku, and configure the database URI correctly in `config.py`.

## Example GraphQL Query

To query the data, use GraphiQL at `http://localhost:5000/gql` or any GraphQL client like Apollo Client or Postman.

### Sample GraphQL Query

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

### Sample Response

```json
{
  "data": {
    "branches": {
      "edges": [
        {
          "node": {
            "branch": "New York Branch",
            "bank": {
              "name": "Bank of America"
            },
            "ifsc": "BOFAUS3N"
          }
        }
      ]
    }
  }
}
```

## Conclusion

This project provides a flexible and efficient GraphQL API to query bank and branch details. The structure is clean and modular, ensuring easy maintainability and scalability. With deployment on Heroku and proper test coverage, this API can be expanded further to meet additional requirements.

