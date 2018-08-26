import os.path, sys
import platform
import distutils.util

# Append the directory in which the binaries were placed to Python's sys.path,
# then import the D DLL.
libDir = os.path.join('build', 'lib.%s-%s' % (
    distutils.util.get_platform(),
    '.'.join(str(v) for v in sys.version_info[:2])
  ))
sys.path.append(os.path.abspath(libDir))

import search

json = '''{
	"Computers": {
		"1": {
			"name": "GTX 1080",
			"cost": 800,
			"merchant": "Nividia"
		},
		"2": {
			"name": "GTX 1070",
			"cost": 300,
			"merchant": "Nividia"
		}
	}
}'''

search.search_products("Hello", json);