from flask import request, jsonify
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType
)
from ariadne.explorer import ExplorerPlayground

# Playground UI
PLAYGROUND_HTML = ExplorerPlayground(title="Task Manager API").html(None)

# Import app and db
from api import app, db

# Import resolvers
from api.queries import get_all_todos, get_single_todo
from api.mutations import (
    create_new_todo,
    mark_todo_done,
    remove_todo,
    change_due_date
)

# Query mapping
query = ObjectType("Query")
query.set_field("todos", get_all_todos)
query.set_field("todo", get_single_todo)

# Mutation mapping
mutation = ObjectType("Mutation")
mutation.set_field("createTodo", create_new_todo)
mutation.set_field("markDone", mark_todo_done)
mutation.set_field("deleteTodo", remove_todo)
mutation.set_field("updateDueDate", change_due_date)

# Load schema
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    [query, mutation],
    snake_case_fallback_resolvers
)

# Routes
@app.route('/')
def home():
    return 'Flask GraphQL API Running'

@app.route("/graphql", methods=["GET"])
def playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_api():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    return jsonify(result), (200 if success else 400)

# Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
