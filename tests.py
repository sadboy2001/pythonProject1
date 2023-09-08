import pytest
from main import sum2, start_stop_rest_service, start_db


def test_sum2():
    assert sum2(15, 8) == 23

# import math
# from main import start_stop_rest_service, start_db
#
#
@pytest.mark.parametrize('a, b, result',
                         [
                             (1, 3, 4),
                             (-1, 1, 0),
                             (6, 7, 13),
                             (9, 8, 17),
                             (10, 11, 21),
                         ])
def test_one(a, b, result):
    assert a + b == result


@pytest.mark.parametrize('c, d, result_m',
                         [
                             (1, 3, 4),
                             (-1, 1, 0),
                             (6, 7, 13),
                             (9, 8, 17),
                         ])
def test_one(c, d, result_m):
    assert c * d == result_m
#
#
def test_two(start_stop_rest_service):
    print('This is test run')
