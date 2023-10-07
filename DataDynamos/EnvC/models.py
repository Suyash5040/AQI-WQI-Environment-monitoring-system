from django.db import models


class userfeed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Feedback=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    


