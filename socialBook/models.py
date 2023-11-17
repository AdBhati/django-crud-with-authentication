from django.db import models
from user.models import User
import uuid


class Upload(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=25, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    caption = models.CharField(max_length=25, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_upload', null=True, blank=True)
 

    # no_of_likes = models.IntegerField(default=0) some line added by dev

    def __str__(self):
        return self.title

    class Meta: 
        db_table = 'upload'

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    post = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='upload_post', null=True, blank=True)
    add_comment = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.add_comment

    class Meta:
        db_table = 'comment'

class Like(models.Model):
    id = models.UUIDField(primary_key=True,  editable=False, default=uuid.uuid4)
    post = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='like_post', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes', null=True, blank=True)
    add_Like = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.add_Like)

    class Meta:
        db_table = 'like'
    
