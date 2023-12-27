from marshmallow import Schema, fields, validates_schema, ValidationError

class SongSchema(Schema):
    id = fields.String(description="UUID")
    titre = fields.String(description="Titre Song")
    artiste = fields.String(description="Nom Artiste")
    description = fields.String(description="Description")
    duree = fields.String(description="Duree")
    release_date = fields.String(description="Release Date")

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

class SongUpdateSchema(BaseSongSchema):
    @validates_schema
    def validates_schemas(self, data, **kwargs):
        if not (("titre" in data and data["titre"] != "") or
                ("artiste" in data and data["artiste"] != "") or
                ("description" in data and data["description"] != "") or
                ("duree" in data and data["duree"] != "") or
                ("release_date" in data and data["release_date"] != "")):
            raise ValidationError("At least one of ['titre', 'artiste', 'description', 'duree', 'release_date'] must be specified")
