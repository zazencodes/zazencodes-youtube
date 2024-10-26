#!/bin/bash

# Display current time in various formats
echo "Current time in 24-hour format: $(date +'%H:%M:%S')"
echo "Current time in 12-hour format: $(date +'%I:%M:%S %p')"
echo "Current date and time: $(date +'%Y-%m-%d %H:%M:%S')"
echo "Current time in RFC 2822 format: $(date -R)"
echo "Current time in ISO 8601 format: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"

