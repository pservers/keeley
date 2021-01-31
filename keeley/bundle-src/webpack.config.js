const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const FaviconsWebpackPlugin = require('favicons-webpack-plugin')

module.exports = {
    entry: 'main.js',
    output: {
        filename: "index-bundle.js",
        path: path.resolve(__dirname, 'static'),
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: 'index.html.tmpl',
            filename: 'index.html',
        }),
        new FaviconsWebpackPlugin({
            logo: 'favicon.png',
        }),
    ],
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource',
            },
        ],
    },
}