# change a line in a file
exec { 'change a line':
  command => '/usr/bin/sudo /bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 10000\"/g" /etc/default/nginx && service nginx restart',
    }
