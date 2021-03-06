from django.contrib import admin
from teacherq.models import Question, AnswerOption, UserProfile



class AnswerOptionInline(admin.TabularInline):
	model = AnswerOption
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
			(None, {'fields': ['question']}),
	]
	inlines = [AnswerOptionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
