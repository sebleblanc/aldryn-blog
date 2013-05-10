# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from aldryn_blog.views import ArchiveView, PostDetailView

urlpatterns = patterns(
    '',
    url(r'^$',
        ArchiveView.as_view(),
        name='latest-posts'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        PostDetailView.as_view(),
        name='post-detail')
)
