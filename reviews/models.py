from django.contrib import auth
from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="name pub"
    )
    website = models.URLField(
        help_text="website"
    )
    email = models.EmailField(
        help_text="email"
    )


class Book(models.Model):
    title = models.CharField(
        max_length=70,
        help_text="name of the book"
    )
    publication_date = models.DateField(
        verbose_name="Date the book released"
    )
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN"
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )
    contributors = models.ManyToManyField(
        'Contributor',
        through="BookContributor"
    )


class Contributor(models.Model):
    first_names = models.CharField(
        max_length=50,
        help_text="The contrib"
    )
    last_names = models.CharField(
        max_length=50,
        help_text="the cotrib last names",
    )
    email = models.EmailField(
        help_text="The contact email"
    )


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name="role cont in book",
        choices=ContributionRole.choices,
        max_length=20
    )


class Review(models.Model):
    content = models.TextField(
        help_text="Review text"
    )
    rating = models.IntegerField(
        help_text="Rating"
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time of review"
    )
    date_edited = models.DateTimeField(
        null=True,
        help_text="The date review was edited"
    )
    creator = models.ForeignKey(
        auth.get_user_model(),
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        help_text="The book that this review for"
    )
