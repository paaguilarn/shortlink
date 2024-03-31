build:
	docker-compose --file docker-compose.yml build --no-cache

status:
	## Show status of containers
	@docker-compose ps

stop:
	## Stop containers
	@docker-compose --file docker-compose.yml stop

clean:
	## Clean all data
	@docker-compose --file docker-compose.yml down

up:
	## Start all or c=<name> containers in foreground
	@docker-compose --file docker-compose.yml up $(c)

start:
	## Start all or c=<name> containers in background
	@docker-compose --file docker-compose.yml up -d $(c)

test:
	## Run tests
	@docker-compose --file docker-compose.yml run --rm backend bash -c "pytest --cov=./ --cov-report=xml"

