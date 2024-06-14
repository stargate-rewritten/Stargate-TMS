FROM maven:3.8.8-amazoncorretto-21-debian

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y\
	git

RUN mkdir GitHub && \
	cd GitHub && \
	git clone "https://github.com/stargate-rewritten/Stargate-Bukkit" && \
	git clone "https://github.com/stargate-rewritten/Stargate-Mechanics" && \
	git clone "https://github.com/stargate-rewritten/Stargate-Mapper" && \
	git clone "https://github.com/stargate-rewritten/Stargate-Customizations" && \
	git clone "https://github.com/stargate-rewritten/Stargate-Interfaces"

RUN cd /GitHub/Stargate-Bukkit && \
	mvn dependency:resolve --fail-never
	
RUN cd /GitHub/Stargate-Mechanics && \
	bash gradlew dependencies --continue
	
RUN cd /GitHub/Stargate-Mapper && \
	mvn dependency:resolve --fail-never
	
RUN cd /GitHub/Stargate-Customizations && \
	mvn dependency:resolve --fail-never

RUN cd /GitHub/Stargate-Interfaces && \
	mvn dependency:resolve --fail-never

COPY /compile.sh /compile.sh
ENTRYPOINT bash compile.sh