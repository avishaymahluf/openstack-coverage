---
plugin_type: test
subparsers:
    openstack-coverage:
        description: Collection of openstack coverage configuration tasks
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: General
              options:
                  aggregator:
                      type: Value
                      default: "undercloud-0"
                      help:  |
                          The host that will aggregate coverage data, generate report and publish to SonarQube.

            - title: Activate
              options:
                  activate:
                      type: Bool
                      default: no
                      help: Install the coverage
                  dfg:
                      type: Value
                      help: Openstack components packages of code to be measured
                      default: all
                  install-hosts:
                      type: Value
                      default: openstack_nodes
                      help: Group of hosts that coverage will be installed on
                  install-rhos-repos:
                      type: Bool
                      default: no
                      help: Install rhos repos during installation of coverage
                  rhos-release:
                      type: Value
                      help:  |
                          The RHOS release version.
                      required_when: "install-rhos-repos == True"

            - title: Collect
              options:
                  collect:
                      type: Bool
                      default: no
                      help: Aggregate covereage and copy to the undercloud by default

            - title: Report
              options:
                  report:
                      type: Bool
                      default: no
                      help: Generate reports

            - title: Publish to SonarQube
              options:
                  publish:
                      type: Bool
                      default: no
                      help: Publish to SonarQube
                  sonar-url:
                      type: Value
                      help: SonarQube host URL
                      required_when: "publish == True"
                  sonar-login:
                      type: Value
                      help: SonarQube login or API token
                      required_when: "publish == True"
                  sonar-password:
                      type: Value
                      help: SonarQube password
                  sonar-project:
                      type: Value
                      action: append
                      help: |
                          The project to publish coverage results.
                          More than one --sonar-project option can be provided.
                          Format: --sonar-project neturon --sonar-project neutron_lbaas
                      required_when: "publish == True"
