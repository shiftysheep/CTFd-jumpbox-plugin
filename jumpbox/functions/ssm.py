import logging
import os
import tempfile

logger = logging.getLogger(__name__)

JUMPBOX_SSM_KEY_PARAMETER = "JUMPBOX_SSM_KEY_PARAMETER"
JUMPBOX_SSM_HOSTNAME_PARAMETER = "JUMPBOX_SSM_HOSTNAME_PARAMETER"
JUMPBOX_SSM_USERNAME_PARAMETER = "JUMPBOX_SSM_USERNAME_PARAMETER"


def get_ssm_config():
    """Fetch jumpbox configuration from AWS SSM Parameter Store.

    Each of the three SSM env vars is optional and independent.
    Returns a dict with keys: private_key_path, hostname, username.
    Values are None for any parameter not configured or not fetched.
    """
    key_param = os.environ.get(JUMPBOX_SSM_KEY_PARAMETER)
    hostname_param = os.environ.get(JUMPBOX_SSM_HOSTNAME_PARAMETER)
    username_param = os.environ.get(JUMPBOX_SSM_USERNAME_PARAMETER)

    if not any([key_param, hostname_param, username_param]):
        return {"private_key_path": None, "hostname": None, "username": None}

    try:
        import boto3
    except ImportError:
        logger.error(
            "boto3 is not installed but JUMPBOX_SSM_* env vars are set. "
            "Install boto3 to use SSM integration."
        )
        return {"private_key_path": None, "hostname": None, "username": None}

    ssm = boto3.client("ssm")
    result = {"private_key_path": None, "hostname": None, "username": None}

    if key_param:
        try:
            response = ssm.get_parameter(Name=key_param, WithDecryption=True)
            private_key = response["Parameter"]["Value"]
            temppk = tempfile.NamedTemporaryFile(
                mode="w", dir="/tmp", delete=False, suffix=".pem"
            )
            temppk.write(private_key)
            temppk.close()
            os.chmod(temppk.name, 0o600)
            result["private_key_path"] = temppk.name
            logger.info("Loaded SSH private key from SSM parameter: %s", key_param)
        except Exception:
            logger.exception(
                "Failed to fetch SSH private key from SSM parameter: %s", key_param
            )

    if hostname_param:
        try:
            response = ssm.get_parameter(Name=hostname_param, WithDecryption=False)
            result["hostname"] = response["Parameter"]["Value"]
            logger.info("Loaded hostname from SSM parameter: %s", hostname_param)
        except Exception:
            logger.exception(
                "Failed to fetch hostname from SSM parameter: %s", hostname_param
            )

    if username_param:
        try:
            response = ssm.get_parameter(Name=username_param, WithDecryption=False)
            result["username"] = response["Parameter"]["Value"]
            logger.info("Loaded username from SSM parameter: %s", username_param)
        except Exception:
            logger.exception(
                "Failed to fetch username from SSM parameter: %s", username_param
            )

    return result
