from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['__str__','choice','vote_count']
    class Meta:
        model = Choice
admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)