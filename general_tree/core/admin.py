from django.contrib import auth
from django.contrib import admin
from django.contrib.sites.models import Site
import django.contrib.auth.models


admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
admin.site.unregister(Site)

admin.site.site_header = 'Генеалогическое дерево'
admin.site.site_title = 'Генеалогическое дерево'
admin.site.index_title = ''
