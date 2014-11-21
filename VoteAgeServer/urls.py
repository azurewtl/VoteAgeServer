from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from VoteAgeApp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'votefeed', views.VoteFeedViewSet)
router.register(r'option', views.OptionViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VoteAgeServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^API/', include(router.urls)),
)
