# Puppet manifest to install and configure Nginx web server

class { 'nginx':
  ensure  => 'installed',
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Class['nginx'],
}

nginx::resource::vhost { 'default':
  www_root    => '/var/www/html',
  port        => '80',
  proxy       => 'http://localhost:80',
  ssl         => false,
  rewrite_to  => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  rewrite_code => 301,
  require     => File['/var/www/html/index.html'],
}
