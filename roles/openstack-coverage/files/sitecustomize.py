import os
import coverage

os.environ.setdefault('COVERAGE_PROCESS_START', "/coverage/.coveragerc")
coverage.process_startup()
