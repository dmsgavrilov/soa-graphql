from ariadne import convert_kwargs_to_snake_case

from app.api.models import Game


def resolve_games(obj, info):
    try:
        game = [game.to_dict() for game in Game.query.all()]
        payload = {
            "success": True,
            "games": game
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_game(obj, info, game_id):
    try:
        game = Game.query.get(game_id)
        payload = {
            "success": True,
            "game": game.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Game item matching id {game_id} not found"]
        }

    return payload
