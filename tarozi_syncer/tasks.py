import frappe
import requests

def hourly():
	
	# send get request
	
	
	r = requests.get("https://agroonline.uz:8443/service_1c.jsp?a=get_main&last_date=20.05.2019_16.28.00&point=0&l=306698947&o=s8MD@QyaF-5nTx ")
	# r = requests.get("google.com")
	# r = frappe.request.get("https://agroonline.uz:8443/service_1c.jsp?a=get_main&last_date=20.05.2019_16.28.00&point=0&l=306698947&o=s8MD@QyaF-5nTx ")
	print(r.text)
	print("Hello World")
	pass