from collections.abc import Iterable
from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField("NAME", max_length=5, blank=True)
    todo = models.CharField("TODO", max_length=50, blank=False)

    def __str__(self):
        return self.todo

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ):
        if not self.name:
            self.name = "abc"

        super().save(force_insert, force_update, using, update_fields)
