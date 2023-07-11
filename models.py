"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.Text)
    description = db.Column(db.Text)


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.Text)
    artist = db.Column(db.Text)
    


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer)
    song_id = db.Column(db.Integer)

    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)



