# Execute a command

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  returns => [0, 1],
}
