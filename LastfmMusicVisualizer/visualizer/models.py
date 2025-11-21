from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class SiteUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_lastfm_username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class LastfmUserProfile(models.Model):
    lastfm_username = models.CharField(max_length=100, unique=True)

    display_name = models.CharField(max_length=100, null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)

    total_scrobbles = models.IntegerField(null=True, blank=True)
    registered_date = models.DateField(null=True, blank=True)

    top_artists = models.JSONField(default=dict)
    top_albums = models.JSONField(default=dict)
    top_tracks = models.JSONField(default=dict)
    recent_tracks = models.JSONField(default=dict)

    last_updated = models.DateTimeField(default=timezone.now)   # When the user's data was last fetched from Last.fm

    def __str__(self):
        return self.lastfm_username

    @admin.display(description='Has recent tracks?')
    def has_recent_tracks(self):
        return bool(self.recent_tracks)

    @admin.display(description="Last updated")
    def last_updated_short(self):
        return self.last_updated.strftime("%Y-%m-%d %H:%M")

    @admin.display(description="Has profile image?")
    def has_avatar(self):
        return bool(self.avatar_url)


class Visualization(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_visualizations')
    lastfm_user = models.ForeignKey(LastfmUserProfile, on_delete=models.CASCADE, related_name='visualizations')

    visualization_type = models.CharField(max_length=100)
    filters = models.JSONField(default=dict, null=True, blank=True)

    favorites = models.ManyToManyField(User, related_name='favorite_visualizations', blank=True)

    image_file = models.FileField(upload_to='visualizations/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.lastfm_user.lastfm_username} ({self.visualization_type})'

    @admin.display(description='Preview link')
    def preview(self):
        if self.image_file:
            return self.image_file.url
        return "(no image)"
