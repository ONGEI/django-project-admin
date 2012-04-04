from django.conf.urls.defaults import patterns, url
from django.conf import settings

urlpatterns = patterns('projectadmin.views',
    url(r'^show/calendar/$','show_calendar',name='project-admin-show-calendar'),
    url(r'^show/calendar/(?P<ano>\d+)/(?P<mes>\d+)/$','show_calendar',name='project-admin-show-calendar-ano-mes'),
)
