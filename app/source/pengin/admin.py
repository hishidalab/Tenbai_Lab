from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
# from .models import UserPostList
# from .models import Post
# admin.site.register(UserPostList)
# admin.site.register(Post)

class UserAdmin(BaseUserAdmin):

    list_display = (
        "loginID",
        "active",
        "staff",
        "admin",
    )
    list_filter = (
        "admin",
        "active",
    )
    filter_horizontal = ()
    ordering = ("loginID",)
    search_fields = ('loginID',)

    fieldsets = (
        (None, {'fields': ('loginID', 'password')}),
        ('Permissions', {'fields': ('staff', 'admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('loginID', 'password1', 'password2')}
        ),
    )

admin.site.register(ImageUpload)
admin.site.register(Comment)
admin.site.register(IconUplodeModel)