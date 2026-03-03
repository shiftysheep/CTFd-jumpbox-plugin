# CTFd Jumpbox Plugin

**What**: CTFd plugin for automated SSH user provisioning on a jumpbox server, built with Flask/paramiko.

**Why**: CTF competitions need temporary SSH access for participants. This plugin provisions accounts on-demand when users visit `/jumpbox`, avoiding manual account creation. SSM integration eliminates post-deploy admin configuration. See [architecture decisions](agent-docs/architecture/decisions.md) for detailed rationale.

See [architecture overview](agent-docs/architecture/overview.md) for system design.

## Quick Start

```bash
docker-compose up  # CTFd on :80, configure jumpbox at /admin/jumpbox_config
```

See [setup guide](agent-docs/development/setup.md) for installation into existing CTFd deployments.

## Development

**Package Manager**: pip | **Tests**: None | **Hooks**: None

Key constraints:
- Plugin installed into CTFd via `install.py`, not standalone
- Single jumpbox config record (`id=1` hardcoded)
- RSA keys only (paramiko limitation)
- No test suite; verify manually with docker-compose

**Resources**:
- [Architecture patterns](agent-docs/architecture/patterns.md)
- [Known limitations](agent-docs/architecture/limitations.md)
- [Deployment constraints](agent-docs/development/deployment.md)
