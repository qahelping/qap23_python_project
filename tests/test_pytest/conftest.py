import pytest


@pytest.fixture()
def user():
    #print("\n+++Вызвали фикстуру 'user'+++")
    yield {"name": "Alica User"}
    #print("\n+++Вернулись в фикстуру 'user'+++")


@pytest.fixture(scope="function", autouse=False)
def auto_use_false():
    #print("\n+++Вызвали фикстуру 'auto_use_false'+++")
    yield {"name": "Alica Auto_use_false"}
    #print("\n+++Вернулись в фикстуру 'auto_use_false'+++")


@pytest.fixture(scope="function", autouse=True)
def auto_use_true():
    pass
    #print("\n+++LOGGING: Вызвали фикстуру 'auto_use'+++")


@pytest.fixture(scope="session", autouse=True)
def session():
    #print("\n+++Вызвали фикстуру 'session'+++")
    yield
    #print("\n+++Вернулись в фикстуру 'session'+++")


@pytest.fixture(scope="package", autouse=True)
def package():
    #print("\n+++Вызвали фикстуру 'package'+++")
    yield
    #print("\n+++Вернулись в фикстуру 'package'+++")


@pytest.fixture(scope="module", autouse=True)
def module():
    #print("\n+++Вызвали фикстуру 'module'+++")
    yield
    #print("\n+++Вернулись в фикстуру 'module'+++")


@pytest.fixture(scope="class", autouse=True)
def class_func():
    #print("\n+++Вызвали фикстуру 'class'+++")
    yield
    #print("\n+++Вернулись в фикстуру 'class'+++")


@pytest.fixture(scope="function", autouse=True)
def function_func():
    #print("\n+++Вызвали фикстуру 'function'+++")
    yield
    #print("\n+++Вернулись в фикстуру 'function'+++")
