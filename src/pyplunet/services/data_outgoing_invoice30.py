from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CurrencyType, TaxType
from ..models import (
    BooleanResult,
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerResult,
    InvoiceItemIN,
    InvoiceItemResult,
    InvoiceResult,
    PriceLineIN,
    PriceLineListResult,
    PriceLineResult,
    PricelistEntryList,
    PricelistListResult,
    PricelistResult,
    PriceUnitListResult,
    PriceUnitResult,
    Result,
    SearchFilter_Invoice,
    StringArrayResult,
    StringResult,
    TaxListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataOutgoingInvoice30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_subject(self, invoice_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the subject.


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getSubject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_subject(self, subject: str, invoice_id: int) -> Result:
        """
        Sets the subject.


        :param subject: str
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setSubject
        response_model = Result

        arg = {"subject": subject, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete(self, invoice_id: int) -> Result:
        """
        Deletes a invoice identified by invoice ID.


        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.delete
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def search(
        self, search_filter: Union[SearchFilter_Invoice, dict]
    ) -> IntegerArrayResult:
        """
        No description of search in docs.


        :param search_filter: SearchFilter_Invoice
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Invoice:
            search_filter = SearchFilter_Invoice(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_documents(self, invoice_id: int) -> StringArrayResult:
        """
        Returns an instance of StringArrayResult, which contains an array of
        relative network paths for all available invoice documents.


        :param invoice_id: int
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceDocuments
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_receivable_account(self, account_id: int, invoice_id: int) -> Result:
        """
        Sets the receivable account.


        :param account_id: int
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setReceivableAccount
        response_model = Result

        arg = {"accountID": account_id, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_revenue_account(self, invoice_id: int) -> StringResult:
        """
        Returns the revenue account.


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getRevenueAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def create_invoice_document(
        self, template: str, format_id: int, invoice_id: int
    ) -> StringResult:
        """
        Method creates an invoice document as rtf-file and returns the unc
        path where the file is located.


        :param template: str
        :param format_id: int
        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.createInvoiceDocument
        response_model = StringResult

        arg = {"template": template, "formatId": format_id, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_receivable_account(self, invoice_id: int) -> StringResult:
        """
        Returns the receivable account.


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getReceivableAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_revenue_account(self, account_id: int, invoice_id: int) -> Result:
        """
        Sets the revenue account.


        :param account_id: int
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setRevenueAccount
        response_model = Result

        arg = {"accountID": account_id, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_is_invoice_exported(self, invoice_id: int, is_exported: bool) -> Result:
        """
        Defines if the invoice is already exported.


        :param invoice_id: int
        :param is_exported: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setIsInvoiceExported
        response_model = Result

        arg = {"invoiceID": invoice_id, "isExported": is_exported}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_invoice_item(
        self, invoice_item: Union[InvoiceItemIN, dict]
    ) -> IntegerResult:
        """
        Creates a new invoice item.


        :param invoice_item: InvoiceItemIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.insertInvoiceItem
        response_model = IntegerResult

        if type(invoice_item) != InvoiceItemIN:
            invoice_item = InvoiceItemIN(**invoice_item).dict()
        else:
            invoice_item = invoice_item.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_item,
            response_model=response_model,
            unpack_dict=False,
        )

    def update_invoice_item(
        self,
        invoice_item: Union[InvoiceItemIN, dict],
        enable_null_or_empty_values: bool,
    ) -> Result:
        """
        Updates a existing invoice item.


        :param invoice_item: InvoiceItemIN
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.updateInvoiceItem
        response_model = Result

        if type(invoice_item) != InvoiceItemIN:
            invoice_item = InvoiceItemIN(**invoice_item).dict()
        else:
            invoice_item = invoice_item.dict()

        arg = {
            "InvoiceItem": invoice_item,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_paid_by_currency_type(
        self, invoice_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the invoice amount
        in the specified (project or home) currency.
        Default currency is the project currency.


        :param invoice_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaidByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"invoiceID": invoice_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_tax_by_currency_type(
        self, invoice_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the summed up taxes in the specified (project or home) currency.
        Default currency is the project currency.


        :param invoice_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getTaxByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"invoiceID": invoice_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_tax_by_type_and_currency_type(
        self,
        invoice_id: int,
        currency_type: Union[CurrencyType, int],
        taxtypes: Union[TaxType, int],
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the specified TaxValue (project or home) currency.
        Possible


        :param invoice_id: int
        :param currency_type: CurrencyType
        :param taxtypes: TaxType
        :return: DoubleResult
        """

        proxy = (
            self.__client.plunet_server.DataOutgoingInvoice30.getTaxByTypeAndCurrencyType
        )
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        if type(taxtypes) == TaxType:
            taxtypes = taxtypes.value
        elif type(taxtypes) == int:
            taxtypes = taxtypes
        else:
            taxtypes = int(taxtypes)

        arg = {
            "invoiceID": invoice_id,
            "currencyType": currency_type,
            "taxtypes": taxtypes,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_payment_due_date(self, invoice_id: int) -> DateResult:
        """
        Retuns the date the invoice is payed.


        :param invoice_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaymentDueDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_net_by_currency_type(
        self, invoice_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the net amount in the specified (project or home) currency.
        Default currency is the project currency.
        NetAmount includes any discounts


        :param invoice_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getNetByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"invoiceID": invoice_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_gross_by_currency_type(
        self, invoice_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the invoice amount in the specified (project or home) currency.
        Default currency is the project currency.


        :param invoice_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getGrossByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"invoiceID": invoice_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_outstanding_by_currency_type(
        self, invoice_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the outstanding
        amount in the specified (project or home) currency.
        Default currency is the project currency.


        :param invoice_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = (
            self.__client.plunet_server.DataOutgoingInvoice30.getOutstandingByCurrencyType
        )
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"invoiceID": invoice_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_payment_due_date(self, invoice_id: int, due_date: datetime) -> Result:
        """
        Defines the date the invoice is payed.


        :param invoice_id: int
        :param due_date: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPaymentDueDate
        response_model = Result

        arg = {"invoiceID": invoice_id, "dueDate": due_date}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_is_invoice_exported(self, invoice_id: int) -> BooleanResult:
        """
        Returns if the invoice is already exported.


        :param invoice_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getIsInvoiceExported
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_tax_types(self, invoice_id: int) -> TaxListResult:
        """
        Returns a list of all tax types which are used within the transfered invoice.
        Possible currency codes can be configured over Admin|Settings|Comany Code


        :param invoice_id: int
        :return: TaxListResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceTaxTypes
        response_model = TaxListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_item_list(self, invoice_id: int) -> InvoiceItemResult:
        """
        Returns a list of all invoice items.


        :param invoice_id: int
        :return: InvoiceItemResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceItemList
        response_model = InvoiceItemResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def delete_invoice_item(self, invoice_item_id: int) -> Result:
        """
        Delets an existing invoice item.


        :param invoice_item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.deleteInvoiceItem
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_currency_code(self, invoice_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the currency code
        of the currently selected invoice (the amount is standard currency).


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCurrencyCode
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_id(self, display_name: str, company_code_id: int) -> IntegerResult:
        """
        Get the invoiceId based on the display number and company code of the invoice.


        :param display_name: str
        :param company_code_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceId
        response_model = IntegerResult

        arg = {"displayName": display_name, "companyCodeId": company_code_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_customer_id(self, customer_id: int, invoice_id: int) -> Result:
        """
        Sets the customer ID for the specified invoice.


        :param customer_id: int
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setCustomerID
        response_model = Result

        arg = {"customerID": customer_id, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_address_id(self, invoice_id: int, address_id: int) -> Result:
        """
        Sets the addressID which has to be related to the invoice related customer.
        Address information can be obtained over
        DataCustomerAddress30


        :param invoice_id: int
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setAddressID
        response_model = Result

        arg = {"invoiceID": invoice_id, "addressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_price_line_list(self, invoice_item_id: int) -> PriceLineListResult:
        """
        Returns a list of all job related PriceLine


        :param invoice_item_id: int
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceLine_List
        response_model = PriceLineListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_price_unit_list(
        self, language_code: str, service: str
    ) -> PriceUnitListResult:
        """
        Returns a list of priceUnit related to the specified service.
        Possible services can be obtained over DataAdmin30.getAvailableServices(String, String)


        :param language_code: str
        :param service: str
        :return: PriceUnitListResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceUnit_List
        response_model = PriceUnitListResult

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist_entry_list(
        self, pricelist_id: int, source_language: str, target_language: str
    ) -> PricelistEntryList:
        """
        Provides all price entries which are related to the Pricelist
        regarding the transfered source and target language.


        :param pricelist_id: int
        :param source_language: str
        :param target_language: str
        :return: PricelistEntryList
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelistEntry_List
        response_model = PricelistEntryList

        arg = {
            "PricelistID": pricelist_id,
            "SourceLanguage": source_language,
            "TargetLanguage": target_language,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist_list(self, invoice_item_id: int) -> PricelistListResult:
        """
        Returns all avaliable Pricelist for this invoice item.
        Note: This is dependent on the related project and the selected customer


        :param invoice_item_id: int
        :return: PricelistListResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelist_List
        response_model = PricelistListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_status(self, invoice_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the status.


        :param invoice_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, invoice_id: int) -> Result:
        """
        Sets the status.


        :param status: int
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setStatus
        response_model = Result

        arg = {"Status": status, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_brief_description(self, invoice_id: int) -> StringResult:
        """
        Returns the brief description.


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getBriefDescription
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_brief_description(self, description: str, invoice_id: int) -> Result:
        """
        Sets the brief description.


        :param description: str
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setBriefDescription
        response_model = Result

        arg = {"description": description, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_contact_person_id(self, invoice_id: int) -> IntegerResult:
        """
        Returns the id to the invoice realted contact person (customer).
        Contact Person details can be obtained over
        DataCustomerContact30


        :param invoice_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getContactPersonID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_contact_person_id(self, invoice_id: int, contact_person_id: int) -> Result:
        """
        Sets the customer depended contact person for the specified invoice.
        Contact Person details can be obtained over
        DataCustomerContact30


        :param invoice_id: int
        :param contact_person_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setContactPersonID
        response_model = Result

        arg = {"invoiceID": invoice_id, "contactPersonID": contact_person_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_price_line(
        self, invoice_item_id: int, price_line_in: Union[PriceLineIN, dict]
    ) -> PriceLineResult:
        """
        Updates a existing PriceLine.


        :param invoice_item_id: int
        :param price_line_in: PriceLineIN
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.updatePriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        arg = {"invoiceItemID": invoice_item_id, "priceLineIN": price_line_in}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_pricelist(self, invoice_item_id: int) -> PricelistResult:
        """
        Returns the current selected Pricelist for the specified invoice item.


        :param invoice_item_id: int
        :return: PricelistResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelist
        response_model = PricelistResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_pricelist(self, invoice_item_id: int, price_list_id: int) -> Result:
        """
        SetÂ´s the selected Pricelist for the specified invoice item.


        :param invoice_item_id: int
        :param price_list_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPricelist
        response_model = Result

        arg = {"InvoiceItemID": invoice_item_id, "priceListID": price_list_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_services_list(self, language_code: str) -> StringArrayResult:
        """
        Deprecated. Please use DataAdmin30.getAvailableServices(String, String) instead.
        Returns a list of all available services.


        :param language_code: str
        :return: StringArrayResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getServices_List
        response_model = StringArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=language_code,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_price_unit(self, price_unit_id: int, language_code: str) -> PriceUnitResult:
        """
        Returns a PriceUnitResult object.
        Possible PriceUnitÂ´s can be obtained over DataItem30.getPriceUnit_List(java.lang.String, java.lang.String, java.lang.String)


        :param price_unit_id: int
        :param language_code: str
        :return: PriceUnitResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceUnit
        response_model = PriceUnitResult

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def insert_price_line(
        self,
        invoice_item_id: int,
        price_line_in: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ) -> PriceLineResult:
        """
        Inserts a new PriceLine to the specified invoice item


        :param invoice_item_id: int
        :param price_line_in: PriceLineIN
        :param create_as_first_item: bool
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.insertPriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        arg = {
            "invoiceItemID": invoice_item_id,
            "priceLineIN": price_line_in,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_price_line(self, invoice_item_id: int, price_line_id: int) -> Result:
        """
        Deletes an existing PriceLine


        :param invoice_item_id: int
        :param price_line_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.deletePriceLine
        response_model = Result

        arg = {"invoiceItemID": invoice_item_id, "priceLineID": price_line_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_po_number(self, invoice_id: int, po_number: str) -> Result:
        """
        Defines if the invoice is already exported.


        :param invoice_id: int
        :param po_number: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPONumber
        response_model = Result

        arg = {"invoiceID": invoice_id, "poNumber": po_number}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_outstanding(self, invoice_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the outstanding
        amount (in project currency).


        :param invoice_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getOutstanding
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_gross(self, invoice_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the invoice amount (in project currency).


        :param invoice_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getGross
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_order_i_ds(self, invoice_id: int) -> IntegerArrayResult:
        """
        Returns an instances of IntegerArrayResult, which contains the order
        IDs.


        :param invoice_id: int
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getOrderIDs
        response_model = IntegerArrayResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_net(self, invoice_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the net amount (in project currency).
        NetAmount includes any discounts


        :param invoice_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getNet
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_paid(self, invoice_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the invoice amount
        (in project currency).


        :param invoice_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaid
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_value_date(self, invoice_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the value date.


        :param invoice_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getValueDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_date(self, invoice_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the invoice
        date.


        :param invoice_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_nr(self, invoice_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the invoice
        number.


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceNr
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_invoice_date(self, invoice_date: datetime, invoice_id: int) -> Result:
        """
        Sets the invoice date.


        :param invoice_date: datetime
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setInvoiceDate
        response_model = Result

        arg = {"invoiceDate": invoice_date, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_tax(self, invoice_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains all taxes as summed up values (in project currency).


        :param invoice_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getTax
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_object(self, invoice_id: int) -> InvoiceResult:
        """
        Method returns an instance of InvoiceResult, which contains an
        instance of Invoice.


        :param invoice_id: int
        :return: InvoiceResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceObject
        response_model = InvoiceResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_value_date(self, value_date: datetime, invoice_id: int) -> Result:
        """
        Sets the value date of the currently selected invoice.


        :param value_date: datetime
        :param invoice_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setValueDate
        response_model = Result

        arg = {"valueDate": value_date, "invoiceID": invoice_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_customer_id(self, invoice_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the customer
        ID.


        :param invoice_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_adress_id(self, invoice_id: int) -> IntegerResult:
        """
        Return the ID of the customer address entry this invoice is mapped to.
        Address information can be obtained over
        DataCustomerAddress30


        :param invoice_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getAdressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_paid_date(self, invoice_id: int) -> DateResult:
        """
        Retuns the date the invoice is payed.


        :param invoice_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaidDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_po_number(self, invoice_id: int) -> StringResult:
        """
        Returns if the PO-number


        :param invoice_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPONumber
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_paid_date(self, invoice_id: int, paid_date: datetime) -> Result:
        """
        Defines the date the invoice is payed.


        :param invoice_id: int
        :param paid_date: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPaidDate
        response_model = Result

        arg = {"invoiceID": invoice_id, "paidDate": paid_date}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_company_code(self, invoice_id: int) -> IntegerResult:
        """
        Returns the type dependent company code, related to the specified
        invoice.


        :param invoice_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCompanyCode
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=invoice_id,
            response_model=response_model,
            unpack_dict=False,
        )
