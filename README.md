# OpenStack Code Coverage

Ansible roles for measuring coverage on the openstack python components 
while deployment and execution of tests.

This repository contains 4 roles for installing, aggregating data, generating reports and publishing to SonarQube:

* Activate - Installs and configures coverage tool and dependencies.
* Collect - Aggregates coverage and copy to the undercloud by default
* Report - Generates coverage html and xml reports
* Publish - Use SonarQube API to push the xml results to a specific project

## Requirements

* An ansible inventory file containing reachable undercloud and overcloud nodes
* Nodes in the inventory file are placed in groups based on their roles

## Roles Variables

### Activate

OpenStack components packages of code to be measured (only one can be specified):

    # measure a specific dfg
    dfg: "network"
    # measure all
    dfg: "all"

Whether to install rhos repos during installation of coverage:

    install_rhos_repos: true

The RHOS release version (This is only needed when the install_rhos_repos is True, to indicate which version of rhos repos to install):

    rhos_release: 12

### Collect

The host that will aggregate coverage data, generate report and publish to SonarQube:

    aggregator: "undercloud-0"

### Report

This role does not require vars.

Please note that this role should run on the same host used as aggregator on collect role.

### Publish

Please note that this role should run on the same host used as aggregator on collect role.

SonarQube host URL:

    sonar_url: http://sonarqubeurl.example.com

SonarQube login or API token:

    sonar_login: "login_or_apitoken"

SonarQube password:

    sonar_password: "password"

The project to publish coverage results:

    sonar_project: "neutron"

## Playbook Usage

### Install Coverage

    - name: Install covarage
      hosts: openstack_nodes
      become: true
      tasks:
        - name: Install coverage
          include_role:
            name: activate
          vars:
            dfg: "network"
            install_rhos_repos: false

### Collect

    - name: Collect coverage data from all nodes
      hosts: openstack_nodes
      gather_facts: no
      become: true
      tasks:
        - name: Collect coverage data from all nodes
          include_role:
            name: collect
          vars:
            aggregator: "undercloud-0"

### Report

    - name: Generate coverage report
      hosts: "undercloud-0"
      gather_facts: no
      become: true
      tasks:
        - name: Generate coverage report
          include_role:
            name: report

### Publish

In order to use this role, the version-discovery should be downloaded and copied from InfraRed
to the roles directory before executing the playbook:
https://github.com/redhat-openstack/infrared/tree/master/infrared/common/roles/version-discovery

The inclusion of version-discovery can be skipped by specifying the "overcloud_version" variable.

    - name: Publish to SonarQube
      hosts: "undercloud-0"
      gather_facts: no
      become: true
      tasks:
        - name: Publish to SonarQube
          include_role:
            name: publish
          vars:
            sonar_url: "http://sonarqubeurl.example.com"
            sonar_login: "login_or_apitoken"
            sonar_project: "neutron"
            overcloud_version: 12  # when this var is specified the version-discovery is skipped

## Infrared Usage

### Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)

2. Install openstack-coverage infrared plugin:

       infrared plugin add https://github.com/rhos-infra/openstack-coverage.git

### Usage examples

Install the coverage on nodes:

    infrared openstack-coverage --activate yes
    # install on a specific group of hosts
    infrared openstack-coverage --activate yes --hosts overcloud_nodes

Install the coverage to measure specific DFG:

    infrared openstack-coverage --activate yes --dfg network

Aggregate coverage and copy to the undercloud:

    infrared openstack-coverage --collect yes

Generate reports:

    infrared openstack-coverage --report yes

Publish results to SonarQube:

    infrared openstack-coverage --publish yes \
    --sonar-url <SONAR_URL>
    --sonar-login <API_TOKEN>
    --sonar-project <PROJECT>
