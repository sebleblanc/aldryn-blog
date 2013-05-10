# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BlogApp(CMSApp):

    name = _('Blog')
    app_name = 'aldryn-blog'
    urls = ['aldryn_blog.urls']

apphook_pool.register(BlogApp)
