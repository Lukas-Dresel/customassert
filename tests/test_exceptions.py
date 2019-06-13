import sys

import customassert
from customassert import get_asserter
from customassert.callbacks import exception_cb, builtin_assert_cb


class TestFailureException(Exception):
    def __init__(self, cause_exception, cause_exc_info, *args, **kwargs):
        super(TestFailureException, self).__init__(*args, **kwargs)

        self.exception = cause_exception
        self.info = cause_exc_info


class ExpectedExceptionNotThrownError(TestFailureException):
    pass


class UnexpectedExceptionThrownError(TestFailureException):
    pass


class expects_exception(object):
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            try:
                f(*args, **kwargs)
                raise ExpectedExceptionNotThrownError(None, None, 
                        'Test failed. [{}] did not throw expected '
                        'exception [{}]'.format(f, self.expected_exception))
            except BaseException as ex:
                if type(ex) != self.expected_exception:
                    raise UnexpectedExceptionThrownError(ex, sys.exc_info(),
                        'Test failed. [{}] threw exception [{}] of type [{}], '
                        'expected was [{}]'.format(f, ex, type(ex),
                            self.expected_exception),
                        )
                else:
                    print('Test succeeded.')
                    return True

        return wrapped




@expects_exception(ValueError)
def test_case_value_error():
    functionNameAsString = sys._getframe().f_code.co_name
    print(functionNameAsString)
    asserter = get_asserter("{}.{}".format(__name__, functionNameAsString))
    asserter.set_on_failure_callback(exception_cb(ValueError))
    # This should now raise a ValueError
    asserter.assert_true(False)
    return None # Uninteresting, should not be reached


@expects_exception(AssertionError)
def test_case_assertion_error():
    functionNameAsString = sys._getframe().f_code.co_name
    print(functionNameAsString)
    asserter = get_asserter("{}.{}".format(__name__, functionNameAsString))
    asserter.set_on_failure_callback(exception_cb(AssertionError))
    # This should now raise a AssertionError
    asserter.assert_true(False)
    return None # Uninteresting, should not be reached


@expects_exception(AssertionError)
def test_case_debug_builtin_assert():
    functionNameAsString = sys._getframe().f_code.co_name
    print(functionNameAsString)
    asserter = get_asserter("{}.{}".format(__name__, functionNameAsString))
    asserter.set_on_failure_callback(builtin_assert_cb())
    asserter.assert_true(False)
    return None # Uninteresting, should not be reached


def test_case_optimized_builtin_assert():
    functionNameAsString = sys._getframe().f_code.co_name
    print(functionNameAsString)
    asserter = get_asserter("{}.{}".format(__name__, functionNameAsString))
    asserter.set_on_failure_callback(builtin_assert_cb())
    asserter.assert_true(False)
    # In this case, the assertion should have been optimized out, we expect to reach here
    # This is to match the behavior of the builtin assert statement
    return None

if __name__ == '__main__':
    test_case_value_error()
    test_case_assertion_error()
    if __debug__:
        test_case_debug_builtin_assert()
    else:
        test_case_optimized_builtin_assert()
