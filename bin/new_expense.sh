#!/usr/bin/bash


TOKEN=12345678
BASE_URL=http://localhost:8081

curl --data "token=$TOKEN&amount=$1&note=$2" http://localhost:8091/api/expense/
