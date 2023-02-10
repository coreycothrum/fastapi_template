## initial setup
## usage
### start the application
    docker compose down  && \
    docker compose up       \
        --build             \
        --detach            \
        --force-recreate    \
        --remove-orphans    \
        --wait           &&
    docker compose logs -f

### stop the application
    docker compose down

## contributing
how to work in this repo

### use pre-commit
keep this repo clean, use [pre-commit](https://pre-commit.com/)

1. install [pre-commit](https://pre-commit.com/#1-install-pre-commit)

2. apply [pre-commit](https://pre-commit.com/#3-install-the-git-hook-scripts) config to local git hook script(s):

        pre-commit install

3. (optional, as needed) update [pre-commit](https://pre-commit.com/#pre-commit-autoupdate) config to latest:

        pre-commit autoupdate

4. (optional, as needed) manually run [pre-commit](https://pre-commit.com/#pre-commit-run) check(s)

        pre-commit run --all-files
