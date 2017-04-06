.PHONY: build release test clean

build:
	python setup.py sdist bdist_wheel

release:
	python setup.py sdist bdist_wheel upload

test:
	rm -rf build
	py.test --cov=ratecounter
	coverage html

clean:
	rm -rf build/*
	find . -name __pycache__ | xargs rm -rf
