""" Tests for blog.permissions """

from rest_framework.test import APITestCase


# Create your tests here.
class PermissionsTest(APITestCase):
    """Tests for custom access permissions"""

    def test_is_owner_permission(self):
        """Test IsOwner permission"""

        pass

    def test_is_account_owner_permission(self):
        """Test IsAccountOwner permission"""

        pass

    def test_is_read_only_permission(self):
        """Test IsReadOnly permission"""

        pass

    def test_is_list_only_permission(self):
        """Test IsListOnly permission"""

        pass
