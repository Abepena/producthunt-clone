from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=150)
    url = models.URLField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="icons/")
    body = models.TextField()
    #hunter is the user who created the product
    hunter = models.ForeignKey(User, on_delete="CASCADE")

    def pretty_pub_date(self):
        return self.pub_date.strftime("%a, %B %D %Y ")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
