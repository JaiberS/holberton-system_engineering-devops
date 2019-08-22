# HTML header
exec { 'change to head HTML':
  command => '/usr/bin/sudo /bin/sed -i "14i\ \tadd_header X-Served-By $(cat /etc/hostname);" /etc/nginx/nginx.conf && /usr/bin/sudo /usr/sbin/service nginx restart',
    }