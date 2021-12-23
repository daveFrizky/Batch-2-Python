from config import db, ma

class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.String(32),index=True,primary_key=True)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    # avo_a = db.Column(db.Integer)
    # avo_b = db.Column(db.REAL)
    # avo_c = db.Column(db.REAL)
    # type = db.Column(db.Integer)
    # region_id=db.Column(db.Integer)
    

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        sqla_session = db.session    
        load_instance=True