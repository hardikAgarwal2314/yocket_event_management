from django.db import models


class BaseModel(models.Model):
    """Inherit from this when creating new models."""
    class Meta:
        abstract = True
        ordering = ("created",)

    created = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)
    updated = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        props = [f"{prop}={getattr(self, prop)!r}" for prop in self.__REPR__ if hasattr(self, prop)]
        return f'{self.__class__.__name__}({", ".join(props)})'

    __REPR__ = ("id",)


class Events(BaseModel):
    class Meta:
        ordering = ("created",)

    unique_together = ("name", "starting_time", "duration")

    name = models.CharField(max_length=100, db_index=True,)
    starting_time = models.DateTimeField(blank=True, db_index=True, null=True)
    duration = models.IntegerField(
        default=0,
        db_index=True,
        help_text=(
            "The duration of the event in minutes"
        ),
    )