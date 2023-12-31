# coding: utf-8

"""
    WorldCat Search API v. 2

    Searching of WorldCat  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.bibs_detailed_holdings.get import FindBibDetailedHoldings
from openapi_client.paths.bibs_holdings.get import FindBibHoldings
from openapi_client.paths.bibs_summary_holdings.get import FindBibSummaryHoldings


class MemberGeneralHoldingsApi(
    FindBibDetailedHoldings,
    FindBibHoldings,
    FindBibSummaryHoldings,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
