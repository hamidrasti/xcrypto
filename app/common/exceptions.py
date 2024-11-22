class ApplicationError(Exception):
    def __init__(self, message, extra=None, status=None):
        super().__init__(message)

        self.message = message or ""
        self.extra = extra or {}
        self.status = status or 400
