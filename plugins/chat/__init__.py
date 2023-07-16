try:
    from .chat_action import ChatPlugin
    ChatPlugin().register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))