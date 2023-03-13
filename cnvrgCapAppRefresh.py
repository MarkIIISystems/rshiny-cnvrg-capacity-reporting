#!/usr/bin/python3
import argh
import sys
import time
from cnvrgv2 import Cnvrg



# declaring:

def start():
	#"Attempts to start the Cnvrg pvCnvrgCapacityReport Rshiny app."
	cnvrg = Cnvrg(domain="https://xxxxxxx", email="xxxxx@xxxxxx.xxx",password="xxxxxxxxxxxxxxx")
	myproj = cnvrg.projects.get("pv-capacity-reporting")
	wb = myproj.webapps.create(title="pvCnvrgCapacityReport",templates=["medium","large"],file_name="app.R",webapp_type="rshiny")
	time.sleep(5)
	myproj = cnvrg.projects.get("pv-capacity-reporting")
	wbs = myproj.webapps.list(sort="-created_at")
	for wb in wbs:
		if wb.title == 'pvCnvrgCapacityReport' and wb.status == 'ongoing':
			print("Webapp pvCnvrgCapacityReport has started")
		else:
			print(wb.title + " is in status: " + wb.status)
			sys.exit("Exiting: " + wb.title + " is in status: " + wb.status)
		

def stop():
	#"Attempts to stop and delete the Cnvrg pvCnvrgCapacityReport Rshiny app."
	cnvrg = Cnvrg(domain="https://xxxxxxx", email="xxxxx@xxxxxx.xxx",password="xxxxxxxxxxxxxxx")
	myproj = cnvrg.projects.get("pv-capacity-reporting")
	wbs = myproj.webapps.list(sort="-created_at")
	for wb in wbs:
		if wb.title == 'pvCnvrgCapacityReport':
			print("Attempting to stop/delete pvCnvrgCapacityReport App")
			#deleteslug = wb.slug
			wb.delete()
		else:
			print("Couldnot find slug for app pvCnvrgCapacityReport.")
			sys.exit("Exiting: Webapp slug not found.")
		


# assembling:
parser = argh.ArghParser()
parser.add_commands([start, stop])

# dispatching:

if __name__ == '__main__':
	parser.dispatch()
