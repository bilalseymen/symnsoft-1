from django.db import models
from autoslug import AutoSlugField

# Create your models here.

# PAGE_CATEGORY = (
#     ("OKULUMUZ", "OKULUMUZ"),
#     ("EĞİTİMİMİZ", "EĞİTİMİMİZ"),
# )

class pageModel(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    # category = models.CharField(max_length=20, choices=PAGE_CATEGORY, default='OKULUMUZ')

