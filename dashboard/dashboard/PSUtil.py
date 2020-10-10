import json
import psutil

from dashboard.Image import draw_black, get_enhanced_icon, h_black_image, h_red_image, small_font


def print_stats():
	stats = get_stats()

	odometer_icon = get_enhanced_icon('assets/speed/odometer.jpeg', 45, False)
	download_icon = get_enhanced_icon('assets/speed/download.jpeg', 25, False)
	upload_icon = get_enhanced_icon('assets/speed/upload.jpeg', 25, False)

	h_red_image.paste(odometer_icon, (2, 128))
	# h_black_image.paste(download_icon, (50, 138))
	draw_black.text(
		(82, 130),
		stats['cpu_usage'] + '%',
		font=small_font,
		fill=0)
	draw_black.text(
		(82, 150),
		stats['ram_usage'] + '%',
		font=small_font,
		fill=0)

	# h_black_image.paste(upload_icon, (160, 138))
	draw_black.text(
		(160, 130),
		stats['ip_address'],
		font=small_font,
		fill=0)


def get_stats():
	return {
		# Load average of last 15 minutes
		'cpu_usage': str(psutil.getloadavg()[2]),
		'cpu_temp': str(psutil.sensors_temperatures()['cpu_thermal'][0].current),
		# Ram percentage used
		'ram_usage': str(psutil.virtual_memory().percent),
		'ip_address': str(psutil.net_if_addrs()['wlan0'][0].address),
	}
