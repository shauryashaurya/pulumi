"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2016-2023, Pulumi Corporation.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pulumi.codegen.hcl_pb2
import pulumi.plugin_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AboutResponse(google.protobuf.message.Message):
    """AboutResponse returns runtime information about the language."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    EXECUTABLE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    executable: builtins.str
    """the primary executable for the runtime of this language."""
    version: builtins.str
    """the version of the runtime for this language."""
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """other information about this language."""
    def __init__(
        self,
        *,
        executable: builtins.str = ...,
        version: builtins.str = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["executable", b"executable", "metadata", b"metadata", "version", b"version"]) -> None: ...

global___AboutResponse = AboutResponse

@typing_extensions.final
class GetProgramDependenciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    TRANSITIVEDEPENDENCIES_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name."""
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program."""
    transitiveDependencies: builtins.bool
    """if transitive dependencies should be included in the result."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        transitiveDependencies: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["program", b"program", "project", b"project", "pwd", b"pwd", "transitiveDependencies", b"transitiveDependencies"]) -> None: ...

global___GetProgramDependenciesRequest = GetProgramDependenciesRequest

@typing_extensions.final
class DependencyInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the dependency."""
    version: builtins.str
    """The version of the dependency."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "version", b"version"]) -> None: ...

global___DependencyInfo = DependencyInfo

@typing_extensions.final
class GetProgramDependenciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEPENDENCIES_FIELD_NUMBER: builtins.int
    @property
    def dependencies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DependencyInfo]:
        """the dependencies of this program"""
    def __init__(
        self,
        *,
        dependencies: collections.abc.Iterable[global___DependencyInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dependencies", b"dependencies"]) -> None: ...

global___GetProgramDependenciesResponse = GetProgramDependenciesResponse

@typing_extensions.final
class GetRequiredPluginsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name."""
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["program", b"program", "project", b"project", "pwd", b"pwd"]) -> None: ...

global___GetRequiredPluginsRequest = GetRequiredPluginsRequest

@typing_extensions.final
class GetRequiredPluginsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PLUGINS_FIELD_NUMBER: builtins.int
    @property
    def plugins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.plugin_pb2.PluginDependency]:
        """a list of plugins required by this program."""
    def __init__(
        self,
        *,
        plugins: collections.abc.Iterable[pulumi.plugin_pb2.PluginDependency] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["plugins", b"plugins"]) -> None: ...

global___GetRequiredPluginsResponse = GetRequiredPluginsResponse

@typing_extensions.final
class RunRequest(google.protobuf.message.Message):
    """RunRequest asks the interpreter to execute a program."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConfigEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    PROJECT_FIELD_NUMBER: builtins.int
    STACK_FIELD_NUMBER: builtins.int
    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    DRYRUN_FIELD_NUMBER: builtins.int
    PARALLEL_FIELD_NUMBER: builtins.int
    MONITOR_ADDRESS_FIELD_NUMBER: builtins.int
    QUERYMODE_FIELD_NUMBER: builtins.int
    CONFIGSECRETKEYS_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    project: builtins.str
    """the project name."""
    stack: builtins.str
    """the name of the stack being deployed into."""
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program to execute."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any arguments to pass to the program."""
    @property
    def config(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """the configuration variables to apply before running."""
    dryRun: builtins.bool
    """true if we're only doing a dryrun (preview)."""
    parallel: builtins.int
    """the degree of parallelism for resource operations (<=1 for serial)."""
    monitor_address: builtins.str
    """the address for communicating back to the resource monitor."""
    queryMode: builtins.bool
    """true if we're only doing a query."""
    @property
    def configSecretKeys(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """the configuration keys that have secret values."""
    organization: builtins.str
    """the organization of the stack being deployed into."""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        stack: builtins.str = ...,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        config: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        dryRun: builtins.bool = ...,
        parallel: builtins.int = ...,
        monitor_address: builtins.str = ...,
        queryMode: builtins.bool = ...,
        configSecretKeys: collections.abc.Iterable[builtins.str] | None = ...,
        organization: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "config", b"config", "configSecretKeys", b"configSecretKeys", "dryRun", b"dryRun", "monitor_address", b"monitor_address", "organization", b"organization", "parallel", b"parallel", "program", b"program", "project", b"project", "pwd", b"pwd", "queryMode", b"queryMode", "stack", b"stack"]) -> None: ...

global___RunRequest = RunRequest

@typing_extensions.final
class RunResponse(google.protobuf.message.Message):
    """RunResponse is the response back from the interpreter/source back to the monitor."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    BAIL_FIELD_NUMBER: builtins.int
    error: builtins.str
    """An unhandled error if any occurred."""
    bail: builtins.bool
    """An error happened.  And it was reported to the user.  Work should stop immediately
    with nothing further to print to the user.  This corresponds to a "result.Bail()"
    value in the 'go' layer.
    """
    def __init__(
        self,
        *,
        error: builtins.str = ...,
        bail: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bail", b"bail", "error", b"error"]) -> None: ...

global___RunResponse = RunResponse

@typing_extensions.final
class InstallDependenciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIRECTORY_FIELD_NUMBER: builtins.int
    IS_TERMINAL_FIELD_NUMBER: builtins.int
    directory: builtins.str
    """the program's working directory."""
    is_terminal: builtins.bool
    """if we are running in a terminal and should use ANSI codes"""
    def __init__(
        self,
        *,
        directory: builtins.str = ...,
        is_terminal: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["directory", b"directory", "is_terminal", b"is_terminal"]) -> None: ...

global___InstallDependenciesRequest = InstallDependenciesRequest

@typing_extensions.final
class InstallDependenciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STDOUT_FIELD_NUMBER: builtins.int
    STDERR_FIELD_NUMBER: builtins.int
    stdout: builtins.bytes
    """a line of stdout text."""
    stderr: builtins.bytes
    """a line of stderr text."""
    def __init__(
        self,
        *,
        stdout: builtins.bytes = ...,
        stderr: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["stderr", b"stderr", "stdout", b"stdout"]) -> None: ...

global___InstallDependenciesResponse = InstallDependenciesResponse

@typing_extensions.final
class RunPluginRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PWD_FIELD_NUMBER: builtins.int
    PROGRAM_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    ENV_FIELD_NUMBER: builtins.int
    pwd: builtins.str
    """the program's working directory."""
    program: builtins.str
    """the path to the program to execute."""
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any arguments to pass to the program."""
    @property
    def env(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """any environment variables to set as part of the program."""
    def __init__(
        self,
        *,
        pwd: builtins.str = ...,
        program: builtins.str = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        env: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["args", b"args", "env", b"env", "program", b"program", "pwd", b"pwd"]) -> None: ...

global___RunPluginRequest = RunPluginRequest

@typing_extensions.final
class RunPluginResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STDOUT_FIELD_NUMBER: builtins.int
    STDERR_FIELD_NUMBER: builtins.int
    EXITCODE_FIELD_NUMBER: builtins.int
    stdout: builtins.bytes
    """a line of stdout text."""
    stderr: builtins.bytes
    """a line of stderr text."""
    exitcode: builtins.int
    """the exit code of the provider."""
    def __init__(
        self,
        *,
        stdout: builtins.bytes = ...,
        stderr: builtins.bytes = ...,
        exitcode: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["exitcode", b"exitcode", "output", b"output", "stderr", b"stderr", "stdout", b"stdout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["exitcode", b"exitcode", "output", b"output", "stderr", b"stderr", "stdout", b"stdout"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["output", b"output"]) -> typing_extensions.Literal["stdout", "stderr", "exitcode"] | None: ...

global___RunPluginResponse = RunPluginResponse

@typing_extensions.final
class GenerateProgramRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SourceEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SOURCE_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    @property
    def source(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """the PCL source of the project."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    def __init__(
        self,
        *,
        source: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        loader_target: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["loader_target", b"loader_target", "source", b"source"]) -> None: ...

global___GenerateProgramRequest = GenerateProgramRequest

@typing_extensions.final
class GenerateProgramResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class SourceEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DIAGNOSTICS_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    @property
    def diagnostics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.codegen.hcl_pb2.Diagnostic]:
        """any diagnostics from code generation."""
    @property
    def source(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]:
        """the generated program source code."""
    def __init__(
        self,
        *,
        diagnostics: collections.abc.Iterable[pulumi.codegen.hcl_pb2.Diagnostic] | None = ...,
        source: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["diagnostics", b"diagnostics", "source", b"source"]) -> None: ...

global___GenerateProgramResponse = GenerateProgramResponse

@typing_extensions.final
class GenerateProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LocalDependenciesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SOURCE_DIRECTORY_FIELD_NUMBER: builtins.int
    TARGET_DIRECTORY_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    STRICT_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    LOCAL_DEPENDENCIES_FIELD_NUMBER: builtins.int
    source_directory: builtins.str
    """the directory to generate the project from."""
    target_directory: builtins.str
    """the directory to generate the project in."""
    project: builtins.str
    """the JSON-encoded pulumi project file."""
    strict: builtins.bool
    """if PCL binding should be strict or not."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    @property
    def local_dependencies(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """local dependencies to use instead of using the package system. This is a map of package name to a local
        path of a language specific artifact to use for the SDK for that package.
        """
    def __init__(
        self,
        *,
        source_directory: builtins.str = ...,
        target_directory: builtins.str = ...,
        project: builtins.str = ...,
        strict: builtins.bool = ...,
        loader_target: builtins.str = ...,
        local_dependencies: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["loader_target", b"loader_target", "local_dependencies", b"local_dependencies", "project", b"project", "source_directory", b"source_directory", "strict", b"strict", "target_directory", b"target_directory"]) -> None: ...

global___GenerateProjectRequest = GenerateProjectRequest

@typing_extensions.final
class GenerateProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIAGNOSTICS_FIELD_NUMBER: builtins.int
    @property
    def diagnostics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[pulumi.codegen.hcl_pb2.Diagnostic]:
        """any diagnostics from code generation."""
    def __init__(
        self,
        *,
        diagnostics: collections.abc.Iterable[pulumi.codegen.hcl_pb2.Diagnostic] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["diagnostics", b"diagnostics"]) -> None: ...

global___GenerateProjectResponse = GenerateProjectResponse

@typing_extensions.final
class GeneratePackageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ExtraFilesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.bytes
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    DIRECTORY_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    EXTRA_FILES_FIELD_NUMBER: builtins.int
    LOADER_TARGET_FIELD_NUMBER: builtins.int
    directory: builtins.str
    """the directory to generate the package in."""
    schema: builtins.str
    """the JSON-encoded schema."""
    @property
    def extra_files(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.bytes]:
        """extra files to copy to the package output."""
    loader_target: builtins.str
    """The target of a codegen.LoaderServer to use for loading schemas."""
    def __init__(
        self,
        *,
        directory: builtins.str = ...,
        schema: builtins.str = ...,
        extra_files: collections.abc.Mapping[builtins.str, builtins.bytes] | None = ...,
        loader_target: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["directory", b"directory", "extra_files", b"extra_files", "loader_target", b"loader_target", "schema", b"schema"]) -> None: ...

global___GeneratePackageRequest = GeneratePackageRequest

@typing_extensions.final
class GeneratePackageResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GeneratePackageResponse = GeneratePackageResponse
