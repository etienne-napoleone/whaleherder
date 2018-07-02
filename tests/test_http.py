import pytest
from whaleherder import main


@pytest.fixture
def app():
    main.app.testing = True
    return main.app.test_client()


@pytest.fixture
def wrong_app():
    main.app.testing = True
    main.docker._docker = main.docker.pydocker.DockerClient(
        base_url='unix://wrong/path')
    return main.app.test_client()


def test_ping(app):
    response = app.get('/ping')
    assert b'Connected to Docker' in response.data


def test_error_ping(wrong_app):
    with pytest.raises(Exception):
        app.get('/ping')
