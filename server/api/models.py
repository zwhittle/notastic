# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Methodology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WDModule(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ('order','name',)

    def __str__(self):
        return self.name

class ProjectPhase(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=15)
    color_code = models.CharField(max_length=7)
    red = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    blue = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def rgb(self):
        return "rgb({0}, {1}, {2})".format(red, green, blue)

class TenantBuild(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class TestingCycle(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)

    class Meta:
        # ordering = ('created',)
        ordering = ('name',)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey('Client', related_name='projects', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='projects', null=True, blank=True, on_delete=models.CASCADE)
    status = models.ForeignKey('Status', related_name='projects', blank=True, null=True, on_delete=models.CASCADE)
    methodology = models.ForeignKey('Methodology', related_name='projects', on_delete=models.CASCADE)
    phase_one_project = models.BooleanField(default=True)
    active_phase = models.ForeignKey(ProjectPhase, related_name='clients', blank=True, null=True, on_delete=models.CASCADE)
    phases = models.ManyToManyField(ProjectPhase, through='PhaseInfo')
    go_live_date = models.DateField(null=True, blank=True)
    kickoff_date = models.DateField(null=True, blank=True)
    first_payroll = models.DateField(null=True, blank=True)
    scope = models.ManyToManyField(WDModule)
    builds = models.ManyToManyField(TenantBuild, through='TenantBuildInfo')
    testing_cycles = models.ManyToManyField(TestingCycle, through='TestingCycleInfo')

    class Meta:
        # ordering = ('created',)
        ordering = ('name',)

    def __str__(self):
        return self.name

class TenantBuildInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    build = models.ForeignKey(TenantBuild, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('start_date', 'end_date')

    def __str__(self):
        return "{0} - {1}".format(self.project, self.build)

class PhaseInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phase = models.ForeignKey(ProjectPhase, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('project', 'start_date', 'end_date')

    def __str__(self):
        return "{0} - {1}".format(self.project, self.phase)

class TestingCycleInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    cycle = models.ForeignKey(TestingCycle, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('project', 'start_date', 'end_date')

    def __str__(self):
        return "{0} - {1}".format(self.project, self.cycle)

class Note(models.Model):
    project = models.ForeignKey('Project', related_name='notes', blank=True, null=True, on_delete=models.CASCADE)
    client = models.ForeignKey('Client', related_name='notes', blank=True, null=True, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    owner =  models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        # ordering = ('created',)
        ordering = ('project',)

    def __str__(self):
        return self.body
