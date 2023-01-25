from django.db import models

class User(models.Model):
    """AI is creating summary for User

    Args:
        models ([type]): [description]
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    created_on = models.DateField()
    image_url = models.CharField(max_length=200)
