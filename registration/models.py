import django.db.models
import uuid


class User(django.db.models.Model):
    objects = django.db.models.Manager()
    id = django.db.models.BigAutoField(primary_key=True)
    uuid = django.db.models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    email = django.db.models.EmailField(unique=True)
    first_name = django.db.models.CharField(max_length=50)
    middle_name = django.db.models.CharField(max_length=50)
    last_name = django.db.models.CharField(max_length=50)
