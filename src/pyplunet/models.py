from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel as BM

from .enums import (
    AddressType,
    CallbackType,
    ContactType,
    CreditNoteStatus,
    CustomerStatus,
    CustomerType,
    EventType,
    ItemStatus,
    JobStatus,
    PayableStatus,
    ProjectType,
    PropertyType,
    ResourceStatus,
    ResourceType,
    TaxType,
    TextModuleType,
    TextModuleUsageArea,
    WorkingStatus,
)


class BaseModel(BM):
    class Config:
        use_enum_values = True


class JobTrackingTime(BaseModel):
    """
    Used in:
        DataJob30
    """

    resourceID: int
    comment: Optional[str]
    dateFrom: Optional[datetime]
    dateTo: Optional[datetime]


class Amount(BaseModel):
    """
    Used in:
        DataJob30
    """

    baseUnitName: Optional[str]
    grossQuantity: Optional[float]
    netQuantity: Optional[float]
    serviceType: Optional[str]


class Tax(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30
    """

    active: bool
    expenseAccount: Optional[str]
    revenueAccount: Optional[str]
    taxDescription: Optional[str]
    taxRate: float
    taxType: TaxType


class PriceLine(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJob30,
        DataItem30
    """

    amount: float
    amount_perUnit: float
    memo: Optional[str]
    priceLineID: int
    priceUnitID: int
    sequence: int
    taxType: TaxType
    time_perUnit: float
    unit_price: float


class PriceUnit(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    articleNumber: Optional[str]
    description: Optional[str]
    memo: Optional[str]
    priceUnitID: int
    service: Optional[str]


class PayableItem(BaseModel):
    """
    Used in:
        DataPayable30
    """

    briefDescription: Optional[str]
    invoiceID: int
    itemNumber: int
    jobDate: Optional[datetime]
    jobNo: Optional[str]
    jobStatus: JobStatus
    payableItemID: int
    projectType: ProjectType
    totalprice: float


class Textmodule(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataResource30,
        DataCustomer30,
        ReportCustomer30,
        DataCustomFields30
    """

    availableValues: Optional[List[Optional[str]]] = None
    dateValue: Optional[datetime]
    flag: Optional[str]
    flag_MainTextModule: Optional[str]
    selectedValues: Optional[List[Optional[str]]] = None
    stringValue: Optional[str]
    textModuleType: TextModuleType


class SelectionEntry_TimeFrame(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataOrder30,
        DataQuote30,
        DataRequest30
    """

    dateFrom: datetime
    dateRelation: int
    dateTo: datetime


class Invoice(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    briefDescription: Optional[str]
    currencyCode: Optional[str]
    customerID: int
    gross: float
    invoiceDate: Optional[datetime]
    invoiceDocuments: Optional[List[Optional[str]]] = None
    invoiceID: int
    invoiceNr: Optional[str]
    net: float
    orderIDs: Optional[List[Optional[int]]] = None
    outgoing: float
    paid: float
    status: int
    subject: Optional[str]
    tax: float
    valueDate: Optional[datetime]


class InvoiceItem(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    briefDescription: Optional[str]
    comment: Optional[str]
    invoiceID: int
    invoiceItemID: int
    itemNumber: Optional[str]
    languageCombinationID: int
    orderID: int
    totalPrice: float


class Pricelist(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30,
        DataResource30
    """

    ResourcePricelistID: int
    pricelistID: int
    PricelistNameEN: Optional[str]
    currency: Optional[str]
    memo: Optional[str]
    withWhiteSpace: bool


class Property(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJobRound30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataResource30,
        DataCustomer30,
        ReportCustomer30,
        DataCustomFields30
    """

    avaliablePropertyValueIDList: Optional[List[Optional[int]]] = None
    mainPropertyNameEnglish: Optional[str]
    propertyNameEnglish: Optional[str]
    propertyType: PropertyType
    selectedPropertyValueID: int
    selectedPropertyValueList: Optional[List[Optional[int]]] = None


class PricelistEntry(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    amountPerUnit: float
    pricePerUnit: float
    priceUnitID: int


class CreditNoteItem(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    briefDescription: Optional[str]
    creditNoteID: int
    creditNoteItemID: int
    itemNumber: Optional[str]
    taxTypeID: int
    totalPrice: float


class Currency(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    currencyID: int
    description: Optional[str]
    isoCode: Optional[str]


class Language(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    active: bool
    favorite: bool
    folderName: Optional[str]
    id: int
    isoCode: Optional[str]
    name: Optional[str]


class Callback(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    benutzerID: int
    callbackType: CallbackType
    dataService: int
    errorCount: int
    eventType: EventType
    mainID: int
    objectType: int
    serverAddress: Optional[str]


class CompanyCode(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    companyCodeID: int
    companyCodeRights: bool
    description_Long: Optional[str]
    description_Short: Optional[str]
    isCompanyCodeInvoice: bool


class Country(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    ID: int
    isoCode: Optional[str]
    name: Optional[str]


class Service(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    abbreviation: Optional[str]
    id: int
    jobCategory: Optional[str]
    name: Optional[str]


class Job(BaseModel):
    """
    Used in:
        DataJob30
    """

    countSourceFiles: int
    dueDate: Optional[datetime]
    itemID: int
    jobID: int
    jobTypeFull: Optional[str]
    jobTypeShort: Optional[str]
    projectID: int
    projectType: ProjectType
    resourceID: int
    startDate: Optional[datetime]
    status: int


class TrackingTimeList(BaseModel):
    """
    Used in:
        DataJob30
    """

    completed: float
    trackingTimeList: Optional[List[Optional[JobTrackingTime]]] = None


class JobTrackingTimeIN(BaseModel):
    """
    Used in:
        DataJob30
    """

    comment: str
    completed: float
    dateFrom: datetime
    dateTo: datetime
    resourceID: int


class JobMetric(BaseModel):
    """
    Used in:
        DataJob30
    """

    amounts: Optional[List[Optional[Amount]]] = None
    totalPrice: float
    totalPriceJobCurrency: float


class JobRound(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    assignmentLimitToFirstX: int
    assignmentLimitType: int
    assignmentMethod: int
    jobID: int
    jobRoundID: int
    jobRoundNumber: int
    projectType: ProjectType
    sendNotificationOnFailure: bool
    sendNotificationOnJobAccept: bool
    sendNotificationOnJobReject: bool
    startNextRoundAutomatically: bool
    status: int


class JobRoundRankingMethod(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    methodType: int
    priority: int


class JobRoundSearchCriteria(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    includeNonRespondingResources: bool
    includeNotRequestedResources: bool
    includeRejectingResources: bool
    propertyList: Optional[List[Optional[Property]]] = None
    resourceStatus: Optional[List[Optional[ResourceStatus]]] = None
    roundId: int
    searchCriterionId: int
    workingStatus: Optional[List[Optional[WorkingStatus]]] = None


class Order(BaseModel):
    """
    Used in:
        DataOrder30
    """

    currency: Optional[str]
    customerContactID: int
    customerID: int
    deliveryDeadline: Optional[datetime]
    orderClosingDate: Optional[datetime]
    orderDate: Optional[datetime]
    orderDisplayName: Optional[str]
    orderID: int
    projectManagerID: int
    projectName: Optional[str]
    rate: float
    requestID: int
    subject: Optional[str]


class Link(BaseModel):
    """
    Used in:
        DataOrder30
    """

    linkId: int
    memo: Optional[str]
    projectType: ProjectType
    sourceOrderId: int
    targetOrderId: int


class SelectionEntry_TeamMember(BaseModel):
    """
    Used in:
        DataOrder30,
        DataQuote30
    """

    ID: int
    teamMember: int


class Template(BaseModel):
    """
    Used in:
        DataOrder30,
        DataQuote30
    """

    customerID: int
    templateDescription: Optional[str]
    templateID: int
    templateName: Optional[str]


class Quote(BaseModel):
    """
    Used in:
        DataQuote30
    """

    creationDate: Optional[datetime]
    currency: Optional[str]
    orderID: Optional[List[Optional[int]]] = None
    projectName: Optional[str]
    quoteID: int
    quoteNumber: Optional[str]
    rate: float
    requestID: int
    status: int
    subject: Optional[str]


class SelectionEntry_Customer(BaseModel):
    """
    Used in:
        DataQuote30,
        DataRequest30
    """

    customerEntryType: int
    mainID: int


class SelectionEntry_Resource(BaseModel):
    """
    Used in:
        DataQuote30
    """

    mainID: int
    resourceEntryType: int


class Request(BaseModel):
    """
    Used in:
        DataRequest30
    """

    briefDescription: Optional[str]
    creationDate: Optional[datetime]
    deliveryDate: Optional[datetime]
    orderID: int
    orderIDList: Optional[List[Optional[int]]] = None
    quotationDate: Optional[datetime]
    quoteID: int
    quoteIDList: Optional[List[Optional[int]]] = None
    requestID: int
    status: int
    subject: Optional[str]


class Item(BaseModel):
    """
    Used in:
        DataItem30
    """

    briefDescription: Optional[str]
    comment: Optional[str]
    deliveryDeadline: Optional[datetime]
    invoiceID: int
    itemID: int
    jobIDList: Optional[List[Optional[int]]] = None
    orderID: int
    projectID: int
    projectType: ProjectType
    reference: Optional[str]
    sourceLanguage: Optional[str]
    status: int
    targetLanguage: Optional[str]
    totalPrice: float


class Resource(BaseModel):
    """
    Used in:
        DataResource30
    """

    academicTitle: Optional[str]
    costCenter: Optional[str]
    currency: Optional[str]
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    fullName: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    resourceID: int
    resourceType: ResourceType
    skypeID: Optional[str]
    status: int
    supervisor1: Optional[str]
    supervisor2: Optional[str]
    userId: int
    website: Optional[str]
    workingStatus: WorkingStatus


class Account(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    accountDescription: Optional[str]
    accountID: int
    accountNumber: Optional[str]
    accountType: int
    active: bool


class PaymentInfo(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    accountHolder: Optional[str]
    accountID: int
    BIC: Optional[str]
    contractNumber: Optional[str]
    debitAccount: Optional[str]
    IBAN: Optional[str]
    paymentMethodID: int
    preselectedTaxID: int
    salesTaxID: Optional[str]


class Customer(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    academicTitle: Optional[str]
    costCenter: Optional[str]
    currency: Optional[str]
    customerID: int
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    fullName: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    skypeID: Optional[str]
    status: int
    userId: int
    website: Optional[str]


class Workflow(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    description: Optional[str]
    name: Optional[str]
    status: int
    type: int
    workflowId: int


class CustomerContact(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    addressID: int
    costCenter: Optional[str]
    customerContactID: int
    customerID: int
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    phone: Optional[str]
    status: int
    supervisor1: Optional[str]
    supervisor2: Optional[str]
    userId: int


class ResourceContact(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    academicTitle: Optional[str]
    addressID: int
    costCenter: Optional[str]
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    resourceContactID: int
    resourceID: int
    skypeID: Optional[str]
    status: int
    userId: int


class User(BaseModel):
    """
    Used in:
        DataUser30
    """

    contactID: int
    contactType: ContactType
    customerContactID: int
    password: Optional[str]
    userID: int
    userName: Optional[str]


class Result(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataAdmin30,
        DataJob30,
        DataJobRound30,
        ReportJob30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30,
        DataResource30,
        DataCustomer30,
        DataCustomerContact30,
        ReportCustomer30,
        DataResourceContact30,
        DataCustomerAddress30,
        DataResourceAddress30,
        DataDocument30,
        RequestDocText30,
        DataUser30,
        DataCustomFields30
    """

    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class IntegerResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJob30,
        DataJobRound30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30,
        DataResource30,
        DataCustomer30,
        DataCustomerContact30,
        DataResourceContact30,
        DataCustomerAddress30,
        DataResourceAddress30,
        RequestDocText30
    """

    data: int
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class StringResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataAdmin30,
        DataJob30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30,
        DataResource30,
        DataCustomer30,
        DataCustomerContact30,
        DataResourceContact30,
        DataCustomerAddress30,
        DataResourceAddress30,
        RequestDocText30,
        DataCustomFields30
    """

    data: Optional[str]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class TaxListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30
    """

    data: Optional[List[Optional[Tax]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class DoubleResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30
    """

    data: float
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class DateResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJob30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30,
        DataCustomer30
    """

    data: Optional[datetime]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PriceLineIN(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJob30,
        DataItem30
    """

    amount: float
    amount_perUnit: float
    memo: Optional[str]
    priceLineID: int
    priceUnitID: int
    taxType: TaxType
    time_perUnit: float
    unit_price: float


class PriceLineResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJob30,
        DataItem30
    """

    data: Optional[PriceLine]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PriceUnitListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[Optional[PriceUnit]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class BooleanResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataOrder30,
        DataRequest30
    """

    data: bool
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PriceLineListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[Optional[PriceLine]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PayableItemResultList(BaseModel):
    """
    Used in:
        DataPayable30
    """

    data: Optional[List[Optional[PayableItem]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PriceUnitResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[PriceUnit]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PayableItemIN(BaseModel):
    """
    Used in:
        DataPayable30
    """

    briefDescription: Optional[str]
    invoiceID: int
    itemNumber: int
    jobDate: Optional[datetime]
    jobID: int
    jobNo: Optional[str]
    jobStatus: JobStatus
    totalprice: float


class SearchFilter_Payable(BaseModel):
    """
    Used in:
        DataPayable30
    """

    exported: int
    isoCodeCurrency: Optional[str]
    languageCode: Optional[str]
    resourceID: int
    payableStatus: PayableStatus
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: SelectionEntry_TimeFrame


class IntegerArrayResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataJobRound30,
        ReportJob30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataItem30,
        DataResource30,
        DataCustomer30,
        DataCustomerContact30,
        ReportCustomer30,
        DataResourceContact30,
        DataCustomerAddress30,
        DataResourceAddress30,
        RequestDocText30
    """

    data: Optional[List[Optional[int]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class StringArrayResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataAdmin30,
        DataJob30,
        DataOrder30,
        DataItem30,
        DataDocument30
    """

    data: Optional[List[Optional[str]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class InvoiceResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    data: Optional[Invoice]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class InvoiceItemIN(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    briefDescription: Optional[str]
    comment: Optional[str]
    invoiceID: int
    invoiceItemID: int
    languageCombinationID: int
    orderID: int
    totalPrice: float


class InvoiceItemResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    data: Optional[List[Optional[InvoiceItem]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PricelistListResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30,
        DataResource30
    """

    data: Optional[List[Optional[Pricelist]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Invoice(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    customerID: int
    languageCode: str
    propertiesList: Optional[List[Optional[Property]]]
    invoiceStatus: int
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: SelectionEntry_TimeFrame


class PricelistEntryList(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[Optional[PricelistEntry]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PricelistResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[Pricelist]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_CreditNote(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    customerID: int
    languageCode: str
    propertiesList: Optional[List[Optional[Property]]]
    creditNoteStatus: CreditNoteStatus
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: SelectionEntry_TimeFrame


class CreditNoteItemIN(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    briefDescription: Optional[str]
    creditNoteID: int
    taxTypeID: int
    totalPrice: float


class CreditNoteListResult(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    data: Optional[List[Optional[CreditNoteItem]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CurrencyList(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[Currency]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class LanguageListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[Language]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CallbackListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[Callback]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CompanyCodeListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[CompanyCode]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CountryListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[Country]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ServiceListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Optional[Service]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[Job]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobListResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[List[Optional[Job]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobIN(BaseModel):
    """
    Used in:
        DataJob30
    """

    contactPersonID: int
    dueDate: Optional[datetime]
    itemID: int
    jobID: int
    projectID: int
    projectType: ProjectType
    resourceID: int
    startDate: Optional[datetime]
    status: int


class JobTrackingTimeResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[TrackingTimeList]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobTrackingTimeListIN(BaseModel):
    """
    Used in:
        DataJob30
    """

    trackingTimes: List[JobTrackingTimeIN]


class JobMetricResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[JobMetric]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobRoundIN(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    assignmentLimitToFirstX: int
    assignmentLimitType: int
    assignmentMethod: int
    jobID: int
    jobRoundID: int
    jobRoundNumber: int
    projectType: ProjectType
    sendNotificationOnFailure: bool
    sendNotificationOnJobAccept: bool
    sendNotificationOnJobReject: bool
    startNextRoundAutomatically: bool
    status: int


class JobRoundSearchCriteriaIN(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    includeNonRespondingResources: bool
    includeNotRequestedResources: bool
    includeRejectingResources: bool
    propertyList: Optional[List[Optional[Property]]] = None
    resourceStatus: Optional[List[Optional[ResourceStatus]]] = None
    roundId: int
    searchCriterionId: int
    workingStatus: Optional[List[Optional[WorkingStatus]]] = None


class JobRoundResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[JobRound]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobRoundRankingMethodList(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[List[Optional[JobRoundRankingMethod]]] = None


class JobRoundRankingMethodListResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[List[Optional[JobRoundRankingMethod]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class JobRoundSearchcriteriaResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[JobRoundSearchCriteria]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Job(BaseModel):
    """
    Used in:
        ReportJob30
    """

    customerID: int
    item_Status: int
    job_CreationDate_from: Optional[datetime]
    job_CreationDate_to: Optional[datetime]
    job_SourceLanguage: Optional[str]
    job_Status: int
    job_TargetLanguage: Optional[str]
    job_resourceID: int


class OrderResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[Order]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class OrderIN(BaseModel):
    """
    Used in:
        DataOrder30
    """

    currency: Optional[str]
    customerContactID: int
    customerID: int
    deliveryDeadline: Optional[datetime]
    orderDate: Optional[datetime]
    orderID: int
    projectManagerID: int
    projectManagerMemo: Optional[str]
    projectName: Optional[str]
    rate: Optional[float]
    referenceNumber: Optional[str]
    subject: Optional[str]


class LinkListResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[List[Optional[Link]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Order(BaseModel):
    """
    Used in:
        DataOrder30
    """

    customerID: int
    itemStatus: Optional[List[Optional[ItemStatus]]]
    languageCode: str
    orderStatus: int
    projectDescription: Optional[str]
    projectName: Optional[str]
    projectType: ProjectType
    propertiesList: Optional[List[Optional[Property]]]
    sourceLanguage: Optional[str]
    statusProjectFileArchiving: int
    targetLanguage: Optional[str]
    teamMember: Optional[SelectionEntry_TeamMember]
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: Optional[SelectionEntry_TimeFrame]


class TemplateListResult(BaseModel):
    """
    Used in:
        DataOrder30,
        DataQuote30
    """

    data: Optional[List[Optional[Template]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class IntegerList(BaseModel):
    """
    Used in:
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataResource30,
        DataCustomer30,
        DataCustomFields30
    """

    integerList: Optional[List[Optional[int]]] = None


class OrderListResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[List[Optional[Order]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class QuoteResult(BaseModel):
    """
    Used in:
        DataQuote30
    """

    data: Optional[Quote]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class QuoteListResult(BaseModel):
    """
    Used in:
        DataQuote30
    """

    data: Optional[List[Optional[Quote]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class QuoteIN(BaseModel):
    """
    Used in:
        DataQuote30
    """

    creationDate: Optional[datetime]
    currency: Optional[str]
    customerID: int
    projectManagerMemo: Optional[str]
    projectName: Optional[str]
    quoteID: int
    referenceNumber: Optional[str]
    status: int
    subject: Optional[str]


class SearchFilter_Quote(BaseModel):
    """
    Used in:
        DataQuote30
    """

    languageCode: str
    propertiesList: Optional[List[Optional[Property]]]
    selectionEntryCustomer: Optional[SelectionEntry_Customer]
    SelectionEntry_Resource: Optional[SelectionEntry_Resource]
    SelectionEntry_TeamMember: Optional[SelectionEntry_TeamMember]
    sourceLanguage: Optional[str]
    quoteStatus: int
    targetLanguage: Optional[str]
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: Optional[SelectionEntry_TimeFrame]


class RequestIN(BaseModel):
    """
    Used in:
        DataRequest30
    """

    briefDescription: Optional[str]
    creationDate: Optional[datetime]
    deliveryDate: Optional[datetime]
    orderID: int
    quotationDate: Optional[datetime]
    quoteID: int
    requestID: int
    status: int
    subject: Optional[str]


class RequestResult(BaseModel):
    """
    Used in:
        DataRequest30
    """

    data: Optional[Request]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class RequestListResult(BaseModel):
    """
    Used in:
        DataRequest30
    """

    data: Optional[List[Optional[Request]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Request(BaseModel):
    """
    Used in:
        DataRequest30
    """

    languageCode: str
    propertiesList: Optional[List[Optional[Property]]]
    SelectionEntry_Customer: Optional[SelectionEntry_Customer]
    sourceLanguage: Optional[str]
    requestStatus: int
    targetLanguage: Optional[str]
    textmodulesList: Optional[List[Optional[Textmodule]]]
    timeFrame: Optional[SelectionEntry_TimeFrame]


class ItemListResult(BaseModel):
    """
    Used in:
        DataItem30
    """

    data: Optional[List[Optional[Item]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ItemIN(BaseModel):
    """
    Used in:
        DataItem30
    """

    briefDescription: Optional[str]
    comment: Optional[str]
    deliveryDeadline: Optional[datetime]
    itemID: int
    projectID: int
    projectType: ProjectType
    reference: Optional[str]
    status: int
    totalPrice: float


class ItemResult(BaseModel):
    """
    Used in:
        DataItem30
    """

    data: Optional[Item]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ResourceListResult(BaseModel):
    """
    Used in:
        DataResource30
    """

    data: Optional[List[Optional[Resource]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ResourceResult(BaseModel):
    """
    Used in:
        DataResource30
    """

    data: Optional[Resource]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Resource(BaseModel):
    """
    Used in:
        DataResource30
    """

    contact_resourceID: int
    email: Optional[str]
    languageCode: str
    name1: Optional[str]
    name2: Optional[str]
    propertiesList: Optional[List[Optional[Property]]]
    resourceType: ResourceType
    resourceStatus: ResourceStatus
    sourceLanguageCode: Optional[str]
    targetLanguageCode: Optional[str]
    textmodulesList: Optional[List[Optional[Textmodule]]]
    workingStatus: WorkingStatus


class AccountResult(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    data: Optional[Account]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ResourceIN(BaseModel):
    """
    Used in:
        DataResource30
    """

    academicTitle: Optional[str]
    costCenter: Optional[str]
    currency: Optional[str]
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    fullName: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    resourceID: int
    resourceType: ResourceType
    skypeID: Optional[str]
    status: int
    supervisor1: Optional[str]
    supervisor2: Optional[str]
    userId: int
    website: Optional[str]
    workingStatus: WorkingStatus


class PaymentInfoResult(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    data: Optional[PaymentInfo]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CustomerListResult(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    data: Optional[List[Optional[Customer]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CustomerIN(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    academicTitle: Optional[str]
    costCenter: Optional[str]
    currency: Optional[str]
    customerID: int
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    fullName: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    skypeID: Optional[str]
    status: int
    userId: int
    website: Optional[str]


class CustomerResult(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    data: Optional[Customer]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class SearchFilter_Customer(BaseModel):
    """
    Used in:
        DataCustomer30,
        ReportCustomer30
    """

    contact_resourceID: int
    customerType: CustomerType
    email: Optional[str]
    languageCode: str
    name1: Optional[str]
    name2: Optional[str]
    propertiesList: Optional[List[Optional[Property]]]
    sourceLanguageCode: Optional[str]
    customerStatus: CustomerStatus
    textmodulesList: Optional[List[Optional[Textmodule]]]


class WorkflowListResult(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    data: Optional[List[Optional[Workflow]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CustomerContactListResult(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    data: Optional[List[Optional[CustomerContact]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class CustomerContactIN(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    addressID: int
    costCenter: Optional[str]
    customerContactID: int
    customerID: int
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    phone: Optional[str]
    status: int
    supervisor1: Optional[str]
    supervisor2: Optional[str]
    userId: int


class CustomerContactResult(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    data: Optional[CustomerContact]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ResourceContactIN(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    academicTitle: Optional[str]
    addressID: int
    email: Optional[str]
    externalID: Optional[str]
    fax: Optional[str]
    formOfAddress: int
    mobilePhone: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    opening: Optional[str]
    phone: Optional[str]
    resourceContactID: int
    resourceID: int
    skypeID: Optional[str]
    status: int
    userId: int


class ResourceContactResult(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    data: Optional[ResourceContact]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class ResourceContactListResult(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    data: Optional[List[Optional[ResourceContact]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class AddressIN(BaseModel):
    """
    Used in:
        DataCustomerAddress30,
        DataResourceAddress30
    """

    addressID: int
    addressType: AddressType
    city: Optional[str]
    country: Optional[str]
    description: Optional[str]
    name1: Optional[str]
    name2: Optional[str]
    office: Optional[str]
    state: Optional[str]
    street: Optional[str]
    street2: Optional[str]
    zip: Optional[str]


class FileResult(BaseModel):
    """
    Used in:
        DataDocument30
    """

    fileContent: Optional[bytes]
    fileSize: int
    filename: Optional[str]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class UserResult(BaseModel):
    """
    Used in:
        DataUser30
    """

    data: Optional[User]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class UserListResult(BaseModel):
    """
    Used in:
        DataUser30
    """

    data: Optional[List[Optional[User]]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class TextmoduleIN(BaseModel):
    """
    Used in:
        DataCustomFields30
    """

    dateValue: Optional[datetime]
    flag: Optional[str]
    selectedValues: Optional[List[Optional[str]]] = None
    stringValue: Optional[str]
    textModuleUsageArea: TextModuleUsageArea


class TextmoduleResult(BaseModel):
    """
    Used in:
        DataCustomFields30
    """

    data: Optional[Textmodule]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None


class PropertyResult(BaseModel):
    """
    Used in:
        DataCustomFields30
    """

    data: Optional[Property]
    statusCode: int
    statusCodeAlphanumeric: Optional[str]
    statusMessage: Optional[str]
    warning_StatusCodeList: Optional[List[Optional[int]]] = None
