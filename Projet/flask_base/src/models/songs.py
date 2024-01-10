from src.helpers import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.String(255), primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    artiste = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duree = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.String(255), nullable=False)
    
    # Ajout du champ ratings (relation One-to-Many avec le modèle Rating)
    ratings = db.relationship('Rating', backref='song', lazy=True)

    def __init__(self, uuid, titre, artiste, description, duree, release_date):
        self.id = uuid
        self.titre = titre
        self.artiste = artiste
        self.description = description
        self.duree = duree
        self.release_date = release_date
    
    def is_empty(self):
        return (not self.id or self.id == "") and \
               (not self.titre or self.titre == "") and \
               (not self.artiste or self.artiste == "") and \
               (not self.description or self.description == "") and \
               (not self.duree or self.duree == "") and \
               (not self.release_date or self.release_date == "")

    @staticmethod
    def from_dict(obj):
        return Song(
            uuid=obj.get("uuid"),
            titre=obj.get("titre"),
            artiste=obj.get("artiste"),
            description=obj.get("description"),
            duree=obj.get("duree"),
            release_date=obj.get("release_date")
        )

# Ajout du modèle pour les évaluations (ratings)
class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.String(255), primary_key=True)
    comment = db.Column(db.String(255))
    rating = db.Column(db.Integer, nullable=False)
    rating_date = db.Column(db.String(255), nullable=False)
    song_id = db.Column(db.String(255), db.ForeignKey('songs.id'), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    
    def __init__(self, comment, rating, rating_date, song_id, user_id):
        self.comment = comment
        self.rating = rating
        self.rating_date = rating_date
        self.song_id = song_id
        self.user_id = user_id

    @staticmethod
    def from_dict(obj):
        return Rating(
            comment=obj.get("comment"),
            rating=obj.get("rating"),
            rating_date=obj.get("rating_date"),
            song_id=obj.get("song_id"),
            user_id=obj.get("user_id")
        )
