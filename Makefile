notexblock.up: .build/image
	docker-compose -f docker-compose.yml up -d

notexblock.down:
	docker-compose -f docker-compose.yml down


.build/image: .build requirements.txt
	docker build -t notexblock .
	touch .build/notexblock.build
 
.build:
	mkdir .build 





