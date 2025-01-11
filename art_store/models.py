from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default="2024-12-10")

    def __str__(self):
        return self.review_text


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default="2024-12-10")

    def __str__(self):
        return f"{self.item.name} for {self.user.username} on {self.date}"