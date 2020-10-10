import requests

from dashboard.Image import draw_black, get_enhanced_icon, h_black_image, h_red_image, small_font
from dashboard.Config import country, covid_url


def get_covid(url_suffix):
	current_covid = requests.get(covid_url + url_suffix)
	if current_covid.ok:
		current_covid_dictionary = current_covid.json()
		return {
			'total_cases': current_covid_dictionary.get('cases'),
			'today_cases': current_covid_dictionary.get('todayCases'),
			'active_cases': current_covid_dictionary.get('active'),
			'deaths': current_covid_dictionary.get('deaths'),
			'today_deaths': current_covid_dictionary.get('todayDeaths'),
		}
	else:
		return {}


def print_covid():
	# covid_global = get_covid('all')
	covid_local = get_covid('countries/' + country + '?allowNull=1')
	covid_yesterday = get_covid('countries/' + country + '?yesterday=1')

	# Use yesterday data when today data is not available
	if covid_local['today_cases'] is None:
		covid_local['today_cases'] = covid_yesterday['today_cases']
	if covid_local['today_deaths'] is None:
		covid_local['today_deaths'] = covid_yesterday['today_deaths']

	covid_icon = get_enhanced_icon('assets/covid/covid.jpeg', 45, False)
	global_icon = get_enhanced_icon('assets/covid/total.jpg', 25, False)
	local_icon = get_enhanced_icon('assets/covid/today.jpg', 25, False)
	cough_icon = get_enhanced_icon('assets/covid/cough.jpeg', 22, False)
	skull_icon = get_enhanced_icon('assets/covid/skull.jpeg', 22, False)

	h_red_image.paste(covid_icon, (2, 80))
	h_black_image.paste(global_icon, (50, 90))
	h_black_image.paste(cough_icon, (82, 80))
	h_black_image.paste(skull_icon, (78, 102))
	draw_black.text(
		(110, 85),
		# str(covid_local['total_cases']),
		str(round(covid_local['total_cases'] / 1000, 1)) + 'k',
		font=small_font,
		fill=0)
	draw_black.text(
		(110, 105),
		str(covid_local['deaths']),
		# covid_local['deaths'].rsplit(',', 2)[0] + '.' + covid_local['deaths'].rsplit(',', 2)[1][:2] + 'M',
		font=small_font,
		fill=0)

	h_black_image.paste(local_icon, (160, 90))
	h_black_image.paste(cough_icon, (192, 80))
	h_black_image.paste(skull_icon, (188, 102))
	draw_black.text(
		(218, 85),
		str(covid_local['today_cases']),
		# covid_local['total_cases'].rsplit(',', 2)[0] + '.' + covid_local['total_cases'].rsplit(',', 2)[1][:2] + 'M',
		font=small_font,
		fill=0)
	draw_black.text(
		(218, 105),
		str(covid_local['today_deaths']),
		font=small_font,
		fill=0)
