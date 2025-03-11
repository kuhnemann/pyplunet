from __future__ import annotations
from pydantic import BaseModel as BM
from pydantic import ConfigDict
from typing import Optional, List
from datetime import datetime

from .enums import (
    ContactType,
    WorkingStatus,
    CallbackType,
    TaxType,
    CreditNoteStatus,
    ItemStatus,
    TextModuleType,
    CustomerType,
    CustomerStatus,
    AddressType,
    TextModuleUsageArea,
    JobStatus,
    ResourceType,
    ResourceStatus,
    ProjectType,
    EventType,
    PayableStatus,
    PropertyType,
    JobRoundStatus,
    QuoteStatusType,
    RequestStatusType,
    ContactPersonStatus,
    InvoiceStatusType,
    ArchivStatus,
)


class BaseModel(BM):
    model_config = ConfigDict(use_enum_values=True)


class Amount(BaseModel):
    """
    Used in:
        DataJob30
    """

    baseUnitName: Optional[str] = None
    grossQuantity: Optional[float] = None
    netQuantity: Optional[float] = None
    serviceType: Optional[str] = None


class Tax(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30
    """

    active: bool
    expenseAccount: Optional[str] = None
    revenueAccount: Optional[str] = None
    taxDescription: Optional[str] = None
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
    memo: Optional[str] = None
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
        DataAdmin30,
        DataJob30,
        DataItem30
    """

    active: bool
    articleNumber: Optional[str] = None
    description: Optional[str] = None
    memo: Optional[str] = None
    priceUnitID: int
    service: Optional[str] = None


class PayableItem(BaseModel):
    """
    Used in:
        DataPayable30
    """

    briefDescription: Optional[str] = None
    invoiceID: int
    itemNumber: int
    jobDate: Optional[datetime] = None
    jobNo: Optional[str] = None
    jobStatus: JobStatus
    payableItemID: int
    projectType: ProjectType
    taxType: TaxType
    totalprice: float


class Textmodule(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataAdmin30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataResource30,
        DataCustomer30,
        ReportCustomer30,
        DataCustomFields30
    """

    availableValues: Optional[List[str]] = None
    dateValue: Optional[datetime] = None
    flag: Optional[str] = None
    flag_MainTextModule: Optional[str] = None
    selectedValues: Optional[List[str]] = None
    stringValue: Optional[str] = None
    textModuleLabel: Optional[str] = None
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

    briefDescription: Optional[str] = None
    currencyCode: Optional[str] = None
    customerID: int
    gross: float
    invoiceDate: Optional[datetime] = None
    invoiceDocuments: Optional[List[str]] = None
    invoiceID: int
    invoiceNr: Optional[str] = None
    net: float
    orderIDs: Optional[List[int]] = None
    outgoing: float
    paid: float
    status: InvoiceStatusType | int
    subject: Optional[str] = None
    tax: float
    valueDate: Optional[datetime] = None


class InvoiceItem(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    briefDescription: Optional[str] = None
    comment: Optional[str] = None
    invoiceID: int
    invoiceItemID: int
    itemNumber: Optional[str] = None
    languageCombinationID: int
    orderID: int
    orderItemId: int
    taxType: TaxType
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
    PricelistNameEN: Optional[str] = None
    currency: Optional[str] = None
    memo: Optional[str] = None
    withWhiteSpace: bool
    adminPriceListId: int
    adminPriceListPartnerType: Optional[ContactType] = None


class Property(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataCreditNote30,
        DataAdmin30,
        DataJobRound30,
        DataOrder30,
        DataQuote30,
        DataRequest30,
        DataResource30,
        DataCustomer30,
        ReportCustomer30,
        DataCustomFields30
    """

    avaliablePropertyValueIDList: Optional[List[int]] = None
    mainPropertyNameEnglish: Optional[str] = None
    propertyNameEnglish: Optional[str] = None
    propertyType: PropertyType
    selectedPropertyValueID: int
    selectedPropertyValueList: Optional[List[int]] = None


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

    briefDescription: Optional[str] = None
    creditNoteID: int
    creditNoteItemID: int
    itemNumber: Optional[str] = None
    taxTypeID: int
    totalPrice: float


class PropertyResult(BaseModel):
    """
    Used in:
        DataAdmin30,
        DataCustomFields30
    """

    data: Optional[Property] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class Language(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    active: bool
    favorite: bool
    folderName: Optional[str] = None
    id: int
    isoCode: Optional[str] = None
    name: Optional[str] = None


class Currency(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    currencyID: int
    description: Optional[str] = None
    isoCode: Optional[str] = None


class PropertyValue(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    active: bool
    id: int
    label: Optional[str] = None


class Country(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    ID: int
    isoCode: Optional[str] = None
    name: Optional[str] = None


class Workflow(BaseModel):
    """
    Used in:
        DataAdmin30,
        DataCustomer30
    """

    description: Optional[str] = None
    name: Optional[str] = None
    status: WorkingStatus | int
    type: int
    workflowId: int


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
    serverAddress: Optional[str] = None


class CompanyCode(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    companyCodeID: int
    companyCodeRights: bool
    description_Long: Optional[str] = None
    description_Short: Optional[str] = None
    isCompanyCodeInvoice: bool


class Service(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    abbreviation: Optional[str] = None
    id: int
    jobCategory: Optional[str] = None
    name: Optional[str] = None


class Job(BaseModel):
    """
    Used in:
        DataJob30
    """

    countSourceFiles: int
    dueDate: Optional[datetime] = None
    itemID: int
    jobID: int
    jobTypeFull: Optional[str] = None
    jobTypeShort: Optional[str] = None
    projectID: int
    projectType: ProjectType
    resourceID: int
    startDate: Optional[datetime] = None
    status: JobStatus | int


class TrackingTimeList(BaseModel):
    """
    Used in:
        DataJob30
    """

    completed: float
    trackingTimeList: Optional[List[JobTrackingTime]] = None


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

    amounts: Optional[List[Amount]] = None
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
    status: JobRoundStatus | int


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
    propertyList: Optional[List[Property]] = None
    resourceStatus: Optional[List[ResourceStatus]] = None
    roundId: int
    searchCriterionId: int
    workingStatus: Optional[List[WorkingStatus]] = None


class Order(BaseModel):
    """
    Used in:
        DataOrder30
    """

    currency: Optional[str] = None
    customerContactID: int
    customerID: int
    deliveryDeadline: Optional[datetime] = None
    orderClosingDate: Optional[datetime] = None
    orderDate: Optional[datetime] = None
    orderDisplayName: Optional[str] = None
    orderID: int
    projectManagerID: int
    projectName: Optional[str] = None
    rate: float
    requestID: int
    subject: Optional[str] = None


class Link(BaseModel):
    """
    Used in:
        DataOrder30
    """

    linkId: int
    memo: Optional[str] = None
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
    templateDescription: Optional[str] = None
    templateID: int
    templateName: Optional[str] = None


class Quote(BaseModel):
    """
    Used in:
        DataQuote30
    """

    creationDate: Optional[datetime] = None
    currency: Optional[str] = None
    orderID: Optional[List[int]] = None
    projectName: Optional[str] = None
    quoteID: int
    quoteNumber: Optional[str] = None
    rate: float
    requestID: int
    status: QuoteStatusType | int
    subject: Optional[str] = None


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

    briefDescription: Optional[str] = None
    creationDate: Optional[datetime] = None
    deliveryDate: Optional[datetime] = None
    orderID: int
    orderIDList: Optional[List[int]] = None
    quotationDate: Optional[datetime] = None
    quoteID: int
    quoteIDList: Optional[List[int]] = None
    requestID: int
    status: RequestStatusType | int
    subject: Optional[str] = None


class Item(BaseModel):
    """
    Used in:
        DataItem30
    """

    briefDescription: Optional[str] = None
    comment: Optional[str] = None
    deliveryDeadline: Optional[datetime] = None
    invoiceID: int
    itemID: int
    jobIDList: Optional[List[int]] = None
    orderID: int
    projectID: int
    projectType: ProjectType
    reference: Optional[str] = None
    sourceLanguage: Optional[str] = None
    status: ItemStatus | int
    targetLanguage: Optional[str] = None
    taxType: TaxType
    totalPrice: float


class Resource(BaseModel):
    """
    Used in:
        DataResource30
    """

    academicTitle: Optional[str] = None
    costCenter: Optional[str] = None
    currency: Optional[str] = None
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    fullName: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    resourceID: int
    resourceType: ResourceType
    skypeID: Optional[str] = None
    status: ResourceStatus | int
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: int
    website: Optional[str] = None
    workingStatus: WorkingStatus


class Account(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    accountDescription: Optional[str] = None
    accountID: int
    accountNumber: Optional[str] = None
    accountType: int
    active: bool


class PaymentInfo(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    accountHolder: Optional[str] = None
    accountID: int
    BIC: Optional[str] = None
    contractNumber: Optional[str] = None
    debitAccount: Optional[str] = None
    IBAN: Optional[str] = None
    paymentMethodID: int
    preselectedTaxID: int
    salesTaxID: Optional[str] = None


class Customer(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    academicTitle: Optional[str] = None
    costCenter: Optional[str] = None
    currency: Optional[str] = None
    customerID: int
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    fullName: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    skypeID: Optional[str] = None
    status: CustomerStatus | int
    userId: int
    website: Optional[str] = None


class CustomerContact(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    addressID: int
    costCenter: Optional[str] = None
    customerContactID: int
    customerID: int
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    phone: Optional[str] = None
    status: ContactPersonStatus | int
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: int


class ResourceContact(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    academicTitle: Optional[str] = None
    addressID: int
    costCenter: Optional[str] = None
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    resourceContactID: int
    resourceID: int
    skypeID: Optional[str] = None
    status: ContactPersonStatus | int
    userId: int


class User(BaseModel):
    """
    Used in:
        DataUser30
    """

    contactID: int
    contactType: ContactType
    customerContactID: int
    password: Optional[str] = None
    userID: int
    userName: Optional[str] = None


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
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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

    data: Optional[str] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class TaxListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataCreditNote30
    """

    data: Optional[List[Tax]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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

    data: Optional[datetime] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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
    memo: Optional[str] = None
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

    data: Optional[PriceLine] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PriceUnitListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataAdmin30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[PriceUnit]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PriceLineListResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[PriceLine]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PayableItemResultList(BaseModel):
    """
    Used in:
        DataPayable30
    """

    data: Optional[List[PayableItem]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PriceUnitResult(BaseModel):
    """
    Used in:
        DataPayable30,
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[PriceUnit] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PayableItemIN(BaseModel):
    """
    Used in:
        DataPayable30
    """

    briefDescription: Optional[str] = None
    invoiceID: int
    itemNumber: int
    jobDate: Optional[datetime] = None
    jobID: int
    jobNo: Optional[str] = None
    jobStatus: JobStatus
    taxType: TaxType
    totalprice: float


class SearchFilter_Payable(BaseModel):
    """
    Used in:
        DataPayable30
    """

    exported: int
    isoCodeCurrency: Optional[str] = None
    languageCode: Optional[str] = None
    resourceID: int
    payableStatus: PayableStatus
    textmodulesList: Optional[List[Textmodule]] = None
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

    data: Optional[List[int]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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

    data: Optional[List[str]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class InvoiceResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    data: Optional[Invoice] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class InvoiceItemIN(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    briefDescription: Optional[str] = None
    comment: Optional[str] = None
    invoiceID: int
    invoiceItemID: int
    languageCombinationID: int
    orderID: int
    taxType: TaxType
    totalPrice: float


class InvoiceItemResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    data: Optional[List[InvoiceItem]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PricelistListResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30,
        DataResource30
    """

    data: Optional[List[Pricelist]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Invoice(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30
    """

    customerID: int
    exported: int
    languageCode: str
    propertiesList: Optional[List[Property]] = None
    invoiceStatus: InvoiceStatusType | int
    textmodulesList: Optional[List[Textmodule]] = None
    timeFrame: SelectionEntry_TimeFrame


class PricelistEntryList(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[List[PricelistEntry]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PricelistResult(BaseModel):
    """
    Used in:
        DataOutgoingInvoice30,
        DataJob30,
        DataItem30
    """

    data: Optional[Pricelist] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_CreditNote(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    customerID: int
    exported: int
    languageCode: str
    propertiesList: Optional[List[Property]] = None
    creditNoteStatus: CreditNoteStatus
    textmodulesList: Optional[List[Textmodule]] = None
    timeFrame: SelectionEntry_TimeFrame


class CreditNoteItemIN(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    briefDescription: Optional[str] = None
    creditNoteID: int
    taxTypeID: int
    totalPrice: float


class CreditNoteListResult(BaseModel):
    """
    Used in:
        DataCreditNote30
    """

    data: Optional[List[CreditNoteItem]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PropertyListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    m_Data: Optional[List[PropertyResult]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class LanguageListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Language]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CurrencyList(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Currency]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class languageResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[Language] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class PropertyValueListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[PropertyValue]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CountryListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Country]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class WorkflowListResult(BaseModel):
    """
    Used in:
        DataAdmin30,
        DataCustomer30
    """

    data: Optional[List[Workflow]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class TextmoduleListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Textmodule]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CallbackListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Callback]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CompanyCodeListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[CompanyCode]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ServiceListResult(BaseModel):
    """
    Used in:
        DataAdmin30
    """

    data: Optional[List[Service]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[Job] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobListResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[List[Job]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobIN(BaseModel):
    """
    Used in:
        DataJob30
    """

    contactPersonID: int
    dueDate: Optional[datetime] = None
    itemID: int
    jobID: int
    projectID: int
    projectType: ProjectType
    resourceID: int
    startDate: Optional[datetime] = None
    status: JobStatus | int


class JobTrackingTimeResult(BaseModel):
    """
    Used in:
        DataJob30
    """

    data: Optional[TrackingTimeList] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobTrackingTime(BaseModel):
    """
    Used in:
        DataJob30
    """

    resourceID: int
    comment: Optional[str] = None
    dateFrom: Optional[datetime] = None
    dateTo: Optional[datetime] = None


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

    data: Optional[JobMetric] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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
    status: JobRoundStatus | int


class JobRoundSearchCriteriaIN(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    includeNonRespondingResources: bool
    includeNotRequestedResources: bool
    includeRejectingResources: bool
    propertyList: Optional[List[Property]] = None
    resourceStatus: Optional[List[ResourceStatus]] = None
    roundId: int
    searchCriterionId: int
    workingStatus: Optional[List[WorkingStatus]] = None


class JobRoundResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[JobRound] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobRoundRankingMethodList(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[List[JobRoundRankingMethod]] = None


class JobRoundRankingMethodListResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[List[JobRoundRankingMethod]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class JobRoundSearchcriteriaResult(BaseModel):
    """
    Used in:
        DataJobRound30
    """

    data: Optional[JobRoundSearchCriteria] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Job(BaseModel):
    """
    Used in:
        ReportJob30
    """

    customerID: int
    item_Status: ItemStatus | int
    job_CreationDate_from: Optional[datetime] = None
    job_CreationDate_to: Optional[datetime] = None
    job_SourceLanguage: Optional[str] = None
    job_Status: JobStatus | int
    job_TargetLanguage: Optional[str] = None
    job_resourceID: int


class OrderResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[Order] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class OrderIN(BaseModel):
    """
    Used in:
        DataOrder30
    """

    currency: Optional[str] = None
    customerContactID: int
    customerID: int
    deliveryDeadline: Optional[datetime] = None
    orderDate: Optional[datetime] = None
    orderID: int
    projectManagerID: int
    projectManagerMemo: Optional[str] = None
    projectName: Optional[str] = None
    rate: float
    referenceNumber: Optional[str] = None
    subject: Optional[str] = None


class LinkListResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[List[Link]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Order(BaseModel):
    """
    Used in:
        DataOrder30
    """

    customerID: int
    itemStatus: Optional[List[ItemStatus]] = None
    languageCode: str
    orderStatus: ArchivStatus | int
    projectDescription: Optional[str] = None
    projectName: Optional[str] = None
    projectType: ProjectType
    propertiesList: Optional[List[Property]] = None
    sourceLanguage: Optional[str] = None
    statusProjectFileArchiving: int
    targetLanguage: Optional[str] = None
    teamMember: Optional[SelectionEntry_TeamMember] = None
    textmodulesList: Optional[List[Textmodule]] = None
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class TemplateListResult(BaseModel):
    """
    Used in:
        DataOrder30,
        DataQuote30
    """

    data: Optional[List[Template]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


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

    integerList: Optional[List[int]] = None


class OrderListResult(BaseModel):
    """
    Used in:
        DataOrder30
    """

    data: Optional[List[Order]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class QuoteResult(BaseModel):
    """
    Used in:
        DataQuote30
    """

    data: Optional[Quote] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class QuoteListResult(BaseModel):
    """
    Used in:
        DataQuote30
    """

    data: Optional[List[Quote]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class QuoteIN(BaseModel):
    """
    Used in:
        DataQuote30
    """

    creationDate: Optional[datetime] = None
    currency: Optional[str] = None
    customerID: int
    projectManagerMemo: Optional[str] = None
    projectName: Optional[str] = None
    quoteID: int
    referenceNumber: Optional[str] = None
    status: QuoteStatusType | int
    subject: Optional[str] = None


class SearchFilter_Quote(BaseModel):
    """
    Used in:
        DataQuote30
    """

    languageCode: str
    propertiesList: Optional[List[Property]] = None
    selectionEntryCustomer: Optional[SelectionEntry_Customer] = None
    SelectionEntry_Resource: Optional[SelectionEntry_Resource] = None
    SelectionEntry_TeamMember: Optional[SelectionEntry_TeamMember] = None
    sourceLanguage: Optional[str] = None
    quoteStatus: QuoteStatusType | int
    targetLanguage: Optional[str] = None
    textmodulesList: Optional[List[Textmodule]] = None
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class RequestIN(BaseModel):
    """
    Used in:
        DataRequest30
    """

    briefDescription: Optional[str] = None
    creationDate: Optional[datetime] = None
    deliveryDate: Optional[datetime] = None
    orderID: int
    quotationDate: Optional[datetime] = None
    quoteID: int
    requestID: int
    status: RequestStatusType | int
    subject: Optional[str] = None


class RequestResult(BaseModel):
    """
    Used in:
        DataRequest30
    """

    data: Optional[Request] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class RequestListResult(BaseModel):
    """
    Used in:
        DataRequest30
    """

    data: Optional[List[Request]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Request(BaseModel):
    """
    Used in:
        DataRequest30
    """

    languageCode: str
    propertiesList: Optional[List[Property]] = None
    SelectionEntry_Customer: Optional[SelectionEntry_Customer] = None
    sourceLanguage: Optional[str] = None
    requestStatus: RequestStatusType | int
    targetLanguage: Optional[str] = None
    textmodulesList: Optional[List[Textmodule]] = None
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class ItemListResult(BaseModel):
    """
    Used in:
        DataItem30
    """

    data: Optional[List[Item]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ItemIN(BaseModel):
    """
    Used in:
        DataItem30
    """

    briefDescription: Optional[str] = None
    comment: Optional[str] = None
    deliveryDeadline: Optional[datetime] = None
    itemID: int
    projectID: int
    projectType: ProjectType
    reference: Optional[str] = None
    status: ItemStatus | int
    taxType: TaxType
    totalPrice: float


class ItemResult(BaseModel):
    """
    Used in:
        DataItem30
    """

    data: Optional[Item] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ResourceListResult(BaseModel):
    """
    Used in:
        DataResource30
    """

    data: Optional[List[Resource]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ResourceResult(BaseModel):
    """
    Used in:
        DataResource30
    """

    data: Optional[Resource] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Resource(BaseModel):
    """
    Used in:
        DataResource30
    """

    contact_resourceID: int
    email: Optional[str] = None
    languageCode: str
    name1: Optional[str] = None
    name2: Optional[str] = None
    propertiesList: Optional[List[Property]] = None
    resourceType: ResourceType
    resourceStatus: ResourceStatus
    sourceLanguageCode: Optional[str] = None
    targetLanguageCode: Optional[str] = None
    textmodulesList: Optional[List[Textmodule]] = None
    workingStatus: WorkingStatus


class AccountResult(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    data: Optional[Account] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ResourceIN(BaseModel):
    """
    Used in:
        DataResource30
    """

    academicTitle: Optional[str] = None
    costCenter: Optional[str] = None
    currency: Optional[str] = None
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    fullName: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    resourceID: int
    resourceType: ResourceType
    skypeID: Optional[str] = None
    status: ResourceStatus | int
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: int
    website: Optional[str] = None
    workingStatus: WorkingStatus


class PaymentInfoResult(BaseModel):
    """
    Used in:
        DataResource30,
        DataCustomer30
    """

    data: Optional[PaymentInfo] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CustomerListResult(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    data: Optional[List[Customer]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CustomerIN(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    academicTitle: Optional[str] = None
    costCenter: Optional[str] = None
    currency: Optional[str] = None
    customerID: int
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    fullName: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    skypeID: Optional[str] = None
    status: CustomerStatus | int
    userId: int
    website: Optional[str] = None


class CustomerResult(BaseModel):
    """
    Used in:
        DataCustomer30
    """

    data: Optional[Customer] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class SearchFilter_Customer(BaseModel):
    """
    Used in:
        DataCustomer30,
        ReportCustomer30
    """

    contact_resourceID: int
    customerType: CustomerType
    email: Optional[str] = None
    languageCode: str
    name1: Optional[str] = None
    name2: Optional[str] = None
    propertiesList: Optional[List[Property]] = None
    sourceLanguageCode: Optional[str] = None
    customerStatus: CustomerStatus
    textmodulesList: Optional[List[Textmodule]] = None


class CustomerContactListResult(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    data: Optional[List[CustomerContact]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class CustomerContactIN(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    addressID: int
    costCenter: Optional[str] = None
    customerContactID: int
    customerID: int
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    phone: Optional[str] = None
    status: ContactPersonStatus | int
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: int


class CustomerContactResult(BaseModel):
    """
    Used in:
        DataCustomerContact30
    """

    data: Optional[CustomerContact] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ResourceContactIN(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    academicTitle: Optional[str] = None
    addressID: int
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    resourceContactID: int
    resourceID: int
    skypeID: Optional[str] = None
    status: ContactPersonStatus | int
    userId: int


class ResourceContactResult(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    data: Optional[ResourceContact] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class ResourceContactListResult(BaseModel):
    """
    Used in:
        DataResourceContact30
    """

    data: Optional[List[ResourceContact]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class AddressIN(BaseModel):
    """
    Used in:
        DataCustomerAddress30,
        DataResourceAddress30
    """

    addressID: int
    addressType: AddressType
    city: Optional[str] = None
    country: Optional[str] = None
    description: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    office: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None
    street2: Optional[str] = None
    zip: Optional[str] = None


class FileResult(BaseModel):
    """
    Used in:
        DataDocument30
    """

    fileContent: Optional[bytes] = None
    fileSize: int
    filename: Optional[str] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class UserResult(BaseModel):
    """
    Used in:
        DataUser30
    """

    data: Optional[User] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class UserListResult(BaseModel):
    """
    Used in:
        DataUser30
    """

    data: Optional[List[User]] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None


class TextmoduleIN(BaseModel):
    """
    Used in:
        DataCustomFields30
    """

    dateValue: Optional[datetime] = None
    flag: Optional[str] = None
    selectedValues: Optional[List[str]] = None
    stringValue: Optional[str] = None
    textModuleUsageArea: TextModuleUsageArea


class TextmoduleResult(BaseModel):
    """
    Used in:
        DataCustomFields30
    """

    data: Optional[Textmodule] = None
    statusCode: int
    statusCodeAlphanumeric: Optional[str] = None
    statusMessage: Optional[str] = None
    warning_StatusCodeList: Optional[List[int]] = None
