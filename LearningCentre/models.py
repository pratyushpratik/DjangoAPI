from django.db import models
import datetime


class LearningCentreCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class LearningCentreSubCategories(models.Model):
    category = models.ForeignKey(LearningCentreCategories, on_delete=models.CASCADE)
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subcategory_name


class LearningCentreSubCategoriesQuestionAnswer(models.Model):
    category = models.ForeignKey(LearningCentreCategories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(LearningCentreSubCategories, on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=10000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question