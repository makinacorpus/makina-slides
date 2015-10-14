all:
	landslide index.cfg

service:
	cd demo && gunicorn -w 10 wsgi:app
