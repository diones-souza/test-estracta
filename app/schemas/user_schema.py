from marshmallow import Schema, fields, validate

class CreateSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

class UpdateSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(validate=validate.Length(min=6))
