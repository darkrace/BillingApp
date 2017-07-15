	import os
	import sys
path='/home/pythonanywheredarkrace/BillingApp'
if  path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'BillingApp.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())