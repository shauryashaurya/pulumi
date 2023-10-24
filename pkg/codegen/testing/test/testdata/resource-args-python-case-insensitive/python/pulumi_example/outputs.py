# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'Pet',
]

@pulumi.output_type
class Pet(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        Pet._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


