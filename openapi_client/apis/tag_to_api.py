import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.bibliographic_resources_api import BibliographicResourcesApi
from openapi_client.apis.tags.local_holdings_resources_api import LocalHoldingsResourcesApi
from openapi_client.apis.tags.member_general_holdings_api import MemberGeneralHoldingsApi
from openapi_client.apis.tags.member_shared_print_holdings_api import MemberSharedPrintHoldingsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BIBLIOGRAPHIC_RESOURCES: BibliographicResourcesApi,
        TagValues.LOCAL_HOLDINGS_RESOURCES: LocalHoldingsResourcesApi,
        TagValues.MEMBER_GENERAL_HOLDINGS: MemberGeneralHoldingsApi,
        TagValues.MEMBER_SHARED_PRINT_HOLDINGS: MemberSharedPrintHoldingsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BIBLIOGRAPHIC_RESOURCES: BibliographicResourcesApi,
        TagValues.LOCAL_HOLDINGS_RESOURCES: LocalHoldingsResourcesApi,
        TagValues.MEMBER_GENERAL_HOLDINGS: MemberGeneralHoldingsApi,
        TagValues.MEMBER_SHARED_PRINT_HOLDINGS: MemberSharedPrintHoldingsApi,
    }
)
