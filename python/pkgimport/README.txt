This package is a demo for chekcking statements of the type
from . import foo
from pkg import *
from ..base import base_foo
from .base import base_foo
Take care of cyclic dependencies. These tend to be fatal when importing.

