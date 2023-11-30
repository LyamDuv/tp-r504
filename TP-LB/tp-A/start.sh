#!/bin/bash

docker build -t im-nginx-lb -f Dockerfile .

mkdir -p shared1
mkdir -p shared2

echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

docker run -d \
	--name nginx1 -p 81:80 -v "$(pwd)/shared1:/usr/share/nginx/html" nginx
docker run -d \
	--name nginx2 -p 82:80 -v "$(pwd)/shared2:/usr/share/nginx/html" nginx

docker run -d -p 83:80 im-nginx-lb

hello1=0
hello2=0

for ((i = 1; i <= 500; i++)); 
do
    b="<h1>Hello 1</h1>"
    c="<h1>Hello 2</h1>"
    a=$(curl -s http://localhost:83/)  # Utilisation de $(...) pour capturer la sortie de la commande curl

    if [ "$a" == "$b" ]; then
        ((hello1++))
    fi

    if [ "$a" == "$c" ]; then
        ((hello2++))
    fi
done

echo "Nombre de pages avec hello 1 : $hello1"
echo "Nombre de pages avec hello 2 : $hello2"
