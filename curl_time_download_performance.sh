#!/bin/bash

set -e

# curl function
target=$@

curltime()
{
 curl -w "\\t %{time_namelookup}; \\t %{time_connect}; \\t %{time_appconnect}; \\t %{time_pretransfer}; \\t %{time_redirect}; \\t %{time_starttransfer}; \\t %{time_total}\\n" -o /dev/null -s -k $@
}

echo -e "timestamp; time_namelookup; time_connect; time_appconnect; time_pretransfer; time_redirect; time_starttransfer; time_total"

while true; do
  dd=$(TZ='UTC' date +"%F %T %Z")
  bb=$(curltime $target)
  echo "$dd"\; "$bb"
  sleep 1
done
