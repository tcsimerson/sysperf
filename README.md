# sysperf
System performance tool for NetBackup infrastructure.

### General description

This is a merging of the flexperf tool (used for Flex appliance consolidation analysis) and sar-perf (general system performance tool) into a common code base.

### Containers and images

Container solution that involves several images and 3 running containers.  The containers utilize a private network that hides the sysperf container from the outside world.

- Images used
  - sysperf-base:  based upon the Alpine 3.16.0 Linux variant with the following additional packages and Python modules added:
    - Linux packages
      - python3
      - py3-pip
    - Python modules
      - openpyxl
      - flask
      - requests
  - sysperf:  core for the API engine
  - flexperf:  web interface for FCP that will make API calls to sysperf to process the data but this container will generate the consolidation Excel workbook.
  - sar-perf:  web interface for sar-perf that will make API calls to sysperf to process the data but this container will actually generate the Excel workbook.
- Containers
  - sysperf
  - flexperf
  - sar-perf



### Starting and stopping sysperf containers

TBD:  build a script that builds the private network along with staring all the containers.  Will also need a script to stop all containers and delete the private network.  In the meantime, here's the command to build the private network:

`podman network create sysperf-net`

Be sure to include `--net sysperf-net` to the container run command.
