#! /bin/sh
rm -r output/
mkdir output/
mv vis.heprep.zip output/
cd output/
unzip vis.heprep.zip
java -jar /opt/HepRep/HepRApp.jar event-0000000001.heprep
