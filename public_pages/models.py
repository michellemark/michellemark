"""
@Copyright Michelle Mark 2018
@author Michelle Mark

Database models for main pages including contact me
"""
from django.db import models

from django.core.validators import RegexValidator


class ContactMe(models.Model):
    your_name = models.CharField(max_length=50, validators=[RegexValidator(r'^[\w\s\-]+$',
                                                                           'Letters, numbers, spaces and or - are allowed')])
    message = models.TextField(max_length=10000, validators=[
        RegexValidator(r'^[\w\d\s\t\n\r\!\@\#\$\%\(\)\\_\+\-\=\?\<\>\,\.\:\&//]+$',
                       'Letters, numbers, spaces, new lines and or !@#$%&()-_+=:<>?/,. are allowed')])
    time_submitted = models.DateTimeField(auto_now_add=True)
    responded_to = models.BooleanField(default=False)

    class Meta:
        db_table = 'contact_me'
        verbose_name_plural = 'Contact Me Submissions'
        ordering = ['time_submitted','responded_to']

    def __str__(self):

        return self.time_submitted.strftime('%Y-%m-%d %I:%M %p')
