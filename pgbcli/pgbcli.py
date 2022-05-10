from random import randint as mbps
from time import sleep, ctime

__author__ = "MatheusTGP"
__version__ = "1.0"

colors = {
	'red': '\033[01;31m',
	'green': '\033[01;32m',
	'yellow': '\033[01;33',
	'blue': '\033[01;34m',
	'magenta': '\033[01;35m',
	'cyan': '\033[01;36m',
	'white': '\033[01;37m',
	'none': '\033[00;00m'
}

def progressBar(text='Baixando:', color='none', theme='.', max_upload=5, total=100, speed=0.500, **kwargs):
	"""PGBCLI

	Chame esta função para que voce possa exibir a barra de progresso.
	"""
	global colors

	try:
		bar_speed = 0
		percent_total = 0
		color = colors.get(color)
		color_default = colors.get('none')

		while (percent_total < total):
			speed_upload = mbps(1, max_upload)
			bar_speed += 1
			print(f"\r{text} [ " + f'{color_default}{color}{theme}{color_default}'*(bar_speed)+f' ] {percent_total}%', end='', flush=True)
			sleep(speed)
			percent_total += speed_upload
	
	except KeyboardInterrupt:
		print("\nprogressbar stopped.")

def pgb_version():
	'''Show the module Version'''
	print(f"PGB-CLI v{__version__}")
