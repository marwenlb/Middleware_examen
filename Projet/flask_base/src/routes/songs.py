import json
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from src.models.http_exceptions import *
from src.schemas.songs import SongSchema
from src.schemas.errors import *
from src.schemas.songs import SongUpdateSchema
import src.services.songs as song_service


# from routes import songs
songs = Blueprint(name="songs", import_name=__name__)

@songs.route('/', methods=['GET'])
def get_songs():
    songs_data, status_code = song_service.get_all_songs()
    # Utiliser SongSchema(many=True).dump avec songs_data
    return jsonify(SongSchema(many=True).dump(songs_data)), status_code

@songs.route('/<id>', methods=['GET'])
def get_song(id):
    return song_service.get_song(id)


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
        error = ConflictSchema().loads(json.dumps({"message": "Song already exists"}))
        return error, error.get("code")
    except UnprocessableEntity:
        error = UnprocessableEntitySchema().loads(json.dumps({"message": "One required field was empty"}))
        return error, error.get("code")
    except Forbidden:
        error = ForbiddenSchema().loads(json.dumps({"message": "Can't manage other songs"}))
        return error, error.get("code")
    except Exception:
        error = SomethingWentWrongSchema().loads("{}")
        return error, error.get("code")

@songs.route('/<id>', methods=['PUT'])
def put_song(id):
    
    # parser le body
    try:
        song_update = SongUpdateSchema().loads(json_data=request.data.decode('utf-8'))
    except ValidationError as e:
        error = UnprocessableEntitySchema().loads(json.dumps({"message": e.messages.__str__()}))
        return error, error.get("code")

    try:
        return song_service.put_song(id, song_update)
    except Conflict:
        error = ConflictSchema().loads(json.dumps({"message": "Song already exists"}))
        return error, error.get("code")
    except UnprocessableEntity:
        error = UnprocessableEntitySchema().loads(json.dumps({"message": "One required field was empty"}))
        return error, error.get("code")
    except Forbidden:
        error = ForbiddenSchema().loads(json.dumps({"message": "Can't manage other songs"}))
        return error, error.get("code")
    except Exception:
        error = SomethingWentWrongSchema().loads("{}")
        return error, error.get("code")

@songs.route('/<id>', methods=['DELETE'])
def delete_song(id):
    try:
        success = song_service.delete_song(id)
        if success:
            return jsonify({"message": "Song deleted successfully"}), 200
        else:
            return jsonify({"message": "Song not found"}), 404
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

