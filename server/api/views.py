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
        'clients': reverse('client-list', request=request, format=format),
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
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and
    'destroy' actions
    """
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

# class ProjectAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     resource_name = 'projects'
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         return Project.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ProjectRudView(generics.RetrieveUpdateDestroyAPIView):
#     resource_name = 'projects'
#     lookup_field = 'id'
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         return Project.objects.all()
#
# class ClientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     resource_name = 'clients'
#     serializer_class = ClientSerializer
#
#     def get_queryset(self):
#         return Client.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ClientRudView(generics.RetrieveUpdateDestroyAPIView):
#     resource_name = 'clients'
#     lookup_field = 'id'
#     serializer_class = ClientSerializer
#
#     def get_queryset(self):
#         return Client.objects.all()
#
# class NoteAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     resource_name = 'notes'
#     serializer_class = NoteSerializer
#
#     def get_queryset(self):
#         return Note.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class NoteRudView(generics.RetrieveUpdateDestroyAPIView):
#     resource_name = 'notes'
#     serializer_class = NoteSerializer
#
#     def get_queryset(self):
#         return Note.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
