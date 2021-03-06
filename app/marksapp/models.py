from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import validate_slug


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=128, blank=True)

    PUBLIC = "PB"
    PRIVATE = "PV"
    visibility_choices = [(PUBLIC, "Public"), (PRIVATE, "Private")]
    visibility = models.CharField(
        choices=visibility_choices, max_length=2, default=PUBLIC
    )

    def __str__(self):
        return "{} | {}".format(self.user.username, self.visibility)


class Tag(models.Model):
    name = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField("date added", default=timezone.now)
    last_bumped = models.DateTimeField("last bumped", blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def tags_str(self):
        return ", ".join(t.name for t in self.tags.all())

    def __str__(self):
        return "[{}] - {} - {} - [{}] - <{}>".format(
            self.date_added, self.user.username, self.name, self.url, self.tags_str()
        )
