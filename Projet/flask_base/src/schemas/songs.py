from marshmallow import Schema, fields, validates_schema, ValidationError

class RatingSchema(Schema):
    comment = fields.String(description="Comment")
    id = fields.String(description="ID")
    rating = fields.Integer(description="Rating")
    rating_date = fields.DateTime(description="Rating Date")
    song_id = fields.String(description="Song ID")
    user_id = fields.String(description="User ID")

class SongSchema(Schema):
    id = fields.String(description="UUID")
    titre = fields.String(description="Titre Song")
    artiste = fields.String(description="Nom Artiste")
    description = fields.String(description="Description")
    duree = fields.String(description="Duree")
    release_date = fields.String(description="Release Date")
    ratings = fields.Nested(RatingSchema, many=True)

    @staticmethod
    def is_empty(obj):
        return (not obj.get("id") or obj.get("id") == "") and \
               (not obj.get("titre") or obj.get("titre") == "") and \
               (not obj.get("artiste") or obj.get("artiste") == "") and \
               (not obj.get("description") or obj.get("description") == "") and \
               (not obj.get("duree") or obj.get("duree") == "") and \
               (not obj.get("release_date") or obj.get("release_date") == "")

class BaseSongSchema(Schema):
    titre = fields.String(description="titre song", required=True)
    artiste = fields.String(description="Nom Artiste ", required=True)
    description = fields.String(description="Description")
    duree = fields.String(description="Duree")
    release_date = fields.String(description="Release Date")
    ratings = fields.Nested(RatingSchema, many=True)

class SongUpdateSchema(BaseSongSchema):
    @validates_schema
    def validates_schemas(self, data, **kwargs):
        if not (("titre" in data and data["titre"] != "") or
                ("artiste" in data and data["artiste"] != "") or
                ("description" in data and data["description"] != "") or
                ("duree" in data and data["duree"] != "") or
                ("release_date" in data and data["release_date"] != "") or
                ("ratings" in data and data["ratings"])):
            raise ValidationError("At least one of ['titre', 'artiste', 'description', 'duree', 'release_date', 'ratings'] must be specified")
