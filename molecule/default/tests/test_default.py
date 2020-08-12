import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

solr_port = 8983
solr_core = 'catalog'
solr_home = '/var/solr'


def test_solr_service(host):
    solr = host.service('solr')

    assert solr.is_running
    assert solr.is_enabled


def test_solr_port(host):
    socket = host.socket('tcp://0.0.0.0:8983')

    assert socket.is_listening


def test_solr_schema(host):
    schema = host.file('%s/data/%s/conf/schema.xml' % (solr_home, solr_core))

    assert schema.exists


def test_solrconfig(host):
    config = host.file('%s/data/%s/conf/solrconfig.xml'
                       % (solr_home, solr_core))

    assert config.exists
    assert config.contains('<requestHandler name="/replication" '
                           + 'class="solr.ReplicationHandler">')


def test_solr_core(host):
    host.ansible(
        'uri',
        'url=http://localhost:%s/solr/%s/get' % (solr_port, solr_core),
        check=False
        )

# these tests only apply to catalog-next for the moment, so we
# override solr_core


def test_solr_stopwords_file(host):
    solr_core = 'catalog-next'
    stopwords_path = '%s/data/%s/conf/stopwords.txt' % (solr_home, solr_core)
    stopwords = host.file(stopwords_path)

    assert stopwords.exists


def test_solr_stopwords_in_schema(host):
    solr_core = 'catalog-next'
    schema_path = '%s/data/%s/conf/schema.xml' % (solr_home, solr_core)
    schema = host.file(schema_path)

    assert schema.exists
    assert schema.contains('<filter class="solr.StopFilterFactory"')
    assert schema.contains('<filter class="solr.SuggestStopFilterFactory"')
