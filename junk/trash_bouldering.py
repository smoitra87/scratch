from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
import time
import os
import random
import math
import subprocess
import itertools

values = [math.pi, math.e, math.log(10), math.log(2) ] + [math.sqrt(i) for i in (2,3,5)] 
values = ["{:5f}".format(v) for v in values]
values += ["e^ipi + 1 = 0"]


names = [
"Donald Duck",
"Filet Minyon",
"P. Ennis",
"Dr James B GrossWeiner",
"Dr Shit Fun Chew",
"Tiny Cox",
"Mr SackRider",
"Dick Power",
"Dr Rick Titball",
"Mr Dick Felt",
"Diana Dbag",
"Fannie Licker",
"Dick Thrasher",
"MacDonald Berger",
"Dr Joelle Rollo-Koster",
"Loony Warde",
"Hardy Harr",
"Mr Moe Lester",
"Dr Hurt"
]

ids = [
"METHIONYLTHREONYLTHREONYGLUTAMINYLARGINYLISOLEUCINE",
"LOPADOTEMACHOSELACHOGALEOKRANIOLEIPSANPTERYGON",
"PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
"PARASTRATIOSPHECOMYIASTRATIOSPHECOMYIOIDES",
"PSEUDOPSEUDOHYPOPARATHYROIDISM",
"FLOCCINAUCINIHILIPILIFICATION",
"SUBDERMATOGLYPHIC"
]
ids = map(str.lower, ids)


def run_driver() : 
	# Create a new instance of the Firefox driver
	driver = webdriver.Firefox()

	# go to the google home page
	driver.get("https://docs.google.com/forms/d/1EdxL7W_vKy3sdQT0FMyUQGhNJYoGvdT2y8Y8RmQRHms/viewform")

	# the page is ajaxy so the title is originally this:
	print driver.title

	name_field = driver.find_element_by_id('entry_1643579124')
	name_field.send_keys(random.choice(names))

	andrew_field = driver.find_element_by_id('entry_288041692')
	andrew_field.send_keys(random.choice(ids))

	rides_field = driver.find_element_by_id('entry_563406483')
	rides_field.send_keys(random.choice(values))

	comment_field = driver.find_element_by_id('entry_1020333155')
	comment_field.send_keys(subprocess.check_output("fortune").strip())

	for radio in ('group_477188083_1','group_1679155372_1'):
		yes_field = driver.find_element_by_id(radio)
		yes_field.click()

	submit = driver.find_element_by_id('ss-submit')
	submit.submit()
	time.sleep(2)
	try:
		driver.switch_to_alert().accept()
		print("Alert accepted")
		time.sleep(2)
	except Exception as e:
		pass
	driver.quit()

if __name__ == '__main__':
	while True : 
		run_driver()
		time.sleep(random.randint(30,60))

