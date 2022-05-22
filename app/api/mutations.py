from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from app.api import db
from app.api.models import Game


@convert_kwargs_to_snake_case
def resolve_create_game(obj, info, status, date, comments):
    try:
        date = datetime.strptime(date, '%d-%m-%Y').date()
        game = Game(
            status=status, date=date, comments=comments
        )
        db.session.add(game)
        db.session.commit()
        payload = {
            "success": True,
            "todo": game.to_dict()
        }

    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_delete_game(obj, info, game_id):
    try:
        game = Game.query.get(game_id)
        db.session.delete(game)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Game matching id {game_id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_add_comments(obj, info, game_id, comments):
    try:
        game = Game.query.get(game_id)
        if game:
            game.comments += comments
        db.session.add(game)
        db.session.commit()
        payload = {
            "success": True,
            "game": game.to_dict()
        }

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Game matching id {game_id} not found"]
        }

    return payload
