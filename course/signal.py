from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender = User) # using decorater
def userLoggedIn(sender, request, user, **kwargs):
    print('sender : ', sender)
    print('request : ', request)
    print('User : ', user)
    print(f'kwargs :  {kwargs}')

    # track IP address------
    ip = request.META.get('REMOTE_ADDR')
    print('IP : ', ip)
    request.session['IP'] = ip