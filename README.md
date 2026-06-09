# Учебный проект для группы QAP23

## Установка всех пакетов

Создайте `requirements.txt` в корне проекта или скачайте из этого репозитория:

```[.pre-commit-config.yaml](../qap21_python_project/.pre-commit-config.yaml)
pytest
selenium
webdriver-manager
```

Установите всё разом:

```bash
pip install -r requirements.txt
```

---


## Установка Git hooks

После установки зависимостей установите Git hooks:

```bash
pre-commit install
```

## Запуск первого теста

Запуск тестов:

```bash
pytest -q
```

## Запуск первого теста с разными ключами

**Базовые:**

```bash
pytest          # стандартный вывод
pytest -v       # подробные имена тестов
pytest -q       # тихий режим
pytest tests/test_pytest/test_intro.py -v -s --cache-clear --tb=short  # пример
```

Полезные флаги на практике
```bash
#-s — не захватывать stdout/stderr (удобно для дебага print)
#--lf — запустить только “упавшие” на прошлом прогоне
#--ff — сначала упавшие, потом остальные
#--durations=10 — показать 10 самых долгих тестов
```bash

**Отбор тестов:**

```bash
pytest tests/test_python_org_wait.py   # один файл
pytest tests -k search                 # по подстроке в имени
pytest -k "not e2e"                    # исключить
```

**Маркеры:**

```python
import pytest

@pytest.mark.e2e
def test_something():
    ...
```

Запуск по маркеру:

```bash
pytest -m e2e
```

**Поведение при падениях и отчёты:**

```bash
pytest -x            # стоп на первом фейле
pytest --maxfail=1   # то же
pytest -ra           # причины skip/xfail
pytest -s            # показать print()/stdout
```


```bash
allure serve .allure-results

allure generate .allure-results -o .allure-report --clean
allure open .allure-report
```
