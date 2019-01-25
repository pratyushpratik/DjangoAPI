from django.contrib import admin
from .models import LearningCentreCategories, LearningCentreSubCategories, LearningCentreSubCategoriesQuestionAnswer

# Register your models here.

admin.site.register(LearningCentreCategories)
admin.site.register(LearningCentreSubCategories)
admin.site.register(LearningCentreSubCategoriesQuestionAnswer)