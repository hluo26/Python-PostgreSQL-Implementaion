from app import db

class City(db.Model):

    __tablename__ = 'City'
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    zip_code = db.Column(db.String(50))

    def __init__(self, name, zip_code):
        self.name = name
        self.zip_code = zip_code

    def __repr__(self):
        return 'The Name is {}, and the zip code is {}'.format(self.name, self.zip_code)
