.PHONY: setup test

setup:
	pip install -r requirements.txt
	ansible-galaxy install -r requirements.yml

test:
	molecule test
