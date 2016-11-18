import re
from collections import defaultdict

_ASSERTER_CHILD_NAME_REGEX = '[a-zA-Z0-9_]+'


class AsserterNode(object):
    def __init__(self, parent, on_failure_callback=None):
        if not parent is None or isinstance(parent, AsserterNode):
            raise ValueError('Invalid parent {} of type {}'.format(parent, type(parent)))

        self._parent = parent
        self._children = defaultdict(lambda: AsserterNode(self))
        self._on_failure = on_failure_callback

    def on_failure(self, *args, **kwargs):
        if self._on_failure is not None:
            self._on_failure(*args, **kwargs)
        return self._parent.on_failure(*args, **kwargs)

    def assert_true(self, condition, *args, **kwargs):
        if condition:
            return True

        self.on_failure(*args, **kwargs)

    def set_on_failure_callback(self, callback):
        if not callback is None and not hasattr(callback, '__call__'):
            raise ValueError('The callback {} of type {} is not callable'.format(callback, type(callback)))

        self._on_failure = callback

    def get_child(self, name):
        if not isinstance(name, str) or not re.fullmatch(_ASSERTER_CHILD_NAME_REGEX, name):
            return ValueError('Invalid asserter child name {} of type {}'.format(name, type(name)))

        return self._children[name]