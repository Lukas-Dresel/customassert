from . import on_failure_callback_factory
from .asserter_node import *


_root_asserter = AsserterNode(None, on_failure_callback=on_failure_callback_factory.exception(AssertionError))


def get_asserter(asserter_name):
    if len(asserter_name) == 0:
        raise ValueError("The asserter name cannot be empty!")

    current_node = _root_asserter
    for child_name in asserter_name.split('.'):
        current_node = current_node.get_child(child_name)

    return current_node

