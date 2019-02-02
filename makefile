SHELL='/bin/bash'

conda-env:
        conda create --name data-analysis python=3.5 anaconda

create_table:
		psql -h $(DB_HOST) -d $(DB_NAME) -p $(DB_PORT) -U $(DB_USER) -f ./src/create_table.sql

db_login:
		psql -h $(DB_HOST) -d $(DB_NAME) -p $(DB_PORT) -U $(DB_USER)

run_container_ec2:
		sudo docker run -d -p 80:80 --env-file .env prop-map