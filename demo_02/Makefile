DOCKER=docker-compose -f docker-compose.yml

docker-up:
	$(DOCKER) up

init:
	cp .env.aws-credentials.sample .env.aws-credentials

sls:
	$(DOCKER) run sls ${p}
