from pyd.support import setup, Extension

projName = 'search_lib'

setup(
    name=projName,
    version='0.1',
    ext_modules=[
        Extension(projName, ["source/app.d"],
        	optimize=True,
            d_lump=True,
            build_deimos=False)
    ],
)