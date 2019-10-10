# change a line in a file
exec { 'change a line':
  command => '/usr/bin/sudo /bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 30000/g" /etc/security/limits.conf',
    }
exec { 'change another line':
  command => '/usr/bin/sudo /bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 10000/g" /etc/security/limits.conf',
    }

