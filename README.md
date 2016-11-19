customassert
====

customassert - customizable assertions for code in production, not only for debugging purposes

# What?

customassert is a module to allow users to write assertions that can be either turned off or customized to even be usable in production code where usual asserts might be either optimized out or frowned upon.
The way this is achieved is similar to the logging module in that you can access asserter instances by a name.

You can quickly get started by using 
```
import customassert
asserter = customassert.get_asserter(__name__)
asserter.set_on_failure_callback(customassert.on_failure_callback_factory.exception(ValueError))
asserter.assert_true(1 == 0, 'What were you thinking??')
"""

The `customassert.on_failure_callback_factory` has two builtin callbacks you can use,
`exception(exception_type_to_throw) or builtin_assert()`. 

- The `exception` callback will raise an instance of the passed in exception type on assertion failure. 
- The 'builtin_assert` callback will behave just like the normal python `assert` statement in that it will raise an `AssertionError` when the interpreter is in debug mode (`__debug__ == True`) and will not
raise an exception in case the python interpreter is in optimized mode (see `-O` flag of the python interpreter).