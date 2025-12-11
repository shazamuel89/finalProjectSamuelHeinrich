from django.contrib import admin
from .models import SiteUserProfile, LastfmUserProfile, Visualization

@admin.register(SiteUserProfile)
class SiteUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_lastfm_username',)
    search_fields = ('user__username', 'default_lastfm_username',)
    list_filter = ('default_lastfm_username',)


@admin.register(LastfmUserProfile)
class LastfmUserProfileAdmin(admin.ModelAdmin):
    list_display = ('lastfm_username', 'display_name', 'has_avatar', 'registered_date',)
    search_fields = ('lastfm_username', 'display_name',)
    list_filter = ('registered_date',)


@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'lastfm_user',
        'visualization_type',
        'created_at',
        'preview',
        'favorites_count',
    )
    search_fields = (
        'owner__username',
        'lastfm_user__lastfm_username',
        'visualization_type',
    )
    list_filter = ('visualization_type', 'created_at',)

    readonly_fields = ('preview',)

    def favorites_count(self, obj):
        return obj.favorites.count()

    favorites_count.short_description = 'Favorites'