from .models import Profile

def ensure_profile(user):
    profile, created = Profile.objects.get_or_create(user=user)
    return profile