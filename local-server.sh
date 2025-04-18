#!/bin/bash

# Set the local IP address to the variable ip
ip=$(ifconfig en0 | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}')

# Start hugo
hugo server -D --bind $ip --baseURL http://$ip