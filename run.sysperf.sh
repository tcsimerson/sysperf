# This script creates the private container network and then
# starts all the various containers.

# Setting global/configuration variables
WORKING_DIR="/data01/sysperf"
NODE_NAME=`hostname`

# Checking to see if need to run in debug mode
if [ "$1" = "debug" ]
then
	DEBUG=""
else
	DEBUG="-d"
fi

# Creating the private network
echo "Adding sysperf-net private container network"
podman network create sysperf-net

# Starting the sysperf container
VERSION=`cat VERSION.sysperf`
echo "Stopping sysperf container"
podman container stop sysperf
echo "Starting sysperf container"
podman run --rm $DEBUG \
	--net sysperf-net \
        --name sysperf \
        -v $WORKING_DIR/sysperf-data:/sysperf/data \
        sysperf:$VERSION

# Starting the sysperf-web container
echo "Starting sysperf-web container"
VERSION=`cat VERSION.sysperf-web`
echo "Stopping sysperf-web container"
podman container stop sysperf-web
echo "Starting sysperf-web container"
podman run --rm $DEBUG \
	-p 8080:5001/tcp \
        --net sysperf-net \
        --name sysperf-web \
        -v $WORKING_DIR/fcp-logs:/sysperf/fcp-logs \
        -v $WORKING_DIR/fcp-uploads:/sysperf/fcp-uploads \
        -v $WORKING_DIR/spw-logs:/sysperf/spw-logs \
        -v $WORKING_DIR/spw-uploads:/sysperf/spw-uploads \
	-h=$NODE_NAME \
        sysperf-web:$VERSION

# Due to permission issues, need to set directory wide open
echo "Changing perms on uploads directory"
podman exec sysperf-web /bin/chmod 777 /sysperf/fcp-uploads
podman exec sysperf-web /bin/chmod 777 /sysperf/spw-uploads

