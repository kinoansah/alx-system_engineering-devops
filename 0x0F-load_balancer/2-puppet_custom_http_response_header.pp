#!/usr/bin/env bash
# Define a class to configure the custom HTTP header
class custom_http_response_header {
  file { '/etc/nginx/conf.d/custom_response_header.conf':
    ensure  => 'file',
    content => "add_header X-Served-By $hostname;\n",
    notify  => Service['nginx'],
  }
}

# Include the Nginx class to ensure Nginx is installed and running
include nginx

# Include the custom_http_response_header class to configure the custom header
include custom_http_response_header
