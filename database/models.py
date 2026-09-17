from .db import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), default='pending') # pending, approved, rejected, posted
    created_at = db.Column(db.DateTime, default=datetime.utcnow)