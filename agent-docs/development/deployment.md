# Deployment Constraints

## Container Requirements

- CTFd container runs as `root` (required for plugin installation into the image).
- Jumpbox server must have a provisioning user with sudo access and SSH key authentication configured before the plugin can provision users.

## SSH Key Lifecycle

- Keys are written to `/tmp` on the CTFd container filesystem. Container restarts lose uploaded keys unless SSM integration is used or the key is re-uploaded via admin UI.
- SSM integration re-fetches keys on every container start, solving the ephemeral storage problem.

## Config Persistence

- Manual UI config persists in the database across restarts.
- SSM config overwrites database values on each startup. The admin UI warns about this when SSM env vars are detected.
