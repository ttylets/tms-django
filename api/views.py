from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

from rest_framework import viewsets, filters

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.models import Count


@api_view(['GET'])
def test_view(request):
    my_param_1 = request.query_params.get('my_param_1')
    my_param_2 = request.query_params.get('my_param_2')
    data = {'status': 'ok', 'param_values': [my_param_1, my_param_2]}
    return Response(data)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['id', 'question_text', 'pub_date']
    ordering_fields = ['id', 'question_text', 'pub_date']

    def get_queryset(self):
        queryset = Question.objects.prefetch_related('choices')
        min_choice_count = self.request.query_params.get('min_choice_count')
        if min_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__gte=min_choice_count)
        max_choice_count = self.request.query_params.get('max_choice_count')
        if max_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__lte=max_choice_count)
        return queryset


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'question_text', 'pub_date']
    search_fields = ['id', 'question_text', 'pub_date']



