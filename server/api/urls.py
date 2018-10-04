# from .views import ClientAPIView, ClientRudView, ProjectAPIView, ProjectRudView, NoteAPIView, NoteRudView
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'methodologies', views.MethodologyViewSet)
router.register(r'wdmodules', views.WDModuleViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'projectphases', views.ProjectPhaseViewSet)
router.register(r'statuses', views.StatusViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'tenantbuilds', views.TenantBuildViewSet)

# urlpatterns = [
#     url(r'^projects/?$', ProjectAPIView.as_view(), name='project-create'),
#     url(r'^projects/(?P<id>\d+)/?', ProjectRudView.as_view(), name='project-rud'),
#     url(r'^clients/?$', ClientAPIView.as_view(), name='client-create'),
#     url(r'^clients/(?P<id>\d+)/?', ClientRudView.as_view(), name='client-rud'),
#     url(r'^notes/?$', NoteAPIView.as_view(), name='note-create'),
#     url(r'^notes/(?P<id>\d+)/?', NoteRudView.as_view(), name='note-rud'),
# ]

urlpatterns = [
    url(r'^', include(router.urls)),
]
