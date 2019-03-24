from django.contrib import admin
from .models import user,tag,Album,location,tag_photo,comment,UserTofollow,following,photo


admin.site.register(user)
admin.site.register(Album)
admin.site.register(location)
admin.site.register(tag)
admin.site.register(tag_photo)
admin.site.register(comment)
admin.site.register(UserTofollow)
admin.site.register(following)
admin.site.register(photo)
