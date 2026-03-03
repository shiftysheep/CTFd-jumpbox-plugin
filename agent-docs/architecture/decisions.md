# Architecture Decisions

No formal ADRs documented. Implicit decisions discovered from codebase:

### File Path Storage for SSH Keys
Private keys are stored as filesystem paths (not key content) in the database. The actual key is written to a temp file in `/tmp` with `0o600` permissions. This couples database state to filesystem state but avoids storing sensitive material in the DB.

### Single Configuration Record
All JumpboxConfig queries use `filter_by(id=1)`. The plugin supports exactly one jumpbox. This is a deliberate simplification for the CTF use case where a single shared jumpbox is the norm.

### RSA-Only SSH Keys
`paramiko.RSAKey.from_private_key_file()` is used directly, limiting support to RSA keys. Ed25519/ECDSA keys will fail. Chosen for simplicity; paramiko does support other key types if needed.

### SSM Integration as Optional Overlay
SSM config loading was designed as opt-in (env vars trigger it) with lazy boto3 import. This keeps the plugin functional without AWS dependencies. SSM values overwrite DB config on each restart; manual UI changes persist only until next restart when SSM is active.

### Auto-Add SSH Host Key Policy
`paramiko.AutoAddPolicy()` is used instead of strict host key checking. Acceptable for internal CTF infrastructure but would be a security concern in production environments.
