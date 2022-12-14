# Pytest and Code coverage experiments

```
pytest --cov
pytest --cov --cov-report=html
pytest --cov --cov-fail-under 85 && echo "ok"
```

- https://pythonbytes.fm/episodes/show/257/python-launcher-launching-python-everywhere
- https://nedbatchelder.com/blog/202111/coverage_goals.html
- https://stackoverflow.com/questions/59420123/is-there-a-standard-way-to-fail-pytest-if-test-coverage-falls-under-x
- https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260

## Pre-commit

`pre-commit install`

https://pre-commit.com/#3-install-the-git-hook-scripts

## Features

- block requests network access for tests
- check test coverage on pre-commit
- only run specified tests on linux
- use test parameters to check many different inputs in one test