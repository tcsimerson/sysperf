# This script is production run process.  Assumes port 8080 is
# not in use by another HTTPD server.
VERSION=`cat VERSION.sar-perf`
echo "Stopping existing container"
podman container stop sar-perf
echo "Starting sar-perf container"
#podman run --rm -d -p 8080:5001/tcp \
podman run --rm -p 8080:5001/tcp \
	--net sysperf-net \
        --name sar-perf \
        -v $(mktemp -d):/run \
        -v /data01/sysperf/spw-uploads:/sar-perf/www/htdocs/uploads \
        -v /data01/sysperf/spw-logs:/sar-perf/logs \
	-h="sysperf-dev" \
        sar-perf:$VERSION
echo "Changing perms on uploads directory"
podman exec sar-perf /bin/chmod 777 /sar-perf/www/htdocs/uploads

