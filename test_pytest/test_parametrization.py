import pytest

from mems import MemeCollection
from test_data import memes


@pytest.fixture
def empty_collection():
    return MemeCollection()


@pytest.fixture
def memes_collection():
    collection = MemeCollection()
    collection.add_meme('Сидим с бобром за столом', 'песня', 100)
    collection.add_meme('Ты адекватная? А ниче тот факт, что…', 'видео', 601)
    collection.add_meme('Лабубу', 'игра', 7)
    collection.add_meme('Эффект Долиной', 'ситуация', 5001)
    collection.add_meme('6-7', 'ситуация', 31)
    return memes_collection


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

@pytest.mark.param
@pytest.mark.parametrize('title, category, likes, expected_result', memes)
def test_validate_data(title, category, likes, expected_result):
    collection = MemeCollection()
    result = collection.add_meme(title, category, likes)

    assert result == expected_result
