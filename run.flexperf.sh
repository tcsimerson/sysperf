# This script is production run process.  Assumes port 80 is
# not in use by another HTTPD server.
VERSION=`cat VERSION.flexperf`
echo "Stopping existing container"
podman container stop flexperf
echo "Removing all stopped containers"
podman container prune -f
echo "Starting flexperf container"
podman run -d -p 8088:5000/tcp \
        --name flexperf \
        -v $(mktemp -d):/run \
        -v /data01/sysperf/fcp-uploads:/flexperf/www/htdocs/uploads \
        -v /data01/sysperf/fcp-logs:/flexperf/logs \
        flexperf:$VERSION
echo "Changing perms on uploads directory"
podman exec flexperf /bin/chmod 777 /flexperf/www/htdocs/uploads

