import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.bibs_retained_holdings import BibsRetainedHoldings
from openapi_client.apis.paths.bibs_summary_holdings import BibsSummaryHoldings
from openapi_client.apis.paths.bibs_holdings import BibsHoldings
from openapi_client.apis.paths.bibs_detailed_holdings import BibsDetailedHoldings
from openapi_client.apis.paths.bibs import Bibs
from openapi_client.apis.paths.bibs_oclc_number import BibsOclcNumber
from openapi_client.apis.paths.brief_bibs import BriefBibs
from openapi_client.apis.paths.brief_bibs_oclc_number import BriefBibsOclcNumber
from openapi_client.apis.paths.brief_bibs_oclc_number_other_editions import BriefBibsOclcNumberOtherEditions
from openapi_client.apis.paths.my_holdings_control_number import MyHoldingsControlNumber
from openapi_client.apis.paths.my_holdings import MyHoldings
from openapi_client.apis.paths.retained_holdings import RetainedHoldings

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.BIBSRETAINEDHOLDINGS: BibsRetainedHoldings,
        PathValues.BIBSSUMMARYHOLDINGS: BibsSummaryHoldings,
        PathValues.BIBSHOLDINGS: BibsHoldings,
        PathValues.BIBSDETAILEDHOLDINGS: BibsDetailedHoldings,
        PathValues.BIBS: Bibs,
        PathValues.BIBS_OCLC_NUMBER: BibsOclcNumber,
        PathValues.BRIEFBIBS: BriefBibs,
        PathValues.BRIEFBIBS_OCLC_NUMBER: BriefBibsOclcNumber,
        PathValues.BRIEFBIBS_OCLC_NUMBER_OTHEREDITIONS: BriefBibsOclcNumberOtherEditions,
        PathValues.MYHOLDINGS_CONTROL_NUMBER: MyHoldingsControlNumber,
        PathValues.MYHOLDINGS: MyHoldings,
        PathValues.RETAINEDHOLDINGS: RetainedHoldings,
    }
)

path_to_api = PathToApi(
    {
        PathValues.BIBSRETAINEDHOLDINGS: BibsRetainedHoldings,
        PathValues.BIBSSUMMARYHOLDINGS: BibsSummaryHoldings,
        PathValues.BIBSHOLDINGS: BibsHoldings,
        PathValues.BIBSDETAILEDHOLDINGS: BibsDetailedHoldings,
        PathValues.BIBS: Bibs,
        PathValues.BIBS_OCLC_NUMBER: BibsOclcNumber,
        PathValues.BRIEFBIBS: BriefBibs,
        PathValues.BRIEFBIBS_OCLC_NUMBER: BriefBibsOclcNumber,
        PathValues.BRIEFBIBS_OCLC_NUMBER_OTHEREDITIONS: BriefBibsOclcNumberOtherEditions,
        PathValues.MYHOLDINGS_CONTROL_NUMBER: MyHoldingsControlNumber,
        PathValues.MYHOLDINGS: MyHoldings,
        PathValues.RETAINEDHOLDINGS: RetainedHoldings,
    }
)
