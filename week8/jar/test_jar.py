import pytest
from jar import Jar


def test_init():
    """检查是否成功实例化了一个 Jar 对象"""
    jar1 = Jar(10)
    assert jar1.capacity == 10
    assert jar1.size == 0

    jar2 = Jar(20, 5)
    assert jar2.capacity == 20
    assert jar2.size == 5


def test_deposit():
    """测试 deposit() 方法是否正确"""
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3

    # 检查罐子已满的情况
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    """测试 withdraw() 方法是否正确"""
    jar = Jar(10, 5)
    jar.withdraw(3)
    assert jar.size == 2

    # 检查取出超过罐子中现有 cookie 数量的情况
    with pytest.raises(ValueError):
        jar.withdraw(5)


def test_str():
    """测试 __str__() 方法是否正确"""
    jar = Jar(10, 5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar2 = Jar(10)
    assert str(jar2) == ""
