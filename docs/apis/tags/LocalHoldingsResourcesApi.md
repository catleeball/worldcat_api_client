<a id="__pageTop"></a>
# openapi_client.apis.tags.local_holdings_resources_api.LocalHoldingsResourcesApi

All URIs are relative to *https://americas.discovery.api.oclc.org/worldcat/search/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_lhr**](#retrieve_lhr) | **get** /my-holdings/{controlNumber} | Retrieve LHR Resource
[**search_lhr**](#search_lhr) | **get** /my-holdings | Search LHR Resources
[**search_retrained_lhr**](#search_retrained_lhr) | **get** /retained-holdings | Search for shared print LHR Resources

# **retrieve_lhr**
<a id="retrieve_lhr"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_lhr(control_number)

Retrieve LHR Resource

Retrieve LHR Resource

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import local_holdings_resources_api
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
    api_instance = local_holdings_resources_api.LocalHoldingsResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'control-number': "238374600",
    }
    header_params = {
    }
    try:
        # Retrieve LHR Resource
        api_response = api_instance.retrieve_lhr(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocalHoldingsResourcesApi->retrieve_lhr: %s\n" % e)

    # example passing only optional values
    path_params = {
        'control-number': "238374600",
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Retrieve LHR Resource
        api_response = api_instance.retrieve_lhr(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocalHoldingsResourcesApi->retrieve_lhr: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
control-number | ControlNumberSchema | | 

# ControlNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_lhr.ApiResponseFor200) | successful read one of my holdings
400 | [ApiResponseFor400](#retrieve_lhr.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
404 | [ApiResponseFor404](#retrieve_lhr.ApiResponseFor404) | Failed operation - resource not found
405 | [ApiResponseFor405](#retrieve_lhr.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#retrieve_lhr.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#retrieve_lhr.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### retrieve_lhr.ApiResponseFor200
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

#### retrieve_lhr.ApiResponseFor400
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

#### retrieve_lhr.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson

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

#### retrieve_lhr.ApiResponseFor405
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

#### retrieve_lhr.ApiResponseFor406
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

#### retrieve_lhr.ApiResponseFor500
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

# **search_lhr**
<a id="search_lhr"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} search_lhr()

Search LHR Resources

Search LHR Resources

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import local_holdings_resources_api
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
    api_instance = local_holdings_resources_api.LocalHoldingsResourcesApi(api_client)

    # example passing only optional values
    query_params = {
        'oclcNumber': 41266045,
        'barcode': "K123456789",
        'orderBy': "oclcSymbol",
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Search LHR Resources
        api_response = api_instance.search_lhr(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocalHoldingsResourcesApi->search_lhr: %s\n" % e)
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
barcode | BarcodeSchema | | optional
orderBy | OrderBySchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

# BarcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["commitmentExpirationDate", "location", "oclcSymbol", ] if omitted the server will use the default value of "oclcSymbol"

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
200 | [ApiResponseFor200](#search_lhr.ApiResponseFor200) | successful search of my holdings
400 | [ApiResponseFor400](#search_lhr.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#search_lhr.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_lhr.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#search_lhr.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#search_lhr.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#search_lhr.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### search_lhr.ApiResponseFor200
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
**numberOfHoldings** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[detailedHoldings](#detailedHoldings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detailedHoldings

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

#### search_lhr.ApiResponseFor400
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

#### search_lhr.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_lhr.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_lhr.ApiResponseFor405
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

#### search_lhr.ApiResponseFor406
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

#### search_lhr.ApiResponseFor500
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

# **search_retrained_lhr**
<a id="search_retrained_lhr"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} search_retrained_lhr()

Search for shared print LHR Resources

Search for shared print LHR Resources

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import local_holdings_resources_api
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
    api_instance = local_holdings_resources_api.LocalHoldingsResourcesApi(api_client)

    # example passing only optional values
    query_params = {
        'oclcNumber': 41266045,
        'barcode': "K123456789",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'spProgram': "WEST",
        'orderBy': "oclcSymbol",
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Search for shared print LHR Resources
        api_response = api_instance.search_retrained_lhr(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocalHoldingsResourcesApi->search_retrained_lhr: %s\n" % e)
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
barcode | BarcodeSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
spProgram | SpProgramSchema | | optional
orderBy | OrderBySchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

# BarcodeSchema

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

# SpProgramSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["commitmentExpirationDate", "location", "oclcSymbol", ] if omitted the server will use the default value of "oclcSymbol"

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
200 | [ApiResponseFor200](#search_retrained_lhr.ApiResponseFor200) | successful search for retained holdings
400 | [ApiResponseFor400](#search_retrained_lhr.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#search_retrained_lhr.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_retrained_lhr.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#search_retrained_lhr.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#search_retrained_lhr.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#search_retrained_lhr.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### search_retrained_lhr.ApiResponseFor200
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
**numberOfHoldings** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[detailedHoldings](#detailedHoldings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detailedHoldings

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

#### search_retrained_lhr.ApiResponseFor400
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

#### search_retrained_lhr.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_retrained_lhr.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_retrained_lhr.ApiResponseFor405
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

#### search_retrained_lhr.ApiResponseFor406
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

#### search_retrained_lhr.ApiResponseFor500
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

