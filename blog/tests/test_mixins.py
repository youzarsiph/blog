""" Tests for blog.permissions """

from rest_framework.test import APITestCase


# Create your tests here.
class MixinsTest(APITestCase):
    """Tests for custom view mixins"""

    def test_owner_mixin(self):
        """Test OwnerMixin by testing a view that uses it"""

        pass
