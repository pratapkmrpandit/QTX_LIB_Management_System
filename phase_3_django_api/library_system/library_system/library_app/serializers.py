from rest_framework import serializers
from .models import Library,Author,Category,Book,Borrowing,Member,Review

class librarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Library
        fields = '__all__'

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

class bookSerializer(serializers.ModelSerializer):
    class BookSerializer(serializers.ModelSerializer):
        authors = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Author.objects.all()
        )
        categories = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Category.objects.all()
        )

    class Meta:
        model = Book
        fields = "__all__"

class memberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class borrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

