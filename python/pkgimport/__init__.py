"""
A test project to check statements such as 
from pkg import *
from . import subpkg
"""

from .base import base_f1
import subpkg

__all__ = ['subpkg','foo']
