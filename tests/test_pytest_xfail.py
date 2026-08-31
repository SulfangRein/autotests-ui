import pytest


@pytest.mark.xfail(reason="Найден баг, из-за которого тест падает")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг исправлен, но на тесте все ещё висит маркировка")
def test_without_bug():
    pass
