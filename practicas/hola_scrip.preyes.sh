#!/bin/bash 
FECHA="date"
CONFRED="$(ifconfig)"
MENSAJE="hola mundo! \n fecha: ${FECHA} \n configuracion Red: \n ${CONFRED}"
echo "${MENSAJE} > /home/holamundo_start.txt"