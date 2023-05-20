from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionViewTest(TestCase):
    def test_empty_question_list(self):
        response = self.client.get('/api/questions/')
        self.assertEquals(response.status_code, 200)

        data = response.json()
        self.assertEquals(data, [])

    def test_question_list(self):
        Question.objects.create(question_text='Text1', pub_date=timezone.now())
        Question.objects.create(question_text='Text2', pub_date=timezone.now())

        response = self.client.get('/api/questions/')
        self.assertEquals(response.status_code, 200)

        data = response.json()
        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['question_text'], 'Text1')
        self.assertEquals(data[1]['question_text'], 'Text2')

    def test_nonexistent_question_detail(self):
        response = self.client.get('/api/questions/1/')
        self.assertEquals(response.status_code, 404)

    def test_question_detail(self):
        question = Question.objects.create(question_text='Text1', pub_date=timezone.now())

        response = self.client.get(f'/api/questions/{question.id}/')
        self.assertEquals(response.status_code, 200)

        data = response.json()
        self.assertEquals(data['question_text'], question.question_text)
