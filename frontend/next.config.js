const withSass = require('@zeit/next-sass');
const withFonts = require('nextjs-fonts');
module.exports = withSass(withFonts({
        webpack(config, options) {
            return config;
        },
        env: {
            basePath: 'http://web:8000',
        },
        webpackDevMiddleware: config => {
    		config.watchOptions = {
      			poll: 1000,
      			aggregateTimeout: 300,
    		}
    		return config
  		},
    })
);
