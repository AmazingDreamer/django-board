from django.test import TestCase
from django.urls import resolve
from ..views import TopicListView


class BoardTopicsTest(TestCase):
    view = resolve('boards/1/')
    assertEquals = (view.func.view_class, TopicListView)
