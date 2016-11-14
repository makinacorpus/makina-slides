from django.conf.urls import patterns, include, url
from todo.views import TodoListList

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todoproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(regex=r'^login/',
        view='django.contrib.auth.views.login',
        name='login'),

    url(regex=r'^logout/',
        view='django.contrib.auth.views.logout_then_login',
        name='logout'),

    url(r'^$', TodoListList.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/', include('todo.urls')),
)
