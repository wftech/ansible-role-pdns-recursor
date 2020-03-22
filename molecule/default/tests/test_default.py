import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_pdns_installed(host):
    pdns = host.package("pdns-recursor")
    assert pdns.is_installed


def test_pdns_running_and_enabled(host):
    pdns = host.service("pdns-recursor")
    assert pdns.is_running
    assert pdns.is_enabled
