from django.contrib.auth.models import User
from rest_framework import serializers
# from api.models import Methodology, WDModule, ProjectPhase, Status, TenantBuild, TestingCycle, Client, Project, TenantBuildInfo, PhaseInfo, TestingCycleInfo, Note
from api.models import *

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
            'order',
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

class TenantBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantBuild
        fields = (
            'id',
            'name',
        )

class TestingCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingCycle
        fields = (
            'name',
        )

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'client',
            'body',
        )


class ProjectSerializer(serializers.ModelSerializer):
    """
    This needs to be addressed ASAP
    """
    owner = serializers.ReadOnlyField(source='owner.username', required=False)
    # client = serializers.ReadOnlyField(source='client.name')
    # status = StatusSerializer(required=False)
    # phases = ProjectPhaseSerializer(many=True, required=False)
    notes = NoteSerializer(many=True, required=False)
    # methodology = MethodologySerializer()
    # scope = WDModuleSerializer(many=True)
    builds = TenantBuildSerializer(many=True)
    testing_cycles = TestingCycleSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'client',
            'methodology',
            'phase_one_project',
            'phases',
            'active_phase',
            'status',
            'go_live_date',
            'kickoff_date',
            'first_payroll',
            'scope',
            'builds',
            'testing_cycles',
            'notes',
            'owner'
        )

    def create(self, validated_data):

        notes_data = validated_data.pop('notes')
        project = Project.objects.create(**validated_data)
        # project = Project.objects.create(
        #     name=validated_data.get('name'),
        #     client=validated_data.get('client'),
        #     owner=validated_data.get('owner'),
        #     status=validated_data.get('status'),
        #     methodology=validated_data.get('methodology'),
        #     phase_one_project=validated_data.get('phase_one_project'),
        #     active_phase=validated_data.get('active_phase'),
        #     phases=validated_data.get('phases')
        #     project_phase=validated_data.get('project_phase'),
        #     go_live_date=validated_data.get('go_live_date'),
        # )

        for note_data in notes_data:
            Note.objects.create(project=project, **note_data)

        return project

class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    notes = NoteSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)

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
