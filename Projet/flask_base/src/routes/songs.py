import json
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from src.models.http_exceptions import *
from src.schemas.songs import SongSchema
from src.schemas.errors import *
import src.services.songs as song_service


# from routes import songs
songs = Blueprint(name="songs", import_name=__name__)

@songs.route('/', methods=['GET'])
def get_songs():
    songs_data, status_code = song_service.get_all_songs()
    # Utiliser SongSchema(many=True).dump avec songs_data
    return jsonify(SongSchema(many=True).dump(songs_data)), status_code

@songs.route('/', methods=['POST'])
def create_song():
    # parser le body
    try:
        song_ajout = SongSchema().loads(json_data=request.data.decode('utf-8'))
    except ValidationError as e:
        error = UnprocessableEntitySchema().loads(json.dumps({"message": e.messages.__str__()}))
        return error, error.get("code")

    try:
        return song_service.create_song(song_ajout)
    except Conflict:
        error = ConflictSchema().loads(json.dumps({"message": "User already exists"}))
        return error, error.get("code")
    except UnprocessableEntity:
        error = UnprocessableEntitySchema().loads(json.dumps({"message": "One required field was empty"}))
        return error, error.get("code")
    except Forbidden:
        error = ForbiddenSchema().loads(json.dumps({"message": "Can't manage other users"}))
        return error, error.get("code")
    except Exception:
        error = SomethingWentWrongSchema().loads("{}")
        return error, error.get("code")

 