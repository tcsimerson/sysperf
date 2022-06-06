#!/usr/bin/sh
#
# Takes a single command line argument to build that
# specific container image.

if [ $# -ne 1 ]
then
	echo "You must provide a single argument that specifies the image to build."
	echo "Valid images are sysperf-base, sar-perf, or flexperf."
	exit 1
fi
case $1 in
	'sysperf-base'|'sysperf'|'sysperf-web')
		IMAGE=$1
		;;
	*)
		echo "Invalid image name specified"
		exit 2
		;;
esac

echo "Removing previous $IMAGE images"
for i in `podman image ls | awk -v image=$IMAGE '{if(match($0,image)){print $2}}'`
do
	echo "	removing version $i"
	podman image rm $IMAGE > /dev/null 2>&1
done

echo
echo "Building new image, version $VERSION"
VERSION=`cat VERSION.$IMAGE`
cd $IMAGE
podman build -t $IMAGE:latest -t $IMAGE:$VERSION .

echo "Done!"
