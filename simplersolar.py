# Simpler solar project
# Calculate remaining time to breakeven from solar installation website

import urllib

site = ["http://egauge14368.egaug.es"]
cost = [30000]
house_array = []
garage_array = []
total_arrays = []
params = ['/cgi-bin/egauge-show?n=1&m&f=1407159000']

def show_webpage():
	full_site = site[0]+params[0]
	f = urllib.urlopen(full_site)
	print f.read()

def main_loop():
	user_input = ""
	while 1:
		user_input = raw_input("Accept defaults?(Y/N/Q)> ")
		if user_input.lower().startswith("q"):
			print "Exiting..."
			break
		elif user_input.lower().startswith("y"):
			print site[0]
			print cost[0]
			show_webpage()
		elif user_input.lower().startswith("n"):
			print "Custom sites not yet ready. Please try again with defaults"
		else:
			pass	

if __name__ == '__main__':
	main_loop()
