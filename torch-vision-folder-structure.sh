#!/bin/bash

mkdir data
cd data/
read -p "class qtd: " qtd
echo "folder that will be created, $qtd"

for i in $(seq 1 $qtd); do
    read -p "names of class $i: " name_class
    mkdir "$name_class"
    echo "folder $name_class created."
done
