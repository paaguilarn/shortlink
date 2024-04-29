from unittest import mock
from uuid import uuid4

from events.base import post_event, subscribe, subscribers


def do_nothing(*args, **kwargs):
    pass


def test_subscribe_new_event():
    event_type = str(uuid4())
    subscribe(event_type=event_type, fn=do_nothing)

    assert event_type in subscribers

    assert callable(subscribers[event_type][-1])

    assert subscribers[event_type][-1].__name__ == "do_nothing"


def test_post_known_event():
    event_type = str(uuid4())
    with mock.patch('tests.events.test_base.do_nothing') as mock_do_nothing:
        subscribe(event_type=event_type, fn=do_nothing)
        post_event(event_type=event_type, data="dummy")
        mock_do_nothing.assert_called()

