#!/bin/bash
cd /tmp
mkdir geodata
cd geodata
/usr/bin/wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
/bin/rm GeoIP.dat
/bin/gunzip GeoIP.dat.gz
/bin/cp GeoIP.dat  /opt/kneto-web/geodata/