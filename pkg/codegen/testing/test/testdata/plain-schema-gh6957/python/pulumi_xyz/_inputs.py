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
    'FooArgs',
]

@pulumi.input_type
class FooArgs:
    def __init__(__self__, *,
                 a: Optional[pulumi.Input[bool]] = None):
        FooArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            a=a,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             a: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if a is not None:
            _setter("a", a)

    @property
    @pulumi.getter
    def a(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "a")

    @a.setter
    def a(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "a", value)


