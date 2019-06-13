customassert
====

customassert - customizable assertions for code in production, not only for 
debugging purposes

# What?

customassert is a module to allow you to write assertions that can be 
either turned off or customized to be more usable in production code where 
usual asserts might be either optimized out or frowned upon. The way this is 
achieved is similar to the logging module in that you can access asserter 
instances by name.

You can quickly get started by using 
```
from customassert import get_asserter
from customassert.callbacks import exception_cb
asserter = get_asserter(__name__)
asserter.set_on_failure_callback(exception_cb(ValueError))
asserter.assert_true(1 == 0, 'What were you thinking??')
```

The `callbacks` module currently has two builtin callbacks you 
can use, `exception_cb(exception_type_to_throw)` and `builtin_assert_cb()`. 

- `exception_cb` will raise an instance of the passed in exception type on 
assertion failure. 
- `builtin_assert_cb` will behave just like the normal python `assert` 
statement in that it will raise an `AssertionError` when the interpreter is in
debug mode (`__debug__ == True`) and will not raise an exception in case the 
python interpreter is in optimized mode (see the `-O` flag of the python 
interpreter).
