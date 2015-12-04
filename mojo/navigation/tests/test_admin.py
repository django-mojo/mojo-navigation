# -*- coding: utf-8 -*-

from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.test.client import RequestFactory

from mojo.navigation.admin import ItemAdmin
from mojo.navigation.tests.models import TestItem


class MockRequest(object):
    pass


class MockSuperUser(object):
    is_active = True
    is_staff = True

    def has_perm(self, perm):
        return True  # pragma: no cover

request = RequestFactory()
request.user = MockSuperUser()
request.csrf_processing_done = True


class ItemAdminTest(TestCase):
    """
    Tests for mojo.navigation.admin.ItemAdmin
    """

    def setUp(self):
        # create a menu parent
        self.menu_parent = TestItem(name=u"Parent")
        self.menu_parent.save()

        # create a menu child
        self.menu_child = TestItem(parent=self.menu_parent, name=u"Child")
        self.menu_child.save()

        # create a site instance
        self.site = AdminSite()

    def test_level_limit_not_set_all_levels_returned(self):
        """
        Testing if level_limit is not set, all levels should be returned in the parent select.
        """
        item_admin = ItemAdmin(TestItem, self.site)
        form = item_admin.get_form(request)
        queryset = form.base_fields['parent']._queryset
        self.assertEqual(len(queryset), 2)
        self.assertIn(self.menu_parent, queryset)
        self.assertIn(self.menu_child, queryset)

    def test_level_limit_set_only_filtered_levels_returned(self):
        """
        Testing if level_limit is set the parent field queryset should filter and remove levels underneath.
        """
        item_admin = ItemAdmin(TestItem, self.site)
        item_admin.level_limit = 1
        form = item_admin.get_form(request)
        queryset = form.base_fields['parent']._queryset
        self.assertEqual(len(form.base_fields['parent']._queryset), 1)
        self.assertNotIn(self.menu_child, queryset)

    def test_level_limit_not_set_do_move_any_level_allowed(self):
        """
        Testing if when the level_limit attribute is not set the do_move method should allow anything.
        """
        item_admin = ItemAdmin(TestItem, self.site)
        instance = item_admin.get_object(request, self.menu_child.id)
        parent_instance = item_admin.get_object(request, self.menu_parent.id)
        item_admin.do_move(instance, 'inside', parent_instance)
        self.assertEqual(instance.parent, parent_instance)

    def test_level_limit_set_do_move_filters_level_allowed(self):
        """
        Testing if when the level_limit attribute is set the move_to method should not allow exceeding it.
        """
        item_admin = ItemAdmin(TestItem, self.site)
        item_admin.level_limit = 0
        instance = item_admin.get_object(request, self.menu_child.id)
        parent_instance = item_admin.get_object(request, self.menu_parent.id)
        with self.assertRaises(Exception):
            item_admin.do_move(instance, 'inside', parent_instance)
