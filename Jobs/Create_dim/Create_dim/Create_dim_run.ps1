$fileDir = Split-Path -Parent $MyInvocation.MyCommand.Path
cd $fileDir
java '-Xms256M' '-Xmx1024M' -cp '.;../lib/routines.jar;../lib/advancedPersistentLookupLib-1.2.jar;../lib/commons-collections-3.2.2.jar;../lib/dom4j-1.6.1.jar;../lib/jboss-serialization.jar;../lib/jersey-client-1.4.jar;../lib/jersey-core-1.4.jar;../lib/log4j-1.2.15.jar;../lib/log4j-1.2.16.jar;../lib/mysql-connector-java-5.1.30-bin.jar;../lib/talendcsv.jar;../lib/trove.jar;create_dim_0_1.jar;' completo.create_dim_0_1.Create_dim  --context=Default %* 