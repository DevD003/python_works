#.PHONY i.e  fake- doesnt create files based on the name when run  and tasks that are phony - with '.' are ignored
.PHONY: install test

#default specifies the first task to go to when Make is run:
default: test

#install develooper dependencies, skip- lock file i.e installed dependency details & updates
install:
	pipenv install --dev --skip-lock

#tests, env var is set to incl. src directory and pytest executable
test:
	PYTHONPATH=./src pytest
#pytest - an executable, a test runner and test framework for python
