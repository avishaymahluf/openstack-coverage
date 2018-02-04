# Code Coverage InfraRed

InfraRed Plugin for code coverage for OSP

## Installation

1. Install infrared (https://github.com/redhat-openstack/infrared)

2. Install openstack-coverage infrared plugin:

       infrared plugin add https://github.com/avishaymahluf/openstack-coverage.git

## Usage

Install the coverage on nodes:

    infrared openstack-coverage --activate yes
    # install on a specific group of hosts
    infrared openstack-coverage --activate yes --hosts overcloud_nodes

Install the coverage to measure specific DFG:

    infrared openstack-coverage --activate yes --dfg network
    
Aggregate covereage and copy to the undercloud:

    infrared openstack-coverage --collect yes

Generate reports:

    infrared openstack-coverage --report yes
