# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from .models import Project, Client, Note, ProjectPhase, Status
from .models import *

class TBInfoInline(admin.TabularInline):
    model = TenantBuildInfo
    extra = 0

class PhaseInfoInline(admin.TabularInline):
    model = PhaseInfo
    extra = 0

class TCInfoInline(admin.TabularInline):
    model = TestingCycleInfo
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    inlines = (TBInfoInline, PhaseInfoInline, TCInfoInline,)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Note)
admin.site.register(ProjectPhase)
admin.site.register(Status)
admin.site.register(Methodology)
admin.site.register(WDModule)
admin.site.register(TenantBuild)
admin.site.register(TestingCycle)
admin.site.register(TenantBuildInfo)
admin.site.register(PhaseInfo)
admin.site.register(TestingCycleInfo)
