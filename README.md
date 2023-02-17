## Initial Setup
### Environment Variables
### SSL Certificates
follow [these instructions](https://github.com/coreycothrum/nginx_certbot_docker_compose#initial-setup) to setup HTTPS certs

## Usage
### Start the Application
    docker compose down  && \
    docker compose up       \
        --build             \
        --detach            \
        --force-recreate    \
        --remove-orphans    \
        --wait           &&
    docker compose logs -f

### Stop the Application
    docker compose down

### Maintenance Shell
this environment can be used to generate alembic migrations

    docker compose run                    \
        --build                           \
        --entrypoint /bin/bash            \
        --rm                              \
        --user "$(id -u):$(id -g)"        \
        --volume "$(pwd)/fastapi":/app:rw \
        fastapi

## Contributing
how to work in/with this repo

### Use Conventional Commits
git commits should adhere to the [conventional commits spec](https://www.conventionalcommits.org/)

### Use `pre-commit`
keep the repo clean, use [pre-commit](https://pre-commit.com/)

1. install [pre-commit](https://pre-commit.com/#1-install-pre-commit)

2. apply [pre-commit](https://pre-commit.com/#3-install-the-git-hook-scripts) config to local git hook script(s):

        pre-commit install
        pre-commit install --hook-type commit-msg

3. (optional, as needed) update [pre-commit](https://pre-commit.com/#pre-commit-autoupdate) config to latest:

        pre-commit autoupdate

4. (optional, as needed) manually run [pre-commit](https://pre-commit.com/#pre-commit-run) check(s)

        pre-commit run --all-files
