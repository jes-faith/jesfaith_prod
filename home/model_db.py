from mongoengine import Document, StringField, DateTimeField
from datetime import datetime, timezone

class PrayerRequest(Document):
    name = StringField()
    email = StringField()
    message = StringField()
    submitted_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {'collection': 'prayer_requests'}
