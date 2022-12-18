#!/usr/bin/bash


TOKEN=1234567
BASE_URL=http://localhost:8081

curl --data "toke=$TOKEN&amout=$1&note=$2" http://localhost:8091/api/expense/
