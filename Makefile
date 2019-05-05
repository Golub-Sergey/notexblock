help: ## Display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'


notexblock.up: .build/image ## up xblock workbench in notexblock container
	docker-compose -f docker-compose.yml up -d

notexblock.shutdown: ## remove notexblock service container and network
	docker-compose -f docker-compose.yml down

notexblock.stop: ## stop notexblock service
	docker-compose -f docker-compose.yml stop

notexblock.shell: ## run notexblock container shell 
	docker-compose exec notexblock bash 

.build/image: .build requirements.txt # command for buid notexblock image
	docker build -t notexblock .
	touch .build/image
 
.build:
	mkdir .build 

clear: ## rebuild notexblock container
	rm -R ./.build




