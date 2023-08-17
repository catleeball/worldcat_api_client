<a id="__pageTop"></a>
# openapi_client.apis.tags.bibliographic_resources_api.BibliographicResourcesApi

All URIs are relative to *https://americas.discovery.api.oclc.org/worldcat/search/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_bib**](#retrieve_bib) | **get** /bibs/{oclcNumber} | Retrieve specific Bibliographic Resource
[**retrieve_brief_bib**](#retrieve_brief_bib) | **get** /brief-bibs/{oclcNumber} | Retrieve specific Bibliographic Resource
[**retrieve_other_editions**](#retrieve_other_editions) | **get** /brief-bibs/{oclcNumber}/other-editions | Retrieve Other Editions related to a particular Bibliographic Resource
[**search_bibs**](#search_bibs) | **get** /bibs | Search Bibliographic Resources
[**search_brief_bibs**](#search_brief_bibs) | **get** /brief-bibs | Search Brief Bibliographic Resources

# **retrieve_bib**
<a id="retrieve_bib"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_bib(oclc_number)

Retrieve specific Bibliographic Resource

Retrieve specific Bibliographic Resource

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import bibliographic_resources_api
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
    api_instance = bibliographic_resources_api.BibliographicResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'oclcNumber': 41266045,
    }
    header_params = {
    }
    try:
        # Retrieve specific Bibliographic Resource
        api_response = api_instance.retrieve_bib(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_bib: %s\n" % e)

    # example passing only optional values
    path_params = {
        'oclcNumber': 41266045,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Retrieve specific Bibliographic Resource
        api_response = api_instance.retrieve_bib(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_bib: %s\n" % e)
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
oclcNumber | OclcNumberSchema | | 

# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_bib.ApiResponseFor200) | successful request for single bib record
400 | [ApiResponseFor400](#retrieve_bib.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#retrieve_bib.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#retrieve_bib.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_bib.ApiResponseFor404) | Failed operation - resource not found
405 | [ApiResponseFor405](#retrieve_bib.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#retrieve_bib.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#retrieve_bib.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### retrieve_bib.ApiResponseFor200
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
**[identifier](#identifier)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[title](#title)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[contributor](#contributor)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subjects](#subjects)** | list, tuple,  | tuple,  |  | [optional] 
**[classification](#classification)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[publishers](#publishers)** | list, tuple,  | tuple,  |  | [optional] 
**[date](#date)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[language](#language)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[edition](#edition)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[source](#source)** | list, tuple,  | tuple,  |  | [optional] 
**[note](#note)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[format](#format)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[musicInfo](#musicInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[digitalAccessAndLocations](#digitalAccessAndLocations)** | list, tuple,  | tuple,  |  | [optional] 
**[description](#description)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[related](#related)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z) | [optional] 
**[work](#work)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[editionCluster](#editionCluster)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**totalEditions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of editions in the workgroup | [optional] value must be a 32 bit integer
**[database](#database)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localTitle](#localTitle)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localContributor](#localContributor)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localSubjects](#localSubjects)** | list, tuple,  | tuple,  |  | [optional] 
**[localNote](#localNote)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localGenres](#localGenres)** | list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# identifier

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | OCLC Number [Admin/BaseOCLCNo || Admin/OCLCNo || C001] | [optional] value must be a 64 bit integer
**lccn** | str,  | str,  | Library of Congress Control Number [v010sa] | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[externalIdentifiers](#externalIdentifiers)** | list, tuple,  | tuple,  | External System Control Number [v029sa,b,c,t] | [optional] 
**[otherStandardIdentifiers](#otherStandardIdentifiers)** | list, tuple,  | tuple,  | Other Standard Identifier [v024sa] | [optional] 
**[dois](#dois)** | list, tuple,  | tuple,  | Digital Object Identifier [v901sb v024sa] | [optional] 
**[mergedOclcNumbers](#mergedOclcNumbers)** | list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | [optional] 
**[gpoNumber](#gpoNumber)** | list, tuple,  | tuple,  | GPO Item number [v074sa] | [optional] 
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

# externalIdentifiers

External System Control Number [v029sa,b,c,t]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | External System Control Number [v029sa,b,c,t] | 

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
**oclcSymbol** | str,  | str,  |  | [optional] 
**systemControlNumber** | str,  | str,  |  | [optional] 
**oaiSetName** | str,  | str,  |  | [optional] 
**contentTypeId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# otherStandardIdentifiers

Other Standard Identifier [v024sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Other Standard Identifier [v024sa] | 

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
**type** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dois

Digital Object Identifier [v901sb v024sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Digital Object Identifier [v901sb v024sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# gpoNumber

GPO Item number [v074sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | GPO Item number [v074sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# title

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mainTitles](#mainTitles)** | list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | [optional] 
**[seriesTitles](#seriesTitles)** | list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | [optional] 
**[uniformTitles](#uniformTitles)** | list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | [optional] 
**[additionalTitles](#additionalTitles)** | list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mainTitles

Main Titles [v245sa,b,c,f,g,k,n,p,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# seriesTitles

Series Titles [(v490,v810,v830 - sa,v)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | 

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
**seriesTitle** | str,  | str,  | [(v490,v810,v830 - sa)] | [optional] 
**volume** | str,  | str,  | [(v490,v810,v830 - sv)] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# uniformTitles

Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) && v240sa,d,f,g,k,l,m,n,o,p,r,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalTitles

Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contributor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[creators](#creators)** | list, tuple,  | tuple,  | Creators of work | [optional] 
**[additionalCreators](#additionalCreators)** | list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | [optional] 
**[statementOfResponsibility](#statementOfResponsibility)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creators

Creators of work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Creators of work | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

# items

[v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[firstName](#firstName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[secondName](#secondName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[nonPersonName](#nonPersonName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**[creatorNotes](#creatorNotes)** | list, tuple,  | tuple,  | subfield d | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  | subfield e | [optional] 
**affiliation** | str,  | str,  | subfield u | [optional] 
**isPrimary** | bool,  | BoolClass,  | whether or not this contributor is the primary one (the 1xx) | [optional] 
**[relatedItem](#relatedItem)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firstName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# secondName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nonPersonName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creatorNotes

subfield d

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield d | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relators

subfield e

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield e | 

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# additionalCreators

Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statementOfResponsibility

245 |c

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

# items

Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[subjectName](#subjectName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**vocabulary** | str,  | str,  | subject authority vocabularies (MESH, FAST, LCSH, RVM) | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**subjectType** | str,  | str,  |  | [optional] 
**uri** | str,  | str,  | URI [6xx s1] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjectName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classification

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dewey** | str,  | str,  | Dewey Decimal Classification Number [v082sa,b] | [optional] 
**lc** | str,  | str,  | Library of Congress Call Number [v050sa,b] | [optional] 
**nlm** | str,  | str,  | National Library of Medicine Call Number [v060sa,b] | [optional] 
**[govDoc](#govDoc)** | list, tuple,  | tuple,  | Government Doc number [v086sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# govDoc

Government Doc number [v086sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Government Doc number [v086sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publishers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Publisher Information [v260sa,b v264sa,b v880sa,b] | 

# items

Publisher Information [v260sa,b v264sa,b v880sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Publisher Information [v260sa,b v264sa,b v880sa,b] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[publisherName](#publisherName)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Publisher Name [v260sb v264sb v880b] | [optional] 
**publicationPlace** | str,  | str,  | Publication Place [v260sa v264sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# publisherName

Publisher Name [v260sb v264sb v880b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Publisher Name [v260sb v264sb v880b] | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# date

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**publicationDate** | str,  | str,  | Date of Publication [v260sc || c008(bytes 07-14) || v264sc || v362sa] | [optional] 
**publicationSequentialDesignationDate** | str,  | str,  | Chronological issue designations [v362sa] | [optional] 
**currentPublicationFrequency** | str,  | str,  | Frequency of Publication [v310sa] | [optional] 
**createDate** | str,  | str,  | Date Record was Created [Admin/CreateDate] | [optional] 
**replaceDate** | str,  | str,  | Date Record was last Updated [Admin/ReplacedDate] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# language

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**itemLanguage** | str,  | str,  | Language of the item [v041sa,j] | [optional] 
**catalogingLanguage** | str,  | str,  | Language record was cataloged in [v040sb] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# edition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statement** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# source

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
**[supplements](#supplements)** | list, tuple,  | tuple,  | Supplements [v949sd] | [optional] 
**[firstPages](#firstPages)** | list, tuple,  | tuple,  | First Page [v949sf] | [optional] 
**[issueDates](#issueDates)** | list, tuple,  | tuple,  | Issue Dates [v949se] | [optional] 
**mainEntry** | str,  | str,  | Main Entry [v773sa] | [optional] 
**[otherPublicationData](#otherPublicationData)** | list, tuple,  | tuple,  | Other Publication Data [v799sa,d,g,o] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supplements

Supplements [v949sd]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplements [v949sd] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# firstPages

First Page [v949sf]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | First Page [v949sf] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issueDates

Issue Dates [v949se]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Issue Dates [v949se] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherPublicationData

Other Publication Data [v799sa,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Other Publication Data [v799sa,d,g,o] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  | Related Parts [v773sg] | [optional] 
**sourceTitle** | str,  | str,  | Source Title [v799st v773st] | [optional] 
**sourceIssn** | str,  | str,  | Source ISSN [v773sx] | [optional] 
**[sourceIsbns](#sourceIsbns)** | list, tuple,  | tuple,  | Source ISBNs [v799sz] | [optional] 
**sourceAuthor** | str,  | str,  | Source Author [v799sa] | [optional] 
**publicationInformation** | str,  | str,  | Publication Information [v773sd] | [optional] 
**[volumes](#volumes)** | list, tuple,  | tuple,  | Volumes [v799sm v949sa] | [optional] 
**[issues](#issues)** | list, tuple,  | tuple,  | Issues [v799sp v949sb] | [optional] 
**[pageRanges](#pageRanges)** | list, tuple,  | tuple,  | Page Range [v949sc] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedParts

Related Parts [v773sg]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Related Parts [v773sg] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sourceIsbns

Source ISBNs [v799sz]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Source ISBNs [v799sz] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# volumes

Volumes [v799sm v949sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Volumes [v799sm v949sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issues

Issues [v799sp v949sb]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Issues [v799sp v949sb] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# pageRanges

Page Range [v949sc]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Page Range [v949sc] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# note

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[generalNotes](#generalNotes)** | list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | [optional] 
**audienceNote** | str,  | str,  | Target Audience Note [v521sa] | [optional] 
**[dissertationNotes](#dissertationNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[castNotes](#castNotes)** | list, tuple,  | tuple,  | Cast Notes [v511sa] | [optional] 
**[performerNotes](#performerNotes)** | list, tuple,  | tuple,  | Performers Notes [v511sa] | [optional] 
**participantNote** | str,  | str,  | Participants Notes [v511sa] | [optional] 
**[eventNotes](#eventNotes)** | list, tuple,  | tuple,  |  | [optional] 
**creditNotes** | str,  | str,  | Production Credits Notes [v508sa] | [optional] 
**[scaleNotes](#scaleNotes)** | list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | [optional] 
**[reproductionNotes](#reproductionNotes)** | list, tuple,  | tuple,  | Reproduction Notes [v533] | [optional] 
**[useAndReproductionNotes](#useAndReproductionNotes)** | list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | [optional] 
**[useownershipAndCustodialHistories](#useownershipAndCustodialHistories)** | list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | [optional] 
**systemDetailNote** | str,  | str,  | System Details Note [v538sa,u,i] | [optional] 
**awardNote** | str,  | str,  | Awards Note [v586sa] | [optional] 
**[languageNotes](#languageNotes)** | list, tuple,  | tuple,  | language note [v546sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# generalNotes

General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | 

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
**text** | str,  | str,  |  | [optional] 
**private** | bool,  | BoolClass,  | 1st indicator of 590 | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dissertationNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

# items

Disseration notes [v502sa,b,c,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disserationNote** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**institution** | str,  | str,  |  | [optional] 
**year** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**miscellaneousInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# castNotes

Cast Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cast Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# performerNotes

Performers Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Performers Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# eventNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

# items

Notes about event [v518sa,d,o,p,3]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**compositeNote** | str,  | str,  |  | [optional] 
**eventDate** | str,  | str,  |  | [optional] 
**eventPlace** | str,  | str,  |  | [optional] 
**eventInfo** | str,  | str,  |  | [optional] 
**material** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scaleNotes

Scale Note for Graphic Material [v507sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reproductionNotes

Reproduction Notes [v533]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Reproduction Notes [v533] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Reproduction Note [v533] | 

# useAndReproductionNotes

Terms Governing Use and Reproduction [v540sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# useownershipAndCustodialHistories

Ownership and Custodial History [v561sa,3,5,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# languageNotes

language note [v546sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | language note [v546sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**generalFormat** | str,  | str,  | General Format Type [Admin/OCLCDef/StdRT] | [optional] must be one of ["Archv", "ArtChapter", "AudioBook", "Book", "CompFile", "Encyc", "Game", "Image", "IntMM", "Jrnl", "Kit", "Map", "MsScr", "Music", "News", "Object", "Snd", "Toy", "Video", "Vis", "Web", ] 
**specificFormat** | str,  | str,  | Specific Format Type [Admin/OCLCDef/StdRT2] | [optional] must be one of ["2D", "Artcl", "Bluray", "Braille", "Cassette", "CD", "Chptr", "Continuing", "Digital", "DVD", "Encyc", "Film", "LargePrint", "LP", "Mic", "mss", "PrintBook", "rec", "Thsis", "VHS", ] 
**[materialTypes](#materialTypes)** | list, tuple,  | tuple,  | Material Types [Admin/OCLCDef/MT[@form&#x3D;&#x27;gen&#x27;]] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# materialTypes

Material Types [Admin/OCLCDef/MT[@form='gen']]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Material Types [Admin/OCLCDef/MT[@form&#x3D;&#x27;gen&#x27;]] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# musicInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instrumentations](#instrumentations)** | list, tuple,  | tuple,  |  | [optional] 
**musicalKey** | str,  | str,  | Musical Key [v384sa] | [optional] 
**[instrumentsCodes](#instrumentsCodes)** | list, tuple,  | tuple,  | Musical Instruments [v048sa,b] | [optional] 
**numericDesignation** | str,  | str,  | Numeric Designation of Musical Work [v383sa,b,c] | [optional] 
**musicalPresentationStatement** | str,  | str,  | Musical Presentation Statement [v254sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instrumentations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Instrumentation [v382sa,b,d,e,n,p,r,s,t,v] | 

# items

Instrumentation [v382sa,b,d,e,n,p,r,s,t,v]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Instrumentation [v382sa,b,d,e,n,p,r,s,t,v] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mediumOfPerformance](#mediumOfPerformance)** | list, tuple,  | tuple,  |  | [optional] 
**[soloists](#soloists)** | list, tuple,  | tuple,  |  | [optional] 
**[doublingInstruments](#doublingInstruments)** | list, tuple,  | tuple,  |  | [optional] 
**[numberOfEnsemblesOfSameTypes](#numberOfEnsemblesOfSameTypes)** | list, tuple,  | tuple,  |  | [optional] 
**[numberOfPerformersOfSameMediums](#numberOfPerformersOfSameMediums)** | list, tuple,  | tuple,  |  | [optional] 
**[alternativeMediumOfPerformances](#alternativeMediumOfPerformances)** | list, tuple,  | tuple,  |  | [optional] 
**numberOfIndividualsPerforming** | str,  | str,  |  | [optional] 
**numberOfPerformers** | str,  | str,  |  | [optional] 
**numberOfEnsembles** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mediumOfPerformance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# soloists

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# doublingInstruments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# numberOfEnsemblesOfSameTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# numberOfPerformersOfSameMediums

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# alternativeMediumOfPerformances

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# instrumentsCodes

Musical Instruments [v048sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Musical Instruments [v048sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# digitalAccessAndLocations

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
**uri** | str,  | str,  | URI of resource [v856su] | 
**materialSpecified** | str,  | str,  | Materials specified |3 | [optional] 
**[instructions](#instructions)** | list, tuple,  | tuple,  | Instruction [v856si] | [optional] 
**[linkText](#linkText)** | list, tuple,  | tuple,  | Text associated with a link |y | [optional] 
**nonPublicNote** | str,  | str,  | Nonpublic note [v856sx] | [optional] 
**[publicNote](#publicNote)** | list, tuple,  | tuple,  | A note pertaining to the electronic location of the source identified in the field |z | [optional] 
**accessMethod** | str,  | str,  | Access method [v856s2] | [optional] 
**accessStatus** | str,  | str,  | Access method [v856s7] | [optional] 
**relationship** | str,  | str,  | Relationship to the item described in the record as a whole [v856 second indicator] | [optional] must be one of ["unknown", "resource", "version of resource", "related resource", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instructions

Instruction [v856si]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Instruction [v856si] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# linkText

Text associated with a link |y

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Text associated with a link |y | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publicNote

A note pertaining to the electronic location of the source identified in the field |z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A note pertaining to the electronic location of the source identified in the field |z | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**physicalDescription** | str,  | str,  | Physical Description [v300sa,b,c,d,e,f,g,3] | [optional] 
**digitalGraphicRepresentation** | str,  | str,  | Digital Graphic Representation [v352sa,b,c,i,q] | [optional] 
**[genres](#genres)** | list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | [optional] 
**[cartographicData](#cartographicData)** | list, tuple,  | tuple,  | Cartographic Mathematical Data [v255sa,b,c] | [optional] 
**[computerFilesCharacteristics](#computerFilesCharacteristics)** | list, tuple,  | tuple,  | Computer File Characteristics [v256sa] | [optional] 
**[formOfWorks](#formOfWorks)** | list, tuple,  | tuple,  | Form of Work [v380sa] | [optional] 
**[abstracts](#abstracts)** | list, tuple,  | tuple,  | Abstract [v520sa,b,c] | [optional] 
**[summaries](#summaries)** | list, tuple,  | tuple,  | Summary [v520sa,b,c] | [optional] 
**[contents](#contents)** | list, tuple,  | tuple,  |  | [optional] 
**[bibliographies](#bibliographies)** | list, tuple,  | tuple,  | Bibliography [v504sa] | [optional] 
**peerReviewed** | str,  | str,  | Is this a peer reviewed work [Admin/OCLCDef/PR] | [optional] must be one of ["Y", "N", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# genres

Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# cartographicData

Cartographic Mathematical Data [v255sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cartographic Mathematical Data [v255sa,b,c] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# computerFilesCharacteristics

Computer File Characteristics [v256sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Computer File Characteristics [v256sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# formOfWorks

Form of Work [v380sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Form of Work [v380sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# abstracts

Abstract [v520sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Abstract [v520sa,b,c] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# summaries

Summary [v520sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Summary [v520sa,b,c] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Formatted Contents Note [v505sa,t,r,g,u] | 

# items

Formatted Contents Note [v505sa,t,r,g,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Formatted Contents Note [v505sa,t,r,g,u] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[contentNote](#contentNote)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[miscellaneousInfo](#miscellaneousInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[statementsOfResponsibility](#statementsOfResponsibility)** | list, tuple,  | tuple,  |  | [optional] 
**[uris](#uris)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contentNote

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# miscellaneousInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# statementsOfResponsibility

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# uris

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# bibliographies

Bibliography [v504sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Bibliography [v504sa] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# related

Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[relatedItems](#relatedItems)** | list, tuple,  | tuple,  |  | [optional] 
**[precedingEntries](#precedingEntries)** | list, tuple,  | tuple,  |  | [optional] 
**[succeedingEntries](#succeedingEntries)** | list, tuple,  | tuple,  |  | [optional] 
**[issuedWithEntries](#issuedWithEntries)** | list, tuple,  | tuple,  | [v777] | [optional] 
**[additionalPhysicalFormEntries](#additionalPhysicalFormEntries)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItems

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# precedingEntries

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# succeedingEntries

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# issuedWithEntries

[v777]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | [v777] | 

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
**displayConstant** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[recordControlOclcNumbers](#recordControlOclcNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[mainEntryHeadings](#mainEntryHeadings)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlOclcNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# mainEntryHeadings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalPhysicalFormEntries

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
**displayConstant** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[recordControlOclcNumbers](#recordControlOclcNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[mainEntryHeadings](#mainEntryHeadings)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlOclcNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# mainEntryHeadings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Id of the workset [Admin/Work/ID] | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items in Workset [Admin/Work/Count] | [optional] value must be a 32 bit integer
**[articleCluster](#articleCluster)** | list, tuple,  | tuple,  | Items in Article Workset [WorkSet/NO] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# articleCluster

Items in Article Workset [WorkSet/NO]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Items in Article Workset [WorkSet/NO] | 

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
**databaseCollection** | str,  | str,  |  | [optional] 
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# editionCluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An id associated with a particular edition cluster [Admin/Edition/ID] | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items in edition cluster | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# database

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | str,  | str,  | Source Collection [Admin/SourceCol] | [optional] 
**collection** | str,  | str,  | Db Collection [root collection attribute] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localTitle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mainTitles](#mainTitles)** | list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | [optional] 
**[seriesTitles](#seriesTitles)** | list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | [optional] 
**[uniformTitles](#uniformTitles)** | list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | [optional] 
**[additionalTitles](#additionalTitles)** | list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mainTitles

Main Titles [v245sa,b,c,f,g,k,n,p,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# seriesTitles

Series Titles [(v490,v810,v830 - sa,v)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | 

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
**seriesTitle** | str,  | str,  | [(v490,v810,v830 - sa)] | [optional] 
**volume** | str,  | str,  | [(v490,v810,v830 - sv)] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# uniformTitles

Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) && v240sa,d,f,g,k,l,m,n,o,p,r,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalTitles

Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localContributor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[creators](#creators)** | list, tuple,  | tuple,  | Creators of work | [optional] 
**[additionalCreators](#additionalCreators)** | list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | [optional] 
**[statementOfResponsibility](#statementOfResponsibility)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creators

Creators of work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Creators of work | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

# items

[v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[firstName](#firstName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[secondName](#secondName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[nonPersonName](#nonPersonName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**[creatorNotes](#creatorNotes)** | list, tuple,  | tuple,  | subfield d | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  | subfield e | [optional] 
**affiliation** | str,  | str,  | subfield u | [optional] 
**isPrimary** | bool,  | BoolClass,  | whether or not this contributor is the primary one (the 1xx) | [optional] 
**[relatedItem](#relatedItem)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firstName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# secondName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nonPersonName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creatorNotes

subfield d

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield d | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relators

subfield e

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield e | 

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# additionalCreators

Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statementOfResponsibility

245 |c

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localSubjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

# items

Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[subjectName](#subjectName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**vocabulary** | str,  | str,  | subject authority vocabularies (MESH, FAST, LCSH, RVM) | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**subjectType** | str,  | str,  |  | [optional] 
**uri** | str,  | str,  | URI [6xx s1] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjectName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localNote

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[generalNotes](#generalNotes)** | list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | [optional] 
**audienceNote** | str,  | str,  | Target Audience Note [v521sa] | [optional] 
**[dissertationNotes](#dissertationNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[castNotes](#castNotes)** | list, tuple,  | tuple,  | Cast Notes [v511sa] | [optional] 
**[performerNotes](#performerNotes)** | list, tuple,  | tuple,  | Performers Notes [v511sa] | [optional] 
**participantNote** | str,  | str,  | Participants Notes [v511sa] | [optional] 
**[eventNotes](#eventNotes)** | list, tuple,  | tuple,  |  | [optional] 
**creditNotes** | str,  | str,  | Production Credits Notes [v508sa] | [optional] 
**[scaleNotes](#scaleNotes)** | list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | [optional] 
**[reproductionNotes](#reproductionNotes)** | list, tuple,  | tuple,  | Reproduction Notes [v533] | [optional] 
**[useAndReproductionNotes](#useAndReproductionNotes)** | list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | [optional] 
**[useownershipAndCustodialHistories](#useownershipAndCustodialHistories)** | list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | [optional] 
**systemDetailNote** | str,  | str,  | System Details Note [v538sa,u,i] | [optional] 
**awardNote** | str,  | str,  | Awards Note [v586sa] | [optional] 
**[languageNotes](#languageNotes)** | list, tuple,  | tuple,  | language note [v546sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# generalNotes

General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | 

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
**text** | str,  | str,  |  | [optional] 
**private** | bool,  | BoolClass,  | 1st indicator of 590 | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dissertationNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

# items

Disseration notes [v502sa,b,c,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disserationNote** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**institution** | str,  | str,  |  | [optional] 
**year** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**miscellaneousInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# castNotes

Cast Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cast Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# performerNotes

Performers Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Performers Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# eventNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

# items

Notes about event [v518sa,d,o,p,3]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**compositeNote** | str,  | str,  |  | [optional] 
**eventDate** | str,  | str,  |  | [optional] 
**eventPlace** | str,  | str,  |  | [optional] 
**eventInfo** | str,  | str,  |  | [optional] 
**material** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scaleNotes

Scale Note for Graphic Material [v507sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reproductionNotes

Reproduction Notes [v533]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Reproduction Notes [v533] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Reproduction Note [v533] | 

# useAndReproductionNotes

Terms Governing Use and Reproduction [v540sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# useownershipAndCustodialHistories

Ownership and Custodial History [v561sa,3,5,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# languageNotes

language note [v546sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | language note [v546sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# localGenres

Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### retrieve_bib.ApiResponseFor400
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

#### retrieve_bib.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_bib.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_bib.ApiResponseFor404
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

#### retrieve_bib.ApiResponseFor405
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

#### retrieve_bib.ApiResponseFor406
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

#### retrieve_bib.ApiResponseFor500
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

# **retrieve_brief_bib**
<a id="retrieve_brief_bib"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_brief_bib(oclc_number)

Retrieve specific Bibliographic Resource

Retrieve specific Bibliographic Resource

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import bibliographic_resources_api
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
    api_instance = bibliographic_resources_api.BibliographicResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'oclcNumber': 41266045,
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Retrieve specific Bibliographic Resource
        api_response = api_instance.retrieve_brief_bib(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_brief_bib: %s\n" % e)

    # example passing only optional values
    path_params = {
        'oclcNumber': 41266045,
    }
    query_params = {
        'showHoldingsIndicators': False,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Retrieve specific Bibliographic Resource
        api_response = api_instance.retrieve_brief_bib(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_brief_bib: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
showHoldingsIndicators | ShowHoldingsIndicatorsSchema | | optional


# ShowHoldingsIndicatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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
oclcNumber | OclcNumberSchema | | 

# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_brief_bib.ApiResponseFor200) | successful request for brief-bib result set
400 | [ApiResponseFor400](#retrieve_brief_bib.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#retrieve_brief_bib.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#retrieve_brief_bib.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_brief_bib.ApiResponseFor404) | Failed operation - resource not found
405 | [ApiResponseFor405](#retrieve_brief_bib.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#retrieve_brief_bib.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#retrieve_brief_bib.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### retrieve_brief_bib.ApiResponseFor200
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

#### retrieve_brief_bib.ApiResponseFor400
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

#### retrieve_brief_bib.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_brief_bib.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_brief_bib.ApiResponseFor404
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

#### retrieve_brief_bib.ApiResponseFor405
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

#### retrieve_brief_bib.ApiResponseFor406
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

#### retrieve_brief_bib.ApiResponseFor500
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

# **retrieve_other_editions**
<a id="retrieve_other_editions"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} retrieve_other_editions(oclc_number)

Retrieve Other Editions related to a particular Bibliographic Resource

Retrieve Other Editions related to a particular Bibliographic Resource

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import bibliographic_resources_api
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
    api_instance = bibliographic_resources_api.BibliographicResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'oclcNumber': 41266045,
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # Retrieve Other Editions related to a particular Bibliographic Resource
        api_response = api_instance.retrieve_other_editions(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_other_editions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'oclcNumber': 41266045,
    }
    query_params = {
        'deweyNumber': [870],
        'datePublished': [2000],
        'heldByGroup': "ASRL",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'inLanguage': ["eng"],
        'inCatalogLanguage': "eng",
        'materialType': "URL",
        'catalogSource': "OCL",
        'itemType': ["book"],
        'itemSubType': ["book-digital"],
        'retentionCommitments': False,
        'spProgram': "WEST",
        'genre': "fiction",
        'topic': "34000000",
        'subtopic': "34932000",
        'audience': "juv",
        'content': ["fic"],
        'openAccess': True,
        'peerReviewed': True,
        'facets': ["creator"],
        'groupVariantRecords': False,
        'preferredLanguage': "fre",
        'showHoldingsIndicators': False,
        'offset': 10,
        'limit': 50,
        'orderBy': "language",
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Retrieve Other Editions related to a particular Bibliographic Resource
        api_response = api_instance.retrieve_other_editions(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->retrieve_other_editions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
deweyNumber | DeweyNumberSchema | | optional
datePublished | DatePublishedSchema | | optional
heldByGroup | HeldByGroupSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
inLanguage | InLanguageSchema | | optional
inCatalogLanguage | InCatalogLanguageSchema | | optional
materialType | MaterialTypeSchema | | optional
catalogSource | CatalogSourceSchema | | optional
itemType | ItemTypeSchema | | optional
itemSubType | ItemSubTypeSchema | | optional
retentionCommitments | RetentionCommitmentsSchema | | optional
spProgram | SpProgramSchema | | optional
genre | GenreSchema | | optional
topic | TopicSchema | | optional
subtopic | SubtopicSchema | | optional
audience | AudienceSchema | | optional
content | ContentSchema | | optional
openAccess | OpenAccessSchema | | optional
peerReviewed | PeerReviewedSchema | | optional
facets | FacetsSchema | | optional
groupVariantRecords | GroupVariantRecordsSchema | | optional
preferredLanguage | PreferredLanguageSchema | | optional
showHoldingsIndicators | ShowHoldingsIndicatorsSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
orderBy | OrderBySchema | | optional


# DeweyNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DatePublishedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# InLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# InCatalogLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaterialTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CatalogSourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ItemTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filter values for General Format | must be one of ["archv", "artchapter", "audiobook", "book", "compfile", "encyc", "game", "image", "intmm", "jrnl", "kit", "map", "msscr", "music", "news", "object", "snd", "toy", "video", "vis", "web", ] 

# ItemSubTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Facet values returned and possible filter Values itemSubType [Admin/OCLCDef/StdRT1 + Admin/OCLCDef/StdRT2] | must be one of ["archv-digital", "archv-", "artchap-artcl", "artchap-chptr", "artchap-digital", "artchap-mss", "audiobook-cd", "audiobook-cassette", "audiobook-digital", "audiobook-lp", "audiobook-", "book-printbook", "book-digital", "book-mic", "book-thsis", "book-mss", "book-largeprint", "book-braille", "book-continuing", "book-", "compfile-digital", "compfile-", "encyc-", "game-digital", "game-", "image-2d", "intmm-digital", "intmm-", "jrnl-print", "jrnl-digital", "kit-", "map-", "map-mss", "map-digital", "msscr-digital", "msscr-mss", "msscr-", "music-cd", "music-lp", "music-digital", "music-cassette", "music-", "news-digital", "news-print", "object-digital", "object-", "snd-", "snd-rec", "toy-", "video-dvd", "video-vhs", "video-digital", "video-film", "video-bluray", "video-", "vis-digital", "vis-", "web-digital", "web-dwn2d", "web-", ] 

# RetentionCommitmentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# SpProgramSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GenreSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TopicSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubtopicSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AudienceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["juv", "nonJuv", ] 

# ContentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["fic", "nonFic", "bio", ] 

# OpenAccessSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PeerReviewedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FacetsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["subject", "creator", "datePublished", "genre", "itemType", "itemSubTypeBrief", "itemSubType", "language", "topic", "subtopic", "content", "audience", "databases", ] 

# GroupVariantRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PreferredLanguageSchema

three character MARC code for language to prefer records in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | three character MARC code for language to prefer records in | 

# ShowHoldingsIndicatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["library", "recency", "bestMatch", "creator", "publicationDateAsc", "publicationDateDesc", "language", "mostWidelyHeld", "title", ] if omitted the server will use the default value of "publicationDateDesc"

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
oclcNumber | OclcNumberSchema | | 

# OclcNumberSchema

the oclc number of a given bibliographic record

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#retrieve_other_editions.ApiResponseFor200) | successful request for other editions
400 | [ApiResponseFor400](#retrieve_other_editions.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#retrieve_other_editions.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#retrieve_other_editions.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#retrieve_other_editions.ApiResponseFor404) | Failed operation - resource not found
405 | [ApiResponseFor405](#retrieve_other_editions.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#retrieve_other_editions.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#retrieve_other_editions.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### retrieve_other_editions.ApiResponseFor200
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

#### retrieve_other_editions.ApiResponseFor400
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

#### retrieve_other_editions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_other_editions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### retrieve_other_editions.ApiResponseFor404
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

#### retrieve_other_editions.ApiResponseFor405
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

#### retrieve_other_editions.ApiResponseFor406
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

#### retrieve_other_editions.ApiResponseFor500
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

# **search_bibs**
<a id="search_bibs"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} search_bibs(q)

Search Bibliographic Resources

Search Bibliographic Resources. Key Indexes <table cellspacing=\"0\"> <tbody><tr><th>Index Name</th> <th>Index Code</th> </tr> <tr><td>Author</td> <td>au</td> </tr><tr><td>Corporate/Conference Name</td> <td>cn</td> </tr><tr><td>ISBN</td> <td>bn</td> </tr><tr><td>ISSN</td> <td>in</td> </tr><tr><td>Keyword</td> <td>kw</td> </tr><tr><td>LCCN</td> <td>dn</td> </tr><tr><td>Notes</td> <td>nt</td> </tr><tr><td>OCLC Number</td> <td>sno</td> </tr><tr><td>Place of publication</td> <td>pl</td> </tr><tr><td>Publisher</td> <td>pb</td> </tr><tr><td>Series</td> <td>se</td> </tr><tr><td>Standard Number</td> <td>sn</td> </tr><tr><td>Subject</td> <td>su</td> </tr><tr><td>Title</td> <td>ti</td> </tr></tbody></table>        

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import bibliographic_resources_api
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
    api_instance = bibliographic_resources_api.BibliographicResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'q': "ti: Simon's Cat",
    }
    header_params = {
    }
    try:
        # Search Bibliographic Resources
        api_response = api_instance.search_bibs(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->search_bibs: %s\n" % e)

    # example passing only optional values
    query_params = {
        'q': "ti: Simon's Cat",
        'deweyNumber': [870],
        'datePublished': [2000],
        'heldByGroup': "ASRL",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'inLanguage': ["eng"],
        'inCatalogLanguage': "eng",
        'materialType': "URL",
        'catalogSource': "OCL",
        'itemType': ["book"],
        'itemSubType': ["book-digital"],
        'retentionCommitments': False,
        'spProgram': "WEST",
        'facets': ["creator"],
        'groupRelatedEditions': False,
        'groupVariantRecords': False,
        'preferredLanguage': "fre",
        'orderBy': "bestMatch",
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Search Bibliographic Resources
        api_response = api_instance.search_bibs(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->search_bibs: %s\n" % e)
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
q | QSchema | | 
deweyNumber | DeweyNumberSchema | | optional
datePublished | DatePublishedSchema | | optional
heldByGroup | HeldByGroupSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
inLanguage | InLanguageSchema | | optional
inCatalogLanguage | InCatalogLanguageSchema | | optional
materialType | MaterialTypeSchema | | optional
catalogSource | CatalogSourceSchema | | optional
itemType | ItemTypeSchema | | optional
itemSubType | ItemSubTypeSchema | | optional
retentionCommitments | RetentionCommitmentsSchema | | optional
spProgram | SpProgramSchema | | optional
facets | FacetsSchema | | optional
groupRelatedEditions | GroupRelatedEditionsSchema | | optional
groupVariantRecords | GroupVariantRecordsSchema | | optional
preferredLanguage | PreferredLanguageSchema | | optional
orderBy | OrderBySchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeweyNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DatePublishedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# InLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# InCatalogLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaterialTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CatalogSourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ItemTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filter values for General Format | must be one of ["archv", "artchapter", "audiobook", "book", "compfile", "encyc", "game", "image", "intmm", "jrnl", "kit", "map", "msscr", "music", "news", "object", "snd", "toy", "video", "vis", "web", ] 

# ItemSubTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Facet values returned and possible filter Values itemSubType [Admin/OCLCDef/StdRT1 + Admin/OCLCDef/StdRT2] | must be one of ["archv-digital", "archv-", "artchap-artcl", "artchap-chptr", "artchap-digital", "artchap-mss", "audiobook-cd", "audiobook-cassette", "audiobook-digital", "audiobook-lp", "audiobook-", "book-printbook", "book-digital", "book-mic", "book-thsis", "book-mss", "book-largeprint", "book-braille", "book-continuing", "book-", "compfile-digital", "compfile-", "encyc-", "game-digital", "game-", "image-2d", "intmm-digital", "intmm-", "jrnl-print", "jrnl-digital", "kit-", "map-", "map-mss", "map-digital", "msscr-digital", "msscr-mss", "msscr-", "music-cd", "music-lp", "music-digital", "music-cassette", "music-", "news-digital", "news-print", "object-digital", "object-", "snd-", "snd-rec", "toy-", "video-dvd", "video-vhs", "video-digital", "video-film", "video-bluray", "video-", "vis-digital", "vis-", "web-digital", "web-dwn2d", "web-", ] 

# RetentionCommitmentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# SpProgramSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FacetsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["subject", "creator", "datePublished", "genre", "itemType", "itemSubTypeBrief", "itemSubType", "language", "topic", "subtopic", "content", "audience", "databases", ] 

# GroupRelatedEditionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# GroupVariantRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PreferredLanguageSchema

three character MARC code for language to prefer records in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | three character MARC code for language to prefer records in | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["library", "recency", "bestMatch", "creator", "publicationDateAsc", "publicationDateDesc", "mostWidelyHeld", "title", ] if omitted the server will use the default value of "bestMatch"

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
200 | [ApiResponseFor200](#search_bibs.ApiResponseFor200) | successful request for bib result set
400 | [ApiResponseFor400](#search_bibs.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#search_bibs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_bibs.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#search_bibs.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#search_bibs.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#search_bibs.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### search_bibs.ApiResponseFor200
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
**[bibRecords](#bibRecords)** | list, tuple,  | tuple,  |  | [optional] 
**[searchFacets](#searchFacets)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bibRecords

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
**[identifier](#identifier)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[title](#title)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[contributor](#contributor)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subjects](#subjects)** | list, tuple,  | tuple,  |  | [optional] 
**[classification](#classification)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[publishers](#publishers)** | list, tuple,  | tuple,  |  | [optional] 
**[date](#date)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[language](#language)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[edition](#edition)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[source](#source)** | list, tuple,  | tuple,  |  | [optional] 
**[note](#note)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[format](#format)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[musicInfo](#musicInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[digitalAccessAndLocations](#digitalAccessAndLocations)** | list, tuple,  | tuple,  |  | [optional] 
**[description](#description)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[related](#related)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z) | [optional] 
**[work](#work)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[editionCluster](#editionCluster)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**totalEditions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of editions in the workgroup | [optional] value must be a 32 bit integer
**[database](#database)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localTitle](#localTitle)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localContributor](#localContributor)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localSubjects](#localSubjects)** | list, tuple,  | tuple,  |  | [optional] 
**[localNote](#localNote)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[localGenres](#localGenres)** | list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# identifier

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | OCLC Number [Admin/BaseOCLCNo || Admin/OCLCNo || C001] | [optional] value must be a 64 bit integer
**lccn** | str,  | str,  | Library of Congress Control Number [v010sa] | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[externalIdentifiers](#externalIdentifiers)** | list, tuple,  | tuple,  | External System Control Number [v029sa,b,c,t] | [optional] 
**[otherStandardIdentifiers](#otherStandardIdentifiers)** | list, tuple,  | tuple,  | Other Standard Identifier [v024sa] | [optional] 
**[dois](#dois)** | list, tuple,  | tuple,  | Digital Object Identifier [v901sb v024sa] | [optional] 
**[mergedOclcNumbers](#mergedOclcNumbers)** | list, tuple,  | tuple,  | Merged OCLC numbers [v019sa] | [optional] 
**[gpoNumber](#gpoNumber)** | list, tuple,  | tuple,  | GPO Item number [v074sa] | [optional] 
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

# externalIdentifiers

External System Control Number [v029sa,b,c,t]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | External System Control Number [v029sa,b,c,t] | 

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
**oclcSymbol** | str,  | str,  |  | [optional] 
**systemControlNumber** | str,  | str,  |  | [optional] 
**oaiSetName** | str,  | str,  |  | [optional] 
**contentTypeId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# otherStandardIdentifiers

Other Standard Identifier [v024sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Other Standard Identifier [v024sa] | 

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
**type** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dois

Digital Object Identifier [v901sb v024sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Digital Object Identifier [v901sb v024sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# gpoNumber

GPO Item number [v074sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | GPO Item number [v074sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# title

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mainTitles](#mainTitles)** | list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | [optional] 
**[seriesTitles](#seriesTitles)** | list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | [optional] 
**[uniformTitles](#uniformTitles)** | list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | [optional] 
**[additionalTitles](#additionalTitles)** | list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mainTitles

Main Titles [v245sa,b,c,f,g,k,n,p,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# seriesTitles

Series Titles [(v490,v810,v830 - sa,v)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | 

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
**seriesTitle** | str,  | str,  | [(v490,v810,v830 - sa)] | [optional] 
**volume** | str,  | str,  | [(v490,v810,v830 - sv)] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# uniformTitles

Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) && v240sa,d,f,g,k,l,m,n,o,p,r,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalTitles

Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contributor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[creators](#creators)** | list, tuple,  | tuple,  | Creators of work | [optional] 
**[additionalCreators](#additionalCreators)** | list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | [optional] 
**[statementOfResponsibility](#statementOfResponsibility)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creators

Creators of work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Creators of work | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

# items

[v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[firstName](#firstName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[secondName](#secondName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[nonPersonName](#nonPersonName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**[creatorNotes](#creatorNotes)** | list, tuple,  | tuple,  | subfield d | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  | subfield e | [optional] 
**affiliation** | str,  | str,  | subfield u | [optional] 
**isPrimary** | bool,  | BoolClass,  | whether or not this contributor is the primary one (the 1xx) | [optional] 
**[relatedItem](#relatedItem)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firstName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# secondName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nonPersonName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creatorNotes

subfield d

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield d | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relators

subfield e

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield e | 

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# additionalCreators

Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statementOfResponsibility

245 |c

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

# items

Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[subjectName](#subjectName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**vocabulary** | str,  | str,  | subject authority vocabularies (MESH, FAST, LCSH, RVM) | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**subjectType** | str,  | str,  |  | [optional] 
**uri** | str,  | str,  | URI [6xx s1] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjectName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classification

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dewey** | str,  | str,  | Dewey Decimal Classification Number [v082sa,b] | [optional] 
**lc** | str,  | str,  | Library of Congress Call Number [v050sa,b] | [optional] 
**nlm** | str,  | str,  | National Library of Medicine Call Number [v060sa,b] | [optional] 
**[govDoc](#govDoc)** | list, tuple,  | tuple,  | Government Doc number [v086sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# govDoc

Government Doc number [v086sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Government Doc number [v086sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publishers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Publisher Information [v260sa,b v264sa,b v880sa,b] | 

# items

Publisher Information [v260sa,b v264sa,b v880sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Publisher Information [v260sa,b v264sa,b v880sa,b] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[publisherName](#publisherName)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Publisher Name [v260sb v264sb v880b] | [optional] 
**publicationPlace** | str,  | str,  | Publication Place [v260sa v264sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# publisherName

Publisher Name [v260sb v264sb v880b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Publisher Name [v260sb v264sb v880b] | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# date

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**publicationDate** | str,  | str,  | Date of Publication [v260sc || c008(bytes 07-14) || v264sc || v362sa] | [optional] 
**publicationSequentialDesignationDate** | str,  | str,  | Chronological issue designations [v362sa] | [optional] 
**currentPublicationFrequency** | str,  | str,  | Frequency of Publication [v310sa] | [optional] 
**createDate** | str,  | str,  | Date Record was Created [Admin/CreateDate] | [optional] 
**replaceDate** | str,  | str,  | Date Record was last Updated [Admin/ReplacedDate] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# language

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**itemLanguage** | str,  | str,  | Language of the item [v041sa,j] | [optional] 
**catalogingLanguage** | str,  | str,  | Language record was cataloged in [v040sb] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# edition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statement** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# source

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
**[supplements](#supplements)** | list, tuple,  | tuple,  | Supplements [v949sd] | [optional] 
**[firstPages](#firstPages)** | list, tuple,  | tuple,  | First Page [v949sf] | [optional] 
**[issueDates](#issueDates)** | list, tuple,  | tuple,  | Issue Dates [v949se] | [optional] 
**mainEntry** | str,  | str,  | Main Entry [v773sa] | [optional] 
**[otherPublicationData](#otherPublicationData)** | list, tuple,  | tuple,  | Other Publication Data [v799sa,d,g,o] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supplements

Supplements [v949sd]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplements [v949sd] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# firstPages

First Page [v949sf]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | First Page [v949sf] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issueDates

Issue Dates [v949se]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Issue Dates [v949se] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherPublicationData

Other Publication Data [v799sa,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Other Publication Data [v799sa,d,g,o] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  | Related Parts [v773sg] | [optional] 
**sourceTitle** | str,  | str,  | Source Title [v799st v773st] | [optional] 
**sourceIssn** | str,  | str,  | Source ISSN [v773sx] | [optional] 
**[sourceIsbns](#sourceIsbns)** | list, tuple,  | tuple,  | Source ISBNs [v799sz] | [optional] 
**sourceAuthor** | str,  | str,  | Source Author [v799sa] | [optional] 
**publicationInformation** | str,  | str,  | Publication Information [v773sd] | [optional] 
**[volumes](#volumes)** | list, tuple,  | tuple,  | Volumes [v799sm v949sa] | [optional] 
**[issues](#issues)** | list, tuple,  | tuple,  | Issues [v799sp v949sb] | [optional] 
**[pageRanges](#pageRanges)** | list, tuple,  | tuple,  | Page Range [v949sc] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedParts

Related Parts [v773sg]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Related Parts [v773sg] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# sourceIsbns

Source ISBNs [v799sz]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Source ISBNs [v799sz] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# volumes

Volumes [v799sm v949sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Volumes [v799sm v949sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# issues

Issues [v799sp v949sb]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Issues [v799sp v949sb] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# pageRanges

Page Range [v949sc]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Page Range [v949sc] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# note

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[generalNotes](#generalNotes)** | list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | [optional] 
**audienceNote** | str,  | str,  | Target Audience Note [v521sa] | [optional] 
**[dissertationNotes](#dissertationNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[castNotes](#castNotes)** | list, tuple,  | tuple,  | Cast Notes [v511sa] | [optional] 
**[performerNotes](#performerNotes)** | list, tuple,  | tuple,  | Performers Notes [v511sa] | [optional] 
**participantNote** | str,  | str,  | Participants Notes [v511sa] | [optional] 
**[eventNotes](#eventNotes)** | list, tuple,  | tuple,  |  | [optional] 
**creditNotes** | str,  | str,  | Production Credits Notes [v508sa] | [optional] 
**[scaleNotes](#scaleNotes)** | list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | [optional] 
**[reproductionNotes](#reproductionNotes)** | list, tuple,  | tuple,  | Reproduction Notes [v533] | [optional] 
**[useAndReproductionNotes](#useAndReproductionNotes)** | list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | [optional] 
**[useownershipAndCustodialHistories](#useownershipAndCustodialHistories)** | list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | [optional] 
**systemDetailNote** | str,  | str,  | System Details Note [v538sa,u,i] | [optional] 
**awardNote** | str,  | str,  | Awards Note [v586sa] | [optional] 
**[languageNotes](#languageNotes)** | list, tuple,  | tuple,  | language note [v546sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# generalNotes

General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | 

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
**text** | str,  | str,  |  | [optional] 
**private** | bool,  | BoolClass,  | 1st indicator of 590 | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dissertationNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

# items

Disseration notes [v502sa,b,c,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disserationNote** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**institution** | str,  | str,  |  | [optional] 
**year** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**miscellaneousInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# castNotes

Cast Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cast Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# performerNotes

Performers Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Performers Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# eventNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

# items

Notes about event [v518sa,d,o,p,3]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**compositeNote** | str,  | str,  |  | [optional] 
**eventDate** | str,  | str,  |  | [optional] 
**eventPlace** | str,  | str,  |  | [optional] 
**eventInfo** | str,  | str,  |  | [optional] 
**material** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scaleNotes

Scale Note for Graphic Material [v507sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reproductionNotes

Reproduction Notes [v533]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Reproduction Notes [v533] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Reproduction Note [v533] | 

# useAndReproductionNotes

Terms Governing Use and Reproduction [v540sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# useownershipAndCustodialHistories

Ownership and Custodial History [v561sa,3,5,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# languageNotes

language note [v546sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | language note [v546sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**generalFormat** | str,  | str,  | General Format Type [Admin/OCLCDef/StdRT] | [optional] must be one of ["Archv", "ArtChapter", "AudioBook", "Book", "CompFile", "Encyc", "Game", "Image", "IntMM", "Jrnl", "Kit", "Map", "MsScr", "Music", "News", "Object", "Snd", "Toy", "Video", "Vis", "Web", ] 
**specificFormat** | str,  | str,  | Specific Format Type [Admin/OCLCDef/StdRT2] | [optional] must be one of ["2D", "Artcl", "Bluray", "Braille", "Cassette", "CD", "Chptr", "Continuing", "Digital", "DVD", "Encyc", "Film", "LargePrint", "LP", "Mic", "mss", "PrintBook", "rec", "Thsis", "VHS", ] 
**[materialTypes](#materialTypes)** | list, tuple,  | tuple,  | Material Types [Admin/OCLCDef/MT[@form&#x3D;&#x27;gen&#x27;]] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# materialTypes

Material Types [Admin/OCLCDef/MT[@form='gen']]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Material Types [Admin/OCLCDef/MT[@form&#x3D;&#x27;gen&#x27;]] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# musicInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instrumentations](#instrumentations)** | list, tuple,  | tuple,  |  | [optional] 
**musicalKey** | str,  | str,  | Musical Key [v384sa] | [optional] 
**[instrumentsCodes](#instrumentsCodes)** | list, tuple,  | tuple,  | Musical Instruments [v048sa,b] | [optional] 
**numericDesignation** | str,  | str,  | Numeric Designation of Musical Work [v383sa,b,c] | [optional] 
**musicalPresentationStatement** | str,  | str,  | Musical Presentation Statement [v254sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instrumentations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Instrumentation [v382sa,b,d,e,n,p,r,s,t,v] | 

# items

Instrumentation [v382sa,b,d,e,n,p,r,s,t,v]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Instrumentation [v382sa,b,d,e,n,p,r,s,t,v] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mediumOfPerformance](#mediumOfPerformance)** | list, tuple,  | tuple,  |  | [optional] 
**[soloists](#soloists)** | list, tuple,  | tuple,  |  | [optional] 
**[doublingInstruments](#doublingInstruments)** | list, tuple,  | tuple,  |  | [optional] 
**[numberOfEnsemblesOfSameTypes](#numberOfEnsemblesOfSameTypes)** | list, tuple,  | tuple,  |  | [optional] 
**[numberOfPerformersOfSameMediums](#numberOfPerformersOfSameMediums)** | list, tuple,  | tuple,  |  | [optional] 
**[alternativeMediumOfPerformances](#alternativeMediumOfPerformances)** | list, tuple,  | tuple,  |  | [optional] 
**numberOfIndividualsPerforming** | str,  | str,  |  | [optional] 
**numberOfPerformers** | str,  | str,  |  | [optional] 
**numberOfEnsembles** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mediumOfPerformance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# soloists

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# doublingInstruments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# numberOfEnsemblesOfSameTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# numberOfPerformersOfSameMediums

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# alternativeMediumOfPerformances

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# instrumentsCodes

Musical Instruments [v048sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Musical Instruments [v048sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# digitalAccessAndLocations

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
**uri** | str,  | str,  | URI of resource [v856su] | 
**materialSpecified** | str,  | str,  | Materials specified |3 | [optional] 
**[instructions](#instructions)** | list, tuple,  | tuple,  | Instruction [v856si] | [optional] 
**[linkText](#linkText)** | list, tuple,  | tuple,  | Text associated with a link |y | [optional] 
**nonPublicNote** | str,  | str,  | Nonpublic note [v856sx] | [optional] 
**[publicNote](#publicNote)** | list, tuple,  | tuple,  | A note pertaining to the electronic location of the source identified in the field |z | [optional] 
**accessMethod** | str,  | str,  | Access method [v856s2] | [optional] 
**accessStatus** | str,  | str,  | Access method [v856s7] | [optional] 
**relationship** | str,  | str,  | Relationship to the item described in the record as a whole [v856 second indicator] | [optional] must be one of ["unknown", "resource", "version of resource", "related resource", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instructions

Instruction [v856si]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Instruction [v856si] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# linkText

Text associated with a link |y

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Text associated with a link |y | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# publicNote

A note pertaining to the electronic location of the source identified in the field |z

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A note pertaining to the electronic location of the source identified in the field |z | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# description

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**physicalDescription** | str,  | str,  | Physical Description [v300sa,b,c,d,e,f,g,3] | [optional] 
**digitalGraphicRepresentation** | str,  | str,  | Digital Graphic Representation [v352sa,b,c,i,q] | [optional] 
**[genres](#genres)** | list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | [optional] 
**[cartographicData](#cartographicData)** | list, tuple,  | tuple,  | Cartographic Mathematical Data [v255sa,b,c] | [optional] 
**[computerFilesCharacteristics](#computerFilesCharacteristics)** | list, tuple,  | tuple,  | Computer File Characteristics [v256sa] | [optional] 
**[formOfWorks](#formOfWorks)** | list, tuple,  | tuple,  | Form of Work [v380sa] | [optional] 
**[abstracts](#abstracts)** | list, tuple,  | tuple,  | Abstract [v520sa,b,c] | [optional] 
**[summaries](#summaries)** | list, tuple,  | tuple,  | Summary [v520sa,b,c] | [optional] 
**[contents](#contents)** | list, tuple,  | tuple,  |  | [optional] 
**[bibliographies](#bibliographies)** | list, tuple,  | tuple,  | Bibliography [v504sa] | [optional] 
**peerReviewed** | str,  | str,  | Is this a peer reviewed work [Admin/OCLCDef/PR] | [optional] must be one of ["Y", "N", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# genres

Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# cartographicData

Cartographic Mathematical Data [v255sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cartographic Mathematical Data [v255sa,b,c] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# computerFilesCharacteristics

Computer File Characteristics [v256sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Computer File Characteristics [v256sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# formOfWorks

Form of Work [v380sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Form of Work [v380sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# abstracts

Abstract [v520sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Abstract [v520sa,b,c] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# summaries

Summary [v520sa,b,c]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Summary [v520sa,b,c] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Formatted Contents Note [v505sa,t,r,g,u] | 

# items

Formatted Contents Note [v505sa,t,r,g,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Formatted Contents Note [v505sa,t,r,g,u] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[contentNote](#contentNote)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[miscellaneousInfo](#miscellaneousInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[statementsOfResponsibility](#statementsOfResponsibility)** | list, tuple,  | tuple,  |  | [optional] 
**[uris](#uris)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contentNote

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# miscellaneousInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# statementsOfResponsibility

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# uris

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# bibliographies

Bibliography [v504sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Bibliography [v504sa] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# related

Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Related [v787] Preceeding [v780] Succeeding [v785] (sa,b,c,d,g,h,i,k,m,n,o,r,s,t,u,w,x,y,z) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[relatedItems](#relatedItems)** | list, tuple,  | tuple,  |  | [optional] 
**[precedingEntries](#precedingEntries)** | list, tuple,  | tuple,  |  | [optional] 
**[succeedingEntries](#succeedingEntries)** | list, tuple,  | tuple,  |  | [optional] 
**[issuedWithEntries](#issuedWithEntries)** | list, tuple,  | tuple,  | [v777] | [optional] 
**[additionalPhysicalFormEntries](#additionalPhysicalFormEntries)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItems

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# precedingEntries

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# succeedingEntries

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
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# issuedWithEntries

[v777]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | [v777] | 

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
**displayConstant** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[recordControlOclcNumbers](#recordControlOclcNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[mainEntryHeadings](#mainEntryHeadings)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlOclcNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# mainEntryHeadings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalPhysicalFormEntries

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
**displayConstant** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[recordControlOclcNumbers](#recordControlOclcNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**[mainEntryHeadings](#mainEntryHeadings)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlOclcNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# mainEntryHeadings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Id of the workset [Admin/Work/ID] | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items in Workset [Admin/Work/Count] | [optional] value must be a 32 bit integer
**[articleCluster](#articleCluster)** | list, tuple,  | tuple,  | Items in Article Workset [WorkSet/NO] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# articleCluster

Items in Article Workset [WorkSet/NO]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Items in Article Workset [WorkSet/NO] | 

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
**databaseCollection** | str,  | str,  |  | [optional] 
**oclcNumber** | decimal.Decimal, int,  | decimal.Decimal,  | the oclc number of a given bibliographic record | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# editionCluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An id associated with a particular edition cluster [Admin/Edition/ID] | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of items in edition cluster | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# database

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | str,  | str,  | Source Collection [Admin/SourceCol] | [optional] 
**collection** | str,  | str,  | Db Collection [root collection attribute] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localTitle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mainTitles](#mainTitles)** | list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | [optional] 
**[seriesTitles](#seriesTitles)** | list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | [optional] 
**[uniformTitles](#uniformTitles)** | list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | [optional] 
**[additionalTitles](#additionalTitles)** | list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mainTitles

Main Titles [v245sa,b,c,f,g,k,n,p,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Main Titles [v245sa,b,c,f,g,k,n,p,s] | 

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
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# seriesTitles

Series Titles [(v490,v810,v830 - sa,v)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Series Titles [(v490,v810,v830 - sa,v)] | 

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
**seriesTitle** | str,  | str,  | [(v490,v810,v830 - sa)] | [optional] 
**volume** | str,  | str,  | [(v490,v810,v830 - sv)] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# uniformTitles

Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) && v240sa,d,f,g,k,l,m,n,o,p,r,s]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Uniform Titles [(v130,v730,v793,v799 - sa,d,f,g,k,l,m,n,o,p,r,s,t) &amp;&amp; v240sa,d,f,g,k,l,m,n,o,p,r,s] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# additionalTitles

Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Added Entry Uniform Titles [v730sa,d,f,g,k,l,m,n,o,p,r,s,i,t,x] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localContributor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[creators](#creators)** | list, tuple,  | tuple,  | Creators of work | [optional] 
**[additionalCreators](#additionalCreators)** | list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | [optional] 
**[statementOfResponsibility](#statementOfResponsibility)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creators

Creators of work

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Creators of work | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

# items

[v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | [v100sa,q,b,c,d,e,4,k v110sa,q,b,c,d,e,4,k,n v111sa,q,c,d,e,j,k,n v700sa,q,b,c,d,e,4,k v710sa,q,b,c,d,e,4,k,n v720sa v711 sa,q,c,d,e,j,k,n v790sa,q,c,d,e,j,k,n v791sa,q,b,c,d,e,4,k v792sa,b,q,c, d,e,j,k,n v796 sa,q,b,c,d,e,4,k v797sa,q,b,c,d,e,4,k,n v798sa,b,q,c, d,e,j,k,n] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[firstName](#firstName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[secondName](#secondName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[nonPersonName](#nonPersonName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**[creatorNotes](#creatorNotes)** | list, tuple,  | tuple,  | subfield d | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  | subfield e | [optional] 
**affiliation** | str,  | str,  | subfield u | [optional] 
**isPrimary** | bool,  | BoolClass,  | whether or not this contributor is the primary one (the 1xx) | [optional] 
**[relatedItem](#relatedItem)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firstName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# secondName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nonPersonName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# creatorNotes

subfield d

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield d | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relators

subfield e

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | subfield e | 

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relatedItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeOfRelationship** | str,  | str,  |  | [optional] 
**relatedItemTitle** | str,  | str,  |  | [optional] 
**[relationshipInfo](#relationshipInfo)** | list, tuple,  | tuple,  |  | [optional] 
**[relatedParts](#relatedParts)** | list, tuple,  | tuple,  |  | [optional] 
**mainEntryHeading** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  | Edition Statement [v250sa] | [optional] 
**qualifyingInfo** | str,  | str,  |  | [optional] 
**publicationInfo** | str,  | str,  |  | [optional] 
**physicalDescription** | str,  | str,  |  | [optional] 
**[seriesData](#seriesData)** | list, tuple,  | tuple,  |  | [optional] 
**materialSpecificDetail** | str,  | str,  |  | [optional] 
**[relatedItemNotes](#relatedItemNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[otherItemIdentifiers](#otherItemIdentifiers)** | list, tuple,  | tuple,  |  | [optional] 
**[reportNumbers](#reportNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**uniformTitle** | str,  | str,  |  | [optional] 
**standardTechReportNumber** | str,  | str,  |  | [optional] 
**[recordControlNumbers](#recordControlNumbers)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**coden** | str,  | str,  |  | [optional] 
**[isbns](#isbns)** | list, tuple,  | tuple,  | International Standard Book Number [v020sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relationshipInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedParts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# seriesData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# relatedItemNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# otherItemIdentifiers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reportNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# recordControlNumbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# additionalCreators

Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional creators of work [(v700,v710,v711,v790,v791,v792,v796,v797,v798) - sa,b,c,d,q,n,k,e,j,4] | 

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
**relationshipInfo** | str,  | str,  |  | [optional] 
**[titles](#titles)** | list, tuple,  | tuple,  |  | [optional] 
**[issns](#issns)** | list, tuple,  | tuple,  | International Standard Serial Numbers | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**relatedData** | str,  | str,  |  | [optional] 
**additionalRelationshipInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# titles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# statementOfResponsibility

245 |c

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | 245 |c | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localSubjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

# items

Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Subjects [v600sa,b,c,d,n,v,x,y,z,e,j,4 v610sa,b,n,v,x,y,z,e,j,4 v611sa,c,d,n,v,x,y,z,e,j,4 v630sa,d,e,f,k,l,m,n,o,d,p,r,s,v,x,y,z,e,j,4 v650sa,b,x,y,z,v,e,j,4 v651sa,x,y,z,v,e,j,4 v655sa,b,c,v,x,y,z,e,j,4 v648sa,v,w,x,y,z,e,j,4 v653sa,e,j,4 v656sa,k,v,x,y,z,3,e,j,4 v657sa,v,x,y,z,3,e,j,4 (v690,v691,v695,v696,v697,v698,v699 sa,b,c,d,e,f,k,l,m,n,o,p,r,s,v,x,y,z,e,j,4)] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[subjectName](#subjectName)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**vocabulary** | str,  | str,  | subject authority vocabularies (MESH, FAST, LCSH, RVM) | [optional] 
**[relators](#relators)** | list, tuple,  | tuple,  |  | [optional] 
**subjectType** | str,  | str,  |  | [optional] 
**uri** | str,  | str,  | URI [6xx s1] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subjectName

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  |  | [optional] 
**romanizedText** | str,  | str,  |  | [optional] 
**languageCode** | str,  | str,  |  | [optional] 
**textDirection** | str,  | str,  |  | [optional] must be one of ["RTL", "LTR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# relators

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
**term** | str,  | str,  |  | [optional] 
**alternateTerm** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localNote

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[generalNotes](#generalNotes)** | list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | [optional] 
**audienceNote** | str,  | str,  | Target Audience Note [v521sa] | [optional] 
**[dissertationNotes](#dissertationNotes)** | list, tuple,  | tuple,  |  | [optional] 
**[castNotes](#castNotes)** | list, tuple,  | tuple,  | Cast Notes [v511sa] | [optional] 
**[performerNotes](#performerNotes)** | list, tuple,  | tuple,  | Performers Notes [v511sa] | [optional] 
**participantNote** | str,  | str,  | Participants Notes [v511sa] | [optional] 
**[eventNotes](#eventNotes)** | list, tuple,  | tuple,  |  | [optional] 
**creditNotes** | str,  | str,  | Production Credits Notes [v508sa] | [optional] 
**[scaleNotes](#scaleNotes)** | list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | [optional] 
**[reproductionNotes](#reproductionNotes)** | list, tuple,  | tuple,  | Reproduction Notes [v533] | [optional] 
**[useAndReproductionNotes](#useAndReproductionNotes)** | list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | [optional] 
**[useownershipAndCustodialHistories](#useownershipAndCustodialHistories)** | list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | [optional] 
**systemDetailNote** | str,  | str,  | System Details Note [v538sa,u,i] | [optional] 
**awardNote** | str,  | str,  | Awards Note [v586sa] | [optional] 
**[languageNotes](#languageNotes)** | list, tuple,  | tuple,  | language note [v546sa] | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# generalNotes

General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | General Notes [v500sa, v501sa, v590sa,s3, (v59x sa-z)] | 

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
**text** | str,  | str,  |  | [optional] 
**private** | bool,  | BoolClass,  | 1st indicator of 590 | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dissertationNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

# items

Disseration notes [v502sa,b,c,d,g,o]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Disseration notes [v502sa,b,c,d,g,o] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**disserationNote** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**institution** | str,  | str,  |  | [optional] 
**year** | str,  | str,  |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**miscellaneousInfo** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# castNotes

Cast Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cast Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# performerNotes

Performers Notes [v511sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Performers Notes [v511sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# eventNotes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

# items

Notes about event [v518sa,d,o,p,3]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Notes about event [v518sa,d,o,p,3] | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**compositeNote** | str,  | str,  |  | [optional] 
**eventDate** | str,  | str,  |  | [optional] 
**eventPlace** | str,  | str,  |  | [optional] 
**eventInfo** | str,  | str,  |  | [optional] 
**material** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scaleNotes

Scale Note for Graphic Material [v507sa,b]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Scale Note for Graphic Material [v507sa,b] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# reproductionNotes

Reproduction Notes [v533]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Reproduction Notes [v533] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Reproduction Note [v533] | 

# useAndReproductionNotes

Terms Governing Use and Reproduction [v540sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Terms Governing Use and Reproduction [v540sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# useownershipAndCustodialHistories

Ownership and Custodial History [v561sa,3,5,u]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ownership and Custodial History [v561sa,3,5,u] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# languageNotes

language note [v546sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | language note [v546sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# localGenres

Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa]

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Genre of work [v655sa,b,v,x,y,z v380sa, (v600,v610,v611,v630,v648, v650,v651,v654 sv) v653sa] | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

#### search_bibs.ApiResponseFor400
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

#### search_bibs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_bibs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_bibs.ApiResponseFor405
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

#### search_bibs.ApiResponseFor406
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

#### search_bibs.ApiResponseFor500
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

# **search_brief_bibs**
<a id="search_brief_bibs"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} search_brief_bibs(q)

Search Brief Bibliographic Resources

Search Bibliographic Resources. Key Indexes <table cellspacing=\"0\"> <tbody><tr><th>Index Name</th> <th>Index Code</th> </tr> <tr><td>Author</td> <td>au</td> </tr><tr><td>Corporate/Conference Name</td> <td>cn</td> </tr><tr><td>ISBN</td> <td>bn</td> </tr><tr><td>ISSN</td> <td>in</td> </tr><tr><td>Keyword</td> <td>kw</td> </tr><tr><td>LCCN</td> <td>dn</td> </tr><tr><td>Notes</td> <td>nt</td> </tr><tr><td>OCLC Number</td> <td>sno</td> </tr><tr><td>Place of publication</td> <td>pl</td> </tr><tr><td>Publisher</td> <td>pb</td> </tr><tr><td>Series</td> <td>se</td> </tr><tr><td>Standard Number</td> <td>sn</td> </tr><tr><td>Subject</td> <td>su</td> </tr><tr><td>Title</td> <td>ti</td> </tr></tbody></table>        

### Example

* OAuth Authentication (worldcat_search_auth):
* OAuth Authentication (worldcat_search_auth):
```python
import openapi_client
from openapi_client.apis.tags import bibliographic_resources_api
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
    api_instance = bibliographic_resources_api.BibliographicResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'q': "ti: Simon's Cat",
    }
    header_params = {
    }
    try:
        # Search Brief Bibliographic Resources
        api_response = api_instance.search_brief_bibs(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->search_brief_bibs: %s\n" % e)

    # example passing only optional values
    query_params = {
        'q': "ti: Simon's Cat",
        'deweyNumber': [870],
        'datePublished': [2000],
        'heldByGroup': "ASRL",
        'heldBy': "TXH",
        'heldBySymbol': ["TXH"],
        'heldByInstitutionID': [128807],
        'inLanguage': ["eng"],
        'inCatalogLanguage': "eng",
        'materialType': "URL",
        'catalogSource': "OCL",
        'itemType': ["book"],
        'itemSubType': ["book-digital"],
        'retentionCommitments': False,
        'spProgram': "WEST",
        'facets': ["creator"],
        'groupRelatedEditions': False,
        'groupVariantRecords': False,
        'preferredLanguage': "fre",
        'showHoldingsIndicators': False,
        'orderBy': "bestMatch",
        'offset': 10,
        'limit': 50,
    }
    header_params = {
        'Accept': "application/json",
    }
    try:
        # Search Brief Bibliographic Resources
        api_response = api_instance.search_brief_bibs(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BibliographicResourcesApi->search_brief_bibs: %s\n" % e)
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
q | QSchema | | 
deweyNumber | DeweyNumberSchema | | optional
datePublished | DatePublishedSchema | | optional
heldByGroup | HeldByGroupSchema | | optional
heldBy | HeldBySchema | | optional
heldBySymbol | HeldBySymbolSchema | | optional
heldByInstitutionID | HeldByInstitutionIDSchema | | optional
inLanguage | InLanguageSchema | | optional
inCatalogLanguage | InCatalogLanguageSchema | | optional
materialType | MaterialTypeSchema | | optional
catalogSource | CatalogSourceSchema | | optional
itemType | ItemTypeSchema | | optional
itemSubType | ItemSubTypeSchema | | optional
retentionCommitments | RetentionCommitmentsSchema | | optional
spProgram | SpProgramSchema | | optional
facets | FacetsSchema | | optional
groupRelatedEditions | GroupRelatedEditionsSchema | | optional
groupVariantRecords | GroupVariantRecordsSchema | | optional
preferredLanguage | PreferredLanguageSchema | | optional
showHoldingsIndicators | ShowHoldingsIndicatorsSchema | | optional
orderBy | OrderBySchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeweyNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# DatePublishedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

# InLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# InCatalogLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MaterialTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CatalogSourceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ItemTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filter values for General Format | must be one of ["archv", "artchapter", "audiobook", "book", "compfile", "encyc", "game", "image", "intmm", "jrnl", "kit", "map", "msscr", "music", "news", "object", "snd", "toy", "video", "vis", "web", ] 

# ItemSubTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Facet values returned and possible filter Values itemSubType [Admin/OCLCDef/StdRT1 + Admin/OCLCDef/StdRT2] | must be one of ["archv-digital", "archv-", "artchap-artcl", "artchap-chptr", "artchap-digital", "artchap-mss", "audiobook-cd", "audiobook-cassette", "audiobook-digital", "audiobook-lp", "audiobook-", "book-printbook", "book-digital", "book-mic", "book-thsis", "book-mss", "book-largeprint", "book-braille", "book-continuing", "book-", "compfile-digital", "compfile-", "encyc-", "game-digital", "game-", "image-2d", "intmm-digital", "intmm-", "jrnl-print", "jrnl-digital", "kit-", "map-", "map-mss", "map-digital", "msscr-digital", "msscr-mss", "msscr-", "music-cd", "music-lp", "music-digital", "music-cassette", "music-", "news-digital", "news-print", "object-digital", "object-", "snd-", "snd-rec", "toy-", "video-dvd", "video-vhs", "video-digital", "video-film", "video-bluray", "video-", "vis-digital", "vis-", "web-digital", "web-dwn2d", "web-", ] 

# RetentionCommitmentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# SpProgramSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FacetsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["subject", "creator", "datePublished", "genre", "itemType", "itemSubTypeBrief", "itemSubType", "language", "topic", "subtopic", "content", "audience", "databases", ] 

# GroupRelatedEditionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# GroupVariantRecordsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PreferredLanguageSchema

three character MARC code for language to prefer records in

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | three character MARC code for language to prefer records in | 

# ShowHoldingsIndicatorsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["library", "recency", "bestMatch", "creator", "publicationDateAsc", "publicationDateDesc", "mostWidelyHeld", "title", ] if omitted the server will use the default value of "bestMatch"

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
200 | [ApiResponseFor200](#search_brief_bibs.ApiResponseFor200) | successful request for brief-bib result set
400 | [ApiResponseFor400](#search_brief_bibs.ApiResponseFor400) | Invalid query. The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#search_brief_bibs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#search_brief_bibs.ApiResponseFor403) | Forbidden
405 | [ApiResponseFor405](#search_brief_bibs.ApiResponseFor405) | Method not supported, see response Allow header
406 | [ApiResponseFor406](#search_brief_bibs.ApiResponseFor406) | Media type not supported
500 | [ApiResponseFor500](#search_brief_bibs.ApiResponseFor500) | Something went wrong (hopfully rare) - please try again

#### search_brief_bibs.ApiResponseFor200
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

#### search_brief_bibs.ApiResponseFor400
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

#### search_brief_bibs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_brief_bibs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### search_brief_bibs.ApiResponseFor405
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

#### search_brief_bibs.ApiResponseFor406
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

#### search_brief_bibs.ApiResponseFor500
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

