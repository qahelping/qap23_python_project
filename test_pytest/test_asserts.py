import pytest


@pytest.mark.assertion
def test_assertion():
    len_arr =  3
    current_len_arr = len([1, 2, 3])
    assert current_len_arr != len_arr, f"Размер массива мы ожидали не {len_arr}, но получили {current_len_arr}"

@pytest.mark.assertion
def test_assertion2():
    current_str = 'строка'
    in_str = '123'
    assert in_str in current_str
