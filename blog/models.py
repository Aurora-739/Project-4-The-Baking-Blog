from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    ingredients = models.TextField(blank=True, help_text="E.g. 100g - flour")
    cooking_utensils = models.TextField(blank=True, help_text="E.g. A stand mixer, A large mixing bowl")
    steps = models.TextField(blank=True, help_text="E.g. Step 1. Add 100g of flour to a large mixing bowl")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


