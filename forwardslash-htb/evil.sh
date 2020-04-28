i=$(backup | grep ERROR | awk '{print $2}');
ln -s /var/backups/config.php.bak /home/chiv/$i;/usr/bin/backup;
