from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Income(models.Model):
    SOURCE_OPTIONS = [
        ("SALARY", "SALARY"),
        ("BUSINESS", "BUSINESS"),
        ("SIDE-HUSTLES", "SIDE-HUSTLES"),
        ("OTHERS", "OTHERS"),
    ]

    source = models.CharField(choices=SOURCE_OPTIONS, max_length=255)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering: ["-date"] # type: ignore

    def __str__(self) -> str:
        return str(self.owner) + "'s income"
