#!/bin/sh -e

# we use a download>generate>delete process because the files npm downloaded are too large (133M) so
# that it is not good to commit them into a version control repository.

SRCDIR=$(dirname $0)/keeley/bundle-src
DSTDIR=$(dirname $0)/keeley/static
#REGISTRY=
REGISTRY="http://registry.npm.taobao.org"

rm -rf "$DSTDIR/node_modules"

# generate a fake package.json (should we have a package.json?)
#npm init --prefix="$DSTDIR" -y > "$DSTDIR/package.json"
#sed -i "1,2d" "$DSTDIR/package.json"
#sed -i 's/\"description": \"\"/\"description\": \"keely\"/g' "$DSTDIR/package.json"

# registry switch
if [ ! -z $REGISTRY ] ; then
	REGISTRY_ARG="--registry=$REGISTRY"
else
	REGISTRY_ARG=""
fi

# install packages
npm install --no-fund --save --only=production --prefix="$SRCDIR" $REGISTRY_ARG bufferutil utf-8-validate @syncfusion/ej2-filemanager
npm install --no-fund --save --only=production --prefix="$SRCDIR" $REGISTRY_ARG webpack webpack-cli css-loader style-loader

# bundle
cat <<-EOF > "$SRCDIR/webpack.config.js"
	module.exports = {
	  entry: './main.js',
	  output: {
	    filename: "$DSTDIR/bundle.js",
	  },
	}
	EOF
webpack --env production --env min --config "$SRCDIR/webpack.config.js"

# remove temp files
if [ "$1" != "--keep" ] ; then
#	rm -f "$DSTDIR/package.json"
#	rm -f "$DSTDIR/package-lock.json"
#	rm -f "$DSTDIR/webpack.config.js"
fi
