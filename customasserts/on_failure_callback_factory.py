def exception(exception_class):
    if not isinstance(exception_class, Exception):
        raise ValueError('exception_class must derive from Exception but was {} of type {}'.format(exception_class, type(exception_class)))

    def _raise(*args, **kwargs):
        raise exception_class(*args, **kwargs)

    return _raise


def builtin_assert():
    def _assert(*args, **kwargs):
        assert False, "args: {}, kwargs: {}".format(args, kwargs)

    return _assert
