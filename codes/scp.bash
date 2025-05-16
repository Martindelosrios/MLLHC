#!/bin/bash
# run with bash scp.bash

# Definir el usuario y la dirección IP del servidor remoto
usuario=ro
direccion_ip=150.244.221.199

# Definir el directorio de origen en el servidor remoto
#directorio_origen=/home/ro/MG5_aMC_v2_9_9/pptox1n2j_nmssm/
directorio_origen=/home/ro/MG5_aMC_v2_9_9/pptox1n3j_nmssm/

# Definir el directorio de destino en la máquina local
#directorio_destino=/home/martinrios/martin/trabajos/MLLHC/data/BP1_1/pptox1n2j_nmssm/
directorio_destino=/home/martinrios/martin/trabajos/MLLHC/data/BP1_1/pptox1n3j_nmssm/

# Establecer la conexión maestra SSH
ssh -o ControlMaster=yes -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip -Nf $usuario@$direccion_ip

# Bucle para transferir archivos del servidor remoto a la máquina local
for ((linea=1; linea<=10; linea++)); do
    archivo_origen="BP1_1_run100k_$linea.lhco"
    scp -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip $usuario@$direccion_ip:$directorio_origen$archivo_origen $directorio_destino
done

# Cerrar la conexión maestra SSH después de la transferencia de archivos
ssh -o ControlPath=/tmp/ssh-control-$usuario@$direccion_ip -O exit $usuario@$direccion_ip

