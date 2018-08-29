from flask_restful import fields

resource_fields = {
    'username': fields.String,
    'pub_date': fields.DateTime(dt_format='iso8601'),
}
