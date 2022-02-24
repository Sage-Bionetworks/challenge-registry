

# Challenge Registry

Monorepo creation status:

|                  | prepare | lint | lint-fix | build | test | coverage | serve | e2e | docker |
|------------------|---------|------|----------|-------|------|----------|-------|-----|--------|
| apps/api         | ✔️       | ✔️    | ✔️        |       | ✔️    |          | ✔️     |     | ✔️      |
| apps/api-db      | ✔️       |      |          |       |      |          | ✔️     |     | ✔️      |
| apps/db-cli      |         | ✔️    | ✔️        | ✔️     | ✔️    |          | ✔️     |     |        |
| apps/web-app     | ✔️       | ✔️    | ✔️        | ✔️     | ✔️    |          | ✔️     |     | ✔️      |
| apps/web-app-e2e |         | ✔️    | ✔️        |       |      |          |       | ✔️   |        |
| libs/api-angular |         | ✔️    | ✔️        | ✔️     | ✔️    |          |       |     |        |
| libs/api-docs    |         |      |          | ✔️     |      |          | ✔️     |     |        |
| libs/api-spec    |         | ✔️    |          | ✔️     |      |          | ✔️     |     |        |

This project was generated using [Nx](https://nx.dev).

## Requirements

- [Docker]
- [Node.js] >= 14
- [Yarn]

## Development

Source `dev-env.sh`.

    . dev-env.sh

Prepare the development environment.

    challenge-registry-prepare

Lint the projects.

    yarn lint

Build the projects.

    yarn build

Test the projects.

    yarn test

Start the stack.

    yarn start

Seed the API DB with the default seed (`production`).

    yarn seed-db

<!-- Links -->

[Docker]: https://docs.docker.com/get-docker/
[Node.js]: https://nodejs.org/en/
[Yarn]: https://yarnpkg.com/
