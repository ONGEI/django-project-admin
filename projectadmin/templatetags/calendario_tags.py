from django import template
from django.db.models import Q
from calendar import Calendar
import datetime
import re
 
register = template.Library()
 
@register.tag(name="get_calendar")
def do_calendar(parser, token):
    syntax_help = "syntax should be \"get_calendar for <month> <year> as <var_name>\""
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments, %s" % (token.contents.split()[0], syntax_help)
    m = re.search(r'for (.*?) (.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments, %s" % (tag_name, syntax_help)
    return GetCalendarNode(*m.groups())
 
class GetCalendarNode(template.Node):
    def __init__(self, month, year, var_name):
        self.year = template.Variable(year)
        self.month = template.Variable(month)
        self.var_name = var_name
        
    def render(self, context):
        mycal = Calendar()
        context[self.var_name] = mycal.monthdatescalendar(int(self.year.resolve(context)), int(self.month.resolve(context)))
        return ''

@register.filter(name="get_peticiones")
def get_peticiones(peticiones, dia):
    return peticiones.filter(Q(creado_fecha__day=dia) | Q(inicio_fecha__day=dia) | Q(terminado_fecha__day=dia) | Q(completo_fecha__day=dia))
