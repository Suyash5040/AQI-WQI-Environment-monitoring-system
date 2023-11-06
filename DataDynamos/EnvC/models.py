from django.db import models


class userfeed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100, null=True)
    Feedback=models.TextField()



class indusfeed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    domain=models.CharField(max_length=50)
    AboutIndustry=models.TextField()

    


