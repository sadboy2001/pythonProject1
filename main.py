import pytest

def sum2(x, y):
    return x + y




#
#
@pytest.fixture(scope='session')
def start_stop_rest_service(start_db):
    print('Start Rest service')
    yield #тесты
    print('Stop Rest service')


@pytest.fixture(scope='session')
def start_db():
    print('Start DB')
    yield #пауза
    print('Stop DB')

