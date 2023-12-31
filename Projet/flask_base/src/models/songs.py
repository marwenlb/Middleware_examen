from src.helpers import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.String(255), primary_key=True)
    titre = db.Column(db.String(255), nullable=False)
    artiste = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duree = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.String(255), nullable=False)

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
