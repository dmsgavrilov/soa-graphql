from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify, render_template, abort

from app.api import app
from app.api.models import Game
from app.api.queries import resolve_games, resolve_game
from app.api.mutations import (
    resolve_create_game,
    resolve_delete_game, resolve_add_comments
)

query = ObjectType("Query")

query.set_field("games", resolve_games)
query.set_field("game", resolve_game)

mutation = ObjectType("Mutation")
mutation.set_field("createGame", resolve_create_game)
mutation.set_field("deleteGame", resolve_delete_game)
mutation.set_field("addComments", resolve_add_comments)

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.route("/games", methods=["GET"])
def get_games():
    games = [game.to_dict() for game in Game.query.all()]
    return render_template("games.html", games=games)


@app.route("/games/<game_id>", methods=["GET"])
def get_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        abort(404)
    return render_template("game.html", game=game.to_dict())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
