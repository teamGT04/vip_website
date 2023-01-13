from project import db
class User(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(length=30), unique=True, nullable=False)
    email_address=db.Column(db.String(length=50),nullable=False)
    password_hash=db.Column(db.String(length=60),nullable=False)
    #items=db.relationship('Item2', backref='owner',lazy=True)
    #vip=db.Column(db.Integer(),db.Foreignkey('item2.uid'))

class Item2(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    place = db.Column(db.String(length=1024), nullable=False)
    #owner=db.column(db.Integer(),db.Foreignkey())
    uid=db.Column(db.Integer(),unique=True)
    #owner=db.relationship('Item2', backref='relative',lazy=True)


    def __repr__(self):
        return f'Item2 {self.name}'
    def __repr__(self):
        return f'User{self.username}'
