#!/bin/sh
cd `dirname $0`
ROOT_PATH=`pwd`
java -Xms256M -Xmx1024M -cp .:$ROOT_PATH:$ROOT_PATH/../lib/routines.jar:$ROOT_PATH/../lib/dom4j-1.6.1.jar:$ROOT_PATH/../lib/jxl.jar:$ROOT_PATH/../lib/log4j-1.2.16.jar:$ROOT_PATH/../lib/mysql-connector-java-5.1.30-bin.jar:$ROOT_PATH/consulta_errores_0_1.jar: completo.consulta_errores_0_1.Consulta_Errores  --context=Default "$@" 