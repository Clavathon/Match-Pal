import os.path, sys
import platform
import distutils.util

# Append the directory in which the binaries were placed to Python's sys.path,
# then import the D DLL.
libDir = os.path.join('search/build', 'lib.%s-%s' % (
    distutils.util.get_platform(),
    '.'.join(str(v) for v in sys.version_info[:2])
  ))
sys.path.append(os.path.abspath(libDir))

from search_lib import *

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

print(search_products("dfds", ["computers"], ""))
