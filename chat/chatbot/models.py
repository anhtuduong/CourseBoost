from django.db import models

class Chat(models.Model):
    user = models.CharField(max_length=10)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'
