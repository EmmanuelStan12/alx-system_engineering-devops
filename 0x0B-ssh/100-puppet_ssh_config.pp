# Setup SSH Client Configuration

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
  path => '/bin/'
}
