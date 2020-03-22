# Ansible role pdns-recursor

[![Build Status](https://travis-ci.org/wftech/ansible-role-pdns-recursor.svg?branch=master)](https://travis-ci.org/wftech/ansible-role-pdns-recursor)

Ansible role to install PowerDNS recursor.

## Requirements

EPEL is required on CentOS.  

## Example Playbook
    
    - hosts: all
      roles:
       - role: wftech.pdns-recursor


Role Variables
--------------

See `defaults/main.yml`

License
-------

GNU General Public License Version 2

Author Information
------------------

Created by [Veros Kaplan][verosk] for [wf tech][wft] internal usage.

[verosk]: https://github.com/VerosK/
[wft]: https://wftech.cz/
