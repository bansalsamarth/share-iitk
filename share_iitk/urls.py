from django.conf.urls import patterns, include, url

from share.views import upload_page, about, contact, home, file_submit, moderator, landing, moderator_approval, search, explore, moderator_reject

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'share_iitk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', upload_page),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^file_submit/$', file_submit),
    url(r'^$', landing),
    url(r'^home/', home),
    url(r'^moderator/', moderator),
    url(r'^moderator_approval/(?P<id>\d+)', moderator_approval),
    url(r'^moderator_reject/(?P<id>\d+)', moderator_reject),    
    url(r'^search/', search),
    url(r'^explore/', explore),
)
