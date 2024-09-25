# Installs a nginx server with custom HTTP header

exec {'update':
	provider => shell,
	command => 'apt-get -y update',
	before => Exec['install nginx'],
}

exec {'install nginx':
	provider => shell,
	command => 'apt-get -y install nginx',
	before => Exec['add custom header'],
}

exec {'add custom header':
	provider => shell
	environment => ["HOST=${hostname}"],
	command => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  	before => Exec['restart nginx'],
}

exec {'restart nginx':
	provider => shell,
	command => 'service nginx restart',
}
