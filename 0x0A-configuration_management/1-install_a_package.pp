# Installs puppet-lint, version 2.1.1

exec { 'install python packages':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
