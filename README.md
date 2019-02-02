# prop-map
Property Mapping


## Creating docker container
Export your env variables to your local env using ```source .env```
Then build your docker container
```
docker build --tag prop_map --build-arg DB_HOST=${DB_HOST} --build-arg DB_USER=${DB_USER} --build-arg DB_PASSWORD=${DB_PASSWORD} --build-arg DB_NAME=${DB_NAME} --build-arg DB_PORT=${DB_PORT} --build-arg MAPBOX_ACCESS_TOKEN=${MAPBOX_ACCESS_TOKEN} .
```
