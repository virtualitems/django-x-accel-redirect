from multiprocessing import cpu_count

# as user
user = 'app1user'
group = 'www-data'

# unix domain socket
bind = 'unix:/var/run/djangoapp/app.sock' # deshabilitar en pruebas
timeout = 500

# processing
worker_class = 'uvicorn.workers.UvicornWorker'
workers = cpu_count() * 2

# paths
chdir = '/home/app1user/djangoapp'
pythonpath = '/home/app1user/djangoapp'

# logging
accesslog = '/var/log/djangoapp/gunicorn_access.log' # deshabilitar en pruebas
errorlog = '/var/log/djangoapp/gunicorn_error.log' # deshabilitar en pruebas
loglevel = 'info' # 'debug' en pruebas
