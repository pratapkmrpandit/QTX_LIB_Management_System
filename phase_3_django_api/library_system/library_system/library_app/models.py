from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    campus_location = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'library'

    def __str__(self):
        return self.name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField(null=True, blank=True)
    total_copies = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    available_copies = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')
    authors = models.ManyToManyField('Author', related_name='books')
    categories = models.ManyToManyField('Category', related_name='books')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title

    def is_available(self):
        return self.available_copies > 0


class Member(models.Model):
    MEMBER_TYPES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]

    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPES)
    registration_date = models.DateField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Borrowing(models.Model):
    borrowing_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrowings")
    borrow_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'borrowing'

    def __str__(self):
        return f"Borrowing {self.borrowing_id}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="reviews")
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True, blank=True
    )
    comment = models.TextField(null=True, blank=True)
    review_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review {self.review_id} on {self.book}"
