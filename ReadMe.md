lazily.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
[![PyPi Status](https://img.shields.io/pypi/v/lazily.py.svg)](https://pypi.python.org/pypi/lazily.py)
[![TravisCI Build Status](https://travis-ci.org/KOLANICH/lazily.py.svg?branch=master)](https://travis-ci.org/KOLANICH/lazily.py)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/lazily.py.svg)](https://coveralls.io/r/KOLANICH/lazily.py)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/lazily.py.svg)](https://libraries.io/github/KOLANICH/lazily.py)

Imports lazily. Supports hooks.

Useful when some long loading packages are optional to use by your app, so you don't want to spend time on loading them every time. The arguments are the same as in [```importlib.import_module```](https://docs.python.org/3/library/importlib.html#importlib.import_module).

Requirements
------------
* [```Python >=3.4```](https://www.python.org/downloads/). [```Python 2``` is dead, stop raping its corpse.](https://python3statement.org/) Use ```2to3``` with manual postprocessing to migrate incompatible code to ```3```. It shouldn't take so much time.

* [```lazy_object_proxy```](https://github.com/ionelmc/python-lazy-object-proxy) [![PyPi Status](https://img.shields.io/pypi/v/lazy-object-proxy.svg)](https://pypi.python.org/pypi/lazy-object-proxy)
[![TravisCI Build Status](https://travis-ci.org/ionelmc/python-lazy-object-proxy.svg?branch=master)](https://travis-ci.org/ionelmc/python-lazy-object-proxy)
[![Coveralls Coverage](https://img.shields.io/coveralls/ionelmc/python-lazy-object-proxy.svg)](https://coveralls.io/r/ionelmc/python-lazy-object-proxy.py)
[![Libraries.io Status](https://img.shields.io/librariesio/github/ionelmc/python-lazy-object-proxy.svg)](https://libraries.io/github/ionelmc/python-lazy-object-proxy) It hooks into cpython and can catch more kinds of actual using of the object than any pure python implementation.


```python
import freeLunch # ModuleNotFoundError: No module named 'freeLunch'
```

```python
from lazily import freeLunch

freeLunch.consume() # ModuleNotFoundError: No module named 'freeLunch'
```

There is a hooks mechanics, but it is a bit broken, don't use for now:

```python
import lazily
def bar():
	raise ImportError("There ain't no such thing as a free lunch.")
lazily.hooks["freeLunch"]=bar
freeLunch=lazily.lazily("freeLunch")

freeLunch.consume() # ImportError: There ain't no such thing as a free lunch.
```

Obviously, `*` in `fromlist` is UB, as it relies on `__all__`, so `_bootstrap.py` in CPython impl tries to read it.