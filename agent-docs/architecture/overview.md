# Architecture Overview

CTFd plugin that automates SSH user provisioning on a dedicated jumpbox server for CTF competitions.

## System Architecture

```
CTFd (Flask) ──[plugin load()]──> Jumpbox Plugin
                                    ├── Admin Config UI (/admin/jumpbox_config)
                                    ├── Admin User Mgmt UI (/admin/jumpbox_user_mgmt)
                                    ├── User Credentials UI (/jumpbox)
                                    ├── REST API (DELETE /api/v1/delete_jump_user)
                                    └── SSM Config Loader (startup-only)
                                          │
                                          ▼
                                    Jumpbox Server (SSH)
                                    └── useradd via paramiko
```

## Plugin Structure

- `jumpbox/__init__.py` - Plugin entry point, Flask blueprints, route definitions
- `jumpbox/functions/functions.py` - SSH connection and user provisioning via paramiko
- `jumpbox/functions/ssm.py` - Optional AWS SSM Parameter Store config loading
- `jumpbox/models/models.py` - SQLAlchemy models (JumpboxConfig, JumpboxUsers)
- `jumpbox/api/api.py` - REST API for user deletion
- `jumpbox/config.json` - CTFd plugin menu registration
- `jumpbox/templates/` - Jinja2 admin and user templates

## Key Integration Points

- Extends CTFd via its plugin system (`load(app)` entry point)
- Uses CTFd's `db` (SQLAlchemy), auth decorators, and user/team utilities
- Single config record pattern: all queries filter by `id=1`
- SSH keys stored as file paths in the database, pointing to `/tmp` files on disk
