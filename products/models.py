import django.db.models


class Search(django.db.models.Model):
    object = django.db.models.Manager()
    id = django.db.models.BigAutoField(primary_key=True)
    text = django.db.models.CharField(max_length=200)
    created_at = django.db.models.DateTimeField(auto_now=True)


class Category(django.db.models.Model):
    objects = django.db.models.Manager()
    id = django.db.models.fields.BigAutoField(primary_key=True)
    name = django.db.models.fields.CharField(max_length=200)


class Product(django.db.models.Model):
    objects = django.db.models.Manager()
    id = django.db.models.fields.BigAutoField(primary_key=True)
    category = django.db.models.ForeignKey(Category, db_constraint=False, on_delete=django.db.models.CASCADE,
                                           default=None)
    title = django.db.models.CharField(max_length=200)
    description = django.db.models.TextField()
    price = django.db.models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
