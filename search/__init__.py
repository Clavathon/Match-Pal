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

# Publicly import functions from the D library
from search_lib import search_products as _search_products

# Wrapper function to raise python errors after D processes
def search_products(input_value, categories, json_string):
	output = _search_products(input_value, categories, json_string)
	if output[0] == -1:
		raise ValueError("Failed to find category in your categories!")
	elif output[0] == -2:
		raise ValueError("Empty input!")
	elif output[0] == -3:
		raise ValueError("Malformed json!")
	return output[1]