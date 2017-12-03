http://adventofcode.com/2017/

Here are my solutions! They're not just good, they're good enough!

# Setup

I use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv). So should you!

```sh
$ git clone https://github.com/havocbane/adventofcode2017
$ cd adventofcode2017
$ pyenv virtualenv 3.6.3 adventofcode
$ pyenv local adventofcode
$ pip install -U pip setuptools wheel
$ pip install -r requirements.txt
```

# Tests

I like [TDD](https://en.wikipedia.org/wiki/Test-driven_development). Some, if not all, days have tests. Well, at least some [pytest](https://github.com/pytest-dev/pytest) ones and maybe some go tests if you're lucky.

```sh
$ py.test # run all tests from the root directory or some from individual day folders.
# and also generate a histogram!
$ py.test --benchmark-histogram=file_prefix
$ go test # You probably need to be in a day folder for this to work.
```

# Run Solutions

```sh
$ cd day#
$ python day#.py
# or maybe I didn't use *just* python?
$ go run day#.go
```

# Quick and Dirty Charting

In case you care to see how fast things might have ran.

```sh
# Macs are dumb. Use some version of python you don't already have I guess?
$ PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.5.4
$ pyenv shell 3.5.4
$ pip install matplotlib ipython
$ ipython
> import matplotlib.pyplot as plt
> # Day 1 times for example... I need more data points :-\
> plt.plot([3.4532e-6, 4.1070e-6, 4.3268e-6, 4.5038e-6, 5.3166e-6, 6.1023e-6, 6.1593e-6, 7.0242e-6, 7.8743e-6, 0.0015408992767333984, 0.00156402587890625])
> plt.ylabel('Time (seconds)')
> plt.show()
```
