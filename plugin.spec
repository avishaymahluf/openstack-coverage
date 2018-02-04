---
plugin_type: test
subparsers:
    openstack-coverage:
        description: Collection of openstack coverage configuration tasks
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Activate
              options:
                  activate:
                      type: Bool
                      default: no
                      help: Install the coverage
                  hosts:
                      type: Value
                      default: openstack_nodes
                      help: Group of hosts that coverage will be installed on
                  dfg:
                      type: Value
                      help: Openstack components packages of code to be measured
                      default: all

            - title: Collect
              options:
                  collect:
                      type: Bool
                      default: no
                      help: Aggregate covereage and copy to the undercloud

            - title: Report
              options:
                  report:
                      type: Bool
                      default: no
                      help: Generate reports
