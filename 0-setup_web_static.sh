#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/{shared,releases/test}
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
NGINX_CONFIG="/etc/nginx/sites-available/default"
NGINX_LOCATION="location /hbnb_static {\n\talias /data/web_static/current;\n\tautoindex off;\n}"
sed -i "/server_name _;/a $NGINX_LOCATION" $NGINX_CONFIG
service nginx restart
