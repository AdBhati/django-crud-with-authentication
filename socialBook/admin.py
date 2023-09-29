from django.contrib import admin
from socialBook.models import Comment,Upload, Like
from user.models import User


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post','add_comment')

class UploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','content','caption','user')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email','password')

class LikeAdmin(admin.ModelAdmin):
    list_display=('id', 'post', 'user','add_Like')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Upload, UploadAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Like, LikeAdmin)