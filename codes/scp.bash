#!/bin/bash
# run with bash scp.bash

# Definir el usuario y la dirección IP del servidor remoto
usuario=ro
direccion_ip=150.244.221.199

# Definir el directorio de origen en el servidor remoto
directorio_origen2=/home/ro/MG5_aMC_v2_9_9/pptox1n2j_nmssm/
directorio_origen3=/home/ro/MG5_aMC_v2_9_9/pptox1n3j_nmssm/

# Definir el directorio de destino en la máquina local
directorio_destino2=/home/martinrios/martin/trabajos/MLLHC/data/BP8/pptox1n2j_nmssm/
directorio_destino3=/home/martinrios/martin/trabajos/MLLHC/data/BP8/pptox1n3j_nmssm/

# Establecer la conexión maestra SSH
ssh -o ControlMaster=yes -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip -Nf $usuario@$direccion_ip

# Bucle para transferir archivos del servidor remoto a la máquina local
for ((linea=1; linea<=4; linea++)); do
    archivo_origen="BP8_"$linea"_run100k_1.lhco"
    scp -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip $usuario@$direccion_ip:$directorio_origen2$archivo_origen $directorio_destino2
    scp -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip $usuario@$direccion_ip:$directorio_origen3$archivo_origen $directorio_destino3
done

# Cerrar la conexión maestra SSH después de la transferencia de archivos
ssh -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip -O exit $usuario@$direccion_ip

