from django.test import TestCase
from .models import User, Company
from rest_framework.test import APIRequestFactory, force_authenticate


from portalbackend.lendapi.v1.accounts.views import UserList, UserDetail


class UserListTestCase(TestCase):
    """
    Tests the UserList View
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = '/lend/v1/users/'
        self.user = User.objects.create(id=2, first_name="FName", last_name="LName", email="test2@mail.com",
                                        username="usertwo", password="datapass")
        Company.objects.create(id=1, name="Test Company", external_id="ABC123",
                               website="https://en.wikipedia.org/wiki/Unit_testing", employee_count=1)

    def test_post(self):
        """
        Tests the Post Method on the UserList
        :return:
        """
        data = {'company': 1, 'username': 'testusername',
                'first_name': 'test', 'last_name': 'user',
                'email': 'test@mail.com', 'password': 'Testpass1'}
        request = self.factory.post(self.url, data)
        response = UserList.as_view()(request)
        desired_response = {'url': 'http://testserver/lend/v1/user/1/', 'username': 'testusername',
                            'first_name': 'test', 'last_name': 'user', 'email': 'test@mail.com', 'company': 1}
        self.assertEqual(response.status_code, 201)
        self.assertEquals(response.data, desired_response)

    def test_get(self):
        """
        Tests the Get Method on the UserList
        :return:
        """
        User.objects.create(id=1, first_name='test', last_name='user', email='test@mail.com',
                            username='testusername',password='TestPass1')
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = UserList.as_view()(request)
        self.assertEquals(len(response.data), 2)
        self.assertEquals(response.status_code, 200)

    def test_delete(self):
        """
        Tests the Delete Method on the UserList, should fail
        :return:
        """
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = UserList.as_view()(request)
        self.assertEquals(response.status_code, 405)


class UserDetailTestCase(TestCase):
    """
    Tests the UserDetail View
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.company = Company.objects.create(id=1, name="Test Company", external_id="ABC123",
                                              website="https://en.wikipedia.org/wiki/Unit_testing", employee_count=1)
        self.user = User.objects.create(id=1, first_name='test', last_name='user', email='test@mail.com',
                                        username='testusername', password='TestPass1', company_id=1)
        self.user_two = User.objects.create(id=2, first_name="FName", last_name="LName", email="test2@mail.com",
                                            username="usertwo", password="datapass")
        self.url = '/lend/v1/user/1/'

    def test_get(self):
        """
        Tests the GET Request on the UserDetail
        :return: User information
        """
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = UserDetail.as_view()(request, pk=1)
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.data['company']['website'])

    def test_put_success(self):
        """
        Tests the PUT Request on the UserDetail when the user matches the request
        :return: Altered Username
        """
        data = {'username': 'testusername', 'first_name': 'NEWtest',
                'last_name': 'user', 'email': 'test@mail.com'}
        request = self.factory.put(self.url, data=data)
        force_authenticate(request, user=self.user)
        response = UserDetail.as_view()(request, pk=1)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['first_name'], 'NEWtest')

    def test_put_failure(self):
        """
        Tests the PUT Request on the UserDetail when the user does not match the request
        :return: Unauthorized Code Failure (401)
        """
        data = {'username': 'testusername', 'first_name': 'NEWtest',
                'last_name': 'user', 'email': 'test@mail.com'}
        request = self.factory.put(self.url, data=data)
        force_authenticate(request, user=self.user_two)
        response = UserDetail.as_view()(request, pk=1)
        self.assertEquals(response.status_code, 401)

    def test_delete_success(self):
        """
        Tests the DELETE Request on the UserDetail when the user matches the request
        :return: Deleted User
        """
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = UserDetail.as_view()(request, pk=1)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(User.objects.filter(pk=1).first(), None)

    def test_delete_failure(self):
        """
        Tests the DELETE Request on the UserDetail when the user does not match the request
        :return: Unauthorized Code Failure (401)
        """
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user_two)
        response = UserDetail.as_view()(request, pk=1)
        self.assertEquals(response.status_code, 401)

