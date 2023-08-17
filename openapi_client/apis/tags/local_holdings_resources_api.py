# coding: utf-8

"""
    WorldCat Search API v. 2

    Searching of WorldCat  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.my_holdings_control_number.get import RetrieveLhr
from openapi_client.paths.my_holdings.get import SearchLhr
from openapi_client.paths.retained_holdings.get import SearchRetrainedLhr


class LocalHoldingsResourcesApi(
    RetrieveLhr,
    SearchLhr,
    SearchRetrainedLhr,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
