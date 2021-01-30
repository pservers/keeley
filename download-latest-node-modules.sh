#!/bin/sh -e
DSTDIR=$(dirname $0)/keeley/static

rm -rf "$DSTDIR/node_modules"

#npm install --only=production --prefix="$DSTDIR" @syncfusion/ej2-filemanager
npm install --only=production --prefix="$DSTDIR" --registry="http://registry.npm.taobao.org" @syncfusion/ej2-filemanager
#cnpm install --only=production --prefix="$DSTDIR" "@syncfusion/ej2-filemanager"
#yarn --cwd "$DSTDIR" --registry=http://registry.npm.taobao.org add @syncfusion/ej2-vue-filemanager
