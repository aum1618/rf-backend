from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cryptocurrency"
        verbose_name_plural = "Cryptocurrencies"


class Blog(models.Model):
    heading = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )

    def __str__(self):
        return self.heading


class Section(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="section_images/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sections"
