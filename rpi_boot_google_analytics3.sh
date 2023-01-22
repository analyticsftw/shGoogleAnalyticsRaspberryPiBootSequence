# rpi_boot_google_analytics3.sh
# Triggers Google Universal Analytics endpoint upon boot
#
# Julien Coquet
# http://juliencoquet.com/en
# @juliencoquet

# Parameters -- your mileage should vary 
endPointBase="https://www.google-analytics.com/collect?v=1"
hitType="&t=event"
clientID="&cid=1337"
accountID="&tid=UA-XXXXXXX-YY"  # Your property ID
hostname="&dh=yourwebsite.com"

# Define Google Analytics event category and action here
eventParams="&ec=Server+Events&ea=Boot"

# Uncomment the lines below to add server time
# serverTime=`date +%H:%M:%S`
# eventParams=$eventParams\&el=$serverTime

# Change to reflect your box's name
userAgent="RaspBerry Pi"

# Endpoint concatenation
endPointFinal=$endPointBase$hitType$clientID$accountID$hostname$eventParams

# Release the Kraken!
wget -nv -U $userAgent -O /dev/null $endPointFinal
