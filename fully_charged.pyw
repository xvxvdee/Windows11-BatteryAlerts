from win11toast import toast
import psutil

# Get battery info
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
icon_image ="https://images.pexels.com/photos/1694830/pexels-photo-1694830.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# Check if battery is fully charged and plugged in
if plugged and percent == "100":
    toast('Charging Status🔋', 'Fully charged! Unplug your laptop', icon=icon_image,button='Dismiss')
