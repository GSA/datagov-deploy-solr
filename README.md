[![CircleCI](https://circleci.com/gh/GSA/datagov-deploy-solr.svg?style=svg)](https://circleci.com/gh/GSA/datagov-deploy-solr)

# datagov-deploy-solr

This project is part of [datagov-deploy](https://github.com/GSA/datagov-deploy).

Ansible role to deploy solr.


## Usage

Include this role in your `requirements.yml`.

```yaml
- src: https://github.com/gsa/datagov-deploy-solr.git
```


### Variables



## Prerequisites for development

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/) 2.7 or 3.5+ in a virtualenv


## Development

Install dependencies.

    $ make setup

Run the tests.

    $ make test
