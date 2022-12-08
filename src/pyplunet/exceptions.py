class PlunetException(Exception):
    pass


class PlunetAuthFailed(PlunetException):
    pass


class PlunetOrderNotFound(PlunetException):
    pass


class NoPlunetSession(PlunetException):
    pass
