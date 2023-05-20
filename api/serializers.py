from polls.models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.HyperlinkedRelatedField(
        view_name='choice-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(
        view_name='question-detail',
        read_only=True
    )

    class Meta:
        model = Choice
        fields = '__all__'
