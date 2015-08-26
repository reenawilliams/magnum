# coding: utf-8

"""
Copyright 2015 SmartBear Software

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

from pprint import pformat
from six import iteritems


class V1GlusterfsVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'endpoints': 'str',
            'path': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'endpoints': 'endpoints',
            'path': 'path',
            'read_only': 'readOnly'
        }

        self._endpoints = None
        self._path = None
        self._read_only = None

    @property
    def endpoints(self):
        """
        Gets the endpoints of this V1GlusterfsVolumeSource.
        gluster hosts endpoints name; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :return: The endpoints of this V1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this V1GlusterfsVolumeSource.
        gluster hosts endpoints name; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :param endpoints: The endpoints of this V1GlusterfsVolumeSource.
        :type: str
        """
        self._endpoints = endpoints

    @property
    def path(self):
        """
        Gets the path of this V1GlusterfsVolumeSource.
        path to gluster volume; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :return: The path of this V1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1GlusterfsVolumeSource.
        path to gluster volume; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :param path: The path of this V1GlusterfsVolumeSource.
        :type: str
        """
        self._path = path

    @property
    def read_only(self):
        """
        Gets the read_only of this V1GlusterfsVolumeSource.
        glusterfs volume to be mounted with read-only permissions; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :return: The read_only of this V1GlusterfsVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1GlusterfsVolumeSource.
        glusterfs volume to be mounted with read-only permissions; see http://releases.k8s.io/v1.0.4/examples/glusterfs/README.md#create-a-pod

        :param read_only: The read_only of this V1GlusterfsVolumeSource.
        :type: bool
        """
        self._read_only = read_only

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
