#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
# Displays only body of a 200 status code response
curl -sL "$1"
