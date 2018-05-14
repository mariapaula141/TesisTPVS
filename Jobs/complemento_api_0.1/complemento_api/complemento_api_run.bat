%~d0
cd %~dp0
java -Xms256M -Xmx1024M -cp .;../lib/routines.jar;../lib/advancedPersistentLookupLib-1.2.jar;../lib/commons-collections-3.2.2.jar;../lib/dom4j-1.6.1.jar;../lib/jboss-serialization.jar;../lib/log4j-1.2.15.jar;../lib/log4j-1.2.16.jar;../lib/mysql-connector-java-5.1.30-bin.jar;../lib/trove.jar;complemento_api_0_1.jar; completo.complemento_api_0_1.complemento_api  --context=Default %* 