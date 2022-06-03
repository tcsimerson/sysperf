# This script is production run process.  Assumes port 8080 is
# not in use by another HTTPD server.
VERSION=`cat VERSION.sysperf`
echo "Stopping existing container"
podman container stop sysperf
echo "Starting sysperf container"
podman run --rm -d \
	--net sysperf-net \
        --name sysperf \
	-e NODE_NAME="sysperf-dev" \
        sysperf:$VERSION

