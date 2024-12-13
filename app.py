from flask import Flask
from flask_graphql import GraphQLView
from models import db
from schema import schema
from config import Config

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

# Add GraphQL endpoint
app.add_url_rule('/gql', view_func=GraphQLView.as_view('gql', schema=schema, graphiql=True))

# Main route
@app.route('/')
def index():
    return "Welcome to the Bank API!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
