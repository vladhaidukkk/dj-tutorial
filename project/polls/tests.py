import datetime as dt

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_recently_published_with_current_question_returns_true(self):
        date = timezone.now()
        current_question = Question(pub_date=date)
        self.assertTrue(current_question.was_published_recently())

    def test_was_recently_published_with_recent_question_returns_true(self):
        date = timezone.now() - dt.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=date)
        self.assertTrue(recent_question.was_published_recently())

    def test_was_recently_published_with_old_question_returns_false(self):
        date = timezone.now() - dt.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=date)
        self.assertFalse(old_question.was_published_recently())

    def test_was_recently_published_with_future_question_returns_false(self):
        date = timezone.now() + dt.timedelta(days=30)
        future_question = Question(pub_date=date)
        self.assertFalse(future_question.was_published_recently())
