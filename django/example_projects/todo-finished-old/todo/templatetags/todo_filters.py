from django import template
register = template.Library()
from datetime import datetime, date

@register.filter(is_safe=True)
def delay(value):

    if not value:
        return 'Not given'

    today= date.today()
    delta = value - today
    
    if delta.days > 1:
        out = "In {0} days".format(delta.days)
    elif delta.days == 1:
        out= "Tomorrow"
    elif delta.days == 0:
        out = "Today"
    else:
        out = "You're late !"

    return out