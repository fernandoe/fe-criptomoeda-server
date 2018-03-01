docker-build:
	# docker build --build-arg http_proxy=http://15.85.195.199:8088 --build-arg https_proxy=http://15.85.195.199:8088 -t fernandoe/fe-criptomoeda-server .
	docker build -t fernandoe/fe-criptomoeda-server .

compose-build:
	# docker-compose build --build-arg http_proxy=http://15.85.195.199:8088 --build-arg https_proxy=http://15.85.195.199:8088 criptomoeda
	docker-compose build criptomoeda

compose-up:
	docker-compose up

compose-migrate:
	docker-compose run criptomoeda python manage.py migrate

compose-createsuperuser:
	docker-compose run criptomoeda python manage.py createsuperuser
