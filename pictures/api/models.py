from django.db import models

class Picture(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    
    like_count = models.IntegerField()
    TAG_CHOICES = (
        ('cute', 'cute'),
        ('angel', 'angel')
    )
    tags = models.CharField(choices=TAG_CHOICES, default='1', max_length=10)

    def __str__(self):
        return str(self.id)