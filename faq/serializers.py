from rest_framework import serializers
from faq.models import Category, FAQ


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Category.objects.all(),
    )

    class Meta:
        model = FAQ
        fields = "__all__"
