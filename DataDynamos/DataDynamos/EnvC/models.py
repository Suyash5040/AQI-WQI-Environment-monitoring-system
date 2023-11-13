from django.db import models


#Getting data from feedback page
class userfeed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100, null=True)
    Feedback=models.TextField()


#Getting data from Suggestion page
class indusfeed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    domain=models.CharField(max_length=50)
    AboutIndustry=models.TextField()

    


