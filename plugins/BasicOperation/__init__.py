try:
    from .action import BasicOperations
    BasicOperations().register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))