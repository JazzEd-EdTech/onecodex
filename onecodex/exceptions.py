class OneCodexException(Exception):
    pass


class MethodNotSupported(OneCodexException):
    """
    The object does not support this operation.
    """
    pass


class PermissionDenied(OneCodexException):
    pass


class ServerError(OneCodexException):
    pass


class UnboundObject(OneCodexException):
    """
    To use against the One Codex server, all classes must be derived from an Api instance.
    """
    pass