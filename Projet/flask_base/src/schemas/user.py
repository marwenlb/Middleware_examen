from marshmallow import Schema, fields, validates_schema, ValidationError


class UserSchema(Schema):
    id = fields.String(description="UUID")
    inscription_date = fields.DateTime(description="Inscription date")
    name = fields.String(description="Name")
    username = fields.String(description="Username")
    email = fields.Email(description="Email")
    premium = fields.Boolean(description="Premium")
    birthdate = fields.String(description="Birthdate")
    country = fields.String(description="Country")

    @staticmethod
    def is_empty(obj):
        return (not obj.get("id") or obj.get("id") == "") and \
               (not obj.get("name") or obj.get("name") == "") and \
               (not obj.get("username") or obj.get("username") == "") and \
               (not obj.get("inscription_date") or obj.get("inscription_date") == "") and \
               (not obj.get("email") or obj.get("email") == "") and \
               (not obj.get("premium") or obj.get("premium") == "") and \
               (not obj.get("birthdate") or obj.get("birthdate") == "") and \
               (not obj.get("country") or obj.get("country") == "")


class BaseUserSchema(Schema):
    name = fields.String(description="Name")
    password = fields.String(description="Password")
    username = fields.String(description="Username")
    email = fields.Email(description="Email")
    premium = fields.Boolean(description="Premium")
    birthdate = fields.String(description="Birthdate")
    country = fields.String(description="Country")



class UserUpdateSchema(BaseUserSchema):
    @validates_schema
    def validates_schemas(self, data, **kwargs):
        if not (("name" in data and data["name"] != "") or
                ("username" in data and data["username"] != "") or
                ("password" in data and data["password"] != "") or
                ("email" in data and data["password"] != "") or
                ("premium" in data and data["premium"] != "") or
                ("birthdate" in data and data["birthdate"] != "")or
                ("country" in data and data["country"] != "")):
            raise ValidationError("at least one of ['name','username','password'] must be specified")
