from django.db import models



class TOTP(models.Model):
    id = models.AutoField(
        primary_key=True
    )

    secret = models.TextField(
        max_length=20,
        null=False,
        blank=False
    )

    userId = models.IntegerField(
        null=False,
        blank=False
    )


class TOTPLog(models.Model):
    date = models.DateTimeField(
        null=False,
        blank=False,
    )

    token = models.TextField(
        max_length=6,
        null=False,
        blank=False
    )

    userId = models.IntegerField(
        null=False,
        blank=False
    )
