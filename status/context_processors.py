from django.contrib.auth.models import User

def group_processor(request):
    if request.user.is_authenticated:
        is_li_group = request.user.groups.filter(name='li').exists() 
    else:
        is_li_group = False

    return {
        'is_li_group': is_li_group,
    }
