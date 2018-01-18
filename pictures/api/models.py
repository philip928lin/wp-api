from django.db import models

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=200)
    source_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    QUESTIONS_CHOICES = (
        ('cute', '你覺得這個看聲可愛嘛？'),
        ('angel', '你覺得這個女生笑起來像天使嗎？')
    )
    topic = models.CharField(choices=QUESTIONS_CHOICES, default='cute', max_length=40)
    
    def __str__(self):
        return str(self.id)+ self.topic
    
class VoteRecord(models.Model):
    id = models.AutoField(primary_key=True)

    voted_image_id = models.IntegerField()
    images_id = models.ForeignKey(Picture,related_name='images_id',on_delete=models.CASCADE)
    voted_feature_id = models.IntegerField()
    features_id = models.ForeignKey(Feature,related_name='features_id',on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50)
    is_voted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta(object):
        unique_together = (('images_id', 'features_id', 'user_id'),)

    def __str__(self):
        unique_together = (self.images_id,self.features_id, self.user_id)        
        return  str(unique_together)
