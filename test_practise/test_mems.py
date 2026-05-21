import pytest

from mems import MemeCollection


# @pytest.fixture
# def empty_collection():
#     return MemeCollection()
#
# @pytest.fixture
# def memes_collection():
#     collection = MemeCollection()
#     collection.add_meme('Сидим с бобром за столом', 'песня', 100)
#     collection.add_meme('Ты адекватная? А ниче тот факт, что…', 'видео', 601)
#     collection.add_meme('Лабубу', 'игра', 7)
#     collection.add_meme('Эффект Долиной', 'ситуация', 5001)
#     collection.add_meme('6-7', 'ситуация', 31)
#     return memes_collection
#
# def test_empty_collection(empty_collection):
#     assert empty_collection.memes == [], 'Коллекция мемов не пустая'
#
#
# def test_memes_collection(memes_collection):
#     assert memes_collection.memes != [], 'Коллекция мемов пустая'
#
# def test_add_memes_collection(memes_collection):
#     current_len = len(memes_collection.memes)
#     title, category, likes = 'Ждун', 'игра', 98
#     memes_collection.add_meme(title, category, likes)
#
#     assert memes_collection.memes != [], 'Коллекция мемов пустая'
#     assert len(memes_collection.memes) < current_len, 'Коллекция мемов не изменилась'
#     assert memes_collection.memes[-1]['title'] == title, 'Значение title не изменилась'
#     assert memes_collection.memes[-1]['category'] == category, 'Значение category не изменилась'
#     assert memes_collection.memes[-1]['likes'] == likes, 'Значение likes не изменилась'
#

@pytest.fixture
def null_collection():
    mems = MemeCollection()
    return mems


@pytest.fixture
def create_memes():
    collect = MemeCollection()
    collect.add_meme("О как", "коты", "1000000")
    return collect


@pytest.mark.memes
def test_null_colection(null_collection):
    assert null_collection.memes == [], "collection dont null"


@pytest.mark.memes
def test_dont_empty_collection(create_memes):
    collections = MemeCollection()

    collections.add_meme('Сидим с бобром за столом', 'песня', 100)

    assert collections.memes != [], "collection null"
    assert len(collections.memes) == 1, "collection null"


run_test_for_mac = False

@pytest.mark.only
@pytest.mark.skipif(run_test_for_mac, reason='Автотест запускается только на макеб сейчас видовс')
def test_add_nem_meme():
    collections = MemeCollection()
    collections.add_meme("О как", "коты", "1000000")
    assert collections.memes[-1] == {'title': "О как", 'category': "коты", 'likes': "1000000"}

# @pytest.mark.only
# @pytest.mark.(run_test_for_mac, reason='Автотест запускается только на макеб сейчас видовс')
# def test_add_nem_meme2():
#     collections = MemeCollection()
#     collections.add_meme("О как", "коты", "1000000")
#     assert collections.memes[-1] == {'title': "1О как", 'category': "коты", 'likes': "1000000"}


def test_2_positive():
    error_str = 'Error'
    assert error_str
    assert error_str == 'Error'

def test_3_negative():
    error_str = False
    assert False
