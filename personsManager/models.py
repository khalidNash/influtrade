from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from datetime import datetime
import re
from django.urls import reverse


# Create your models here.

# contacts model starts here
class Contact(models.Model):
    # contact_id = models.AutoField(primary_key=True) 
    person_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField('Pincode')
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('contact', kwargs={'pk': self.pk})

    def __str__(self):
        return self.person_name


    # def save(self, *args, **kwargs):
    #     self.email = self.email.lower().strip()
    #     if self.email != "":
    #         if not email_re.match(self.email):
    #             raise ValidationError(u'%s is not an email address, dummy!' % self.email)
    #     if self.email == "":
    #         self.email = None
    # super(Contact, self).save(*args, **kwargs)


# contacts model end here

