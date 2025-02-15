from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,          #self si usa per accedere agli attributi(colonne) di User, in questo caso l'id e la mail
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):                                                    #come mi riferisco al elemento del modello 
        return '<People %r>' % self.name

    def serialize(self):
        return {                                                          #ciò che voglio mostrare e lo mostro come dizionario
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eye_color" : self.eye_color,
            "hair_color" : self.hair_color
        }


 
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):                                                    #come mi riferisco al elemento del modello 
        return '<Planet %r>' % self.name

    def serialize(self):
        return {                                                          #ciò che voglio mostrare e lo mostro come dizionario
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population" : self.population,
            "terrain" : self.terrain
        }
    

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(120), nullable=False)
    planet_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)

    planet = db.relationship('Planet')
    people = db.relationship('People')
    user = db.relationship('User')

    def __repr__(self):                                                    #come mi riferisco al elemento del modello 
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {                                                          #ciò che voglio mostrare e lo mostro come dizionario
            "id": self.id
        }
    

       