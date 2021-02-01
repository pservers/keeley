#!/bin/sh -e

# we use a download>generate>delete process because the files npm downloaded are too large (133M) so
# that it is not good to commit them into a version control repository.

SRCDIR=$(dirname $0)/keeley/bundle-src
DSTDIR=$(dirname $0)/keeley/static

#REGISTRY=
REGISTRY="http://registry.npm.taobao.org"

# registry switch
if [ ! -z $REGISTRY ] ; then
	REGISTRY_ARG="--registry=$REGISTRY"
else
	REGISTRY_ARG=""
fi

# install packages
rm -rf "$SRCDIR/node_modules"
npm install --no-fund --no-save --prefix="$SRCDIR" $REGISTRY_ARG

# bundle
webpack --env production --env min --config "$SRCDIR/webpack.config.js"

# remove temp files
if [ "$1" != "--keep" ] ; then
#	rm -f "$DSTDIR/package-lock.json"
#	rm -f "$DSTDIR/webpack.config.js"
fi
