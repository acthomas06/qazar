#!python
import sys
sys.path.insert(0, '.')

from cloudtestenvironment import app as application
application.run(host='127.0.0.1', port=5000, debug=True)