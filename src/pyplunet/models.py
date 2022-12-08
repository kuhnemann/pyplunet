from datetime import datetime
from typing import Any, List, Optional, Union

from pydantic import BaseModel as BM
from pydantic import Field

from .enums import (
    ContactPersonStatus,
    ExportedType,
    InvoiceStatusType,
    PayableStatus,
    ResourceType,
    SearchScope,
    SearchSelection_Customer,
    TimeFrameRelation_Invoice,
    TimeFrameRelation_Quote,
    TimeFrameRelation_Request,
)


class BaseModel(BM):
    class Config:
        use_enum_values = True


class SearchFilter_Customer(BaseModel):
    contact_resourceID: str = "-1"
    customerType: str = "-1"
    email: Optional[str] = None
    languageCode: str = "EN"
    name1: Optional[str] = None
    name2: Optional[str] = None
    propertiesList: List[Any] = Field(default_factory=list)
    sourceLanguageCode: Optional[str] = None
    customerStatus: str = "-1"
    textmodulesList: List[Any] = Field(default_factory=list)


class SelectionEntry_TeamMember(BaseModel):
    ID: int
    teamMember: ResourceType  # resourceEntryType


class SelectionEntry_Customer(BaseModel):
    customerEntryType: Optional[Union[SearchSelection_Customer, int]] = None
    mainID: int


class SelectionEntry_TimeFrame(BaseModel):
    dateFrom: datetime
    dateRelation: Union[
        SearchScope,
        TimeFrameRelation_Invoice,
        TimeFrameRelation_Quote,
        TimeFrameRelation_Request,
    ]
    dateTo: datetime


class SearchFilter_Order(BaseModel):
    customerID: int = -1
    itemStatus: List[Any] = Field(default_factory=list)
    languageCode: str = "EN"
    orderStatus: int = -1
    projectDescription: Optional[str] = None
    projectName: Optional[str] = None
    projectType: int = -1
    propertiesList: List[Any] = Field(default_factory=list)
    sourceLanguage: Optional[str] = None  # ISO 639-code
    statusProjectFileArchiving: int = -1
    targetLanguage: Optional[str] = None
    teamMember: Optional[SelectionEntry_TeamMember] = None
    textmodulesList: List[Any] = Field(default_factory=list)
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class SearchFilter_Quote(BaseModel):
    languageCode: str = "EN"
    propertiesList: List[Any] = Field(default_factory=list)
    selectionEntryCustomer: Optional[SelectionEntry_Customer] = None
    SelectionEntry_Resource: Optional[Any] = None  # TODO
    SelectionEntry_TeamMember: Optional[SelectionEntry_TeamMember] = None
    sourceLanguage: Optional[str] = None
    quoteStatus: Optional[int] = -1
    targetLanguage: Optional[str] = None
    textmodulesList: List[Any] = Field(default_factory=list)
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class SearchFilter_Job(BaseModel):
    customerID: Optional[int] = -1
    item_Status: Optional[int] = -1
    job_CreationDate_from: Optional[datetime] = None
    job_CreationDate_to: Optional[datetime] = None
    job_SourceLanguage: Optional[str] = None
    job_Status: Optional[int] = -1
    job_TargetLanguage: Optional[str] = None
    job_resourceID: Optional[int] = -1


class SearchFilter_Invoice(BaseModel):
    invoiceStatus: Optional[InvoiceStatusType] = "-1"
    customerID: Optional[str] = "-1"
    propertiesList: List[Any] = Field(default_factory=list)
    languageCode: Optional[str] = "EN"
    textmodulesList: List[Any] = Field(default_factory=list)
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class SearchFilter_Payable(BaseModel):
    exported: ExportedType = 3
    payableStatus: Optional[PayableStatus] = -1
    resourceID: Optional[int] = -1
    languageCode: Optional[str] = "EN"
    isoCodeCurrency: Optional[str] = None
    propertiesList: List[Any] = Field(default_factory=list)
    textmodulesList: List[Any] = Field(default_factory=list)
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class SearchFilter_Request(BaseModel):
    languageCode: str = "EN"
    propertiesList: List[Any] = Field(default_factory=list)
    selectionEntry_Customer: Optional[SelectionEntry_Customer] = None
    sourceLanguage: Optional[str] = None
    requestStatus: Optional[int] = -1
    targetLanguage: Optional[str] = None
    textmodulesList: List[Any] = Field(default_factory=list)
    timeFrame: Optional[SelectionEntry_TimeFrame] = None


class OrderIN(BaseModel):
    currency: Optional[Any] = None
    customerContactID: Optional[Any] = None
    customerID: Optional[Any] = None
    deliveryDeadline: Optional[Any] = None
    orderDate: Optional[Any] = None
    orderID: Optional[Any] = None
    projectManagerID: Optional[Any] = None
    projectManagerMemo: Optional[Any] = None
    projectName: Optional[Any] = None
    rate: Optional[Any] = None
    referenceNumber: Optional[Any] = None
    subject: Optional[Any] = None


class CustomerObject(BaseModel):
    academicTitle: Optional[str] = None
    costCenter: Optional[str] = None
    currency: Optional[str] = None
    customerID: int
    email: str
    externalID: Optional[str] = None
    fax: Optional[str] = None
    formOfAddress: int
    fullName: str
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    opening: Optional[str] = None
    phone: Optional[str] = None
    skypeID: Optional[str] = None
    status: int
    userId: int
    website: Optional[str] = None


class CustomerPaymentInformation(BaseModel):
    accountHolder: Optional[str] = None
    accountID: Optional[int] = None
    BIC: Optional[str] = None
    contractNumber: Optional[str] = None
    debitAccount: Optional[str] = None
    IBAN: Optional[str] = None
    paymentMethodID: Optional[int] = None
    preselectedTaxID: Optional[int] = None
    salesTaxID: Optional[str] = None


class CustomerContactObject(BaseModel):
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
    status: ContactPersonStatus
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: int


class CustomerContactIN(BaseModel):
    addressID: Optional[int] = None
    costCenter: Optional[str] = None
    customerContactID: Optional[int] = None
    customerID: Optional[int] = None
    email: Optional[str] = None
    externalID: Optional[str] = None
    fax: Optional[str] = None
    mobilePhone: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[ContactPersonStatus] = None
    supervisor1: Optional[str] = None
    supervisor2: Optional[str] = None
    userId: Optional[int] = None


class InvoiceObject(BaseModel):
    briefDescription: Optional[str] = None
    currencyCode: Optional[str] = None
    customerID: int
    gross: float
    invoiceDate: datetime
    invoiceDocuments: List[int] = Field(default_factory=list)
    invoiceID: int
    invoiceNr: str
    net: float
    orderIDs: List[int] = Field(default_factory=list)
    outgoing: float
    paid: float
    status: InvoiceStatusType
    subject: Optional[str] = None
    tax: float
    valueDate: datetime
