from typing import Any
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from .utils import generate_short_code
# Create your models here.


class ShortUrl(models.Model):
    orig_url = models.URLField()
    short_url = models.CharField(
        max_length=7,
        validators=[MinLengthValidator(7)],
        help_text="Must be exactly 7 Character long",
        unique=True,
        null=False,
    )

    visited = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        """
        for generating user short link code
        """
        short_code = generate_short_code()
        short_url = ShortUrl.objects.filter(short_url=short_code).first()
        if short_url:
            # recursively calls the generate_short_link if there is a duplicate code
            return self.generate_short_link()

        return short_code
