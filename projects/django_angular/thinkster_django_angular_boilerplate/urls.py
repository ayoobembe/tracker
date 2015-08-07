from django.conf.urls import patterns, include, url

from thinkster_django_angular_boilerplate.views import IndexView

urlpatterns = patterns(
    '',

    url(r'^monitor/', include('security_monitor.urls')),

    url('^.*$', IndexView.as_view(), name='index'),
)
