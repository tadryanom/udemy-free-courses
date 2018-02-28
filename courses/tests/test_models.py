from django.test import TestCase

from courses.models import Course

from model_mommy import mommy


class CourseTestCase(TestCase):

    def setUp(self):
        self.course = mommy.make(Course, title='Course 1')

    def test_course_creation(self):
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.__str__(), self.course.title)