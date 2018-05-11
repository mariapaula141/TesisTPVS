#!/bin/sh
cd `dirname $0`
ROOT_PATH=`pwd`
java -Xms256M -Xmx1024M -cp .:$ROOT_PATH:$ROOT_PATH/../lib/routines.jar:$ROOT_PATH/../lib/advancedPersistentLookupLib-1.2.jar:$ROOT_PATH/../lib/commons-collections-3.2.2.jar:$ROOT_PATH/../lib/dom4j-1.6.1.jar:$ROOT_PATH/../lib/jboss-serialization.jar:$ROOT_PATH/../lib/log4j-1.2.15.jar:$ROOT_PATH/../lib/log4j-1.2.16.jar:$ROOT_PATH/../lib/mysql-connector-java-5.1.30-bin.jar:$ROOT_PATH/../lib/talend_file_enhanced_20070724.jar:$ROOT_PATH/../lib/talendcsv.jar:$ROOT_PATH/../lib/trove.jar:$ROOT_PATH/etl_spot_0_1.jar:$ROOT_PATH/create_dim_0_1.jar:$ROOT_PATH/create_fact_0_1.jar: completo.etl_spot_0_1.ETL_Spot  --context=Default "$@" 