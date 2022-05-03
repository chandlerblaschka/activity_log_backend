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
    path(r'dashboard/golf/all/', views.golf),
    path(r'dashboard/golf/bookOrder/', views.golf_book_order),
    path(r'dashboard/<str:industry>/<slug:action>', views.dashboard_filter),
    # path(r'dashboard/<int:year>/<int:month>/<str:industry>/<slug:request>/<str:employee>', views.dashboard_table),
    re_path(r'dashboard/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<industry>\w+)/(?P<action>[-\w]+)/(?P<employee>\w+)', views.dashboard_table),
    path(r'golf/open/', views.golf_open),
    path(r'golf/today/', views.golf_today),
    path(r'golf/this_week/', views.golf_this_week),
    path(r'golf/', views.golf),
    # re_path(r'golf/(?P<pk>[0-9]+)$', views.golf_action),
    re_path(r'edit/(?P<pk>[0-9]+)$', views.edit_action),
 ]