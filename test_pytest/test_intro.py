# import pytest
#
#
# def func(a_1, b_2):
#     if type(a_1) is str or type(b_2) is str:
#         return "Error"
#     nat = 0
#     for i in range(a_1, b_2 + 1):
#         nat += i
#
#     return nat
#
#
# @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 0, 0), (10, 15, 75), (-5, 5, 0)])
# def test_positive(a, b, expected):
#     result = func(a, b)
#     assert result == expected
#     assert type(result) is int
#
#
# @pytest.fixture()
# def a(request):
#     return int(request.param)
#
#
# @pytest.fixture()
# def b(request):
#     return int(request.param)
#
#
# @pytest.mark.parametrize(
#     "a, b, expected",
#     [("1", "2", "Error"), (1, "2", "Error"), ("1", 2, "Error")],
#     ids=["str str", "int str", "str int"],
#     indirect=["a", "b"],
# )
# def test_negative(a, b, expected):
#     print('HELLLO')
#     result = func(a, b)
#     assert result == expected
#     assert type(result) is str
#
#
# # def test_dict():
# #     assert {"A": 1, "B": 2} == {"A": 2, "B": 2}
#
#
import pytest


class TestZeroEx:

    def test_0(self):
        assert 1 / 0

@pytest.mark.usefixtures("auto_use_false")
class TestAutoUser:

    def test_0(self, user):
        print('USER:', user)
        assert user
