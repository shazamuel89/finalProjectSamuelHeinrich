from django.contrib import admin

from .models import SiteUserProfile, LastfmUserProfile, Visualization

admin.site.register(SiteUserProfile)
admin.site.register(LastfmUserProfile)
admin.site.register(Visualization)