def test_user_login():
    print("Hello!")


class TestUserLogin:
    # def __init__(self): конструктора не должно быть в тестовом классе пайтеста
    #     ...
    def test_1(self):
        ...
    def test_2(self):
        ...

def test_assert_positive_case():
    assert 2 + 2 == 4


def test_assert_negative_case():
    four = 2 + 2
    assert four == 5