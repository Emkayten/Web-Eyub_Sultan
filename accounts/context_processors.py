from .models import UserProfile

def user_roles_context(request):
    is_admin = False
    is_verwaltung = False
    is_media = False
    is_hoca = False

    if request.user.is_authenticated:
        user_roles = request.user.userprofile.roles.values_list('name', flat=True)
        is_admin = 'admin' in user_roles
        is_verwaltung = 'verwaltung' in user_roles
        is_media = 'media' in user_roles
        is_hoca = 'hoca' in user_roles

    return {
        'is_admin': is_admin,
        'is_verwaltung': is_verwaltung,
        'is_media': is_media,
        'is_hoca': is_hoca,
    }
