import datetime as dt

from django.test import TestCase
from django.urls import reverse
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


def create_question(text, days):
    date = timezone.now() + dt.timedelta(days=days)
    return Question.objects.create(question_text=text, pub_date=date)


class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_questions"], [])

    def test_past_question(self):
        question = create_question(text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Past question.")
        self.assertQuerySetEqual(response.context["latest_questions"], [question])

    def test_future_question(self):
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_questions"], [])

    def test_future_question_and_past_question(self):
        past_question = create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Past question.")
        self.assertQuerySetEqual(response.context["latest_questions"], [past_question])

    def test_two_past_questions(self):
        question1 = create_question(text="Past question 1.", days=-5)
        question2 = create_question(text="Past question 2.", days=-30)
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Past question 1.")
        self.assertContains(response, "Past question 2.")
        self.assertQuerySetEqual(response.context["latest_questions"], [question1, question2])
