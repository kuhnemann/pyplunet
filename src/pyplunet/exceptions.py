from __future__ import annotations


class PlunetAPIError(Exception):
    status_message: str
    status_code: int
    status_code_alphanumeric: str

    def __str__(self):
        return f"Status code: {self.status_code}; Status code alphanumeric: {self.status_code_alphanumeric};  Status message: {self.status_message}"


class APISessionDoesNotExistOrIsInvalid(PlunetAPIError):
    status_code = -5
    status_code_alphanumeric = "GEN_2"
    status_message = "Session-UUID is invalid."


class InvalidCredentials(PlunetAPIError):
    status_code = -85
    status_code_alphanumeric = "GEN_3"
    status_message = "Invalid credentials."


class UserOfTheCurrentSessionIsNotActiveOrUndefined(PlunetAPIError):
    status_code = -11
    status_code_alphanumeric = "GEN_4"
    status_message = "The user of the current API session is undefined or inactive. API call  rejected."


class MissingRightsForAPIUser(PlunetAPIError):
    status_code = -12
    status_code_alphanumeric = "GEN_5"
    status_message = "The user of the current API session has not the necessary rights to call  this method."


class RequestedDataNotFound(PlunetAPIError):
    status_code = -4
    status_code_alphanumeric = "GEN_6"
    status_message = "The requested data does not exist."


class ParamEmptyOrInvalid(PlunetAPIError):
    status_code = -6
    status_code_alphanumeric = "GEN_7"
    status_message = "The transmitted method parameter was empty or invalid."


class ValueForTypeParameterIsInvalid(PlunetAPIError):
    status_code = -42
    status_code_alphanumeric = "GEN_8"
    status_message = "The transfered value (likely integer) is not valid for the used  operation. Please check the related Enum within the API documentation to  check for possible parameters."


class ValueNotNumeric(PlunetAPIError):
    status_code = -69
    status_code_alphanumeric = "GEN_9"
    status_message = "The transfered value must be numeric."


class ValueNotAvailable(PlunetAPIError):
    status_code = -70
    status_code_alphanumeric = "GEN_10"
    status_message = "Selected value must correspond to an available value."


class ParameterModificationInvalid(PlunetAPIError):
    status_code = -83
    status_code_alphanumeric = "GEN_11"
    status_message = "One or more parameters of the transfered object are not allowed to be  changed by the current user."


class ActionIsNotAllowedDueToObjectRelatedStatus(PlunetAPIError):
    status_code = -103
    status_code_alphanumeric = "GEN_12"
    status_message = "The action is not allowed due to the object related status."


class TypeCannotBeChangedViaUpdate(PlunetAPIError):
    status_code = -89
    status_code_alphanumeric = "GEN_13"
    status_message = "Certain type values cannot simply be changed with an update request. e.g.  the type of an address. In this case, you have to insert a new entry and  delete the old one."


class NoObjectIsInstanciatedForCurrentAPISession(PlunetAPIError):
    status_code = -2
    status_code_alphanumeric = "GEN_14"
    status_message = "There is no project/job/object fetched for the current API session.  Please fetch a project/job/object, before using this method."


class DataRecordIsNotLocked(PlunetAPIError):
    status_code = -13
    status_code_alphanumeric = "GEN_15"
    status_message = "The data record is not locked. Before working on the data record, you  have to lock it."


class FailedToLockDataSet(PlunetAPIError):
    status_code = -15
    status_code_alphanumeric = "GEN_16"
    status_message = "Failed to lock data-set. It seems to be another user is currently working  on it."


class DataLocked(PlunetAPIError):
    status_code = -45
    status_code_alphanumeric = "GEN_17"
    status_message = "Another user blocks the data entry. Cannot modify data."


class RelatedDataEntryCouldNotBeUnlockedAfterAction(PlunetAPIError):
    status_code = -106
    status_code_alphanumeric = "GEN_18"
    status_message = "The related data entry could not be unlocked after the action."


class ObjectWasCreatedWithMultipleIssues(PlunetAPIError):
    status_code = -27
    status_code_alphanumeric = "GEN_19"
    status_message = "Object was created with several errors."


class IncorrectOrCorruptTransferObject(PlunetAPIError):
    status_code = -41
    status_code_alphanumeric = "GEN_20"
    status_message = "The input object you transferred is incorrect or corrupted."


class InvalidPercentageNumber(PlunetAPIError):
    status_code = -102
    status_code_alphanumeric = "GEN_21"
    status_message = "The percentage value must be between 0% and 100%."


class SearchHasToContainAtLeastOneParameter(PlunetAPIError):
    status_code = -105
    status_code_alphanumeric = "GEN_22"
    status_message = "The search has to contain at least one parameter."


class PropertyNotFound(PlunetAPIError):
    status_code = -58
    status_code_alphanumeric = "GEN_23"
    status_message = "System cannot find the requested property."


class PropertyValueNotFound(PlunetAPIError):
    status_code = -59
    status_code_alphanumeric = "GEN_24"
    status_message = "Value is not defined for the property."


class PropertyUnavailable(PlunetAPIError):
    status_code = -60
    status_code_alphanumeric = "GEN_25"
    status_message = "Requested property is not available for the specified project. Please set  a customer first to create the related property fields."


class PropertyInactive(PlunetAPIError):
    status_code = -61
    status_code_alphanumeric = "GEN_26"
    status_message = "Property is not active for the PropertyUsageArea."


class PropertyIsAlreadySetByPriceList(PlunetAPIError):
    status_code = -88
    status_code_alphanumeric = "GEN_27"
    status_message = "Property is already set by the partner related pricelist."


class DataModificationInvalid(PlunetAPIError):
    status_code = -81
    status_code_alphanumeric = "GEN_28"
    status_message = "Data entry modification is not valid due to system regulations."


class DataNotFound(PlunetAPIError):
    status_code = -82
    status_code_alphanumeric = "GEN_29"
    status_message = "Requested data does not exist or no permission is granted."


class NoPricelistSetForRelatedObject(PlunetAPIError):
    status_code = -98
    status_code_alphanumeric = "GEN_30"
    status_message = "There is no pricelist set yet for the related object."


class DeliveryDateIsMissing(PlunetAPIError):
    status_code = -120
    status_code_alphanumeric = "GEN_31"
    status_message = "The delivery date is missing."


class TaxationTypeIsNotDefinied(PlunetAPIError):
    status_code = 1032
    status_code_alphanumeric = "GEN_32"
    status_message = "The TaxType is not definied."


class TimeFrameObjectIsInvalid(PlunetAPIError):
    status_code = 1033
    status_code_alphanumeric = "GEN_33"
    status_message = "TimeFrame Object is invalid."


class DataEntryCanNotBeUnlockedAsItIsLockedByAnotherUser(PlunetAPIError):
    status_code = 1034
    status_code_alphanumeric = "GEN_34"
    status_message = "The data entry can not be unlocked as it is locked by another user. This is likely  to happen if another user uses force rights to unlock this data-entry."


class DeliveryFailed(PlunetAPIError):
    status_code = 1035
    status_code_alphanumeric = "GEN_35"
    status_message = "Delivery failed"


class AccountsAreMissing(PlunetAPIError):
    status_code = 1036
    status_code_alphanumeric = "GEN_36"
    status_message = "There are no accounts within the system"


class StatusCouldNotBeChanged(PlunetAPIError):
    status_code = 1037
    status_code_alphanumeric = "GEN_37"
    status_message = "Status could not be changed"


class DataEntryCouldNotBeDeletedAsItIsInUseByTheApplication(PlunetAPIError):
    status_code = 1038
    status_code_alphanumeric = "GEN_38"
    status_message = (
        "Data entry could not be deleted, as it is still in use by the application"
    )


class DataEntryCouldNotBeDeletedAtTheCurrentStatus(PlunetAPIError):
    status_code = 1039
    status_code_alphanumeric = "GEN_39"
    status_message = "Data entry can not be deleted at the current status"


class CostCenterIsMissing(PlunetAPIError):
    status_code = 1040
    status_code_alphanumeric = "GEN_40"
    status_message = "Cost center is missing"


class MarkedForRequiredReviewBeforeSubmission(PlunetAPIError):
    status_code = 1041
    status_code_alphanumeric = "GEN_41"
    status_message = "Marked for a required review before any submission."


class OneOrManyMandatoryFieldsAreNotFilled(PlunetAPIError):
    status_code = 1042
    status_code_alphanumeric = "GEN_42"
    status_message = "One or many mandatory fields are not filled."


class TemplateCouldNotBeUsed(PlunetAPIError):
    status_code = 1043
    status_code_alphanumeric = "GEN_43"
    status_message = "Template could not be used"


class StartDateIsMissing(PlunetAPIError):
    status_code = 1044
    status_code_alphanumeric = "GEN_44"
    status_message = "Start date is missing"


class ObjectCouldNotBeCreated(PlunetAPIError):
    status_code = 1045
    status_code_alphanumeric = "GEN_45"
    status_message = "Object could not be created"


class TemplateAlreadyExists(PlunetAPIError):
    status_code = 1046
    status_code_alphanumeric = "GEN_46"
    status_message = "Template already exists"


class NoUserForAutomationIsSet(PlunetAPIError):
    status_code = 1047
    status_code_alphanumeric = "GEN_47"
    status_message = "No user for automation is set"


class ContactPersonCouldNotBeDeleted(PlunetAPIError):
    status_code = 1048
    status_code_alphanumeric = "GEN_48"
    status_message = "Contact person could not be deleted"


class InvalidStructure(PlunetAPIError):
    status_code = 1049
    status_code_alphanumeric = "GEN_49"
    status_message = "Invalid structure"


class DeliveryDeadlineIsMissing(PlunetAPIError):
    status_code = 1050
    status_code_alphanumeric = "GEN_50"
    status_message = "The delivery deadline is missing."


class RtfNotCreated(PlunetAPIError):
    status_code = 1051
    status_code_alphanumeric = "GEN_51"
    status_message = "RTF was not created."


class RoundModuleNotActive(PlunetAPIError):
    status_code = 1052
    status_code_alphanumeric = "GEN_52"
    status_message = "The round module is not active. For further information, please contact  the Plunet support."


class RequiredFieldIsEmpty(PlunetAPIError):
    status_code = 1053
    status_code_alphanumeric = "GEN_53"
    status_message = "A field required for this operation is empty."


class UserTypeInvalid(PlunetAPIError):
    status_code = 1054
    status_code_alphanumeric = "GEN_54"
    status_message = "The UserType is invalid."


class StandardContactPersonItemNotActive(PlunetAPIError):
    status_code = 1055
    status_code_alphanumeric = "GEN_55"
    status_message = "The option &#39;Item/Default contact person for jobs&#39; is not activated in your Plunet system.  Please activate it under Admin | Rights | Modules."


class InternalSystemError(PlunetAPIError):
    status_code = -3
    status_code_alphanumeric = "TEC_1"
    status_message = "An internal system error occurred. Please check the system logging file.  [Internal Error]"


class UndefinedError(PlunetAPIError):
    status_code = -100
    status_code_alphanumeric = "TEC_4"
    status_message = "UndefinedError for unknown error."


class DeadEndAndThereIsNoImplementation(PlunetAPIError):
    status_code = -999
    status_code_alphanumeric = "TEC_5"
    status_message = "Dead end and there is no implementation."


class CMS_Error(PlunetAPIError):
    status_code = -40
    status_code_alphanumeric = "TEC_1"
    status_message = "CMS error"


class Warning_ObjectCouldNotBePersistedAsTransferedAndGotSanitized(PlunetAPIError):
    status_code = -1000
    status_code_alphanumeric = "TEC_6"
    status_message = "Object could not be persisted as transferred and got sanitized."


class TypApiErrorNotMapped(PlunetAPIError):
    status_code = 2007
    status_code_alphanumeric = "TEC_7"
    status_message = "An old TypApiError is used that is not mapped to any APIError [Internal  Error]."


class ImplementationIsNotLongerSupportedInThisVersion(PlunetAPIError):
    status_code = 2008
    status_code_alphanumeric = "TEC_8"
    status_message = "The used API call can not be supported anymore. Please read the current api related release notes for further information."


class CallIsDeactivatedDueToSpecificRestrictionsPleaseCheckTheManual(PlunetAPIError):
    status_code = -1111
    status_code_alphanumeric = "TEC_9"
    status_message = "The requested call is deactivated due to special reasons/restrictions. Please check the           documentation/manual for further instructions."


class ExternalErrorCodeReference(PlunetAPIError):
    status_code = 2010
    status_code_alphanumeric = "TEC_10"
    status_message = "Implementation to forward external/and or specific error codes."


class UserIsNotMappedToAnyRightgroup(PlunetAPIError):
    status_code = 2010
    status_code_alphanumeric = "TEC_10"
    status_message = "Implementation to forward external/and or specific error codes."


class InternalSystemErrorWithReference(PlunetAPIError):
    status_code = 2012
    status_code_alphanumeric = "TEC_12"
    status_message = "An internal system error occurred."


class LocktypeInvalid(PlunetAPIError):
    status_code = 2013
    status_code_alphanumeric = "TEC_13"
    status_message = "Locktype is not valid."


class AuthenticationInvalidOrSystemUnavailable(PlunetAPIError):
    status_code = -52
    status_code_alphanumeric = "ADM_1"
    status_message = "The authentication details to the delivery system are invalid or the  webservice is unavailable."


class ExternalSystemURLHasToBeConfiguredToUseActionLinks(PlunetAPIError):
    status_code = -104
    status_code_alphanumeric = "ADM_2"
    status_message = (
        "External system URL has to be configured in order to use action links."
    )


class PriceListNotFound(PlunetAPIError):
    status_code = -36
    status_code_alphanumeric = "ADM_3"
    status_message = "System can&#39;t find the requested pricelist."


class PriceUnitNotFound(PlunetAPIError):
    status_code = -47
    status_code_alphanumeric = "ADM_4"
    status_message = "The system cannot find the price unit specified."


class PriceLineNotFound(PlunetAPIError):
    status_code = -107
    status_code_alphanumeric = "ADM_5"
    status_message = "Priceline does not exist."


class SystemLanguageUnknown(PlunetAPIError):
    status_code = -67
    status_code_alphanumeric = "ADM_6"
    status_message = "Could not identify the system language code."


class TargetLanguageUndefined(PlunetAPIError):
    status_code = -7
    status_code_alphanumeric = "ADM_7"
    status_message = "The requested target language is not defined in system."


class SourceLanguageUndefined(PlunetAPIError):
    status_code = -8
    status_code_alphanumeric = "ADM_8"
    status_message = "The requested source language is not defined in system."


class LanguageCombinationNotFound(PlunetAPIError):
    status_code = -25
    status_code_alphanumeric = "ADM_9"
    status_message = "The requested language combination is not available."


class CurrencyUnknown(PlunetAPIError):
    status_code = -43
    status_code_alphanumeric = "ADM_10"
    status_message = "The currency code does not exist in this system."


class CountryUnknown(PlunetAPIError):
    status_code = -44
    status_code_alphanumeric = "ADM_11"
    status_message = "The country does not exist in this system."


class PropertyValueIdInvalid(PlunetAPIError):
    status_code = -78
    status_code_alphanumeric = "ADM_12"
    status_message = "Invalid property value ID."


class PropertyAreaIdInvalid(PlunetAPIError):
    status_code = -79
    status_code_alphanumeric = "ADM_13"
    status_message = "Invalid PropertyUsageArea."


class PropertyAreaDoesNotSupportMultipleValueSelection(PlunetAPIError):
    status_code = -87
    status_code_alphanumeric = "ADM_14"
    status_message = "Not any PropertyUsageArea does support multiple value selection,  even if the property itself is configured for multiple selection."


class TextmoduleUsageAreaInvalid(PlunetAPIError):
    status_code = 3015
    status_code_alphanumeric = "ADM_15"
    status_message = "Invalid TextModuleUsageArea."


class TextmoduleNotFound(PlunetAPIError):
    status_code = -65
    status_code_alphanumeric = "ADM_16"
    status_message = (
        "The textmodule does not exist or is invisible to the current user."
    )


class TextmoduleMissingRights(PlunetAPIError):
    status_code = -66
    status_code_alphanumeric = "ADM_17"
    status_message = "Missing rights for the current user to edit the textmodule."


class TextmoduleNoListboxOrNotConfiguredForMultipleValues(PlunetAPIError):
    status_code = -68
    status_code_alphanumeric = "ADM_18"
    status_message = "The textmodule is not a list box or is not configured for multiple  selection values."


class MainTextmoduleRequiresValue(PlunetAPIError):
    status_code = -71
    status_code_alphanumeric = "ADM_19"
    status_message = "Textmodule is connected to a main text module which requires a selected  value."


class CompanyCodesAreNotActivated(PlunetAPIError):
    status_code = -106
    status_code_alphanumeric = "ADM_20"
    status_message = "Company codes are not activated in this system."


class PaymentMethodNotFound(PlunetAPIError):
    status_code = 3021
    status_code_alphanumeric = "ADM_21"
    status_message = (
        "The payment method does not exist or is invisible to the current user."
    )


class TextmoduleSelectionOrInputValueIsInvalid(PlunetAPIError):
    status_code = 3022
    status_code_alphanumeric = "ADM_22"
    status_message = "Textmodule selection or input value is invalid."


class EMailUserWasNotFound(PlunetAPIError):
    status_code = 3023
    status_code_alphanumeric = "ADM_23"
    status_message = "Email user was not found"


class EmailWrongSMTPActionForSending(PlunetAPIError):
    status_code = 3024
    status_code_alphanumeric = "ADM_24"
    status_message = "Wrong SMTP action for sending"


class EmailAlreadyWithinOutbox(PlunetAPIError):
    status_code = 3025
    status_code_alphanumeric = "ADM_25"
    status_message = "Email already within outbox"


class EmailNotFound(PlunetAPIError):
    status_code = 3026
    status_code_alphanumeric = "ADM_26"
    status_message = "Email not found"


class EmailNoRecipient(PlunetAPIError):
    status_code = 3027
    status_code_alphanumeric = "ADM_27"
    status_message = "Email no recipient"


class EmailCouldNotBeSendt(PlunetAPIError):
    status_code = 3028
    status_code_alphanumeric = "ADM_28"
    status_message = "Email could not be sent"


class PropertyIsReferencedAndCanNotBeDeleted(PlunetAPIError):
    status_code = 3029
    status_code_alphanumeric = "ADM_29"
    status_message = "Property is referenced and can not be deleted"


class PropertyOneOrManyAreMandatory(PlunetAPIError):
    status_code = 3030
    status_code_alphanumeric = "ADM_30"
    status_message = "One or many properties are mandatory"


class MissingLanguageFolder(PlunetAPIError):
    status_code = 3031
    status_code_alphanumeric = "ADM_31"
    status_message = "There is no folder name defined in &#39;Admin | Languages&#39;"


class NoDefaultProjectManagerConfigured(PlunetAPIError):
    status_code = 3032
    status_code_alphanumeric = "ADM_32"
    status_message = (
        "No product manager ID provided and no &lt;set in the customer profile."
    )


class InvalidDefaultProjectManagerSetting(PlunetAPIError):
    status_code = 3033
    status_code_alphanumeric = "ADM_33"
    status_message = "Invalid value for preselected project manager in Admin - Settings -  Orders. Must be &#39;account manager&#39; or &#39;project manager&#39;, or a project  manager ID must be provided in this call."


class InvalidConfiguration(PlunetAPIError):
    status_code = 3034
    status_code_alphanumeric = "ADM_34"
    status_message = "invalid configuration was tried to be applied"


class AdminAccountNotDefined(PlunetAPIError):
    status_code = 3035
    status_code_alphanumeric = "ADM_35"
    status_message = "Admin account not defined"


class CompanyCodeUnknown(PlunetAPIError):
    status_code = 3036
    status_code_alphanumeric = "ADM_36"
    status_message = "Company code unknown"


class MandatorNotActive(PlunetAPIError):
    status_code = 3037
    status_code_alphanumeric = "ADM_37"
    status_message = "Mandator not active"


class ConfidentialityInvalid(PlunetAPIError):
    status_code = 3038
    status_code_alphanumeric = "ADM_38"
    status_message = "Confidentiality invalid"


class SwitchingUserLanguageFailed(PlunetAPIError):
    status_code = 3039
    status_code_alphanumeric = "ADM_39"
    status_message = "Switching user language failed"


class ReachedMaximumOfUiLanguages(PlunetAPIError):
    status_code = 3040
    status_code_alphanumeric = "ADM_40"
    status_message = "Reached maximum size of ui languages (20)"


class PartnerNotFound(PlunetAPIError):
    status_code = -46
    status_code_alphanumeric = "PAR_1"
    status_message = "The system cannot find the partner specified."


class PartnerTypeInvalid(PlunetAPIError):
    status_code = 4002
    status_code_alphanumeric = "PAR_2"
    status_message = "Please use a valid PartnerType."


class PartnerEntryCouldNotBeDeleted(PlunetAPIError):
    status_code = -30
    status_code_alphanumeric = "PAR_3"
    status_message = "It is not possible to delete this resource/customer."


class RequestedAddressNotFound(PlunetAPIError):
    status_code = -31
    status_code_alphanumeric = "PAR_4"
    status_message = "The requested address does not exist."


class InvoiceOrDeliveryAddressAlreadyExists(PlunetAPIError):
    status_code = -90
    status_code_alphanumeric = "PAR_5"
    status_message = "The referenced partner is already linked to an existing invoice or  delivery address. Only AddressType.OTHER supports unlimited  address entries."


class ThereIsNoPartnerDatasetAvailableForTheCurrentApiSession(PlunetAPIError):
    status_code = -32
    status_code_alphanumeric = "PAR_6"
    status_message = "There is no customer/resource data set available for the current api  session. Please fetch a customer/resource data set, before using this  method."


class ThereIsNoAddressDatasetAvailableForTheCurrentApiSession(PlunetAPIError):
    status_code = -33
    status_code_alphanumeric = "PAR_7"
    status_message = "There is no address data set available for the current api session.  Please fetch a address data set, before using this method."


class FormOfAddressInvalid(PlunetAPIError):
    status_code = 4008
    status_code_alphanumeric = "PAR_8"
    status_message = "The FormOfAddressType is invalid."


class ContactPersonNotActive(PlunetAPIError):
    status_code = 4009
    status_code_alphanumeric = "PAR_9"
    status_message = "The ContactPersonStatus is not set to &#39;active&#39;."


class ResourceNotFound(PlunetAPIError):
    status_code = -28
    status_code_alphanumeric = "RES_1"
    status_message = "The requested resource is not available."


class ResourceIsMissing(PlunetAPIError):
    status_code = -94
    status_code_alphanumeric = "RES_2"
    status_message = "Resource is missing."


class ResourceCannotBeUsed(PlunetAPIError):
    status_code = -84
    status_code_alphanumeric = "RES_3"
    status_message = (
        "Resource can not be used due to dependencies like role or  ResourceStatus."
    )


class ResourceStatusNotActive(PlunetAPIError):
    status_code = -80
    status_code_alphanumeric = "RES_4"
    status_message = "The ResourceStatus is set to  ResourceStatus.NOT_ACTIVE_OR_OLD. Resource needs to be  ResourceStatus.ACTIVE in order to get set."


class NoContactPersonSet(PlunetAPIError):
    status_code = -108
    status_code_alphanumeric = "RES_5"
    status_message = "The contact person is not set/defined."


class ResourceStatusInvalid(PlunetAPIError):
    status_code = 5006
    status_code_alphanumeric = "RES_6"
    status_message = "The ResourceStatus is invalid."


class ResourceTypeInvalid(PlunetAPIError):
    status_code = 5007
    status_code_alphanumeric = "RES_7"
    status_message = "The ResourceType is invalid."


class ContactPersonNotFound(PlunetAPIError):
    status_code = 5008
    status_code_alphanumeric = "RES_8"
    status_message = "The contact person could not be found in the database."


class ResourceIsAlreadyAssignedToAnJobInTheSamePeriod(PlunetAPIError):
    status_code = 5009
    status_code_alphanumeric = "RES_9"
    status_message = "Resource is already assigned to an job in the same period"


class ContactPersonNotMatchingResource(PlunetAPIError):
    status_code = 5010
    status_code_alphanumeric = "RES_10"
    status_message = "The contact person has to be related to the resource."


class ResourceNotMemberOfProjectTeam(PlunetAPIError):
    status_code = 5011
    status_code_alphanumeric = "RES_11"
    status_message = "The resource cannot be set as the contact person for the job, because they are not a member  of the project team for this job."


class CustomerNotFound(PlunetAPIError):
    status_code = -29
    status_code_alphanumeric = "CUS_1"
    status_message = "The requested customer is not available."


class CustomerIsMissing(PlunetAPIError):
    status_code = -92
    status_code_alphanumeric = "CUS_2"
    status_message = "Customer is missing."


class CustomerContactUnknown(PlunetAPIError):
    status_code = -55
    status_code_alphanumeric = "CUS_3"
    status_message = "The specified customer contact is unknown."


class UuidCustomerMappingError(PlunetAPIError):
    status_code = -53
    status_code_alphanumeric = "CUS_4"
    status_message = "The specified UUID within the job xml cannot be mapped to an existing  Plunet customer."


class SystemMissingForCustomer(PlunetAPIError):
    status_code = -54
    status_code_alphanumeric = "CUS_5"
    status_message = "No Plunet system has been provided for the project customer."


class CustomerStatusInvalid(PlunetAPIError):
    status_code = 6006
    status_code_alphanumeric = "CUS_6"
    status_message = "The CustomerStatus is invalid."


class ContactPersonNotMatchingCustomer(PlunetAPIError):
    status_code = 6007
    status_code_alphanumeric = "CUS_7"
    status_message = (
        "The contact person has to be related to the customer of the project."
    )


class ProjectNotFound(PlunetAPIError):
    status_code = -38
    status_code_alphanumeric = "PRO_1"
    status_message = "System can&#39;t find the requested Project. Relates to:   OrderNotFound QuoteNotFound RequestNotFound"


class ProjectTypeInvalid(PlunetAPIError):
    status_code = -21
    status_code_alphanumeric = "PRO_2"
    status_message = "The ProjectType you have entered is invalid."


class ProjectTypeNotActive(PlunetAPIError):
    status_code = -91
    status_code_alphanumeric = "PRO_3"
    status_message = "The ProjectType is not set to &#39;active&#39;."


class CannotChangeProjectStatus(PlunetAPIError):
    status_code = -96
    status_code_alphanumeric = "PRO_4"
    status_message = "Only Projects with the ArchivStatus 2 or 6 can be archived."


class NoCustomerSetForProject(PlunetAPIError):
    status_code = -97
    status_code_alphanumeric = "PRO_5"
    status_message = "No customer is set for project."


class ProjectDescriptionIsMissing(PlunetAPIError):
    status_code = -93
    status_code_alphanumeric = "PRO_6"
    status_message = "The project description is missing."


class NoMasterProjectSpecified(PlunetAPIError):
    status_code = -57
    status_code_alphanumeric = "PRO_7"
    status_message = "No master project has been set for the current project."


class TemplateDoesNotExistOrNotAllowed(PlunetAPIError):
    status_code = -62
    status_code_alphanumeric = "PRO_8"
    status_message = "Template does not exist or the user is not allowed to access it."


class BudgetOverdrawn(PlunetAPIError):
    status_code = -95
    status_code_alphanumeric = "PRO_9"
    status_message = "Is caused when the budget overdrawn."


class ProjecttypeDoesNotExist(PlunetAPIError):
    status_code = -56
    status_code_alphanumeric = "PRO_9"
    status_message = "The ProjectType you have entered is invalid. Note: Duplicate -  Please use ProjectTypeInvalid."


class ProjectCategoryInvalid(PlunetAPIError):
    status_code = -21
    status_code_alphanumeric = "PRO_10"
    status_message = "The project category (see Admin | Miscellaneous | Project category) of  the project is invalid."


class ProjectCategoryNotSet(PlunetAPIError):
    status_code = -21
    status_code_alphanumeric = "PRO_11"
    status_message = "No project category has been set for the project."


class ArchivStatusNotActiveOrPreparation(PlunetAPIError):
    status_code = 7012
    status_code_alphanumeric = "PRO_12"
    status_message = "Cannot process operation. The ArchivStatus has to be set to  ArchivStatus.ACTIVE or ArchivStatus.IN_PREPARATION."


class ProjectManagerIsMissing(PlunetAPIError):
    status_code = 7013
    status_code_alphanumeric = "PRO_13"
    status_message = "There is no project manager selected."


class ProjectNameIsMissing(PlunetAPIError):
    status_code = 7014
    status_code_alphanumeric = "PRO_14"
    status_message = "Project name is missing"


class ProjectIdInvalid(PlunetAPIError):
    status_code = 7015
    status_code_alphanumeric = "PRO_15"
    status_message = "Project ID is missing."


class DateInvalid(PlunetAPIError):
    status_code = 7016
    status_code_alphanumeric = "PRO_16"
    status_message = "Date is invalid."


class FileNameMissing(PlunetAPIError):
    status_code = 7017
    status_code_alphanumeric = "PRO_17"
    status_message = "The file name is missing."


class ComplaintCreationFailed(PlunetAPIError):
    status_code = 7018
    status_code_alphanumeric = "PRO_18"
    status_message = "The creation of the claim failed."


class CommissionNotFound(PlunetAPIError):
    status_code = 7019
    status_code_alphanumeric = "PRO_19"
    status_message = "The commission has not been found."


class ProjectConsistsOfMultiplePackages(PlunetAPIError):
    status_code = 7020
    status_code_alphanumeric = "PRO_20"
    status_message = "Project cannot be delivered as it consists of multiple packages."


class CmsConfigInactive(PlunetAPIError):
    status_code = 7021
    status_code_alphanumeric = "PRO_21"
    status_message = "The cms configuration is not active."


class MasterProjectLimitedToCustomer(PlunetAPIError):
    status_code = 7022
    status_code_alphanumeric = "PRO_22"
    status_message = "This master project is limited to sub projects of same customer."


class ProjectFolderNotFound(PlunetAPIError):
    status_code = 7023
    status_code_alphanumeric = "PRO_23"
    status_message = "It is not possible to archive the order, because the order folder cannot  be found."


class ProjectIDDoesNotBelongToMasterProject(PlunetAPIError):
    status_code = 7023
    status_code_alphanumeric = "PRO_23"
    status_message = "The ID of the project does not belong to a master project."


class TemplateCointainsExternalResourceInProjectTeam(PlunetAPIError):
    status_code = 7024
    status_code_alphanumeric = "PRO_24"
    status_message = (
        "The project template contains external resources in the project team."
    )


class ProjectArchived(PlunetAPIError):
    status_code = 7025
    status_code_alphanumeric = "PRO_25"
    status_message = "The project cannot be modified because it is archived."


class RequestNotFound(PlunetAPIError):
    status_code = -24
    status_code_alphanumeric = "REQ_1"
    status_message = "System can&#39;t find the requested project request."


class QuoteNotFound(PlunetAPIError):
    status_code = -23
    status_code_alphanumeric = "QUO_1"
    status_message = "System can&#39;t find the requested quote."


class QuoteStatusNotNewPreparationOrCheckClearance(PlunetAPIError):
    status_code = 9002
    status_code_alphanumeric = "QUO_2"
    status_message = "Cannot process operation. QuoteStatusType has to be set to one of  the following status:"


class QuoteStatusNotAcceptedChangedOrCancelled(PlunetAPIError):
    status_code = 9003
    status_code_alphanumeric = "QUO_3"
    status_message = "Cannot process operation. QuoteStatusType has to be set to one of  the following status:"


class OrderNotFound(PlunetAPIError):
    status_code = -22
    status_code_alphanumeric = "ORD_1"
    status_message = "System can&#39;t find the requested order."


class OrderHasNoReferenceToRequest(PlunetAPIError):
    status_code = -19
    status_code_alphanumeric = "ORD_2"
    status_message = "There is no order for this request."


class LinksOnlySupportedBetweenOrders(PlunetAPIError):
    status_code = -20
    status_code_alphanumeric = "ORD_3"
    status_message = "Links are currently only supported between orders."


class OrderNotCreatedFromQuote(PlunetAPIError):
    status_code = 3
    status_code_alphanumeric = "ORD_3"
    status_message = "The order could not be created from this quote."


class JobNotFound(PlunetAPIError):
    status_code = -35
    status_code_alphanumeric = "JOB_1"
    status_message = "System can&#39;t find the requested job."


class JobTypeIsUndefinied(PlunetAPIError):
    status_code = -39
    status_code_alphanumeric = "JOB_2"
    status_message = "The JobType is undefined."


class JobStatusChangeImpossible(PlunetAPIError):
    status_code = -64
    status_code_alphanumeric = "JOB_3"
    status_message = "Changing the JobStatus is not possible."


class CannotEditWorkingTimes(PlunetAPIError):
    status_code = -101
    status_code_alphanumeric = "JOB_4"
    status_message = "In order to edit the job working times, the JobStatus has to be  set to 5, 6, 9, 10 or 11."


class JobNotCreated(PlunetAPIError):
    status_code = 14005
    status_code_alphanumeric = "JOB_5"
    status_message = "The job could not be created."


class JobTemplateNotFound(PlunetAPIError):
    status_code = 14006
    status_code_alphanumeric = "JOB_6"
    status_message = "The job-template could not be found"


class JobTemplateNoValid(PlunetAPIError):
    status_code = 14007
    status_code_alphanumeric = "JOB_7"
    status_message = "The job-template is not valid"


class JobCannotBeInvoicedToTheCostCenterForPayables(PlunetAPIError):
    status_code = 14008
    status_code_alphanumeric = "JOB_8"
    status_message = "The job cannot be invoiced to the cost center for payables."


class JobHasAlreadyBeenInvoiced(PlunetAPIError):
    status_code = 14009
    status_code_alphanumeric = "JOB_9"
    status_message = "This job has already been invoiced."


class ThereAreNoAvailableJobsIntoWhichResourcesCanBeEntered(PlunetAPIError):
    status_code = 14010
    status_code_alphanumeric = "JOB_10"
    status_message = "There are no available jobs into which resources can be entered."


class JobIsNotAssignedToAnyItem(PlunetAPIError):
    status_code = 14011
    status_code_alphanumeric = "JOB_11"
    status_message = "Job is not assigned to any item"


class JobCanNotBeRequestedAtThisStatus(PlunetAPIError):
    status_code = 14012
    status_code_alphanumeric = "JOB_12"
    status_message = "Job can not be requested at this status"


class AllPriceLinesAreZeroQuantityOrderJobRequestCancelled(PlunetAPIError):
    status_code = 14013
    status_code_alphanumeric = "JOB_13"
    status_message = (
        "All price lines are 0 -&gt; zero quantity order. Job request cancelled."
    )


class JobCanOnlyBeDeliveredAfterFileUpload(PlunetAPIError):
    status_code = 14014
    status_code_alphanumeric = "JOB_14"
    status_message = "Job can only be delivered after file upload."


class NoDeductionBonusCouldBeAppliedToTheJobBecauseTheJobHasAlreadyBeenInvoiced(
    PlunetAPIError
):
    status_code = 14015
    status_code_alphanumeric = "JOB_15"
    status_message = "No deduction/bonus could be applied to the job, because the job has already been invoiced."


class JobCanNotBeStartedDueToStatus(PlunetAPIError):
    status_code = 14016
    status_code_alphanumeric = "JOB_16"
    status_message = "Job can not be started due to status"


class JobIsNotInvoiced(PlunetAPIError):
    status_code = 14017
    status_code_alphanumeric = "JOB_17"
    status_message = "Job is not invoiced"


class JobQualityRatingMustBeClosedBeforeDelivery(PlunetAPIError):
    status_code = 14017
    status_code_alphanumeric = "JOB_17"
    status_message = "Job quality rating must be closed before delivery."


class RoundDoesNotExist(PlunetAPIError):
    status_code = 14019
    status_code_alphanumeric = "JOB_19"
    status_message = "Round does not exist"


class RoundRankingMethodPositionAlreadyExists(PlunetAPIError):
    status_code = 14020
    status_code_alphanumeric = "JOB_20"
    status_message = "Round ranking position already exists"


class RatingOutOfRange(PlunetAPIError):
    status_code = 14021
    status_code_alphanumeric = "JOB_21"
    status_message = "Rating out of range"


class JobCanNotBeDeliveredWithoutEnterintWorkingTimes(PlunetAPIError):
    status_code = 14022
    status_code_alphanumeric = "JOB_4"
    status_message = "In order to deliver the job, working times must be entered"


class JobStatusInvalid(PlunetAPIError):
    status_code = 14023
    status_code_alphanumeric = "JOB_23"
    status_message = "Job status is invalid."


class JobChecklistIncomplete(PlunetAPIError):
    status_code = 14024
    status_code_alphanumeric = "JOB_24"
    status_message = "Checklist of job is incomplete."


class RoundSearchCriteriaNotFound(PlunetAPIError):
    status_code = 14025
    status_code_alphanumeric = "JOB_25"
    status_message = "The search criteria of the round could not be found."


class RoundStatusInvalid(PlunetAPIError):
    status_code = 14026
    status_code_alphanumeric = "JOB_26"
    status_message = "Job round status is invalid."


class RoundRankingMethodInvalid(PlunetAPIError):
    status_code = 14027
    status_code_alphanumeric = "JOB_27"
    status_message = "Invalid value for the round ranking method. Please check  JobRequestRankingMethod for an overview of all available values."


class RoundAssignedNotFound(PlunetAPIError):
    status_code = 14028
    status_code_alphanumeric = "JOB_28"
    status_message = "There does no assigned round exist for this job."


class JobCannotBeDeletedDueToStatus(PlunetAPIError):
    status_code = 14029
    status_code_alphanumeric = "JOB_29"
    status_message = "You can only delete jobs with status &#39;in preparation&#39;."


class RoundAssignmentMethodInvalid(PlunetAPIError):
    status_code = 14030
    status_code_alphanumeric = "JOB_30"
    status_message = (
        "The current round assignment method is not supported for this  operation."
    )


class ResourceDoesNotMatchJobRoundCriteria(PlunetAPIError):
    status_code = 14031
    status_code_alphanumeric = "JOB_31"
    status_message = "The resource does not match the round criteria selected."


class RoundReviewNotFound(PlunetAPIError):
    status_code = 14032
    status_code_alphanumeric = "JOB_32"
    status_message = "No round with status &#39;review&#39; found for this job."


class JobIDNotFound(PlunetAPIError):
    status_code = 14033
    status_code_alphanumeric = "JOB_33"
    status_message = "The job ID does not exist."


class JobAssignmentIso17100(PlunetAPIError):
    status_code = 14034
    status_code_alphanumeric = "JOB_34"
    status_message = "The selected resources does not fulfill the properties for this job. Please select a resource that fulfills the requirements to guarantee ISO 17100 compliance for this order."


class JobRequestIso17100(PlunetAPIError):
    status_code = 14035
    status_code_alphanumeric = "JOB_35"
    status_message = "At least one of the selected resources does not fulfill the properties for this job. Please select a resource that fulfills the requirements to guarantee ISO 17100 compliance for this order."


class JobNotAutomatic(PlunetAPIError):
    status_code = 14036
    status_code_alphanumeric = "JOB_36"
    status_message = "The call may only be executed for automatic jobs."


class JobIsRunning(PlunetAPIError):
    status_code = 14037
    status_code_alphanumeric = "JOB_37"
    status_message = "The automatic job is currently running and cannot be started."


class AccessToInternalResourcePricesDenied(PlunetAPIError):
    status_code = 14038
    status_code_alphanumeric = "JOB_38"
    status_message = "The job is assigned to an internal resource but the API user does not have the permission to see internal price information."


class JOB_ACCEPTANCE_HAS_BEEN_CANCELED(PlunetAPIError):
    status_code = 14039
    status_code_alphanumeric = "JOB_39"
    status_message = "The job acceptance has been canceled."


class JOB_REJECTION_HAS_BEEN_CANCELED(PlunetAPIError):
    status_code = 14040
    status_code_alphanumeric = "JOB_40"
    status_message = "The job rejection has been canceled."


class JOB_IS_LOCKED_BY_PROJECT_MANAGER_PLEASE_TRY_AGAIN_LATER(PlunetAPIError):
    status_code = 14041
    status_code_alphanumeric = "JOB_41"
    status_message = "The job is locked by a project manager. Please try again later."


class GeneralWritingAccessToInvoicesIsForbidden(PlunetAPIError):
    status_code = -99
    status_code_alphanumeric = "INV_1"
    status_message = "Writing access to invoices is forbidden."


class InvoiceOnlyEditableInPreparation(PlunetAPIError):
    status_code = 11002
    status_code_alphanumeric = "INV_2"
    status_message = (
        "You can only edit invoices with InvoiceStatusType &#34;in  preparation&#34;."
    )


class InvoiceOnlyEditableOutstandingOrReminder(PlunetAPIError):
    status_code = 11003
    status_code_alphanumeric = "INV_3"
    status_message = "You can only edit the invoice field with InvoiceStatusType  &#34;outstanding&#34; or &#34;reminder created&#34;."


class InvoiceDateMustNotBeEarlierThanTheLastInvoiceDate(PlunetAPIError):
    status_code = 11004
    status_code_alphanumeric = "INV_4"
    status_message = "The invoice date must not be earlier than the last invoice date"


class SalesTaxIdMissing(PlunetAPIError):
    status_code = 11005
    status_code_alphanumeric = "INV_5"
    status_message = "The sales TAX ID is missing"


class CollectiveInvoiceCannotBeCreated(PlunetAPIError):
    status_code = 11006
    status_code_alphanumeric = "INV_6"
    status_message = "The collective invoice cannot be created"


class InvalidInvoiceRecipient(PlunetAPIError):
    status_code = 11007
    status_code_alphanumeric = "INV_7"
    status_message = "Invalid invoice recipient"


class InvalidPaymentRecipient(PlunetAPIError):
    status_code = 11008
    status_code_alphanumeric = "INV_8"
    status_message = "Invalid payment recipient"


class IBANIsInvalid(PlunetAPIError):
    status_code = 11009
    status_code_alphanumeric = "INV_9"
    status_message = "Invalid IBAN"


class InvalidReferenceNumber(PlunetAPIError):
    status_code = 11010
    status_code_alphanumeric = "INV_10"
    status_message = "Invalid IBAN"


class AdditionalInformationIsInvalid(PlunetAPIError):
    status_code = 11011
    status_code_alphanumeric = "INV_11"
    status_message = "Additional information is invalid"


class PayableNotFound(PlunetAPIError):
    status_code = 11012
    status_code_alphanumeric = "INV_12"
    status_message = "Could not find the payable."


class CreditNoteNotFound(PlunetAPIError):
    status_code = 12001
    status_code_alphanumeric = "CRD_1"
    status_message = "Could not find credit note (by ID)."


class NoInvoiceForCreditNoteFound(PlunetAPIError):
    status_code = 12002
    status_code_alphanumeric = "CRD_2"
    status_message = "No invoice is found related to the credit note."


class ReceivableNotFound(PlunetAPIError):
    status_code = 13001
    status_code_alphanumeric = "REC_1"
    status_message = "Could not find the receivable."


class AccountNotFound(PlunetAPIError):
    status_code = 13002
    status_code_alphanumeric = "REC_2"
    status_message = "Could not find the account set for the receivable."


class ItemNotFound(PlunetAPIError):
    status_code = -37
    status_code_alphanumeric = "ITM_1"
    status_message = "System can&#39;t find the requested item."


class ProjectItemNotFound(PlunetAPIError):
    status_code = -26
    status_code_alphanumeric = "ITM_2"
    status_message = "The requested project item is not available."


class ItemIdFromDifferentProject(PlunetAPIError):
    status_code = -63
    status_code_alphanumeric = "ITM_3"
    status_message = "Item id has to be from the same project."


class ThereIsNoLanguageCombinationForSpecifiedItem(PlunetAPIError):
    status_code = -20
    status_code_alphanumeric = "ITM_4"
    status_message = "There is no project item for this language combination."


class ItemContainsJobs(PlunetAPIError):
    status_code = -86
    status_code_alphanumeric = "ITM_5"
    status_message = "The item cannot be deleted because it contains jobs."


class LanguageIndependentItemAlreadyExistForThisProject(PlunetAPIError):
    status_code = 15006
    status_code_alphanumeric = "ITM_6"
    status_message = "Language independent item is already existing."


class WorkflowNotFound(PlunetAPIError):
    status_code = 15007
    status_code_alphanumeric = "ITM_7"
    status_message = "Workflow is not available."


class ServiceNotFound(PlunetAPIError):
    status_code = 15008
    status_code_alphanumeric = "ITM_8"
    status_message = "Service not found"


class ItemJobCostsAreZero(PlunetAPIError):
    status_code = 15009
    status_code_alphanumeric = "ITM_9"
    status_message = "The job costs for the item are 0."


class ItemGeneralPricelineIsNotSet(PlunetAPIError):
    status_code = 15010
    status_code_alphanumeric = "ITM_10"
    status_message = "The general price line is not set."


class ItemPricelineNotSet(PlunetAPIError):
    status_code = 15011
    status_code_alphanumeric = "ITM_11"
    status_message = "The price lines of the following services are not set."


class CallNotSupportedForLanguageIndependentItem(PlunetAPIError):
    status_code = 15012
    status_code_alphanumeric = "ITM_12"
    status_message = "This call is not supported for language-independent items."


class NoObserverRegistered(PlunetAPIError):
    status_code = -49
    status_code_alphanumeric = "CAL_1"
    status_message = "No observer has been registered for the transfered parameter."


class NoNotifyRegistered(PlunetAPIError):
    status_code = -50
    status_code_alphanumeric = "CAL_2"
    status_message = "No notify has been registered for the transfered parameter."


class EventTypeInvalid(PlunetAPIError):
    status_code = -48
    status_code_alphanumeric = "CAL_3"
    status_message = "The EventType is invalid or not allowed."


class CanNotReachDestinationServerURL(PlunetAPIError):
    status_code = 20004
    status_code_alphanumeric = "CAL_4"
    status_message = "Can not reach the destination server URL."


class FileDoesNotExistOrFilePathIsInvalid(PlunetAPIError):
    status_code = -1
    status_code_alphanumeric = "FOL_1"
    status_message = "File or folder does not exist. The file path is invalid."


class FileNotFound(PlunetAPIError):
    status_code = -77
    status_code_alphanumeric = "FOL_2"
    status_message = "No files were found in the specified directory."


class FileDoesNotExist(PlunetAPIError):
    status_code = -75
    status_code_alphanumeric = "FOL_3"
    status_message = "File does not exist."


class FileExistsNoOverwritingAllowed(PlunetAPIError):
    status_code = -74
    status_code_alphanumeric = "FOL_4"
    status_message = "File already exists. Overwriting is not supported."


class FailedToOpenURLToExternalFile(PlunetAPIError):
    status_code = -16
    status_code_alphanumeric = "FOL_5"
    status_message = (
        "Failed to open URL to external file. A malformed URL has occurred."
    )


class FailedToOpenInputStreamToDownloadExternalFile(PlunetAPIError):
    status_code = -17
    status_code_alphanumeric = "FOL_6"
    status_message = "Failed to open input stream to download external file."


class FolderNameForLanguageRelatedSubfoldersUndefined(PlunetAPIError):
    status_code = -9
    status_code_alphanumeric = "FOL_7"
    status_message = "Folder name for language-related subfolders is undefined."


class SourceFolderOfRequestedJobIsEmpty(PlunetAPIError):
    status_code = -14
    status_code_alphanumeric = "FOL_8"
    status_message = "The source folder of the requested job is empty."


class FileTypeInvalid(PlunetAPIError):
    status_code = -51
    status_code_alphanumeric = "FOL_9"
    status_message = "The TypeSelector.FileType of the file is invalid."


class FolderTypeInvalid(PlunetAPIError):
    status_code = -76
    status_code_alphanumeric = "FOL_10"
    status_message = "Invalid FolderTypes."


class FailedToInsertText(PlunetAPIError):
    status_code = -18
    status_code_alphanumeric = "FOL_11"
    status_message = "System failed to insert text."


class InternalErrorDuringFileReading(PlunetAPIError):
    status_code = -72
    status_code_alphanumeric = "FOL_12"
    status_message = "Internal error occurred during reading process of the file."


class InternalErrorDuringFileWriting(PlunetAPIError):
    status_code = -73
    status_code_alphanumeric = "FOL_13"
    status_message = "Internal error occurred during writing process of the file."


class EncodingIsNotSupported(PlunetAPIError):
    status_code = -34
    status_code_alphanumeric = "FOL_14"
    status_message = "The requested document encoding is not supported."


class DocumentTemplateIsUnavailable(PlunetAPIError):
    status_code = -10
    status_code_alphanumeric = "FOL_15"
    status_message = "Requested template of the requested document is unavailable. To verify  which templates are available, check the template sets at  Admin|Templates|Template sets."


class FolderDoesNotExist(PlunetAPIError):
    status_code = 16016
    status_code_alphanumeric = "FOL_16"
    status_message = "The Requested folder does not exist."


class FolderCouldNotBeCreated(PlunetAPIError):
    status_code = 16017
    status_code_alphanumeric = "FOL_17"
    status_message = "The context specific folder could not be created"


class PDFCouldNotBeCreated(PlunetAPIError):
    status_code = 16018
    status_code_alphanumeric = "FOL_18"
    status_message = (
        "PDF could not be created or document could not be converted to PDF"
    )


class FileOrFolderCouldNotBeRenamed(PlunetAPIError):
    status_code = 16019
    status_code_alphanumeric = "FOL_19"
    status_message = "File or folder could not be renamed"


class DocumentTemplateNotFound(PlunetAPIError):
    status_code = 16020
    status_code_alphanumeric = "FOL_20"
    status_message = "Document template not found"


class NoFilesSelected(PlunetAPIError):
    status_code = 16021
    status_code_alphanumeric = "FOL_21"
    status_message = "No files selected"


class FileOrFolderCouldNotBeMoved(PlunetAPIError):
    status_code = 16022
    status_code_alphanumeric = "FOL_22"
    status_message = "File or folder could not be moved."


class JobAssigneeIsMissingTheRequiredConfidentialityLevel(PlunetAPIError):
    status_code = 31001
    status_code_alphanumeric = "COR_1"
    status_message = "The job assignee is missing the required confidentiality level"


class ResourceOfTheProjectTeamIsMissingTheRequiredConfidentialityLevel(PlunetAPIError):
    status_code = 31002
    status_code_alphanumeric = "COR_2"
    status_message = (
        "Resource of the project team is missing the required confidentiality level"
    )


class QualityManagerModuleIsNotActive(PlunetAPIError):
    status_code = 31003
    status_code_alphanumeric = "COR_3"
    status_message = "Quality manager module is required to be activel"


class UserIsMissingTheRequiredCatLicence(PlunetAPIError):
    status_code = 32001
    status_code_alphanumeric = "CAT_1"
    status_message = "The current user is missing the required cat license"


class NoAnalysisFile(PlunetAPIError):
    status_code = 32002
    status_code_alphanumeric = "CAT_2"
    status_message = "Analysis file is missing"


class UserIsNotMappedToACatToolSpecificAccount(PlunetAPIError):
    status_code = 32003
    status_code_alphanumeric = "CAT_3"
    status_message = "User is not mapped to a cat tool specific account"


class XTMMissingOrWrongUserRole(PlunetAPIError):
    status_code = 32004
    status_code_alphanumeric = "CAT_4"
    status_message = "The user is assigend to the wrong or no XTM user role"


class MemoQTheAssignmentOfAnotherContactPersonNustBeDoneManually(PlunetAPIError):
    status_code = 32005
    status_code_alphanumeric = "CAT_5"
    status_message = (
        "The assignment of another contact person must be done manually in memoQ"
    )


class WorldServerProjectPositionMappingNotFound(PlunetAPIError):
    status_code = 32006
    status_code_alphanumeric = "CAT_6"
    status_message = "WorldServerProjectPositionMapping not found"


class WorldServerNoAssignedTaskFoundForJobID(PlunetAPIError):
    status_code = 32007
    status_code_alphanumeric = "CAT_7"
    status_message = "No assigned Task found for JobID"


class WorldServerCorruptJobNumber(PlunetAPIError):
    status_code = 32008
    status_code_alphanumeric = "CAT_8"
    status_message = "Corrupt job number"


class WorldServerPositionNotFoundForPositionID(PlunetAPIError):
    status_code = 32009
    status_code_alphanumeric = "CAT_9"
    status_message = "Position not found for PositionID"


class GroupShareNoLinkedUserCouldBeFoundForTheSelectedResource(PlunetAPIError):
    status_code = 32010
    status_code_alphanumeric = "CAT_10"
    status_message = (
        "No linked GroupShare user could be found for the selected resource"
    )


class GroupShareNoProjectCouldBeFoundForThisItem(PlunetAPIError):
    status_code = 32011
    status_code_alphanumeric = "CAT_11"
    status_message = "No GroupShare project could be found for this item"


class SDLTradosStudioTheLanguageCombinationCannotBeDeletedAfterTheProjectHasBeenCreated(
    PlunetAPIError
):
    status_code = 32012
    status_code_alphanumeric = "CAT_12"
    status_message = "The language combination cannot be deleted after the SDL Trados Studio project has been created"


class GroupshareNoLinkedPhaseCouldBeFoundForThisJob(PlunetAPIError):
    status_code = 32013
    status_code_alphanumeric = "CAT_13"
    status_message = "No linked GroupShare phase could be found this job"


class MemoQCallbackProjectCouldNotBeMatched(PlunetAPIError):
    status_code = 32014
    status_code_alphanumeric = "CAT_14"
    status_message = "Callback: Project could not be matched."


class MemoQCallbackCorrespondingProjectIsAlreadyClosedAndUneditable(PlunetAPIError):
    status_code = 32015
    status_code_alphanumeric = "CAT_15"
    status_message = (
        "Callback: The corresponding project is already closed and uneditable."
    )


class MemoqResourceNotSubvendor(PlunetAPIError):
    status_code = 32016
    status_code_alphanumeric = "CAT_16"
    status_message = "MemoQ resource is not linked to a subvendor though the MemoQ role in the job is subvendor."


class MultipleSourceLanguages(PlunetAPIError):
    status_code = 32017
    status_code_alphanumeric = "CAT_17"
    status_message = (
        "Project contains multiple source languages. Could not start CAT analysis."
    )


class ProjectNotUpdatable(PlunetAPIError):
    status_code = 32018
    status_code_alphanumeric = "CAT_18"
    status_message = "MemoQ procekt could not be updated. Too much time has passed between  creation and update."


class TradosProjectNotFound(PlunetAPIError):
    status_code = 32019
    status_code_alphanumeric = "CAT_19"
    status_message = "Trados project could not be found."


class MemoqSettingsNotFound(PlunetAPIError):
    status_code = 32020
    status_code_alphanumeric = "CAT_20"
    status_message = "Memoq settings could not be found."


class CatTemplateNotFound(PlunetAPIError):
    status_code = 32021
    status_code_alphanumeric = "CAT_21"
    status_message = "CAT template could not be found."


class MemoqTmNotFound(PlunetAPIError):
    status_code = 32022
    status_code_alphanumeric = "CAT_22"
    status_message = "Memoq TM could not be found."


class UndefinedWorldserverError(PlunetAPIError):
    status_code = 32023
    status_code_alphanumeric = "CAT_23"
    status_message = "Undefiened worldserver error"


class UndefinedMemsourceError(PlunetAPIError):
    status_code = 32024
    status_code_alphanumeric = "CAT_24"
    status_message = "Undefiened memsource error"


class UndefinedGroupShareError(PlunetAPIError):
    status_code = 32025
    status_code_alphanumeric = "CAT_25"
    status_message = "Undefiened GroupShare error"


class UndefinedMemoQError(PlunetAPIError):
    status_code = 32026
    status_code_alphanumeric = "CAT_26"
    status_message = "Undefiened MemoQ error"


class UndefinedXTMError(PlunetAPIError):
    status_code = 32027
    status_code_alphanumeric = "CAT_27"
    status_message = "Undefiened XTM error"


class MemoqProjectNotFound(PlunetAPIError):
    status_code = 32028
    status_code_alphanumeric = "CAT_28"
    status_message = "Memoq project could not be found."


class MemoqRoleNotFound(PlunetAPIError):
    status_code = 32029
    status_code_alphanumeric = "CAT_29"
    status_message = "Memoq project could not be found."


class MemoqResourceIsSubvendor(PlunetAPIError):
    status_code = 32030
    status_code_alphanumeric = "CAT_30"
    status_message = "MemoQ resource should not be linked to a subvendor because the MemoQ role in the job is not subvendor."


class WorldServerWorkflowMappingMissing(PlunetAPIError):
    status_code = 32031
    status_code_alphanumeric = "CAT_31"
    status_message = (
        "Mapping between Plunet workflow and WorldServer workflow is missing."
    )


class GroupShareNoProjectCouldBeFound(PlunetAPIError):
    status_code = 32032
    status_code_alphanumeric = "CAT_32"
    status_message = "No GroupShare project could be found."


class CatProjectSettingsCouldNotBeFound(PlunetAPIError):
    status_code = 32033
    status_code_alphanumeric = "CAT_33"
    status_message = "CAT project settings could not be found."


class WorkflowCannotBeDeletedBecauseItIsAssignedToCustomers(PlunetAPIError):
    status_code = 33001
    status_code_alphanumeric = "WFL_1"
    status_message = (
        "The workflow cannot be deleted, because it is still assigned to customers"
    )


class WorkflowContainsCycle(PlunetAPIError):
    status_code = 33002
    status_code_alphanumeric = "WFL_2"
    status_message = "Workflow template contains cycle"


class WorkflowInvalid(PlunetAPIError):
    status_code = 33003
    status_code_alphanumeric = "WFL_3"
    status_message = "Workflow is invalid"


class WorkflowIsMissing(PlunetAPIError):
    status_code = 33004
    status_code_alphanumeric = "WFL_4"
    status_message = "Workflow is missing"


PLUNET_ERRORS = {
    -5: APISessionDoesNotExistOrIsInvalid,
    -85: InvalidCredentials,
    -11: UserOfTheCurrentSessionIsNotActiveOrUndefined,
    -12: MissingRightsForAPIUser,
    -4: RequestedDataNotFound,
    -6: ParamEmptyOrInvalid,
    -42: ValueForTypeParameterIsInvalid,
    -69: ValueNotNumeric,
    -70: ValueNotAvailable,
    -83: ParameterModificationInvalid,
    -103: ActionIsNotAllowedDueToObjectRelatedStatus,
    -89: TypeCannotBeChangedViaUpdate,
    -2: NoObjectIsInstanciatedForCurrentAPISession,
    -13: DataRecordIsNotLocked,
    -15: FailedToLockDataSet,
    -45: DataLocked,
    -106: RelatedDataEntryCouldNotBeUnlockedAfterAction,
    -27: ObjectWasCreatedWithMultipleIssues,
    -41: IncorrectOrCorruptTransferObject,
    -102: InvalidPercentageNumber,
    -105: SearchHasToContainAtLeastOneParameter,
    -58: PropertyNotFound,
    -59: PropertyValueNotFound,
    -60: PropertyUnavailable,
    -61: PropertyInactive,
    -88: PropertyIsAlreadySetByPriceList,
    -81: DataModificationInvalid,
    -82: DataNotFound,
    -98: NoPricelistSetForRelatedObject,
    -120: DeliveryDateIsMissing,
    1032: TaxationTypeIsNotDefinied,
    1033: TimeFrameObjectIsInvalid,
    1034: DataEntryCanNotBeUnlockedAsItIsLockedByAnotherUser,
    1035: DeliveryFailed,
    1036: AccountsAreMissing,
    1037: StatusCouldNotBeChanged,
    1038: DataEntryCouldNotBeDeletedAsItIsInUseByTheApplication,
    1039: DataEntryCouldNotBeDeletedAtTheCurrentStatus,
    1040: CostCenterIsMissing,
    1041: MarkedForRequiredReviewBeforeSubmission,
    1042: OneOrManyMandatoryFieldsAreNotFilled,
    1043: TemplateCouldNotBeUsed,
    1044: StartDateIsMissing,
    1045: ObjectCouldNotBeCreated,
    1046: TemplateAlreadyExists,
    1047: NoUserForAutomationIsSet,
    1048: ContactPersonCouldNotBeDeleted,
    1049: InvalidStructure,
    1050: DeliveryDeadlineIsMissing,
    1051: RtfNotCreated,
    1052: RoundModuleNotActive,
    1053: RequiredFieldIsEmpty,
    1054: UserTypeInvalid,
    1055: StandardContactPersonItemNotActive,
    -3: InternalSystemError,
    -100: UndefinedError,
    -999: DeadEndAndThereIsNoImplementation,
    -40: CMS_Error,
    -1000: Warning_ObjectCouldNotBePersistedAsTransferedAndGotSanitized,
    2007: TypApiErrorNotMapped,
    2008: ImplementationIsNotLongerSupportedInThisVersion,
    -1111: CallIsDeactivatedDueToSpecificRestrictionsPleaseCheckTheManual,
    2010: ExternalErrorCodeReference,
    20101: UserIsNotMappedToAnyRightgroup,
    2012: InternalSystemErrorWithReference,
    2013: LocktypeInvalid,
    -52: AuthenticationInvalidOrSystemUnavailable,
    -104: ExternalSystemURLHasToBeConfiguredToUseActionLinks,
    -36: PriceListNotFound,
    -47: PriceUnitNotFound,
    -107: PriceLineNotFound,
    -67: SystemLanguageUnknown,
    -7: TargetLanguageUndefined,
    -8: SourceLanguageUndefined,
    -25: LanguageCombinationNotFound,
    -43: CurrencyUnknown,
    -44: CountryUnknown,
    -78: PropertyValueIdInvalid,
    -79: PropertyAreaIdInvalid,
    -87: PropertyAreaDoesNotSupportMultipleValueSelection,
    3015: TextmoduleUsageAreaInvalid,
    -65: TextmoduleNotFound,
    -66: TextmoduleMissingRights,
    -68: TextmoduleNoListboxOrNotConfiguredForMultipleValues,
    -71: MainTextmoduleRequiresValue,
    -106: CompanyCodesAreNotActivated,
    3021: PaymentMethodNotFound,
    3022: TextmoduleSelectionOrInputValueIsInvalid,
    3023: EMailUserWasNotFound,
    3024: EmailWrongSMTPActionForSending,
    3025: EmailAlreadyWithinOutbox,
    3026: EmailNotFound,
    3027: EmailNoRecipient,
    3028: EmailCouldNotBeSendt,
    3029: PropertyIsReferencedAndCanNotBeDeleted,
    3030: PropertyOneOrManyAreMandatory,
    3031: MissingLanguageFolder,
    3032: NoDefaultProjectManagerConfigured,
    3033: InvalidDefaultProjectManagerSetting,
    3034: InvalidConfiguration,
    3035: AdminAccountNotDefined,
    3036: CompanyCodeUnknown,
    3037: MandatorNotActive,
    3038: ConfidentialityInvalid,
    3039: SwitchingUserLanguageFailed,
    3040: ReachedMaximumOfUiLanguages,
    -46: PartnerNotFound,
    4002: PartnerTypeInvalid,
    -30: PartnerEntryCouldNotBeDeleted,
    -31: RequestedAddressNotFound,
    -90: InvoiceOrDeliveryAddressAlreadyExists,
    -32: ThereIsNoPartnerDatasetAvailableForTheCurrentApiSession,
    -33: ThereIsNoAddressDatasetAvailableForTheCurrentApiSession,
    4008: FormOfAddressInvalid,
    4009: ContactPersonNotActive,
    -28: ResourceNotFound,
    -94: ResourceIsMissing,
    -84: ResourceCannotBeUsed,
    -80: ResourceStatusNotActive,
    -108: NoContactPersonSet,
    5006: ResourceStatusInvalid,
    5007: ResourceTypeInvalid,
    5008: ContactPersonNotFound,
    5009: ResourceIsAlreadyAssignedToAnJobInTheSamePeriod,
    5010: ContactPersonNotMatchingResource,
    5011: ResourceNotMemberOfProjectTeam,
    -29: CustomerNotFound,
    -92: CustomerIsMissing,
    -55: CustomerContactUnknown,
    -53: UuidCustomerMappingError,
    -54: SystemMissingForCustomer,
    6006: CustomerStatusInvalid,
    6007: ContactPersonNotMatchingCustomer,
    -38: ProjectNotFound,
    -21: ProjectTypeInvalid,
    -91: ProjectTypeNotActive,
    -96: CannotChangeProjectStatus,
    -97: NoCustomerSetForProject,
    -93: ProjectDescriptionIsMissing,
    -57: NoMasterProjectSpecified,
    -62: TemplateDoesNotExistOrNotAllowed,
    -95: BudgetOverdrawn,
    -56: ProjecttypeDoesNotExist,
    -21: ProjectCategoryInvalid,
    -21: ProjectCategoryNotSet,
    7012: ArchivStatusNotActiveOrPreparation,
    7013: ProjectManagerIsMissing,
    7014: ProjectNameIsMissing,
    7015: ProjectIdInvalid,
    7016: DateInvalid,
    7017: FileNameMissing,
    7018: ComplaintCreationFailed,
    7019: CommissionNotFound,
    7020: ProjectConsistsOfMultiplePackages,
    7021: CmsConfigInactive,
    7022: MasterProjectLimitedToCustomer,
    7023: ProjectFolderNotFound,
    70231: ProjectIDDoesNotBelongToMasterProject,
    7024: TemplateCointainsExternalResourceInProjectTeam,
    7025: ProjectArchived,
    -24: RequestNotFound,
    -23: QuoteNotFound,
    9002: QuoteStatusNotNewPreparationOrCheckClearance,
    9003: QuoteStatusNotAcceptedChangedOrCancelled,
    -22: OrderNotFound,
    -19: OrderHasNoReferenceToRequest,
    -20: LinksOnlySupportedBetweenOrders,
    3: OrderNotCreatedFromQuote,
    -35: JobNotFound,
    -39: JobTypeIsUndefinied,
    -64: JobStatusChangeImpossible,
    -101: CannotEditWorkingTimes,
    14005: JobNotCreated,
    14006: JobTemplateNotFound,
    14007: JobTemplateNoValid,
    14008: JobCannotBeInvoicedToTheCostCenterForPayables,
    14009: JobHasAlreadyBeenInvoiced,
    14010: ThereAreNoAvailableJobsIntoWhichResourcesCanBeEntered,
    14011: JobIsNotAssignedToAnyItem,
    14012: JobCanNotBeRequestedAtThisStatus,
    14013: AllPriceLinesAreZeroQuantityOrderJobRequestCancelled,
    14014: JobCanOnlyBeDeliveredAfterFileUpload,
    14015: NoDeductionBonusCouldBeAppliedToTheJobBecauseTheJobHasAlreadyBeenInvoiced,
    14016: JobCanNotBeStartedDueToStatus,
    14017: JobIsNotInvoiced,
    140171: JobQualityRatingMustBeClosedBeforeDelivery,
    14019: RoundDoesNotExist,
    14020: RoundRankingMethodPositionAlreadyExists,
    14021: RatingOutOfRange,
    14022: JobCanNotBeDeliveredWithoutEnterintWorkingTimes,
    14023: JobStatusInvalid,
    14024: JobChecklistIncomplete,
    14025: RoundSearchCriteriaNotFound,
    14026: RoundStatusInvalid,
    14027: RoundRankingMethodInvalid,
    14028: RoundAssignedNotFound,
    14029: JobCannotBeDeletedDueToStatus,
    14030: RoundAssignmentMethodInvalid,
    14031: ResourceDoesNotMatchJobRoundCriteria,
    14032: RoundReviewNotFound,
    14033: JobIDNotFound,
    14034: JobAssignmentIso17100,
    14035: JobRequestIso17100,
    14036: JobNotAutomatic,
    14037: JobIsRunning,
    14038: AccessToInternalResourcePricesDenied,
    14039: JOB_ACCEPTANCE_HAS_BEEN_CANCELED,
    14040: JOB_REJECTION_HAS_BEEN_CANCELED,
    14041: JOB_IS_LOCKED_BY_PROJECT_MANAGER_PLEASE_TRY_AGAIN_LATER,
    -99: GeneralWritingAccessToInvoicesIsForbidden,
    11002: InvoiceOnlyEditableInPreparation,
    11003: InvoiceOnlyEditableOutstandingOrReminder,
    11004: InvoiceDateMustNotBeEarlierThanTheLastInvoiceDate,
    11005: SalesTaxIdMissing,
    11006: CollectiveInvoiceCannotBeCreated,
    11007: InvalidInvoiceRecipient,
    11008: InvalidPaymentRecipient,
    11009: IBANIsInvalid,
    11010: InvalidReferenceNumber,
    11011: AdditionalInformationIsInvalid,
    11012: PayableNotFound,
    12001: CreditNoteNotFound,
    12002: NoInvoiceForCreditNoteFound,
    13001: ReceivableNotFound,
    13002: AccountNotFound,
    -37: ItemNotFound,
    -26: ProjectItemNotFound,
    -63: ItemIdFromDifferentProject,
    -20: ThereIsNoLanguageCombinationForSpecifiedItem,
    -86: ItemContainsJobs,
    15006: LanguageIndependentItemAlreadyExistForThisProject,
    15007: WorkflowNotFound,
    15008: ServiceNotFound,
    15009: ItemJobCostsAreZero,
    15010: ItemGeneralPricelineIsNotSet,
    15011: ItemPricelineNotSet,
    15012: CallNotSupportedForLanguageIndependentItem,
    -49: NoObserverRegistered,
    -50: NoNotifyRegistered,
    -48: EventTypeInvalid,
    20004: CanNotReachDestinationServerURL,
    -1: FileDoesNotExistOrFilePathIsInvalid,
    -77: FileNotFound,
    -75: FileDoesNotExist,
    -74: FileExistsNoOverwritingAllowed,
    -16: FailedToOpenURLToExternalFile,
    -17: FailedToOpenInputStreamToDownloadExternalFile,
    -9: FolderNameForLanguageRelatedSubfoldersUndefined,
    -14: SourceFolderOfRequestedJobIsEmpty,
    -51: FileTypeInvalid,
    -76: FolderTypeInvalid,
    -18: FailedToInsertText,
    -72: InternalErrorDuringFileReading,
    -73: InternalErrorDuringFileWriting,
    -34: EncodingIsNotSupported,
    -10: DocumentTemplateIsUnavailable,
    16016: FolderDoesNotExist,
    16017: FolderCouldNotBeCreated,
    16018: PDFCouldNotBeCreated,
    16019: FileOrFolderCouldNotBeRenamed,
    16020: DocumentTemplateNotFound,
    16021: NoFilesSelected,
    16022: FileOrFolderCouldNotBeMoved,
    31001: JobAssigneeIsMissingTheRequiredConfidentialityLevel,
    31002: ResourceOfTheProjectTeamIsMissingTheRequiredConfidentialityLevel,
    31003: QualityManagerModuleIsNotActive,
    32001: UserIsMissingTheRequiredCatLicence,
    32002: NoAnalysisFile,
    32003: UserIsNotMappedToACatToolSpecificAccount,
    32004: XTMMissingOrWrongUserRole,
    32005: MemoQTheAssignmentOfAnotherContactPersonNustBeDoneManually,
    32006: WorldServerProjectPositionMappingNotFound,
    32007: WorldServerNoAssignedTaskFoundForJobID,
    32008: WorldServerCorruptJobNumber,
    32009: WorldServerPositionNotFoundForPositionID,
    32010: GroupShareNoLinkedUserCouldBeFoundForTheSelectedResource,
    32011: GroupShareNoProjectCouldBeFoundForThisItem,
    32012: SDLTradosStudioTheLanguageCombinationCannotBeDeletedAfterTheProjectHasBeenCreated,
    32013: GroupshareNoLinkedPhaseCouldBeFoundForThisJob,
    32014: MemoQCallbackProjectCouldNotBeMatched,
    32015: MemoQCallbackCorrespondingProjectIsAlreadyClosedAndUneditable,
    32016: MemoqResourceNotSubvendor,
    32017: MultipleSourceLanguages,
    32018: ProjectNotUpdatable,
    32019: TradosProjectNotFound,
    32020: MemoqSettingsNotFound,
    32021: CatTemplateNotFound,
    32022: MemoqTmNotFound,
    32023: UndefinedWorldserverError,
    32024: UndefinedMemsourceError,
    32025: UndefinedGroupShareError,
    32026: UndefinedMemoQError,
    32027: UndefinedXTMError,
    32028: MemoqProjectNotFound,
    32029: MemoqRoleNotFound,
    32030: MemoqResourceIsSubvendor,
    32031: WorldServerWorkflowMappingMissing,
    32032: GroupShareNoProjectCouldBeFound,
    32033: CatProjectSettingsCouldNotBeFound,
    33001: WorkflowCannotBeDeletedBecauseItIsAssignedToCustomers,
    33002: WorkflowContainsCycle,
    33003: WorkflowInvalid,
    33004: WorkflowIsMissing,
}


class PlunetClientError(Exception):
    pass


class PlunetAuthFailed(PlunetClientError):
    pass


class PlunetOrderNotFound(PlunetClientError):
    pass


class NoPlunetSession(PlunetClientError):
    pass
