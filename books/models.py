from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_publish = models.DateField(blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    LIST_OF_TYPE = (
    ('Novel','Novel'),
    ('Documentation','Documentation'),
    ('Other','Other'),
    )
    type_of_book = models.CharField(max_length=200, choices=LIST_OF_TYPE, blank=True, null=True)

    def __str__(self):
        return self.title
