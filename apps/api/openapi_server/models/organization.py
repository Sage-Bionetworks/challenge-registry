# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.organization_all_of import OrganizationAllOf
from openapi_server.models.organization_create_request import OrganizationCreateRequest
from openapi_server.models.organization_create_response import OrganizationCreateResponse
from openapi_server import util

from openapi_server.models.organization_all_of import OrganizationAllOf  # noqa: E501
from openapi_server.models.organization_create_request import OrganizationCreateRequest  # noqa: E501
from openapi_server.models.organization_create_response import OrganizationCreateResponse  # noqa: E501

class Organization(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, login=None, email=None, name=None, avatar_url=None, website_url=None, description=None, created_at=None, updated_at=None, type=None):  # noqa: E501
        """Organization - a model defined in OpenAPI

        :param id: The id of this Organization.  # noqa: E501
        :type id: str
        :param login: The login of this Organization.  # noqa: E501
        :type login: str
        :param email: The email of this Organization.  # noqa: E501
        :type email: str
        :param name: The name of this Organization.  # noqa: E501
        :type name: str
        :param avatar_url: The avatar_url of this Organization.  # noqa: E501
        :type avatar_url: str
        :param website_url: The website_url of this Organization.  # noqa: E501
        :type website_url: str
        :param description: The description of this Organization.  # noqa: E501
        :type description: str
        :param created_at: The created_at of this Organization.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Organization.  # noqa: E501
        :type updated_at: datetime
        :param type: The type of this Organization.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'id': str,
            'login': str,
            'email': str,
            'name': str,
            'avatar_url': str,
            'website_url': str,
            'description': str,
            'created_at': datetime,
            'updated_at': datetime,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'login': 'login',
            'email': 'email',
            'name': 'name',
            'avatar_url': 'avatarUrl',
            'website_url': 'websiteUrl',
            'description': 'description',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'type': 'type'
        }

        self._id = id
        self._login = login
        self._email = email
        self._name = name
        self._avatar_url = avatar_url
        self._website_url = website_url
        self._description = description
        self._created_at = created_at
        self._updated_at = updated_at
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Organization':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Organization of this Organization.  # noqa: E501
        :rtype: Organization
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Organization.

        The unique identifier of an account  # noqa: E501

        :return: The id of this Organization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.

        The unique identifier of an account  # noqa: E501

        :param id: The id of this Organization.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def login(self):
        """Gets the login of this Organization.


        :return: The login of this Organization.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this Organization.


        :param login: The login of this Organization.
        :type login: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def email(self):
        """Gets the email of this Organization.

        An email address  # noqa: E501

        :return: The email of this Organization.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Organization.

        An email address  # noqa: E501

        :param email: The email of this Organization.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this Organization.


        :return: The name of this Organization.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organization.


        :param name: The name of this Organization.
        :type name: str
        """

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Organization.


        :return: The avatar_url of this Organization.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Organization.


        :param avatar_url: The avatar_url of this Organization.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def website_url(self):
        """Gets the website_url of this Organization.


        :return: The website_url of this Organization.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this Organization.


        :param website_url: The website_url of this Organization.
        :type website_url: str
        """

        self._website_url = website_url

    @property
    def description(self):
        """Gets the description of this Organization.


        :return: The description of this Organization.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organization.


        :param description: The description of this Organization.
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Organization.


        :return: The created_at of this Organization.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Organization.


        :param created_at: The created_at of this Organization.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Organization.


        :return: The updated_at of this Organization.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Organization.


        :param updated_at: The updated_at of this Organization.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this Organization.


        :return: The type of this Organization.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Organization.


        :param type: The type of this Organization.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
