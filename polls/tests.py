from time import timezone
from django.test import TestCase
from django.db import transaction
from polls.models import Question


@transaction.atomic
def create_questions(raising):
    Question.objects.create(pub_date=timezone.now())
    if raising:
        raise Exception()
    Question.objects.create(pub_date=timezone.now())


class TestTransaction(TestCase):
    def test_transaction(self):
        self.assertEqual(Question.objects.count(), 0)
        create_questions(False)
        self.assertEqual(Question.objects.count(), 2)
        self.assertRaises(Exception, lambda: create_questions(True))

        # check question count is still 2
        self.assertEqual(Question.objects.count(), 2)
