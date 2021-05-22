SCENARIOS := \
  default \
  replication

SCENARIO_TARGETS := $(patsubst %,test-%, $(SCENARIOS))

setup:
	pipenv install --dev

test: $(SCENARIO_TARGETS)

test-%:
	pipenv run molecule test -s $*


.PHONY: setup test
