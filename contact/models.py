from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
