from enum import Enum


class SearchSelection_Resource(Enum):
    AGENCY = 9
    RESOURCE = 1


class FolderTypes(Enum):
    CUSTOMER = 19
    INVOICE = 13
    ORDER_FINAL = 12
    ORDER_ITEM_CAT = 8
    ORDER_ITEM_REFERENCE = 17
    ORDER_ITEM_SOURCE = 16
    ORDER_JOB_IN = 22
    ORDER_JOB_OUT = 23
    ORDER_OUT = 10
    ORDER_PRM = 25
    ORDER_REFERENCE = 5
    ORDER_SOURCE = 6
    QUOTE_FINAL = 11
    QUOTE_ITEM_CAT = 7
    QUOTE_ITEM_REFERENCE = 15
    QUOTE_ITEM_SOURCE = 14
    QUOTE_JOB_IN = 20
    QUOTE_JOB_OUT = 21
    QUOTE_OUT = 9
    QUOTE_PRM = 24
    QUOTE_REFERENCE = 3
    QUOTE_SOURCE = 4
    REQUEST_REFERENCE = 1
    REQUEST_SOURCE = 2
    RESOURCE = 18


class InvoiceType(Enum):
    CREDIT_NOTES = 2
    PAYABLES = 3
    RECEIVABLES = 1


class WorkingStatus(Enum):
    EXTERNAL = 2
    INTERNAL = 1


class QuoteStatusType(Enum):
    ACCEPTED = 7
    CANCELED = 5
    CHANGE_INTO_ORDER = 4
    CHECK_CLEARANCE = 11
    EXPIRED = 6
    IN_PREPARATION = 9
    NEW = 8
    PENDING = 1
    REJECTED = 3
    REVISED = 2


class Format(Enum):
    ABBREVIATED_VERSION = 1
    OUTPUT_AS_IN_ORDER = 6
    QUANTITY_NOT_WEIGHTED = 4
    STANDARD = 0
    STANDARD_WITH_PRICE_MEMO = 5
    TM_DISCONT = 3
    WEIGHTED_QUANTITY = 2


class WorkflowType(Enum):
    ORDER = 1
    QUOTE_ORDER = 2
    STANDARD = 0


class AddressType(Enum):
    DELIVERY = 1
    INVOICE = 2
    OTHER = 3


class JobRequestRankingMethod(Enum):
    JOB_FEEDBACK = 3
    JOBS_FOR_CUSTOMER = 2
    PRICE = 4
    RANKING_RESOURCE_ASSESSMENT = 1


class FormOfAddressType(Enum):
    COMPANY = 3
    MADAM = 2
    SIR = 1


class JobRoundAssignmentMethod(Enum):
    FIRST_COME_FIRST_SERVE = 2
    MANUAL = 1
    TOP_RANKED = 4


class TimeFrameRelation_Quote(Enum):
    EVENT_END_DATE = 9
    EVENT_START_DATE = 8
    INSTRUCTED_DATE = 10
    ITEM_CREATION_DATE = 2
    ITEM_DELIVERY_DATE = 4
    QUOTE_BINDING_DEADLINE_DATE = 6
    QUOTE_CREATION_DATE = 1
    QUOTE_DELIVERY_DATE = 3
    REJECTION_DATE = 7
    REQUEST_DATE = 5


class DocumentStatus(Enum):
    DOCUMENTS_APPROVED = 7
    DOCUMENTS_AVAILABLE = 1
    DOCUMENTS_DOWNLOADED = 2
    DOCUMENTS_IN_REVIEW = 3
    DOCUMENTS_RE_DELIVERED = 6
    NO_DOCUMENTS_AVAILABLE = 0
    POSTPROCESSING_IN_PROGRESS = 5
    POSTPROCESSING_REQUESTED = 4


class APIVersion(Enum):
    Version_25 = "Version_25"
    Version_30 = "Version_30"


class CurrencyType(Enum):
    HOMECURRENCY = 2
    PROJECTCURRENCY = 1


class CompanyCodeType(Enum):
    INVOICE = 1
    RIGHTS = 2


class CustomerType(Enum):
    DIRECT = 0
    DIRECT_INDIRECT = 1
    INDIRECT = 2


class JobRoundStatus(Enum):
    ASSIGNMENT_ERROR = 2
    CANCELED = 5
    IN_PREPARATION = 0
    JOB_ASSIGNED = 3
    NO_ASSIGNMENT = 4
    REACTION_TIME_ELAPSED = 6
    REQUESTED = 1


class CatType(Enum):
    ACROSS = 5
    CATALYST = 14
    DEJAVU = 12
    FALCON = 17
    FUSION = 11
    HELIUM = 15
    IDIOM = 9
    LOGOPORT = 8
    MEMOQ = 4
    MEMSOURCE = 16
    PASSOLO = 7
    PRACTICOUNT = 6
    TRADOS = 1
    TRANSIT = 3
    WORDFAST = 13
    XTM = 10


class SearchSelection_TeamMember(Enum):
    PROJECT_MANAGER = 4
    RESOURCE = 1
    SUPERVISOR = 8


class ItemStatus(Enum):
    ACCEPTED = 12
    APPROVED = 3
    CANCELED = 5
    DELIVERABLE = 7
    DELIVERED = 2
    IN_PREPERATION = 8
    IN_PROGRESS = 1
    INVOICED = 4
    NEW_AUTO = 6
    PAID = 9
    PENDING = 11
    REJECTED = 13
    SUM = 14
    WITHOUT_INVOICE = 10


class ArchivStatus(Enum):
    ACTIVE = 1
    ARCHIVED = 3
    COMPLETED = 6
    COMPLETED_ARCHIVABLE = 2
    IN_PREPARATION = 5
    QUOTE_MOVED_TO_ORDER = 4


class JobRoundAssignmentLimitType(Enum):
    ALL = 0
    LIMIT_X = 1
    MANUAL_SELECTED = 2


class SearchSelection_Customer(Enum):
    ACCOUNT_MANAGER = 7
    CUSTOMER = 1
    INDIRECT_CUSTOMER = 3


class TimeFrameRelation_Request(Enum):
    REQUEST_DATE = 1


class PayableStatus(Enum):
    CANCELED = 3
    CREATED_BY_EXTERNAL_USER = 4
    IN_PREPARATION = 5
    INVOICE_CHECKED = 6
    OUTSTANDING = 1
    PAID = 2


class RequestStatusType(Enum):
    CANCELED = 5
    CHANGED_INTO_ORDER = 7
    CHANGED_INTO_QUOTE = 6
    IN_PREPARATION = 1
    NEW_AUTO = 8
    PENDING = 2
    REJECTED = 9


class ResourceStatus(Enum):
    ACTIVE = 1
    BLOCKED = 3
    DELETION_REQUESTED = 10
    DISQUALIFIED = 9
    NEW = 4
    NEW_AUTO = 6
    NOT_ACTIVE_OR_OLD = 2
    PREMIUM = 5
    PROBATION = 7
    QUALIFIED = 8


class ProjectType(Enum):
    ORDER = 3
    QUOTE = 1


class PropertyUsageArea(Enum):
    CUSTOMER = 1
    ORDER = 6
    ORDER_ITEM = 10
    ORDER_JOB = 12
    QUOTE = 5
    QUOTE_ITEM = 9
    QUOTE_JOB = 11
    REQUEST = 4
    RESOURCE = 2


class ResourceType(Enum):
    PROJECT_MANAGER = 2
    RESOURCES = 0
    SUPERVISOR = 3
    TEAM_MEMBER = 1


class CustomerStatus(Enum):
    ACTIVE = 1
    AQUISITION_ADDRESS = 6
    BLOCKED = 5
    CONTACTED = 3
    DELETION_REQUESTED = 8
    NEW = 4
    NEW_AUTO = 7
    NOT_ACTIVE = 2


class JobStatus(Enum):
    APPROVED = 3
    ASSIGNED_WAITING = 7
    CANCELED = 4
    DELIVERED = 2
    IN_PREPERATION = 0
    IN_PROGRESS = 1
    INVOICE_ACCEPTED = 5
    INVOICE_CHECKED = 9
    INVOICE_CREATED = 10
    OVERDUE = 13
    PAYED = 6
    REQUESTED = 8
    TRANSFERRED_TO_ORDER = 12
    WITHOUT_INVOICE = 11


class CallbackType(Enum):
    NOTIFY = 2
    OBSERVER = 1


class WorkflowStatus(Enum):
    CANCELED = 2
    INPREPARATION = 0
    RELEASED = 1
    RELEASED_FOR_SELECTION = 3


class SearchScope(Enum):
    DATE_OF_ORDER = 1
    END_dATE_EVENT = 8
    INSTALLMENT_DATE = 6
    ITEM_CREATION_DATE = 2
    ITEM_DELIVERED_ON = 5
    ITEM_DUE_DATE = 4
    ORDER_CLOSING_DATE = 9
    ORDER_DUE_DATE = 3
    START_DATE_EVENT = 7


class TaxType(Enum):
    INFO = 3
    INFO_SUM = 6
    PRICE_BLOCK = 12
    SUM = 4
    TAX_1 = 0
    TAX_1_2 = 5
    TAX_1_2_3 = 8
    TAX_1_2_3_4 = 14
    TAX_1_2_3_4_5 = 14
    TAX_1_3 = 10
    TAX_1_4 = 17
    TAX_2 = 1
    TAX_2_3 = 11
    TAX_2_4_5 = 16
    TAX_3 = 7
    TAX_4 = 9
    TAX_5 = 13
    WITHOUT_TAX = 2


class TimeFrameRelation_Invoice(Enum):
    INVOICE_DATE = 1
    PAYABLE_UNTIL = 3
    PAYED = 4
    VALUTA = 2


class ExportedType(Enum):
    BOTH = 3
    EXPORTED = 1
    NOT_EXPORTED = 2


class JobActionLink(Enum):
    ACCEPT_JOB = 1
    DECLINE_JOB = 2
    DOWNLOADLINK_DOCUMENTS_JOB = 4
    JUMP_INTO_JOB = 3


class TextModuleType(Enum):
    DATE_FIELD = 3
    HYPER_LINK = 7
    LIST_BOX = 2
    MEMO_FIELD = 4
    MEMO_HISTORY_FIELD = 5
    NUMBER_FIELD = 6
    TEXT_FIELD = 1


class InvoiceStatusType(Enum):
    CANCELED = 3
    CANCELLATION_VOUCHER = 7
    IN_PREPARATION = 5
    OUTSTANDING = 1
    PAID = 2
    REMINDER_CREATED = 4
    UNCOLLECTABLE = 6
    UNDEFINED = 0


class EventType(Enum):
    DELIVERY_DATE_CHANGED = 5
    ENTRY_DELETED = 3
    NEW_ENTRY_CREATED = 2
    START_DATE_CHANGED = 4
    STATUS_CHANGED = 1
    UNDEFINED = 0


class ContactPersonStatus(Enum):
    ACTIVE = 1
    CONTACTED = 3
    DELETION_REQUESTED = 4
    NOT_ACTIVE = 2


class TextModuleUsageArea(Enum):
    CUSTOMER = 1
    ORDER = 6
    ORDER_CUSTOMER_LOGIN = 19
    ORDER_JOB = 11
    PAYMENT = 8
    QUOTE = 5
    QUOTE_CUSTOMER_LOGIN = 18
    QUOTE_JOB = 10
    RECEIVABLES = 7
    RECEIVABLES_CREDIT_NOTE = 9
    REQUEST = 4
    REQUEST_CUSTOMER_LOGIN = 17
    RESOURCE = 2
    VENDOR = 3


class ContactType(Enum):
    CUSTOMER = 1
    MISCELLANEOUS = 3
    RESOURCE = 2


class CreditNoteStatus(Enum):
    CANCELLATION_VOUCHER = 5
    CANCELLED = 4
    CLEARED = 3
    IN_PREPARATION = 1
    OPEN = 2
    PAID = 6


class ProjectManagementType(Enum):
    MEMBER_OF_PROJECT_TEAM = 1
    PROJECT_MANAGEMENT = 0
    PROJECT_MANAGER = 2
    SUPERVISOR = 3


class PropertyType(Enum):
    MULTI_SELECT = 2
    SINGLE_SELECT = 1


class OrderActionLink(Enum):
    JUMP_INTO_ORDER = 1
    JUMP_INTO_ORDER_ASSET = 2


class ProjectClassType(Enum):
    ALL = 0
    INTERPRETING = 2
    TRANSLATION = 1
