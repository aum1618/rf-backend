from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category", null=True
    )

    def __str__(self):
        return f"Question No {self.pk}"
