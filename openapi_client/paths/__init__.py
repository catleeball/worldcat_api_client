# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    BIBSRETAINEDHOLDINGS = "/bibs-retained-holdings"
    BIBSSUMMARYHOLDINGS = "/bibs-summary-holdings"
    BIBSHOLDINGS = "/bibs-holdings"
    BIBSDETAILEDHOLDINGS = "/bibs-detailed-holdings"
    BIBS = "/bibs"
    BIBS_OCLC_NUMBER = "/bibs/{oclcNumber}"
    BRIEFBIBS = "/brief-bibs"
    BRIEFBIBS_OCLC_NUMBER = "/brief-bibs/{oclcNumber}"
    BRIEFBIBS_OCLC_NUMBER_OTHEREDITIONS = "/brief-bibs/{oclcNumber}/other-editions"
    MYHOLDINGS_CONTROL_NUMBER = "/my-holdings/{controlNumber}"
    MYHOLDINGS = "/my-holdings"
    RETAINEDHOLDINGS = "/retained-holdings"
