from .global_settings import *

try:
    from .local_setting import *
except ImportError:
    pass
