from django.db import models

# Create your models here.
class UserInformation(models.Model):
    fname = models.CharField(max_length=12)
    lname = models.CharField(max_length=12)
    # GENDER FIELD WITH CHOICES
    MALE = 'ML'
    FEMALE = 'FM'
    NON_BINARY = 'NB'
    PREFER_NOT_TO_SAY = 'PNTS'
    OTHER = 'OTHR'
    GENDER_CHOICES = [
        (MALE,"Male"),
        (FEMALE,"Female"),
        (NON_BINARY,"Non-Binary"),
        (PREFER_NOT_TO_SAY,"Prefer-Not-to-Say"),
        (OTHER,"Other"),
    ]
    gender = models.CharField(
        max_length=12,
        choices=GENDER_CHOICES,
        default=PREFER_NOT_TO_SAY,
    )
    dob = models.DateField()
    email = models.EmailField()
    ph_num = models.IntegerField()

class Credentials(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
