# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.challenge_readme_all_of import ChallengeReadmeAllOf
from openapi_server.models.challenge_readme_create_request import ChallengeReadmeCreateRequest
from openapi_server.models.challenge_readme_create_response import ChallengeReadmeCreateResponse
from openapi_server import util

from openapi_server.models.challenge_readme_all_of import ChallengeReadmeAllOf  # noqa: E501
from openapi_server.models.challenge_readme_create_request import ChallengeReadmeCreateRequest  # noqa: E501
from openapi_server.models.challenge_readme_create_response import ChallengeReadmeCreateResponse  # noqa: E501

class ChallengeReadme(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, text=None, created_at=None, updated_at=None):  # noqa: E501
        """ChallengeReadme - a model defined in OpenAPI

        :param id: The id of this ChallengeReadme.  # noqa: E501
        :type id: str
        :param text: The text of this ChallengeReadme.  # noqa: E501
        :type text: str
        :param created_at: The created_at of this ChallengeReadme.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this ChallengeReadme.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'id': str,
            'text': str,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt'
        }

        self._id = id
        self._text = text
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'ChallengeReadme':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChallengeReadme of this ChallengeReadme.  # noqa: E501
        :rtype: ChallengeReadme
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ChallengeReadme.

        The unique identifier of a challenge README  # noqa: E501

        :return: The id of this ChallengeReadme.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChallengeReadme.

        The unique identifier of a challenge README  # noqa: E501

        :param id: The id of this ChallengeReadme.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def text(self):
        """Gets the text of this ChallengeReadme.


        :return: The text of this ChallengeReadme.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ChallengeReadme.


        :param text: The text of this ChallengeReadme.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def created_at(self):
        """Gets the created_at of this ChallengeReadme.


        :return: The created_at of this ChallengeReadme.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ChallengeReadme.


        :param created_at: The created_at of this ChallengeReadme.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ChallengeReadme.


        :return: The updated_at of this ChallengeReadme.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ChallengeReadme.


        :param updated_at: The updated_at of this ChallengeReadme.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
