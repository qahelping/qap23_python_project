# import re
# from datetime import datetime, timedelta
#
# import pytest
#
# # Создать фикстуру которая будет генерирует timestamp
# # Создать автотесты которые будут проверять что функция `format_timestamp` правильно форматирует данные
# # пример
# # '2024-01-01 15:00:00'
# # '01.01.2024 15:00'
# # '15:00:00'
# # '2024-01-01'
# # * проверять не на совпадение строки, а по regexp
#
# patterns = {
#     "standard": r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$",
#     "short": r"^\d{2}\.\d{2}\.\d{4} - \d{2}:\d{2}$",
#     "time_only": r"^\d{2}:\d{2}:\d{2}$",
#     "date_only": r"^\d{4}-\d{2}-\d{2}$",
# }
#
#
# @pytest.fixture
# def get_data():
#     base_dt = datetime.now()
#     base_ts_ms = int(base_dt.timestamp() * 1000)
#     return base_ts_ms
#
#
# def format_timestamp(timestamp_ms, format_type="standard", offset_hours=0):
#     timestamp_seconds = timestamp_ms / 1000
#     dt = datetime.fromtimestamp(timestamp_seconds)
#     corrected_dt = dt + timedelta(hours=offset_hours)
#     formats = {
#         "standard": "%Y-%m-%d %H:%M:%S",
#         "short": "%d.%m.%Y - %H:%M",
#         "time_only": "%H:%M:%S",
#         "date_only": "%Y-%m-%d",
#     }
#
#     return corrected_dt.strftime(formats.get(format_type))
#
#
# @pytest.mark.parametrize("type_of_format", ["standard", "short", "time_only", "date_only"])
# def test_format_timestamp(get_data, type_of_format):
#     result = format_timestamp(get_data, type_of_format)
#     assert re.match(patterns[type_of_format], result)
