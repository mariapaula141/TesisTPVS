%~d0
cd %~dp0
java -Xms256M -Xmx1024M -cp .;../lib/routines.jar;../lib/dom4j-1.6.1.jar;../lib/jersey-client-1.4.jar;../lib/jersey-core-1.4.jar;../lib/log4j-1.2.16.jar;../lib/mariadb-java-client-2.2.1.jar;../lib/mysql-connector-java-5.1.30-bin.jar;../lib/talend_file_enhanced_20070724.jar;../lib/talendcsv.jar;etl_fut_0_1.jar; completo.etl_fut_0_1.ETL_Fut  --context=Default %* 