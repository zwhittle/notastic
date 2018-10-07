from rest_framework import generics, mixins, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from api.models import Methodology, WDModule, ProjectPhase, Status, Project, Client, Note
from api.serializers import MethodologySerializer, WDModuleSerializer, ProjectPhaseSerializer, StatusSerializer,TenantBuildSerializer, ProjectSerializer, ClientSerializer, NoteSerializer, UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'methodologies': reverse('methodology-list', request=request, format=format),
        'wd_modules': reverse('wdmodule-list', request=request, format=format),
        'project_phases': reverse('projectphase-list', request=request, format=format),
        'statuses': reverse('status-list', request=request, format=format),
        'tenant_builds': reverse('tenantbuild-list', request=request, format=format),
        'testing_cycles': reverse('testingcycle-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format)
    })

class MethodologyViewSet(viewsets.ModelViewSet):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer

class WDModuleViewSet(viewsets.ModelViewSet):
    queryset = WDModule.objects.all()
    serializer_class = WDModuleSerializer

class ProjectPhaseViewSet(viewsets.ModelViewSet):
    queryset = ProjectPhase.objects.all()
    serializer_class = ProjectPhaseSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TenantBuildViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = TenantBuildSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
