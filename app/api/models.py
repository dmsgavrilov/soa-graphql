from app.api import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    date = db.Column(db.Date)
    comments = db.Column(db.ARRAY(db.String))

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "date": str(self.date.strftime('%d-%m-%Y')),
            "comments": self.comments
        }


db.create_all()
