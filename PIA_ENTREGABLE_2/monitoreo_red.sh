#!/bin/bash
function ERROR(){
        echo "ERROR EN LA LINEA $1"
        exit 1
}

function traffic_network(){
        Interface="eth0"
        if ! ip link show "$Interface"> /dev/null 2>&1; then
                echo "$Interface NO EXISTE"
                exit 1
        fi
        sudo iftop -i "$Interface" || ERROR $LINENO
}
traffic_network
