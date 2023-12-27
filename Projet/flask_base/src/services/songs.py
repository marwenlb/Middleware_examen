import json
import requests
from marshmallow import EXCLUDE
from sqlalchemy import exc

from src.models.songs import Song as SongModel
from src.schemas.songs import SongSchema

import src.repositories.songs as songs_repository
from src.models.http_exceptions import SomethingWentWrong, Forbidden, UnprocessableEntity, Conflict

songs_url = "http://localhost:8080/songs/" 
    

def get_all_songs():
    response = requests.request(method="GET", url=songs_url)
    return response.json(), response.status_code

def get_song(id):
    response = requests.request(method="GET", url=songs_url+id)
    return response.json(), response.status_code


def create_song(songs_register):
    # on récupère le modèle utilisateur pour la BDD
    song_model = SongModel.from_dict(songs_register)
    # on récupère le schéma utilisateur pour la requête vers l'API users
    song_schema = SongSchema().loads(json.dumps(songs_register), unknown=EXCLUDE)

    # on crée l'utilisateur côté API users
    response = requests.request(method="POST", url=songs_url, json=song_schema)
    if response.status_code != 200:
        return response.json(), response.status_code

    # on ajoute l'utilisateur dans la base de données
    # pour que les données entre API et BDD correspondent
    try:
        song_model.id = response.json()["id"]
        songs_repository.add_song(song_model)
    except Exception:
        raise SomethingWentWrong

    return response.json(), response.status_code



def get_song_from_db(self, song_id):
    return self.song_repository.get_song(song_id)

def song_exists(self, song_id):
    return self.get_song_from_db(song_id) is not None

