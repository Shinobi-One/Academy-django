from django.http import HttpRequest


def get_ip(request:HttpRequest):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded :
        user_ip = x_forwarded
    else :
        user_ip = request.META.get('REMOTE_ADDR')

    return user_ip
