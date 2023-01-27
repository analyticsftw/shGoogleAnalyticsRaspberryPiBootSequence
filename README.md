# shGoogleAnalyticsRaspberryPiBootSequence
Script to track your Raspberry Pi's boot sequence and other system events with Google Analytics

The scripts in this repository manage various versions of Google Analytics (Universal Analytics and Google Analytics 4)

Note that the Google Analytics 4 script uses Python instead of shell for easier JSON usage.

## To start the script at boot/reboot, use a CRON task, e.g.
- `crontab -e` to open the scheduled tasks list
- Add a new line in the crontab file such as

  `@reboot sh /home/pi/projects/rpi_boot_google_analytics3.sh`
  
  or
  
  `@reboot python /home/pi/projects/rpi_boot_google_analytics4.py`


View the example video at: https://www.youtube.com/watch?v=_ylggGtdUGA

Original blog post at: https://juliencoquet.com/en/blog/2013/09/18/more-raspberry-pi-and-google-universal-analytics-goodness/
