/** @type {import('next').NextConfig} */
const nextConfig = {
	experimental: {
	  appDir: true
	},
	async rewrites() {
	  return [
		{
		  source: '/api/:path*',
		  destination: `${process.env.BACKEND_URL}/api/:path*` // Proxy to Backend
		}
	  ];
	}
  };
  
  module.exports = nextConfig;
  