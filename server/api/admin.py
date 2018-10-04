# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Client, Note, ProjectPhase, Status

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Note)
admin.site.register(ProjectPhase)
admin.site.register(Status)
