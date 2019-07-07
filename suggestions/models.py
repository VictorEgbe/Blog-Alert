from django.db import models


class Suggestion(models.Model):
    name = models.CharField(max_length=120)
    suggestion = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.suggestion) > 20:
            return self.suggestion[:20] + '...'
        return self.suggestion
