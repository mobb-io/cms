# Gunicorn configuration file

bind = '0.0.0.0:8000'

workers = '3' 
workerClass = 'tornado' 
timeout = '300'
gracefulTimeout = '300' 

loglevel = 'info'
errorlog = '-'
accesslog = '-'
