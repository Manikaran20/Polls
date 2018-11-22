# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your ehrimodels here.
from Gehri.models import Question
admin.site.register(Question)

from Gehri.models import Choice
admin.site.register(Choice)


