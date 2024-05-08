# Installs puppet-lint, version 2.1.1

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
