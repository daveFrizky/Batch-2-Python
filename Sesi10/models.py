from config import db, ma

class Avocado(db.Model):
    __tablename__ = 'avocado'
    # dumpKey = db.column(db.Integer)
    date = db.Column(db.String(32),index=True)
    avgprice = db.Column(db.REAL)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.REAL)
    avo_c = db.Column(db.REAL)
    type = db.Column(db.Integer)
    regionid = db.Column(db.Integer,  primary_key=True)
    

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        sqla_session = db.session    
        load_instance=True