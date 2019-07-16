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
                  containers:
                      type: Bool
                      default: no
                      help: Openstack services are in containers
                  openstack-version:
                      type: Value
                      required: true
                      help:  |
                          The Openstack version.
                  discover-puddle:
                      type: Bool
                      default: no
                      help: Run discover puddle and fetch the info into file

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

                  registry-mirror:
                      type: Value
                      help: The alternative docker registry to use for deployment.

                  registry-namespace:
                      type: Value
                      help: The alternative docker registry namespace to use for deployment.

                  registry-prefix:
                      type: Value
                      help: The images prefix

                  registry-tag:
                      type: Value
                      help: The images tag


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

            - title: Storage
              options:
                  storage-activate:
                      type: Bool
                      default: no
                      help: Send collected raw data coverage results to storage
                  storage-hostname:
                      type: Value
                      help: Storage hostname to which collected raw data coverage results should be sent
                  storage-log-dir:
                      type: Value
                      help: Storage logs directory in which collected raw data coverage results should be stored
                  storage-user:
                      type: Value
                      default: rhos-ci
                      help: Storage server username
                  storage-key:
                      type: Value
                      help: Storage server key

            - title: Jenkins Job Metadata
              options:
                  jenkins-job-name:
                      type: Value
                      help: Jenkins Job name
                      required_when: "storage == True"
                  jenkins-build-id:
                      type: Value
                      help: Jenkins build ID
                      required_when: "storage == True"

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
