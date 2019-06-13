def exception_cb(exception_class):
    if not issubclass(exception_class, BaseException):
        raise ValueError(
                'exception_class must derive from BaseException but was {} of type {}'.format(
            exception_class, type(exception_class)
            )
        )

    def _raise(*args, **kwargs):
        raise exception_class(*args, **kwargs)

    return _raise


def builtin_assert_cb():
    def _assert(*args, **kwargs):
        assert False, "args: {}, kwargs: {}".format(args, kwargs)

    return _assert
