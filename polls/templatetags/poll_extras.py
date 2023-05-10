from django import template
from jalali_date import date2jalali, datetime2jalali

register = template.Library()


@register.filter("show_date")
def cut(value):
    """shoe to exact_date"""
    return date2jalali(value)

@register.filter("show_time")
def cut(value):
    """shoe to exact_date"""
    return datetime2jalali(value)
