from win11toast import toast
import psutil

# Get battery info
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
icon_image ="https://images.pexels.com/photos/1694830/pexels-photo-1694830.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# Check if laptop is charging
if plugged:
    toast('Charging Status🔌', 'Laptop is now charging. Current charge: '+percent+'%', icon=icon_image,button='Dismiss')