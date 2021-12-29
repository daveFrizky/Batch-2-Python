from datetime import datetime
from config import db, ma
from marshmallow import fields

class Directors(db.Model):
    __tablename__ = 'directors'
    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    department = db.Column(db.String(32))
    movie = db.relationship(
        'Movies',
        backref='director',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        # order_by='asc(Movies.title)'
    )

class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String)
    budget = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.String)
    revenue=db.Column(db.Integer)
    title=db.Column(db.String)
    vote_average=db.Column(db.Integer)
    vote_count=db.Column(db.REAL)
    overview=db.Column(db.String)
    tagline=db.Column(db.String)
    uid=db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))


class DirectorsSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Directors
        sqla_session = db.session
        load_instance = True
        include_relationships = True

    movie = fields.Nested("DirectorMovieSchema", default=[],many=True)

class DirectorMovieSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    release_date = fields.Str()
    revenue=fields.Int()
    title=fields.Str()
    vote_average=fields.Int()
    vote_count=fields.Float()
    overview=fields.Str()
    tagline=fields.Str()
    uid=fields.Int()
    director_id = fields.Int()


class MoviesSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movies
        sqla_session = db.session
        load_instance = True
        include_relationships = True
    
    director = fields.Nested("MovieDirectorSchema", default=None)
    


class MovieDirectorSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    name = fields.Str()
    id = fields.Int()
    gender =fields.Int()
    uid = fields.Str()
    department = fields.Str()