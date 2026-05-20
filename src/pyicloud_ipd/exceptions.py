class PyiCloudException(Exception):
    """Generic iCloud exception."""

    pass


# API
class PyiCloudAPIResponseException(PyiCloudException):
    """iCloud response exception."""

    def __init__(self, reason: str, code: str | None = None):
        self.reason = reason
        self.code = code
        message = reason or ""
        if code:
            message += f" ({code})"

        super().__init__(message)


class PyiCloudServiceNotActivatedException(PyiCloudAPIResponseException):
    """iCloud service not activated exception."""

    pass


class PyiCloudServiceUnavailableException(PyiCloudException):
    """iCloud service not available (503)"""

    pass


class PyiCloudConnectionErrorException(PyiCloudException):
    """Cannot connect to Apple iCloud service"""

    pass


# Login
class PyiCloudFailedLoginException(PyiCloudException):
    """iCloud failed login exception."""

    pass


class PyiCloudFailedMFAException(PyiCloudException):
    """iCloud failed validating multi-factor auth exception."""

    pass


class PyiCloud2SARequiredException(PyiCloudException):
    """iCloud 2SA required exception."""

    def __init__(self, apple_id: str):
        message = f"Two-step authentication required for account: {apple_id}"
        super().__init__(message)


class PyiCloudNoStoredPasswordAvailableException(PyiCloudException):
    """iCloud no stored password exception."""

    pass


# Webservice specific
class PyiCloudNoDevicesException(PyiCloudException):
    """iCloud no device exception."""

    pass


# PyiCloudConnectionException is actively used in base.py for domain mismatch
class PyiCloudConnectionException(PyiCloudException):
    pass
