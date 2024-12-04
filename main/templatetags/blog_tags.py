from django import template
from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Value
from users.models import User

register = template.Library()

@register.simple_tag()
def total_users():
    return User.objects.all().count()