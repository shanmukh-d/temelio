from django.test import TestCase
from django.contrib.auth.models import User
from common import models
from common import dal

class DalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.permission = models.Permissions.objects.create(name='test_permission')
        self.user_permissions = models.UserPermissions.objects.create(user=self.user)
        self.user_permissions.permissions.add(self.permission)

    def test_get_user_from_username(self):
        print('shanu')
        with self.subTest('User not found'):
            user = dal.get_user_from_username('non_existent_user')
            self.assertIsNone(user)

        with self.subTest('User found'):
            user = dal.get_user_from_username('testuser')
            self.assertEqual(user, self.user)

    def test_check_if_user_has_permission(self):
        with self.subTest('When user does not have permission'):
            has_permission = dal.check_if_user_has_permission(self.user, 'non_existent_permission')
            self.assertFalse(has_permission)

        with self.subTest('When user has permission'):
            has_permission = dal.check_if_user_has_permission(self.user, 'test_permission')
            self.assertTrue(has_permission)
        
        with self.subTest('When user has multiple permissions'):
            permission = models.Permissions.objects.create(name='test_permission_2')
            self.user_permissions.permissions.add(permission)
            has_permission = dal.check_if_user_has_permission(self.user, 'test_permission_2')
            self.assertTrue(has_permission)