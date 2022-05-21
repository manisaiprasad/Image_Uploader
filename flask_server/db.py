from datetime import datetime
from email.mime import image

from click import command, echo
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext


# Initialize SQLAlchemy with no settings
db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'created': self.created
        }


@command("init-db")
@with_appcontext
def init_db_command():
    """Initialize the database."""
    db.create_all()
    echo("Initialized the database.")


def init_app(app):
    """Initialize the Flask app for database usage."""
    db.init_app(app)
    app.cli.add_command(init_db_command)
