#!/usr/bin/env bash

docker run --rm  \
        -v "$(pwd)/db/flywaysql:/flyway/sql" --network "pyinfocrawler_postgres" \
        -v "$(pwd)/db/flyway.conf:/flyway/conf/flyway.conf" \
        flyway/flyway:6.5.2 baseline
docker run --rm  \
        -v "$(pwd)/db/flywaysql:/flyway/sql" --network "pyinfocrawler_postgres" \
        -v "$(pwd)/db/flyway.conf:/flyway/conf/flyway.conf" \
        flyway/flyway:6.5.2 migrate
docker run --rm \
        -v "$(pwd)/db/flywaysql:/flyway/sql" --network "pyinfocrawler_postgres" \
        -v "$(pwd)/db/flyway.conf:/flyway/conf/flyway.conf" \
        flyway/flyway:6.5.2 info
