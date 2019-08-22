# HTML header
exec { 'change to head HTML':
  command => '/usr/bin/sudo /usr/bin/apt-get -y update && /usr/bin/sudo /usr/bin/apt-get -y install nginx && /usr/bin/sudo /bin/echo "Holberton School" | /usr/bin/sudo /usr/bin/tee /var/www/html/index.html && /usr/bin/sudo /bin/sed -i "14i\ \tadd_header X-Served-By $(cat /etc/hostname);" /etc/nginx/nginx.conf && /usr/bin/sudo /usr/sbin/service nginx restart',
    }