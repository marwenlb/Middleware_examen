from src.helpers import db
from src.models.songs import Song

def get_all_songs(self):
    return Song.query.all()

def get_song_from_id(id):
    return Song.query.get(id)
    
def add_song(song):
    db.session.add(song)
    db.session.commit()

