# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'SsisEnvironmentReferenceResponse',
    'SsisEnvironmentResponse',
    'SsisFolderResponse',
    'SsisPackageResponse',
    'SsisParameterResponse',
    'SsisProjectResponse',
    'SsisVariableResponse',
    'StorageAccountKeyResponse',
]

@pulumi.output_type
class SsisEnvironmentReferenceResponse(dict):
    """
    Ssis environment reference.
    """
    def __init__(__self__, *,
                 environment_folder_name: Optional[str] = None,
                 environment_name: Optional[str] = None,
                 id: Optional[float] = None,
                 reference_type: Optional[str] = None):
        """
        Ssis environment reference.
        :param str environment_folder_name: Environment folder name.
        :param str environment_name: Environment name.
        :param float id: Environment reference id.
        :param str reference_type: Reference type
        """
        SsisEnvironmentReferenceResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            environment_folder_name=environment_folder_name,
            environment_name=environment_name,
            id=id,
            reference_type=reference_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             environment_folder_name: Optional[str] = None,
             environment_name: Optional[str] = None,
             id: Optional[float] = None,
             reference_type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if environment_folder_name is None and 'environmentFolderName' in kwargs:
            environment_folder_name = kwargs['environmentFolderName']
        if environment_name is None and 'environmentName' in kwargs:
            environment_name = kwargs['environmentName']
        if reference_type is None and 'referenceType' in kwargs:
            reference_type = kwargs['referenceType']

        if environment_folder_name is not None:
            _setter("environment_folder_name", environment_folder_name)
        if environment_name is not None:
            _setter("environment_name", environment_name)
        if id is not None:
            _setter("id", id)
        if reference_type is not None:
            _setter("reference_type", reference_type)

    @property
    @pulumi.getter(name="environmentFolderName")
    def environment_folder_name(self) -> Optional[str]:
        """
        Environment folder name.
        """
        return pulumi.get(self, "environment_folder_name")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[str]:
        """
        Environment name.
        """
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Environment reference id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="referenceType")
    def reference_type(self) -> Optional[str]:
        """
        Reference type
        """
        return pulumi.get(self, "reference_type")


@pulumi.output_type
class SsisEnvironmentResponse(dict):
    """
    Ssis environment.
    """
    def __init__(__self__, *,
                 type: str,
                 description: Optional[str] = None,
                 folder_id: Optional[float] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None,
                 variables: Optional[Sequence['outputs.SsisVariableResponse']] = None):
        """
        Ssis environment.
        :param str type: The type of SSIS object metadata.
               Expected value is 'Environment'.
        :param str description: Metadata description.
        :param float folder_id: Folder id which contains environment.
        :param float id: Metadata id.
        :param str name: Metadata name.
        :param Sequence['SsisVariableResponse'] variables: Variable in environment
        """
        SsisEnvironmentResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            description=description,
            folder_id=folder_id,
            id=id,
            name=name,
            variables=variables,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[str] = None,
             description: Optional[str] = None,
             folder_id: Optional[float] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             variables: Optional[Sequence['outputs.SsisVariableResponse']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if type is None:
            raise TypeError("Missing 'type' argument")
        if folder_id is None and 'folderId' in kwargs:
            folder_id = kwargs['folderId']

        _setter("type", 'Environment')
        if description is not None:
            _setter("description", description)
        if folder_id is not None:
            _setter("folder_id", folder_id)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if variables is not None:
            _setter("variables", variables)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of SSIS object metadata.
        Expected value is 'Environment'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Metadata description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[float]:
        """
        Folder id which contains environment.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Metadata id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def variables(self) -> Optional[Sequence['outputs.SsisVariableResponse']]:
        """
        Variable in environment
        """
        return pulumi.get(self, "variables")


@pulumi.output_type
class SsisFolderResponse(dict):
    """
    Ssis folder.
    """
    def __init__(__self__, *,
                 type: str,
                 description: Optional[str] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None):
        """
        Ssis folder.
        :param str type: The type of SSIS object metadata.
               Expected value is 'Folder'.
        :param str description: Metadata description.
        :param float id: Metadata id.
        :param str name: Metadata name.
        """
        SsisFolderResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            description=description,
            id=id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[str] = None,
             description: Optional[str] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if type is None:
            raise TypeError("Missing 'type' argument")

        _setter("type", 'Folder')
        if description is not None:
            _setter("description", description)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of SSIS object metadata.
        Expected value is 'Folder'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Metadata description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Metadata id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SsisPackageResponse(dict):
    """
    Ssis Package.
    """
    def __init__(__self__, *,
                 type: str,
                 description: Optional[str] = None,
                 folder_id: Optional[float] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None,
                 parameters: Optional[Sequence['outputs.SsisParameterResponse']] = None,
                 project_id: Optional[float] = None,
                 project_version: Optional[float] = None):
        """
        Ssis Package.
        :param str type: The type of SSIS object metadata.
               Expected value is 'Package'.
        :param str description: Metadata description.
        :param float folder_id: Folder id which contains package.
        :param float id: Metadata id.
        :param str name: Metadata name.
        :param Sequence['SsisParameterResponse'] parameters: Parameters in package
        :param float project_id: Project id which contains package.
        :param float project_version: Project version which contains package.
        """
        SsisPackageResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            description=description,
            folder_id=folder_id,
            id=id,
            name=name,
            parameters=parameters,
            project_id=project_id,
            project_version=project_version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[str] = None,
             description: Optional[str] = None,
             folder_id: Optional[float] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             parameters: Optional[Sequence['outputs.SsisParameterResponse']] = None,
             project_id: Optional[float] = None,
             project_version: Optional[float] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if type is None:
            raise TypeError("Missing 'type' argument")
        if folder_id is None and 'folderId' in kwargs:
            folder_id = kwargs['folderId']
        if project_id is None and 'projectId' in kwargs:
            project_id = kwargs['projectId']
        if project_version is None and 'projectVersion' in kwargs:
            project_version = kwargs['projectVersion']

        _setter("type", 'Package')
        if description is not None:
            _setter("description", description)
        if folder_id is not None:
            _setter("folder_id", folder_id)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if parameters is not None:
            _setter("parameters", parameters)
        if project_id is not None:
            _setter("project_id", project_id)
        if project_version is not None:
            _setter("project_version", project_version)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of SSIS object metadata.
        Expected value is 'Package'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Metadata description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[float]:
        """
        Folder id which contains package.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Metadata id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.SsisParameterResponse']]:
        """
        Parameters in package
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[float]:
        """
        Project id which contains package.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectVersion")
    def project_version(self) -> Optional[float]:
        """
        Project version which contains package.
        """
        return pulumi.get(self, "project_version")


@pulumi.output_type
class SsisParameterResponse(dict):
    """
    Ssis parameter.
    """
    def __init__(__self__, *,
                 data_type: Optional[str] = None,
                 default_value: Optional[str] = None,
                 description: Optional[str] = None,
                 design_default_value: Optional[str] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None,
                 required: Optional[bool] = None,
                 sensitive: Optional[bool] = None,
                 sensitive_default_value: Optional[str] = None,
                 value_set: Optional[bool] = None,
                 value_type: Optional[str] = None,
                 variable: Optional[str] = None):
        """
        Ssis parameter.
        :param str data_type: Parameter type.
        :param str default_value: Default value of parameter.
        :param str description: Parameter description.
        :param str design_default_value: Design default value of parameter.
        :param float id: Parameter id.
        :param str name: Parameter name.
        :param bool required: Whether parameter is required.
        :param bool sensitive: Whether parameter is sensitive.
        :param str sensitive_default_value: Default sensitive value of parameter.
        :param bool value_set: Parameter value set.
        :param str value_type: Parameter value type.
        :param str variable: Parameter reference variable.
        """
        SsisParameterResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_type=data_type,
            default_value=default_value,
            description=description,
            design_default_value=design_default_value,
            id=id,
            name=name,
            required=required,
            sensitive=sensitive,
            sensitive_default_value=sensitive_default_value,
            value_set=value_set,
            value_type=value_type,
            variable=variable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_type: Optional[str] = None,
             default_value: Optional[str] = None,
             description: Optional[str] = None,
             design_default_value: Optional[str] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             required: Optional[bool] = None,
             sensitive: Optional[bool] = None,
             sensitive_default_value: Optional[str] = None,
             value_set: Optional[bool] = None,
             value_type: Optional[str] = None,
             variable: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if data_type is None and 'dataType' in kwargs:
            data_type = kwargs['dataType']
        if default_value is None and 'defaultValue' in kwargs:
            default_value = kwargs['defaultValue']
        if design_default_value is None and 'designDefaultValue' in kwargs:
            design_default_value = kwargs['designDefaultValue']
        if sensitive_default_value is None and 'sensitiveDefaultValue' in kwargs:
            sensitive_default_value = kwargs['sensitiveDefaultValue']
        if value_set is None and 'valueSet' in kwargs:
            value_set = kwargs['valueSet']
        if value_type is None and 'valueType' in kwargs:
            value_type = kwargs['valueType']

        if data_type is not None:
            _setter("data_type", data_type)
        if default_value is not None:
            _setter("default_value", default_value)
        if description is not None:
            _setter("description", description)
        if design_default_value is not None:
            _setter("design_default_value", design_default_value)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if required is not None:
            _setter("required", required)
        if sensitive is not None:
            _setter("sensitive", sensitive)
        if sensitive_default_value is not None:
            _setter("sensitive_default_value", sensitive_default_value)
        if value_set is not None:
            _setter("value_set", value_set)
        if value_type is not None:
            _setter("value_type", value_type)
        if variable is not None:
            _setter("variable", variable)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[str]:
        """
        Parameter type.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[str]:
        """
        Default value of parameter.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Parameter description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="designDefaultValue")
    def design_default_value(self) -> Optional[str]:
        """
        Design default value of parameter.
        """
        return pulumi.get(self, "design_default_value")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Parameter id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Parameter name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def required(self) -> Optional[bool]:
        """
        Whether parameter is required.
        """
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def sensitive(self) -> Optional[bool]:
        """
        Whether parameter is sensitive.
        """
        return pulumi.get(self, "sensitive")

    @property
    @pulumi.getter(name="sensitiveDefaultValue")
    def sensitive_default_value(self) -> Optional[str]:
        """
        Default sensitive value of parameter.
        """
        return pulumi.get(self, "sensitive_default_value")

    @property
    @pulumi.getter(name="valueSet")
    def value_set(self) -> Optional[bool]:
        """
        Parameter value set.
        """
        return pulumi.get(self, "value_set")

    @property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[str]:
        """
        Parameter value type.
        """
        return pulumi.get(self, "value_type")

    @property
    @pulumi.getter
    def variable(self) -> Optional[str]:
        """
        Parameter reference variable.
        """
        return pulumi.get(self, "variable")


@pulumi.output_type
class SsisProjectResponse(dict):
    """
    Ssis project.
    """
    def __init__(__self__, *,
                 type: str,
                 description: Optional[str] = None,
                 environment_refs: Optional[Sequence['outputs.SsisEnvironmentReferenceResponse']] = None,
                 folder_id: Optional[float] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None,
                 parameters: Optional[Sequence['outputs.SsisParameterResponse']] = None,
                 version: Optional[float] = None):
        """
        Ssis project.
        :param str type: The type of SSIS object metadata.
               Expected value is 'Project'.
        :param str description: Metadata description.
        :param Sequence['SsisEnvironmentReferenceResponse'] environment_refs: Environment reference in project
        :param float folder_id: Folder id which contains project.
        :param float id: Metadata id.
        :param str name: Metadata name.
        :param Sequence['SsisParameterResponse'] parameters: Parameters in project
        :param float version: Project version.
        """
        SsisProjectResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            description=description,
            environment_refs=environment_refs,
            folder_id=folder_id,
            id=id,
            name=name,
            parameters=parameters,
            version=version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[str] = None,
             description: Optional[str] = None,
             environment_refs: Optional[Sequence['outputs.SsisEnvironmentReferenceResponse']] = None,
             folder_id: Optional[float] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             parameters: Optional[Sequence['outputs.SsisParameterResponse']] = None,
             version: Optional[float] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if type is None:
            raise TypeError("Missing 'type' argument")
        if environment_refs is None and 'environmentRefs' in kwargs:
            environment_refs = kwargs['environmentRefs']
        if folder_id is None and 'folderId' in kwargs:
            folder_id = kwargs['folderId']

        _setter("type", 'Project')
        if description is not None:
            _setter("description", description)
        if environment_refs is not None:
            _setter("environment_refs", environment_refs)
        if folder_id is not None:
            _setter("folder_id", folder_id)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if parameters is not None:
            _setter("parameters", parameters)
        if version is not None:
            _setter("version", version)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of SSIS object metadata.
        Expected value is 'Project'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Metadata description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="environmentRefs")
    def environment_refs(self) -> Optional[Sequence['outputs.SsisEnvironmentReferenceResponse']]:
        """
        Environment reference in project
        """
        return pulumi.get(self, "environment_refs")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[float]:
        """
        Folder id which contains project.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Metadata id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.SsisParameterResponse']]:
        """
        Parameters in project
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def version(self) -> Optional[float]:
        """
        Project version.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class SsisVariableResponse(dict):
    """
    Ssis variable.
    """
    def __init__(__self__, *,
                 data_type: Optional[str] = None,
                 description: Optional[str] = None,
                 id: Optional[float] = None,
                 name: Optional[str] = None,
                 sensitive: Optional[bool] = None,
                 sensitive_value: Optional[str] = None,
                 value: Optional[str] = None):
        """
        Ssis variable.
        :param str data_type: Variable type.
        :param str description: Variable description.
        :param float id: Variable id.
        :param str name: Variable name.
        :param bool sensitive: Whether variable is sensitive.
        :param str sensitive_value: Variable sensitive value.
        :param str value: Variable value.
        """
        SsisVariableResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            data_type=data_type,
            description=description,
            id=id,
            name=name,
            sensitive=sensitive,
            sensitive_value=sensitive_value,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             data_type: Optional[str] = None,
             description: Optional[str] = None,
             id: Optional[float] = None,
             name: Optional[str] = None,
             sensitive: Optional[bool] = None,
             sensitive_value: Optional[str] = None,
             value: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if data_type is None and 'dataType' in kwargs:
            data_type = kwargs['dataType']
        if sensitive_value is None and 'sensitiveValue' in kwargs:
            sensitive_value = kwargs['sensitiveValue']

        if data_type is not None:
            _setter("data_type", data_type)
        if description is not None:
            _setter("description", description)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if sensitive is not None:
            _setter("sensitive", sensitive)
        if sensitive_value is not None:
            _setter("sensitive_value", sensitive_value)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[str]:
        """
        Variable type.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Variable description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[float]:
        """
        Variable id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Variable name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sensitive(self) -> Optional[bool]:
        """
        Whether variable is sensitive.
        """
        return pulumi.get(self, "sensitive")

    @property
    @pulumi.getter(name="sensitiveValue")
    def sensitive_value(self) -> Optional[str]:
        """
        Variable sensitive value.
        """
        return pulumi.get(self, "sensitive_value")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Variable value.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class StorageAccountKeyResponse(dict):
    """
    An access key for the storage account.
    """
    def __init__(__self__, *,
                 creation_time: str,
                 key_name: str,
                 permissions: str,
                 value: str):
        """
        An access key for the storage account.
        :param str creation_time: Creation time of the key, in round trip date format.
        :param str key_name: Name of the key.
        :param str permissions: Permissions for the key -- read-only or full permissions.
        :param str value: Base 64-encoded value of the key.
        """
        StorageAccountKeyResponse._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            creation_time=creation_time,
            key_name=key_name,
            permissions=permissions,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             creation_time: Optional[str] = None,
             key_name: Optional[str] = None,
             permissions: Optional[str] = None,
             value: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if creation_time is None and 'creationTime' in kwargs:
            creation_time = kwargs['creationTime']
        if creation_time is None:
            raise TypeError("Missing 'creation_time' argument")
        if key_name is None and 'keyName' in kwargs:
            key_name = kwargs['keyName']
        if key_name is None:
            raise TypeError("Missing 'key_name' argument")
        if permissions is None:
            raise TypeError("Missing 'permissions' argument")
        if value is None:
            raise TypeError("Missing 'value' argument")

        _setter("creation_time", creation_time)
        _setter("key_name", key_name)
        _setter("permissions", permissions)
        _setter("value", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Creation time of the key, in round trip date format.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        Name of the key.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def permissions(self) -> str:
        """
        Permissions for the key -- read-only or full permissions.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Base 64-encoded value of the key.
        """
        return pulumi.get(self, "value")


