from django.contrib import admin
from .models import *
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.reqister(Answer)