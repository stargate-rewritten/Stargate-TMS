#!/bin/sh
mkdir GitHub
cd GitHub
git clone "https://github.com/stargate-rewritten/Stargate-Bukkit"
git clone "https://github.com/stargate-rewritten/Stargate-Mechanics"
git clone "https://github.com/stargate-rewritten/Stargate-Mapper"
git clone "https://github.com/stargate-rewritten/Stargate-Customizations"
git clone "https://github.com/stargate-rewritten/Stargate-Interfaces"

cd /GitHub/Stargate-Bukkit
mvn clean install -DskipTests
cp /GitHub/Stargate-Bukkit/target/Stargate-*.jar /plugins
cd /GitHub/Stargate-Mechanics
mvn clean install -DskipTests
cp /GitHub/Stargate-Mechanics/target/StargateMechanics-*.jar /plugins
cd /GitHub/Stargate-Mapper
mvn clean install -DskipTests
cp /GitHub/Stargate-Mapper/target/StargateMapper-*.jar /plugins
cd /GitHub/Stargate-Customizations
mvn clean install -DskipTests
cp /GitHub/Stargate-Customizations/target/StargateCustomizations-*.jar /plugins
cd /GitHub/Stargate-Interfaces
mvn clean install -DskipTests
cp /GitHub/Stargate-Interfaces/target/StargateInterfaces-*.jar /plugins
cd ~