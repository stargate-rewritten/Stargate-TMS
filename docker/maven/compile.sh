#!/bin/sh
cd /GitHub/ColorBukkit
git pull origin
mvn clean install -DskipTests

cd /GitHub/Stargate-Bukkit
git pull origin
mvn clean install -DskipTests
cp /GitHub/Stargate-Bukkit/target/Stargate-*.jar /plugins

cd /GitHub/Stargate-Mechanics
git pull origin
bash gradlew clean install
cp /GitHub/Stargate-Mechanics/build/libs/StargateMechanics-*.jar /plugins

cd /GitHub/Stargate-Mapper
git pull origin
mvn clean install -DskipTests
cp /GitHub/Stargate-Mapper/target/StargateMapper-*.jar /plugins

cd /GitHub/Stargate-Customizations
git pull origin
mvn clean install -DskipTests
cp /GitHub/Stargate-Customizations/target/StargateCustomizations-*.jar /plugins

cd /GitHub/Stargate-Interfaces
git pull origin
mvn clean install -DskipTests
cp /GitHub/Stargate-Interfaces/target/StargateInterfaces-*.jar /plugins