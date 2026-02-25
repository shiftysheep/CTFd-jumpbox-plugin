# Known Limitations

## Security

### Command Injection Risk in User Provisioning
- **Issue**: SSH commands constructed via f-string interpolation in `functions.py` - `ssh_user_add()`. Username/password from `uuid4().hex` are safe today, but the function accepts arbitrary strings.
- **Impact**: If provisioning inputs were ever user-controlled, shell injection would be possible.
- **Workaround**: Current code generates credentials internally from UUID hex; never accepts user input for these fields.

### Plaintext Password Storage
- **Issue**: User passwords stored unencrypted in `JumpboxUsers.password` column.
- **Impact**: Database access exposes all jumpbox credentials.
- **Workaround**: None currently. Acceptable for short-lived CTF competitions.

### No SSH Host Key Verification
- **Issue**: `AutoAddPolicy()` accepts any host key without verification.
- **Impact**: Vulnerable to MITM attacks on the SSH connection to the jumpbox.
- **Workaround**: None. Mitigated by running on trusted internal networks.

## Operational

### Temp File Accumulation
- **Issue**: SSH key files written to `/tmp` with `delete=False` are never cleaned up by the plugin.
- **Impact**: Disk usage grows over restarts. Each SSM load or key upload creates a new temp file.
- **Workaround**: OS-level `/tmp` cleanup or manual deletion.

### No User Lifecycle Management
- **Issue**: Deleting a CTFd user does not automatically remove their jumpbox account. The admin must use the jumpbox user management UI separately.
- **Impact**: Orphaned accounts on the jumpbox server.
- **Workaround**: Manual cleanup via admin UI delete API.

### No Connection Pooling
- **Issue**: Each `ssh_user_add()` call opens a new SSH connection.
- **Impact**: Slow under concurrent provisioning; possible connection exhaustion.
- **Workaround**: None. Mitigated by lazy provisioning (one connection per user, on first visit).

## Testing

### No Test Suite
- **Issue**: No tests exist. No test framework configured.
- **Impact**: Changes must be verified manually against a running CTFd instance.
- **Workaround**: Manual verification with docker-compose environment.
