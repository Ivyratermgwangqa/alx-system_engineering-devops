# This Puppet script configures the SSH client

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
