# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BIBLIOGRAPHIC_RESOURCES = "Bibliographic Resources"
    LOCAL_HOLDINGS_RESOURCES = "Local Holdings Resources"
    MEMBER_GENERAL_HOLDINGS = "Member General Holdings"
    MEMBER_SHARED_PRINT_HOLDINGS = "Member Shared Print Holdings"
