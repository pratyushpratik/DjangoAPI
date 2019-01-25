from rest_framework import serializers
from .models import LearningCentreCategories, LearningCentreSubCategories, LearningCentreSubCategoriesQuestionAnswer


class LearningCentreSubCategoriesQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = LearningCentreSubCategoriesQuestionAnswer
        fields = '__all__'


class LearningCentreSubCategoriesSerializer(serializers.ModelSerializer):

    learning_centre_subcategories_questions_answers = LearningCentreSubCategoriesQuestionAnswerSerializer(source='learningcentresubcategoriesquestionanswer_set', many=True)

    class Meta:
        model = LearningCentreSubCategories
        fields = ('category', 'subcategory_id', 'subcategory_name', 'date_added', 'learning_centre_subcategories_questions_answers')


class LearningCentreCategoriesSerializer(serializers.ModelSerializer):

    learning_centre_subcategories = LearningCentreSubCategoriesSerializer(source='learningcentresubcategories_set', many=True)

    class Meta:
        model = LearningCentreCategories
        fields = ('category_id', 'category_name', 'date_added', 'learning_centre_subcategories')