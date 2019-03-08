from distutils.core import setup
import py2exe
setup(console = ["antivirus.py"])
setup(console = [{
    'script':"antivirus.py",
    "icon_resources": [(0,'babyicon.ico')]
	}])
