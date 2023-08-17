<a id="__pageTop"></a>
# openapi_client.apis.tags.member_general_holdings_api.MemberGeneralHoldingsApi

All URIs are relative to *https://americas.discovery.api.oclc.org/worldcat/search/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_bib_detailed_holdings**](#find_bib_detailed_holdings) | **get** /bibs-detailed-holdings | Find detailed info of member holdings for a known item
[**find_bib_holdings**](#find_bib_holdings) | **get** /bibs-holdings | Find member holdings for a known item
[**find_bib_summary_holdings**](#find_bib_summary_holdings) | **get** /bibs-summary-holdings | Get summary of holdings for a known item

# **find_bib_detailed_holdings**
<a id="find_bib_detailed_holdings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_bib_detailed_holdings()

Find detailed info of member holdings for a known item

Given a known item, search member library holdings for detailed information

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import member_general_holdings_api
from pprint import pprint
# Defining the host is optional and defaults to https://americas.discovery.api.oclc.org/worldcat/search/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = member_general_holdings_api.MemberGeneralHoldingsApi(api_client)

    # example passing only optional values
    query_params = {
        'oclcNumber': 41266045,
        'isbn': "0439136350",
        'issn': "0099-1333",
        'heldByGroup': "ASRL",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Find detailed info of member holdings for a known item
        api_response = api_instance.find_bib_detailed_holdings(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MemberGeneralHoldingsApi->find_bib_detailed_holdings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
oclcNumber | OclcNumberSchema | | optional
isbn | IsbnSchema | | optional
issn | IssnSchema | | optional
heldByGroup | HeldByGroupSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

# IsbnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IssnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeldByGroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeldBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeldBySymbolSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | institution OCLC Symbol. Special characters need to be encoded properly. | 

# HeldByInstitutionIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_bib_detailed_holdings.ApiResponseFor200) | Successful search
400 | [ApiResponseFor400](#find_bib_detailed_holdings.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#find_bib_detailed_holdings.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#find_bib_detailed_holdings.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#find_bib_detailed_holdings.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#find_bib_detailed_holdings.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#find_bib_detailed_holdings.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### find_bib_detailed_holdings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**numberOfRecords** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[briefRecords](#briefRecords)** | list, tuple,  | tuple,  |  | [optional] 
**[searchFacets](#searchFacets)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# briefRecords

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str,  | str,  | machine readable date 008 | 
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer
**creator** | str,  | str,  | List of creators as single string | 
**edition** | str,  | str,  | Edition Statement [v250sa] | 
**publisher** | str,  | str,  |  | 
**language** | str,  | str,  | Language of the item [v041sa,j] | 
**title** | str,  | str,  | Linked [v880sa,b] if present or [v245sa,b] | 
**generalFormat** | str,  | str,  | General Format Type [Admin/OCLCDef/StdRT] | [optional] must be one of ["Archv", "ArtChapter", "AudioBook", "Book", "CompFile", "Encyc", "Game", "Image", "IntMM", "Jrnl", "Kit", "Map", "MsScr", "Music", "News", "Object", "Snd", "Toy", "Video", "Vis", "Web", ] 
**specificFormat** | str,  | str,  | Specific Format Type [Admin/OCLCDef/StdRT2] | [optional] must be one of ["2D", "Artcl", "Bluray", "Braille", "Cassette", "CD", "Chptr", "Continuing", "Digital", "DVD", "Encyc", "Film", "LargePrint", "LP", "Mic", "mss", "PrintBook", "rec", "Thsis", "VHS", ] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[mergedOclcNumbers](#mergedOclcNumbers)** | list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | [optional] 
**[catalogingInfo](#catalogingInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[institutionHolding](#institutionHolding)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# isbns

International Standard Book Number [v020sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Book Number [v020sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issns

International Standard Serial Numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Serial Numbers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | International Standard Serial Number [v022sal v700,v710,v711,v773,v776,v777,v780,v785 - sx] | 

# mergedOclcNumbers

Merged OCLC numbers [v019sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# catalogingInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**catalogingAgency** | str,  | str,  | Cataloging Agency [v040/sa] | [optional] 
**transcribingAgency** | str,  | str,  | Transcribing Agency [v040/sc] | [optional] 
**catalogingLanguage** | str,  | str,  | Language record was cataloged in [v040sb] | [optional] 
**levelOfCataloging** | str,  | str,  | Level of cataloging [LDR position 5] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# institutionHolding

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**totalHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings for this item [Holdings/TotalLibCount || FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalWorksHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings in the workset [FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalEditions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of editions in the workgroup | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | list, tuple,  | tuple,  |  | 
[one_of_1](#one_of_1) | list, tuple,  | tuple,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | Country of holding institution [Holdings/Library/Country] | [optional] 
**state** | str,  | str,  | State of holding institution [Holdings/Library/State] | [optional] 
**oclcSymbol** | str,  | str,  | Oclc Symbol of holding institution [Holdings/Library/InstSym] | [optional] 
**registryId** | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | [optional] 
**institutionName** | str,  | str,  | Name of holding institution [Holdings/Library/InstName] | [optional] 
**alsoCalled** | str,  | str,  | Some name the library might also be called | [optional] 
**[address](#address)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**institutionType** | str,  | str,  | The type of institution | [optional] must be one of ["ACADEMIC", "PUBLIC", "REGIONAL_OR_NATIONAL", "OTHER", "CORPORATE_SPECIAL_LIBRARY", "HEALTH", "MUSEUM_OR_ARCHIVES", "LAW", "MUSIC", "LIBRARY_NETWORK_GROUP", ] 
**hasOPACLink** | bool,  | BoolClass,  | Whether or not the library has an OPAC deep links | [optional] 
**distance** | str,  | str,  | Distance from location if lat/log was specified | [optional] 
**self** | str,  | str,  | URI to find more info about the institution | [optional] 
**illStatus** | str,  | str,  | ILL status [Holdings/Library/ILLStatus] | [optional] 
**illGroup** | str,  | str,  | ILL group [Holdings/Library/ILLGroup] | [optional] 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint] | [optional] must be one of ["Y", "N", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# address

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**street1** | str,  | str,  | Name of street | [optional] 
**street2** | str,  | str,  | Name of street 2 | [optional] 
**city** | str,  | str,  | Name of city | [optional] 
**state** | str,  | str,  | Name of the State/Province, per ISO 3166-2. | [optional] 
**postalCode** | str,  | str,  | Postal Code | [optional] 
**country** | str,  | str,  | Two-character Country Code, per ISO 3166. | [optional] 
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | [optional] value must be a 64 bit float
**lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oclcNumber** | str,  | str,  | OCLC Number [LHR -&gt; HldDetRec/c004] | 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint || LHR -&gt; HldDetRec/Admin/SPReg] | must be one of ["Y", "N", ] 
**format** | str,  | str,  | material format [LHR -&gt; HldDetRec/c007] | 
**lhrControlNumber** | str,  | str,  | LHR Control Number [LHR -&gt; HldDetRec/c001] | 
**lhrDateEntered** | str,  | str,  | LHR Date Entered [LHR -&gt; HldDetRec/Admin/CreateDate] | 
**lhrLastUpdated** | str,  | str,  | LHR Date Last Used [LHR -&gt; HldDetRec/Admin/ReplacedDate] | 
**lendingPolicy** | str,  | str,  | local lending policy [LHR -&gt; HldDetRec/Admin/Lend] | 
**[location](#location)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | [optional] 
**copyNumber** | str,  | str,  | copy number [LHR -&gt; HldDetRec/v852st] | [optional] 
**[callNumber](#callNumber)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | [optional] 
**[sharedPrintCommitments](#sharedPrintCommitments)** | list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | [optional] 
**summary** | str,  | str,  | summary statement [LHR -&gt; HldSummRec/v966sa] | [optional] 
**[holdingParts](#holdingParts)** | list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location

Local holding location [LHR -> v852sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**holdingLocation** | str,  | str,  | Institution Symbol [LHR -&gt; v852sa] | [optional] 
**sublocationCollection** | str,  | str,  | Sublocation or collection [LHR -&gt; v852sb] | [optional] 
**shelvingLocation** | str,  | str,  | Shelving location [LHR -&gt; v852sc] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# callNumber

Local call number [LHR -> v852sh,i,j,k,l,m]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayCallNumber** | str,  | str,  | Display call Number [LHR -&gt; v852 |k,h,i,m / |j/ |l] | [optional] 
**classificationPart** | str,  | str,  | LHR -&gt; v852sh | [optional] 
**[itemParts](#itemParts)** | list, tuple,  | tuple,  | LHR -&gt; v852si | [optional] 
**shelvingControlNumber** | str,  | str,  | LHR -&gt; v852sj | [optional] 
**[prefixes](#prefixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sk | [optional] 
**shelvingForm** | str,  | str,  | LHR -&gt; v852sl | [optional] 
**[suffixes](#suffixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sm | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# itemParts

LHR -> v852si

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852si | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# prefixes

LHR -> v852sk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sk | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# suffixes

LHR -> v852sm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sm | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sharedPrintCommitments

shared print details [LHR -> HldDetRec/v583]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actionNote** | str,  | str,  | Action Note [LHR -&gt; HldDetRec/v583sa] | [optional] 
**materialsSpecified** | str,  | str,  | Materials Sepcified [LHR -&gt; HldDetRec/v583s3] | [optional] 
**institution** | str,  | str,  | Institution to which applies [LHR -&gt; HldDetRec/v583s5] | [optional] 
**dateOfAction** | str,  | str,  | date of action [LHR -&gt; HldDetRec/v583sc] | [optional] 
**commitmentExpirationDate** | str,  | str,  | commitment expiration date [LHR -&gt; HldDetRec/v583sd] | [optional] 
**authorization** | str,  | str,  | Authorization [LHR -&gt; HldDetRec/v583sf] | [optional] 
**methodOfAction** | str,  | str,  | Method of Action [LHR -&gt; HldDetRec/v583si] | [optional] 
**siteOfAction** | str,  | str,  | Site of Action [LHR -&gt; HldDetRec/v583sj] | [optional] 
**status** | str,  | str,  | Status [LHR -&gt; HldDetRec/v583sl] | [optional] 
**uri** | str,  | str,  | URI [LHR -&gt; HldDetRec/v583su] | [optional] 
**publicNote** | str,  | str,  | Public Note [LHR -&gt; HldDetRec/v583sz] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# holdingParts

Textual Holding [LHR -> HldDetRec/v866,v867,v868] Item Information Holding [LHR -> HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -> HldDetRec/v863,v864,v865]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**linkingAndSequenceNumber** | str,  | str,  | Field link and sequence number [852/863-865/866-868/876-878 | s8] | [optional] 
**summaryOfHoldings** | str,  | str,  | Summary of Holdings [https://www.loc.gov/marc/holdings/echdcntf.html] | [optional] 
**[enumerations](#enumerations)** | list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | [optional] 
**[chronologies](#chronologies)** | list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | [optional] 
**textualHoldings** | str,  | str,  | [866-8 |a] | [optional] 
**itemMaterialSpecified** | str,  | str,  | [876-8 |3] | [optional] 
**pieceDesignation** | str,  | str,  | Piece Designation [852/863-865/866-868/876-878 |p] | [optional] 
**[cancelledPieceDesignations](#cancelledPieceDesignations)** | list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | [optional] 
**temporaryLocation** | str,  | str,  | Temporary location [876-878 |l] | [optional] 
**[publicNotes](#publicNotes)** | list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | [optional] 
**[yearRanges](#yearRanges)** | list, tuple,  | tuple,  | Year as Range [si] | [optional] 
**[volumeRanges](#volumeRanges)** | list, tuple,  | tuple,  | Volume Number As Range [sb] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# enumerations

Enumerations [853-855/863-865 |a-h]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# chronologies

Chronologies [853-855/863-865 |i-v]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cancelledPieceDesignations

Cancelled Piece Designation [876-878 |r]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publicNotes

Public notes [852/863-865/866-868/876-878 |z]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# yearRanges

Year as Range [si]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Year as Range [si] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# volumeRanges

Volume Number As Range [sb]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Volume Number As Range [sb] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# searchFacets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[subFacet](#subFacet)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subFacetItemBrief](#subFacetItemBrief)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacetItemBrief

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_detailed_holdings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_detailed_holdings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_detailed_holdings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_detailed_holdings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_detailed_holdings.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_detailed_holdings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[worldcat_search_auth](../../../README.md#worldcat_search_auth), [worldcat_search_auth](../../../README.md#worldcat_search_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_bib_holdings**
<a id="find_bib_holdings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_bib_holdings()

Find member holdings for a known item

Given a known item, find the member libraries who hold it

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import member_general_holdings_api
from pprint import pprint
# Defining the host is optional and defaults to https://americas.discovery.api.oclc.org/worldcat/search/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = member_general_holdings_api.MemberGeneralHoldingsApi(api_client)

    # example passing only optional values
    query_params = {
        'oclcNumber': 41266045,
        'isbn': "0439136350",
        'issn': "0099-1333",
        'holdingsAllEditions': True,
        'holdingsAllVariantRecords': True,
        'preferredLanguage': "fre",
        'heldInCountry': "US",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'lat': 37.502508,
        'lon': -122.22702,
        'distance': 10,
        'unit': "M",
        'numberNearestHoldings': 20,
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Find member holdings for a known item
        api_response = api_instance.find_bib_holdings(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MemberGeneralHoldingsApi->find_bib_holdings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
oclcNumber | OclcNumberSchema | | optional
isbn | IsbnSchema | | optional
issn | IssnSchema | | optional
holdingsAllEditions | HoldingsAllEditionsSchema | | optional
holdingsAllVariantRecords | HoldingsAllVariantRecordsSchema | | optional
preferredLanguage | PreferredLanguageSchema | | optional
heldInCountry | HeldInCountrySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
lat | LatSchema | | optional
lon | LonSchema | | optional
distance | DistanceSchema | | optional
unit | UnitSchema | | optional
numberNearestHoldings | NumberNearestHoldingsSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

# IsbnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IssnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HoldingsAllEditionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HoldingsAllVariantRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PreferredLanguageSchema

three character MARC code for language to prefer records in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | three character MARC code for language to prefer records in | 

# HeldInCountrySchema

Two-character Country Code, per ISO 3166.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Two-character Country Code, per ISO 3166. | 

# HeldBySymbolSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | institution OCLC Symbol. Special characters need to be encoded properly. | 

# HeldByInstitutionIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | 

# LatSchema

Latitude

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | value must be a 64 bit float

# LonSchema

Longitude

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | value must be a 64 bit float

# DistanceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# UnitSchema

The unit of measure is either (M) for miles or (K) for kilometers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The unit of measure is either (M) for miles or (K) for kilometers | must be one of ["M", "K", ] if omitted the server will use the default value of "M"

# NumberNearestHoldingsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0value must be a 32 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10value must be a 32 bit integer

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_bib_holdings.ApiResponseFor200) | Successful search
400 | [ApiResponseFor400](#find_bib_holdings.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#find_bib_holdings.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#find_bib_holdings.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#find_bib_holdings.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#find_bib_holdings.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#find_bib_holdings.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### find_bib_holdings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**numberOfRecords** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[briefRecords](#briefRecords)** | list, tuple,  | tuple,  |  | [optional] 
**[searchFacets](#searchFacets)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# briefRecords

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str,  | str,  | machine readable date 008 | 
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer
**creator** | str,  | str,  | List of creators as single string | 
**edition** | str,  | str,  | Edition Statement [v250sa] | 
**publisher** | str,  | str,  |  | 
**language** | str,  | str,  | Language of the item [v041sa,j] | 
**title** | str,  | str,  | Linked [v880sa,b] if present or [v245sa,b] | 
**generalFormat** | str,  | str,  | General Format Type [Admin/OCLCDef/StdRT] | [optional] must be one of ["Archv", "ArtChapter", "AudioBook", "Book", "CompFile", "Encyc", "Game", "Image", "IntMM", "Jrnl", "Kit", "Map", "MsScr", "Music", "News", "Object", "Snd", "Toy", "Video", "Vis", "Web", ] 
**specificFormat** | str,  | str,  | Specific Format Type [Admin/OCLCDef/StdRT2] | [optional] must be one of ["2D", "Artcl", "Bluray", "Braille", "Cassette", "CD", "Chptr", "Continuing", "Digital", "DVD", "Encyc", "Film", "LargePrint", "LP", "Mic", "mss", "PrintBook", "rec", "Thsis", "VHS", ] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[mergedOclcNumbers](#mergedOclcNumbers)** | list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | [optional] 
**[catalogingInfo](#catalogingInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[institutionHolding](#institutionHolding)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# isbns

International Standard Book Number [v020sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Book Number [v020sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issns

International Standard Serial Numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Serial Numbers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | International Standard Serial Number [v022sal v700,v710,v711,v773,v776,v777,v780,v785 - sx] | 

# mergedOclcNumbers

Merged OCLC numbers [v019sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# catalogingInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**catalogingAgency** | str,  | str,  | Cataloging Agency [v040/sa] | [optional] 
**transcribingAgency** | str,  | str,  | Transcribing Agency [v040/sc] | [optional] 
**catalogingLanguage** | str,  | str,  | Language record was cataloged in [v040sb] | [optional] 
**levelOfCataloging** | str,  | str,  | Level of cataloging [LDR position 5] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# institutionHolding

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**totalHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings for this item [Holdings/TotalLibCount || FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalWorksHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings in the workset [FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalEditions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of editions in the workgroup | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | list, tuple,  | tuple,  |  | 
[one_of_1](#one_of_1) | list, tuple,  | tuple,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | Country of holding institution [Holdings/Library/Country] | [optional] 
**state** | str,  | str,  | State of holding institution [Holdings/Library/State] | [optional] 
**oclcSymbol** | str,  | str,  | Oclc Symbol of holding institution [Holdings/Library/InstSym] | [optional] 
**registryId** | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | [optional] 
**institutionName** | str,  | str,  | Name of holding institution [Holdings/Library/InstName] | [optional] 
**alsoCalled** | str,  | str,  | Some name the library might also be called | [optional] 
**[address](#address)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**institutionType** | str,  | str,  | The type of institution | [optional] must be one of ["ACADEMIC", "PUBLIC", "REGIONAL_OR_NATIONAL", "OTHER", "CORPORATE_SPECIAL_LIBRARY", "HEALTH", "MUSEUM_OR_ARCHIVES", "LAW", "MUSIC", "LIBRARY_NETWORK_GROUP", ] 
**hasOPACLink** | bool,  | BoolClass,  | Whether or not the library has an OPAC deep links | [optional] 
**distance** | str,  | str,  | Distance from location if lat/log was specified | [optional] 
**self** | str,  | str,  | URI to find more info about the institution | [optional] 
**illStatus** | str,  | str,  | ILL status [Holdings/Library/ILLStatus] | [optional] 
**illGroup** | str,  | str,  | ILL group [Holdings/Library/ILLGroup] | [optional] 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint] | [optional] must be one of ["Y", "N", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# address

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**street1** | str,  | str,  | Name of street | [optional] 
**street2** | str,  | str,  | Name of street 2 | [optional] 
**city** | str,  | str,  | Name of city | [optional] 
**state** | str,  | str,  | Name of the State/Province, per ISO 3166-2. | [optional] 
**postalCode** | str,  | str,  | Postal Code | [optional] 
**country** | str,  | str,  | Two-character Country Code, per ISO 3166. | [optional] 
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | [optional] value must be a 64 bit float
**lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oclcNumber** | str,  | str,  | OCLC Number [LHR -&gt; HldDetRec/c004] | 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint || LHR -&gt; HldDetRec/Admin/SPReg] | must be one of ["Y", "N", ] 
**format** | str,  | str,  | material format [LHR -&gt; HldDetRec/c007] | 
**lhrControlNumber** | str,  | str,  | LHR Control Number [LHR -&gt; HldDetRec/c001] | 
**lhrDateEntered** | str,  | str,  | LHR Date Entered [LHR -&gt; HldDetRec/Admin/CreateDate] | 
**lhrLastUpdated** | str,  | str,  | LHR Date Last Used [LHR -&gt; HldDetRec/Admin/ReplacedDate] | 
**lendingPolicy** | str,  | str,  | local lending policy [LHR -&gt; HldDetRec/Admin/Lend] | 
**[location](#location)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | [optional] 
**copyNumber** | str,  | str,  | copy number [LHR -&gt; HldDetRec/v852st] | [optional] 
**[callNumber](#callNumber)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | [optional] 
**[sharedPrintCommitments](#sharedPrintCommitments)** | list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | [optional] 
**summary** | str,  | str,  | summary statement [LHR -&gt; HldSummRec/v966sa] | [optional] 
**[holdingParts](#holdingParts)** | list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location

Local holding location [LHR -> v852sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**holdingLocation** | str,  | str,  | Institution Symbol [LHR -&gt; v852sa] | [optional] 
**sublocationCollection** | str,  | str,  | Sublocation or collection [LHR -&gt; v852sb] | [optional] 
**shelvingLocation** | str,  | str,  | Shelving location [LHR -&gt; v852sc] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# callNumber

Local call number [LHR -> v852sh,i,j,k,l,m]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayCallNumber** | str,  | str,  | Display call Number [LHR -&gt; v852 |k,h,i,m / |j/ |l] | [optional] 
**classificationPart** | str,  | str,  | LHR -&gt; v852sh | [optional] 
**[itemParts](#itemParts)** | list, tuple,  | tuple,  | LHR -&gt; v852si | [optional] 
**shelvingControlNumber** | str,  | str,  | LHR -&gt; v852sj | [optional] 
**[prefixes](#prefixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sk | [optional] 
**shelvingForm** | str,  | str,  | LHR -&gt; v852sl | [optional] 
**[suffixes](#suffixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sm | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# itemParts

LHR -> v852si

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852si | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# prefixes

LHR -> v852sk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sk | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# suffixes

LHR -> v852sm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sm | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sharedPrintCommitments

shared print details [LHR -> HldDetRec/v583]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actionNote** | str,  | str,  | Action Note [LHR -&gt; HldDetRec/v583sa] | [optional] 
**materialsSpecified** | str,  | str,  | Materials Sepcified [LHR -&gt; HldDetRec/v583s3] | [optional] 
**institution** | str,  | str,  | Institution to which applies [LHR -&gt; HldDetRec/v583s5] | [optional] 
**dateOfAction** | str,  | str,  | date of action [LHR -&gt; HldDetRec/v583sc] | [optional] 
**commitmentExpirationDate** | str,  | str,  | commitment expiration date [LHR -&gt; HldDetRec/v583sd] | [optional] 
**authorization** | str,  | str,  | Authorization [LHR -&gt; HldDetRec/v583sf] | [optional] 
**methodOfAction** | str,  | str,  | Method of Action [LHR -&gt; HldDetRec/v583si] | [optional] 
**siteOfAction** | str,  | str,  | Site of Action [LHR -&gt; HldDetRec/v583sj] | [optional] 
**status** | str,  | str,  | Status [LHR -&gt; HldDetRec/v583sl] | [optional] 
**uri** | str,  | str,  | URI [LHR -&gt; HldDetRec/v583su] | [optional] 
**publicNote** | str,  | str,  | Public Note [LHR -&gt; HldDetRec/v583sz] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# holdingParts

Textual Holding [LHR -> HldDetRec/v866,v867,v868] Item Information Holding [LHR -> HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -> HldDetRec/v863,v864,v865]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**linkingAndSequenceNumber** | str,  | str,  | Field link and sequence number [852/863-865/866-868/876-878 | s8] | [optional] 
**summaryOfHoldings** | str,  | str,  | Summary of Holdings [https://www.loc.gov/marc/holdings/echdcntf.html] | [optional] 
**[enumerations](#enumerations)** | list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | [optional] 
**[chronologies](#chronologies)** | list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | [optional] 
**textualHoldings** | str,  | str,  | [866-8 |a] | [optional] 
**itemMaterialSpecified** | str,  | str,  | [876-8 |3] | [optional] 
**pieceDesignation** | str,  | str,  | Piece Designation [852/863-865/866-868/876-878 |p] | [optional] 
**[cancelledPieceDesignations](#cancelledPieceDesignations)** | list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | [optional] 
**temporaryLocation** | str,  | str,  | Temporary location [876-878 |l] | [optional] 
**[publicNotes](#publicNotes)** | list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | [optional] 
**[yearRanges](#yearRanges)** | list, tuple,  | tuple,  | Year as Range [si] | [optional] 
**[volumeRanges](#volumeRanges)** | list, tuple,  | tuple,  | Volume Number As Range [sb] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# enumerations

Enumerations [853-855/863-865 |a-h]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# chronologies

Chronologies [853-855/863-865 |i-v]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cancelledPieceDesignations

Cancelled Piece Designation [876-878 |r]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publicNotes

Public notes [852/863-865/866-868/876-878 |z]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# yearRanges

Year as Range [si]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Year as Range [si] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# volumeRanges

Volume Number As Range [sb]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Volume Number As Range [sb] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# searchFacets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[subFacet](#subFacet)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subFacetItemBrief](#subFacetItemBrief)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacetItemBrief

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_holdings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_holdings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_holdings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_holdings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_holdings.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_holdings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[worldcat_search_auth](../../../README.md#worldcat_search_auth), [worldcat_search_auth](../../../README.md#worldcat_search_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_bib_summary_holdings**
<a id="find_bib_summary_holdings"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} find_bib_summary_holdings()

Get summary of holdings for a known item

Given a known item, get summary of holdings

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import member_general_holdings_api
from pprint import pprint
# Defining the host is optional and defaults to https://americas.discovery.api.oclc.org/worldcat/search/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Configure OAuth2 access token for authorization: worldcat_search_auth
configuration = openapi_client.Configuration(
    host = "https://americas.discovery.api.oclc.org/worldcat/search/v2",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = member_general_holdings_api.MemberGeneralHoldingsApi(api_client)

    # example passing only optional values
    query_params = {
        'oclcNumber': 41266045,
        'isbn': "0439136350",
        'issn': "0099-1333",
        'holdingsAllEditions': True,
        'holdingsAllVariantRecords': True,
        'preferredLanguage': "fre",
        'heldInCountry': "US",
        'heldByGroup': "ASRL",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'lat': 37.502508,
        'lon': -122.22702,
        'distance': 10,
        'unit': "M",
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Get summary of holdings for a known item
        api_response = api_instance.find_bib_summary_holdings(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MemberGeneralHoldingsApi->find_bib_summary_holdings: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
oclcNumber | OclcNumberSchema | | optional
isbn | IsbnSchema | | optional
issn | IssnSchema | | optional
holdingsAllEditions | HoldingsAllEditionsSchema | | optional
holdingsAllVariantRecords | HoldingsAllVariantRecordsSchema | | optional
preferredLanguage | PreferredLanguageSchema | | optional
heldInCountry | HeldInCountrySchema | | optional
heldByGroup | HeldByGroupSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
lat | LatSchema | | optional
lon | LonSchema | | optional
distance | DistanceSchema | | optional
unit | UnitSchema | | optional


# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

# IsbnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IssnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HoldingsAllEditionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# HoldingsAllVariantRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PreferredLanguageSchema

three character MARC code for language to prefer records in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | three character MARC code for language to prefer records in | 

# HeldInCountrySchema

Two-character Country Code, per ISO 3166.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Two-character Country Code, per ISO 3166. | 

# HeldByGroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeldBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HeldBySymbolSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | institution OCLC Symbol. Special characters need to be encoded properly. | 

# HeldByInstitutionIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | 

# LatSchema

Latitude

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | value must be a 64 bit float

# LonSchema

Longitude

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | value must be a 64 bit float

# DistanceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# UnitSchema

The unit of measure is either (M) for miles or (K) for kilometers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The unit of measure is either (M) for miles or (K) for kilometers | must be one of ["M", "K", ] if omitted the server will use the default value of "M"

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_bib_summary_holdings.ApiResponseFor200) | Successful search
400 | [ApiResponseFor400](#find_bib_summary_holdings.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#find_bib_summary_holdings.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#find_bib_summary_holdings.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#find_bib_summary_holdings.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#find_bib_summary_holdings.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#find_bib_summary_holdings.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### find_bib_summary_holdings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**numberOfRecords** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[briefRecords](#briefRecords)** | list, tuple,  | tuple,  |  | [optional] 
**[searchFacets](#searchFacets)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# briefRecords

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str,  | str,  | machine readable date 008 | 
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer
**creator** | str,  | str,  | List of creators as single string | 
**edition** | str,  | str,  | Edition Statement [v250sa] | 
**publisher** | str,  | str,  |  | 
**language** | str,  | str,  | Language of the item [v041sa,j] | 
**title** | str,  | str,  | Linked [v880sa,b] if present or [v245sa,b] | 
**generalFormat** | str,  | str,  | General Format Type [Admin/OCLCDef/StdRT] | [optional] must be one of ["Archv", "ArtChapter", "AudioBook", "Book", "CompFile", "Encyc", "Game", "Image", "IntMM", "Jrnl", "Kit", "Map", "MsScr", "Music", "News", "Object", "Snd", "Toy", "Video", "Vis", "Web", ] 
**specificFormat** | str,  | str,  | Specific Format Type [Admin/OCLCDef/StdRT2] | [optional] must be one of ["2D", "Artcl", "Bluray", "Braille", "Cassette", "CD", "Chptr", "Continuing", "Digital", "DVD", "Encyc", "Film", "LargePrint", "LP", "Mic", "mss", "PrintBook", "rec", "Thsis", "VHS", ] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[mergedOclcNumbers](#mergedOclcNumbers)** | list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | [optional] 
**[catalogingInfo](#catalogingInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[institutionHolding](#institutionHolding)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# isbns

International Standard Book Number [v020sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Book Number [v020sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issns

International Standard Serial Numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | International Standard Serial Numbers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | International Standard Serial Number [v022sal v700,v710,v711,v773,v776,v777,v780,v785 - sx] | 

# mergedOclcNumbers

Merged OCLC numbers [v019sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# catalogingInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**catalogingAgency** | str,  | str,  | Cataloging Agency [v040/sa] | [optional] 
**transcribingAgency** | str,  | str,  | Transcribing Agency [v040/sc] | [optional] 
**catalogingLanguage** | str,  | str,  | Language record was cataloged in [v040sb] | [optional] 
**levelOfCataloging** | str,  | str,  | Level of cataloging [LDR position 5] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# institutionHolding

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**totalHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings for this item [Holdings/TotalLibCount || FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalWorksHoldingCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of holdings in the workset [FRBRHoldings/B] | [optional] value must be a 32 bit integer
**totalEditions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of editions in the workgroup | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | list, tuple,  | tuple,  |  | 
[one_of_1](#one_of_1) | list, tuple,  | tuple,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | Country of holding institution [Holdings/Library/Country] | [optional] 
**state** | str,  | str,  | State of holding institution [Holdings/Library/State] | [optional] 
**oclcSymbol** | str,  | str,  | Oclc Symbol of holding institution [Holdings/Library/InstSym] | [optional] 
**registryId** | decimal.Decimal, int,  | decimal.Decimal,  | The identifier in the WorldCat Registry for the institution | [optional] 
**institutionName** | str,  | str,  | Name of holding institution [Holdings/Library/InstName] | [optional] 
**alsoCalled** | str,  | str,  | Some name the library might also be called | [optional] 
**[address](#address)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**institutionType** | str,  | str,  | The type of institution | [optional] must be one of ["ACADEMIC", "PUBLIC", "REGIONAL_OR_NATIONAL", "OTHER", "CORPORATE_SPECIAL_LIBRARY", "HEALTH", "MUSEUM_OR_ARCHIVES", "LAW", "MUSIC", "LIBRARY_NETWORK_GROUP", ] 
**hasOPACLink** | bool,  | BoolClass,  | Whether or not the library has an OPAC deep links | [optional] 
**distance** | str,  | str,  | Distance from location if lat/log was specified | [optional] 
**self** | str,  | str,  | URI to find more info about the institution | [optional] 
**illStatus** | str,  | str,  | ILL status [Holdings/Library/ILLStatus] | [optional] 
**illGroup** | str,  | str,  | ILL group [Holdings/Library/ILLGroup] | [optional] 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint] | [optional] must be one of ["Y", "N", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# address

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**street1** | str,  | str,  | Name of street | [optional] 
**street2** | str,  | str,  | Name of street 2 | [optional] 
**city** | str,  | str,  | Name of city | [optional] 
**state** | str,  | str,  | Name of the State/Province, per ISO 3166-2. | [optional] 
**postalCode** | str,  | str,  | Postal Code | [optional] 
**country** | str,  | str,  | Two-character Country Code, per ISO 3166. | [optional] 
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Latitude | [optional] value must be a 64 bit float
**lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | Longitude | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oclcNumber** | str,  | str,  | OCLC Number [LHR -&gt; HldDetRec/c004] | 
**hasSharedPrintCommitment** | str,  | str,  | institution has shared print commitment [Holdings/LibHasSharedPrint || LHR -&gt; HldDetRec/Admin/SPReg] | must be one of ["Y", "N", ] 
**format** | str,  | str,  | material format [LHR -&gt; HldDetRec/c007] | 
**lhrControlNumber** | str,  | str,  | LHR Control Number [LHR -&gt; HldDetRec/c001] | 
**lhrDateEntered** | str,  | str,  | LHR Date Entered [LHR -&gt; HldDetRec/Admin/CreateDate] | 
**lhrLastUpdated** | str,  | str,  | LHR Date Last Used [LHR -&gt; HldDetRec/Admin/ReplacedDate] | 
**lendingPolicy** | str,  | str,  | local lending policy [LHR -&gt; HldDetRec/Admin/Lend] | 
**[location](#location)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | [optional] 
**copyNumber** | str,  | str,  | copy number [LHR -&gt; HldDetRec/v852st] | [optional] 
**[callNumber](#callNumber)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | [optional] 
**[sharedPrintCommitments](#sharedPrintCommitments)** | list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | [optional] 
**summary** | str,  | str,  | summary statement [LHR -&gt; HldSummRec/v966sa] | [optional] 
**[holdingParts](#holdingParts)** | list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location

Local holding location [LHR -> v852sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local holding location [LHR -&gt; v852sa,b,c] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**holdingLocation** | str,  | str,  | Institution Symbol [LHR -&gt; v852sa] | [optional] 
**sublocationCollection** | str,  | str,  | Sublocation or collection [LHR -&gt; v852sb] | [optional] 
**shelvingLocation** | str,  | str,  | Shelving location [LHR -&gt; v852sc] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# callNumber

Local call number [LHR -> v852sh,i,j,k,l,m]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Local call number [LHR -&gt; v852sh,i,j,k,l,m] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**displayCallNumber** | str,  | str,  | Display call Number [LHR -&gt; v852 |k,h,i,m / |j/ |l] | [optional] 
**classificationPart** | str,  | str,  | LHR -&gt; v852sh | [optional] 
**[itemParts](#itemParts)** | list, tuple,  | tuple,  | LHR -&gt; v852si | [optional] 
**shelvingControlNumber** | str,  | str,  | LHR -&gt; v852sj | [optional] 
**[prefixes](#prefixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sk | [optional] 
**shelvingForm** | str,  | str,  | LHR -&gt; v852sl | [optional] 
**[suffixes](#suffixes)** | list, tuple,  | tuple,  | LHR -&gt; v852sm | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# itemParts

LHR -> v852si

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852si | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# prefixes

LHR -> v852sk

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sk | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# suffixes

LHR -> v852sm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | LHR -&gt; v852sm | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sharedPrintCommitments

shared print details [LHR -> HldDetRec/v583]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | shared print details [LHR -&gt; HldDetRec/v583] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actionNote** | str,  | str,  | Action Note [LHR -&gt; HldDetRec/v583sa] | [optional] 
**materialsSpecified** | str,  | str,  | Materials Sepcified [LHR -&gt; HldDetRec/v583s3] | [optional] 
**institution** | str,  | str,  | Institution to which applies [LHR -&gt; HldDetRec/v583s5] | [optional] 
**dateOfAction** | str,  | str,  | date of action [LHR -&gt; HldDetRec/v583sc] | [optional] 
**commitmentExpirationDate** | str,  | str,  | commitment expiration date [LHR -&gt; HldDetRec/v583sd] | [optional] 
**authorization** | str,  | str,  | Authorization [LHR -&gt; HldDetRec/v583sf] | [optional] 
**methodOfAction** | str,  | str,  | Method of Action [LHR -&gt; HldDetRec/v583si] | [optional] 
**siteOfAction** | str,  | str,  | Site of Action [LHR -&gt; HldDetRec/v583sj] | [optional] 
**status** | str,  | str,  | Status [LHR -&gt; HldDetRec/v583sl] | [optional] 
**uri** | str,  | str,  | URI [LHR -&gt; HldDetRec/v583su] | [optional] 
**publicNote** | str,  | str,  | Public Note [LHR -&gt; HldDetRec/v583sz] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# holdingParts

Textual Holding [LHR -> HldDetRec/v866,v867,v868] Item Information Holding [LHR -> HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -> HldDetRec/v863,v864,v865]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Textual Holding [LHR -&gt; HldDetRec/v866,v867,v868] Item Information Holding [LHR -&gt; HldDetRec/v876,v877,v878] Enumeration Chronology Holding [LHR -&gt; HldDetRec/v863,v864,v865] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**linkingAndSequenceNumber** | str,  | str,  | Field link and sequence number [852/863-865/866-868/876-878 | s8] | [optional] 
**summaryOfHoldings** | str,  | str,  | Summary of Holdings [https://www.loc.gov/marc/holdings/echdcntf.html] | [optional] 
**[enumerations](#enumerations)** | list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | [optional] 
**[chronologies](#chronologies)** | list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | [optional] 
**textualHoldings** | str,  | str,  | [866-8 |a] | [optional] 
**itemMaterialSpecified** | str,  | str,  | [876-8 |3] | [optional] 
**pieceDesignation** | str,  | str,  | Piece Designation [852/863-865/866-868/876-878 |p] | [optional] 
**[cancelledPieceDesignations](#cancelledPieceDesignations)** | list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | [optional] 
**temporaryLocation** | str,  | str,  | Temporary location [876-878 |l] | [optional] 
**[publicNotes](#publicNotes)** | list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | [optional] 
**[yearRanges](#yearRanges)** | list, tuple,  | tuple,  | Year as Range [si] | [optional] 
**[volumeRanges](#volumeRanges)** | list, tuple,  | tuple,  | Volume Number As Range [sb] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# enumerations

Enumerations [853-855/863-865 |a-h]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Enumerations [853-855/863-865 |a-h] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# chronologies

Chronologies [853-855/863-865 |i-v]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Chronologies [853-855/863-865 |i-v] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

# items

The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The caption and value pair for a caption describing a numeric, alphabetic, and/or date designation for an item. The caption is defined as an attribute on the element and the value for the caption is defined by the element contents. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**caption** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cancelledPieceDesignations

Cancelled Piece Designation [876-878 |r]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cancelled Piece Designation [876-878 |r] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publicNotes

Public notes [852/863-865/866-868/876-878 |z]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Public notes [852/863-865/866-868/876-878 |z] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# yearRanges

Year as Range [si]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Year as Range [si] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# volumeRanges

Volume Number As Range [sb]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Volume Number As Range [sb] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from** | str,  | str,  |  | [optional] 
**to** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# searchFacets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[subFacet](#subFacet)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subFacetItemBrief](#subFacetItemBrief)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subFacetItemBrief

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | str,  | str,  |  | [optional] 
**facetType** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_summary_holdings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_summary_holdings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_summary_holdings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### find_bib_summary_holdings.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor405ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor405ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_summary_holdings.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### find_bib_summary_holdings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

RFC 7807 description of an error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RFC 7807 description of an error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | A URI reference [RFC3986] that identifies the problem type. | [optional] must be one of ["https://developer.api.oclc.org/errors/NOT_ACCEPTABLE", "https://developer.api.oclc.org/errors/NOT_ALLOWED", "https://developer.api.oclc.org/errors/INTERAL_SERVER_ERROR", "https://developer.api.oclc.org/errors/BAD_REQUEST", "https://developer.api.oclc.org/errors/NOT_FOUND", "https://developer.api.oclc.org/errors/NOT_ELIGIBLE", "https://developer.api.oclc.org/errors/MISSING_QUERY_PARAMETER", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETERS", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_VALUE", "https://developer.api.oclc.org/errors/INVALID_QUERY_PARAMETER_NAME", "https://developer.api.oclc.org/errors/SYNTAX_ERROR", "https://developer.api.oclc.org/errors/INVALID_DOCUMENT", "https://developer.api.oclc.org/errors/MISSING_ELEMENT", "https://developer.api.oclc.org/errors/INVALID_ELEMENT_VALUE", ] 
**title** | str,  | str,  | A short, human-readable summary of the problem type. | [optional] 
**instance** | str,  | str,  | A URI reference that identifies the specific occurrence of the problem. | [optional] 
**detail** | str,  | str,  | A human-readable explanation specific to this occurrence of the problem., | [optional] 
**[invalidParams](#invalidParams)** | list, tuple,  | tuple,  | An array of validation errors. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# invalidParams

An array of validation errors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of validation errors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

# items

The validation error descriptor.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The validation error descriptor. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[worldcat_search_auth](../../../README.md#worldcat_search_auth), [worldcat_search_auth](../../../README.md#worldcat_search_auth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

