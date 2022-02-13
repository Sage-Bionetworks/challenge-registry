# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class OrgMembershipCreateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, state=None, role=None, organization_id=None, user_id=None):  # noqa: E501
        """OrgMembershipCreateRequest - a model defined in OpenAPI

        :param state: The state of this OrgMembershipCreateRequest.  # noqa: E501
        :type state: str
        :param role: The role of this OrgMembershipCreateRequest.  # noqa: E501
        :type role: str
        :param organization_id: The organization_id of this OrgMembershipCreateRequest.  # noqa: E501
        :type organization_id: str
        :param user_id: The user_id of this OrgMembershipCreateRequest.  # noqa: E501
        :type user_id: str
        """
        self.openapi_types = {
            'state': str,
            'role': str,
            'organization_id': str,
            'user_id': str
        }

        self.attribute_map = {
            'state': 'state',
            'role': 'role',
            'organization_id': 'organizationId',
            'user_id': 'userId'
        }

        self._state = state
        self._role = role
        self._organization_id = organization_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'OrgMembershipCreateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrgMembershipCreateRequest of this OrgMembershipCreateRequest.  # noqa: E501
        :rtype: OrgMembershipCreateRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self):
        """Gets the state of this OrgMembershipCreateRequest.

        The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation.  # noqa: E501

        :return: The state of this OrgMembershipCreateRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OrgMembershipCreateRequest.

        The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation.  # noqa: E501

        :param state: The state of this OrgMembershipCreateRequest.
        :type state: str
        """
        allowed_values = ["active", "pending"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def role(self):
        """Gets the role of this OrgMembershipCreateRequest.

        The user's membership type in the organization.  # noqa: E501

        :return: The role of this OrgMembershipCreateRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OrgMembershipCreateRequest.

        The user's membership type in the organization.  # noqa: E501

        :param role: The role of this OrgMembershipCreateRequest.
        :type role: str
        """
        allowed_values = ["admin", "member"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def organization_id(self):
        """Gets the organization_id of this OrgMembershipCreateRequest.

        The unique identifier of an organization  # noqa: E501

        :return: The organization_id of this OrgMembershipCreateRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this OrgMembershipCreateRequest.

        The unique identifier of an organization  # noqa: E501

        :param organization_id: The organization_id of this OrgMembershipCreateRequest.
        :type organization_id: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this OrgMembershipCreateRequest.

        The unique identifier of a user  # noqa: E501

        :return: The user_id of this OrgMembershipCreateRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this OrgMembershipCreateRequest.

        The unique identifier of a user  # noqa: E501

        :param user_id: The user_id of this OrgMembershipCreateRequest.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id
