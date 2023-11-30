#!/bin/bash

docker build -t im-nginx-lb Dockerfile .

mkdir -p shared1
mkdir -p shared2

echo "<h1>Hello1</h1>" > /shared1/index.html
echo "<h1>Hello2</h1>" > /shared2/index.html

docker run -d -p 81:80 --name nginx1 im-nginx-lb
dicker run -d -p 82:80 --name nginx2 im-nginx-lb
