# import pytest
#
import pytest


class TestUserClass:

    @pytest.mark.usefixtures("user")
    def test_user(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user1(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user2(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user3(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"


class TestUser2Class:

    @pytest.mark.usefixtures("user")
    def test_user(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user1(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user2(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"

    @pytest.mark.usefixtures("user")
    def test_user3(self, user):
        print("\n+++Запустили тест 'test_user'+++")
        assert user.get("name") == "Alica"
