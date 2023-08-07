from marshmallow import Schema, fields, validate

class AuthSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
