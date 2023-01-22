# rpi_boot_google_analytics4.py
# Triggers Google Analytics 4 endpoint upon boot
# Use as-is or called from your etc.d folder
#
# Julien Coquet
# http://juliencoquet.com/en
# For reference: https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference?client_type=gtag
# @juliencoquet

import requests

# Parameters -- your mileage should vary 
endPointBase = "https://www.google-analytics.com/mp/collect"
apiSecret = "api_secret=taDfzse2Qo6J744RwdH7OA"                    # Change with API secret from GA4 admin interface
measurementID = "measurement_id=G-4S82DT2XKJ"        # Change with property measurement ID from GA4 admin interface

# Endpoint concatenation
endPointFinal = endPointBase + '?' + measurementID + '&' + apiSecret

# Define Google Analytics event parameters to be sent as payload
clientID="1337"
userID="raspberry"
eventName="boot" 
eventParams={
    "client_id":clientID,
    "user_id":userID,
    "events": [{"name": eventName}]
}

# Release the Kraken!
x = requests.post(endPointFinal, json = eventParams)
