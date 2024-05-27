cd /usr/share/java
sudo service jenkins stop
sudo mv jenkins.war ./jenkins.war.old
sudo wget https://updates.jenkins-ci.org/latest/jenkins.war
sudo service jenkins start