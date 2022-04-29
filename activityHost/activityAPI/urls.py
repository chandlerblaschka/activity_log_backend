from django.urls import include, path, re_path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'master', views.MasterViewSet)
# router.register(r'golf', views.GolfViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'dashboard/', views.dashboard),
    path(r'golf/open/', views.golf_open),
    path(r'golf/', views.golf),
    # re_path(r'golf/(?P<pk>[0-9]+)$', views.golf_action),
    re_path(r'edit/(?P<pk>[0-9]+)$', views.edit_action),
 ]