#!/bin/sh -e

DSTDIR=$(dirname $0)/keeley/static
#REGISTRY=
REGISTRY="http://registry.npm.taobao.org"

rm -rf "$DSTDIR/node_modules"

# generate a fake package.json (should we have a package.json?)
npm init --prefix="$DSTDIR" -y > "$DSTDIR/package.json"
sed -i "1,2d" "$DSTDIR/package.json"
sed -i 's/\"description": \"\"/\"description\": \"keely\"/g' "$DSTDIR/package.json"

# registry switch
if [ ! -z $REGISTRY ] ; then
    REGISTRY_ARG="--registry=$REGISTRY"
else
    REGISTRY_ARG=""
fi

# install packages
npm install --no-fund --no-save --only=production --prefix="$DSTDIR" $REGISTRY_ARG bufferutil
npm install --no-fund --no-save --only=production --prefix="$DSTDIR" $REGISTRY_ARG utf-8-validate
npm install --no-fund --no-save --only=production --prefix="$DSTDIR" $REGISTRY_ARG @syncfusion/ej2-filemanager

# remove temp files
rm -f "$DSTDIR/package.json"
rm -f "$DSTDIR/package-lock.json"




#yarn --cwd "$DSTDIR" --registry=http://registry.npm.taobao.org add @syncfusion/ej2-vue-filemanager
