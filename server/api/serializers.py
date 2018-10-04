from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Methodology, WDModule, ProjectPhase, Status, Client, Note, Project, TenantBuild

class MethodologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = (
            'name',
        )

class WDModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WDModule
        fields = (
            'name',
        )

class ProjectPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhase
        fields = (
            'id',
            'name',
        )

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'id',
            'name',
            'color_code',
            'red',
            'green',
            'blue',
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'client',
            'body',
        )

class TenantBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantBuild
        fields = (
            'id',
            'name',
            'start_date',
            'end_date'
        )

class ProjectSerializer(serializers.ModelSerializer):
    """
    This needs to be addressed ASAP
    """
    owner = serializers.ReadOnlyField(source='owner.username', allow_null=True)
    client = serializers.ReadOnlyField(source='client.name', allow_null=True)
    status = StatusSerializer(read_only=True, allow_null=True)
    project_phase = ProjectPhaseSerializer(read_only=True, allow_null=True)
    notes = NoteSerializer(many=True, allow_null=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'client',
            'status',
            'project_phase',
            'go_live_date',
            'notes',
            'owner'
        )

    def create(self, validated_data):
        notes_data = validated_data.pop('notes')
        project = Project.objects.create(**validated_data)
        project = Project.objects.create(
            name=validated_data.get('name'),
            client=validated_data.get('client'),
            status=validated_data.get('status'),
            project_phase=validated_data.get('project_phase'),
            go_live_date=validated_data.get('go_live_date'),
        )

        for note_data in notes_data:
            Note.objects.create(project=project, **note_data)

        return project

class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    notes = NoteSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'owner',
            'notes',
            'projects',
        )

    def create(self, validated_data):
        notes_data = validated_data.pop('notes')
        projects_data = validated_data.pop('projects')
        client = Client.objects.create(**validated_data)

        for note_data in notes_data:
            Note.objects.create(client=client, **note_data)

        for project_data in projects_data:
            Project.objects.create(client=client, **project_data)

        return client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
