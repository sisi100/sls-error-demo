DOCKER=docker-compose -f docker-compose.yml

docker-up:
	$(DOCKER) up

init:
	cp .env.aws-credentials.sample .env.aws-credentials

sls:
	$(DOCKER) run sls ${p}

deploy:
	$(DOCKER) run sls sh ./script/deploy.sh

remove:
	$(DOCKER) run sls sh ./script/remove.sh
