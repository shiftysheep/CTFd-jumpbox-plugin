# Development Setup

## Non-Standard Installation

This plugin is not standalone. It must be installed into an existing CTFd deployment:

- `install.py` copies the `jumpbox/` directory into CTFd's `CTFd/plugins/` and appends dependency installation to CTFd's Dockerfile.
- When using docker, the plugin's `requirements.txt` is installed during the CTFd image build, not separately.
- The `dockerfile` in this repo is a minimal wrapper that extends `ctfd/ctfd:latest`.

## Environment Variables (SSM Integration)

Three optional env vars activate AWS SSM config loading. See `docker-compose.yaml` for examples. Standard boto3 credential chain is used (instance role, env vars, or `~/.aws/credentials`).

## Database

Plugin tables are auto-created via `app.db.create_all()` in `load()`. No migrations. Uses CTFd's configured database (MariaDB in docker-compose).

## Docker Networks

`docker-compose.yaml` defines two networks: `default` (public-facing) and `internal` (DB/cache isolation). The CTFd service bridges both.
