#!/usr/bin/env bash

clear

echo "------------------------------------------------------------------"
echo "LIST"
echo "------------------------------------------------------------------"
curl -i http://localhost:5000/api/v1/fits-files

echo "------------------------------------------------------------------"
echo "GET"
echo "------------------------------------------------------------------"
curl -i http://localhost:5000/api/v1/fits-files/a59d38bc2bfe0a71c54ce366233997b1

echo "------------------------------------------------------------------"
echo "GET NON EXISTENT"
echo "------------------------------------------------------------------"
curl -i http://localhost:5000/api/v1/fits-files/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
