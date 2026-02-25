# Design Patterns

### Blueprint-per-Feature
**What**: Each feature area (admin config, user management, user status) is a separate Flask Blueprint registered in `load()`.
**Where**: `jumpbox/__init__.py`
**Why**: CTFd plugin architecture requires explicit blueprint registration; separating concerns allows independent route namespacing.

### Provision-on-First-Visit
**What**: Jumpbox user accounts are created lazily when a user first visits `/jumpbox`, not when they register for the CTF.
**Where**: `jumpbox/__init__.py` - `user_status()` route handler
**Why**: Avoids provisioning accounts for users who never need jumpbox access; reduces load on the jumpbox server.

### Dual-Mode User Tracking
**What**: `JumpboxUsers` has both `team_id` and `user_id` (nullable). Only one is populated based on CTFd's teams/users mode.
**Where**: `jumpbox/models/models.py`
**Why**: CTFd supports both team-based and individual competitions; the plugin must work in either mode using `is_teams_mode()`.

### Startup-Only Config Hydration
**What**: SSM parameters are fetched once during `load()` and written to the database. No runtime refresh.
**Where**: `jumpbox/__init__.py` - `_apply_ssm_config()`
**Why**: Keeps the request path simple (always reads from DB); restart to pick up config changes.
