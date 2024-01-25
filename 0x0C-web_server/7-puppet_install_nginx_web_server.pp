# Puppet manifest for installing and configuring Nginx

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /usr/share/nginx/html;
      index index.html;

      server_name _;

      location / {
        try_files \$uri \$uri/ =404;
      }

      error_page 404 /404.html;
      location = /404.html {
        root /usr/share/nginx/html;
        internal;
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Reload Nginx to apply changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

# Create Hello World! index.html
file { '/usr/share/nginx/html/index.html':
  content => 'Hello World!',
  notify  => Service['nginx'],
}
