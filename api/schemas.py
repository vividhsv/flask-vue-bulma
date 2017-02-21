from marshmallow import Schema, fields
from marshmallow import ValidationError
from marshmallow import validates_schema

from models import User
from extentions import ma


class PageArgsSchema(Schema):
    page = fields.Int(load_only=True, missing=1)
    per_page = fields.Int(load_only=True, missing=20)

    class Meta:
        strict = True


class PageSchema(Schema):
    page = fields.Integer(dump_to='page', dump_only=True)
    pages = fields.Integer(dump_to='numPages', dump_only=True)
    per_page = fields.Integer(dump_to='perPage', dump_only=True)
    total = fields.Integer(dump_to='totalItems', dump_only=True)


class UserSchema(ma.ModelSchema):
    email = fields.Email(required=True)

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', unknown)

    class Meta:
        model = User
        load_only = ("password",)
        strict = True


class UserPageSchema(PageSchema):
    items = fields.Nested(UserSchema, many=True, dump_only=True)