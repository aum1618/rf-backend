from rest_framework import serializers
from blog.models import Category, Blog, Section


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Blog
        fields = "__all__"
