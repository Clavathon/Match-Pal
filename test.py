import json
from search import *

json = '''{
	"computers": {
	    "1": {
	        "merchant": "pny",
	        "cost": "339.0",
	        "name": "pny geforce gtx 1060 6gb"
	    },
	    "0": {
	        "merchant": "evga",
	        "cost": "209.0",
	        "name": "evga geforce gtx 1060 3gb"
	    },
	    "3": {
	        "merchant": "msi",
	        "cost": "46.02",
	        "name": "msi geforce gt 2gb"
	    },
	    "2": {
	        "merchant": "evga",
	        "cost": "757.0",
	        "name": "evga geforce gtx 1080 ti 11gb"
	    },
	    "5": {
	        "merchant": "msi",
	        "cost": "29.98",
	        "name": "msi radeon 1gb r6450-md1gd3"
	    },
	    "4": {
	        "merchant": "gigabyte",
	        "cost": "139.99",
	        "name": "gigabyte geforce gtx 1050 2gb"
	    },
	    "7": {
	        "merchant": "msi",
	        "cost": "49.99",
	        "name": "msi radeon 6450 2gb"
	    },
	    "6": {
	        "merchant": "xfx",
	        "cost": "239.99",
	        "name": "xfx radeon rx 580 8gb"
	    },
	    "8": {
	        "merchant": "asus",
	        "cost": "139.99",
	        "name": "asus radeon rx 560 4gb"
	    }
	}
}'''

out = search_products("r6", [], json)
assert(out == [(8, 1.0), (6, 0.6666666666666666), (5, 0.3333333333333333), (7, 0.16666666666666666)])
try:
	out = search_products("", [], json)
except ValueError as e:
	pass
else:
	print("Failed to catch no input error!")
try:
	out = search_products("bull", ["invalid_category"], json)
except ValueError as e:
	pass
else:
	print("Failed to catch invalid category error!")
try:
	out = search_products("bull", [], "{ ' }")
except ValueError as e:
	pass
else:
	print("Failed to catch invalid json error!")