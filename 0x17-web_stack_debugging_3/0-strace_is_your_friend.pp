#Fixes bad ""pphp" extensions to "php" in "wp-settings.php".

$target_file = '/var/www/html/wp-settings.php'

#Fix WordPress configuration by replacing line containing "phpp" with "php"

exec { 'fix_wordpress_config':
  command => "sed -i 's/phpp/php/g' ${target_file}",
  path    => ['/bin','/usr/bin']
}
