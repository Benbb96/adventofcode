from day1 import first, second


def test_01a(day01_numbers):
    assert first(day01_numbers) == 786811


def test_01b(day01_numbers):
    assert second(day01_numbers) == 199068980
