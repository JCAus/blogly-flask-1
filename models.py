"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from traitlets import default

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    '''User class'''

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    auto_increment=True)

    first_name = db.Column(db.String(50),
                            nullable=False)
    
    last_name = db.Column(db.String(50),
                            nullable=False)

    img_url = db.Column(db.VARCHAR(1000), default="https://img.myloview.com/stickers/default-avatar-profile-icon-vector-social-media-user-image-700-240336019.jpg")

