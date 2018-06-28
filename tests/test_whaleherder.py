# -*- coding: utf-8 -*-
"""
    Whaleherder Tests
    ~~~~~~~~~~~~
    Tests Whaleherder.
    :copyright: 2018 Etienne Napoleone
    :license: BSD, see LICENSE for more details.
"""

import pytest
from whaleherder import main


@pytest.fixture
def app():
    main.app.testing = True
    return main.app.test_client()

def test_ping(app):
    rv = app.get('/ping')
    assert b'Connected to Docker' in rv.data
