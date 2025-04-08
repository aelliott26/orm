from django.contrib import admin

from .models import User, Reporter, Article, Publication

admin.site.register(User)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)



