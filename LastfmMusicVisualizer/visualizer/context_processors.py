from .models import SiteUserProfile

def default_lastfm_username(request):
    if request.user.is_authenticated:
        try:
            return {
                "default_username": request.user.siteuserprofile.default_lastfm_username
            }
        except SiteUserProfile.DoesNotExist:
            return { "default_username": None }
    return { "default_username": None }
