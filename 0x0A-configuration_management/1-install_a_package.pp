# Installs flask with pip3 package manager
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
