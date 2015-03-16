from django.conf.urls import patterns, include, url
from django.conf import settings
from projects.views import ProjectCreateView, MemberCreateView, MemberDeleteView

urlpatterns = patterns(
    '',
    url(r'^create/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^members/create/(?P<pk>\d+)$', MemberCreateView.as_view(),
        name='member_create'),
    url(r'^members/delete/(?P<pk>\d+)$', MemberDeleteView.as_view(),
        name='member_delete'),
)
