from django.contrib import admin
from users.models import Contact, Post, FilesUpload, Comment, Matches

# Register your models here. 

admin.site.register(Contact)

#uploading profile info code changes
admin.site.register(Post)
admin.site.register(FilesUpload)
admin.site.register(Comment)
admin.site.register(Matches)