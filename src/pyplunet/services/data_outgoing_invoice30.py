from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CurrencyType, TaxType
from ..models import InvoiceItemIN, PriceLineIN, SearchFilter_Invoice

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataOutgoingInvoice30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def create_invoice_document(self, template: str, format_id: int, invoice_id: int):
        """
        Method creates an invoice document as rtf-file and returns the uncpath where the file is located.

        :param template: str
        :param format_id: int
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.createInvoiceDocument

        arg = {"template": template, "formatId": format_id, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def delete(self, invoice_id: int):
        """
        Deletes a invoice identified by invoice ID.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.delete

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def delete_invoice_item(self, invoice_item_id: int):
        """
        Delets an existing invoice item.

        :param invoice_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.deleteInvoiceItem

        return self.__client.make_request(proxy, invoice_item_id, unpack_dict=False)

    def delete_price_line(self, invoice_item_id: int, price_line: int):
        """
        Deletes an existing PriceLine

        :param invoice_item_id: int
        :param price_line: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.deletePriceLine

        arg = {"invoiceItemID": invoice_item_id, "priceLine": price_line}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_adress_id(self, invoice_id: int):
        """
        Return the ID of the customer address entry this invoice is mapped to.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getAdressID

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_brief_description(self, invoice_id: int):
        """
        Returns the brief description.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getBriefDescription

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_company_code(self, invoice_id: int):
        """
        Returns the type dependent company code, related to the specifiedinvoice.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCompanyCode

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_contact_person_id(self, invoice_id: int):
        """
        Returns the id to the invoice realted contact person (customer).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getContactPersonID

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_currency_code(self, invoice_id: int):
        """
        Returns an instance of StringResult, which contains the currency codeof the currently selected invoice (the amount is standard currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCurrencyCode

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_customer_id(self, invoice_id: int):
        """
        Returns an instance of IntegerResult, which contains the customerID.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getCustomerID

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_gross(self, invoice_id: int):
        """
        Returns an instance of DoubleResult, which contains the invoice amount (in project currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getGross

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_gross_by_currency_type(self, invoice_id: int, currency_type: CurrencyType):
        """
        Returns an instance of DoubleResult, which contains the invoice amount in the specified (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getGrossByCurrencyType

        arg = {"invoiceID": invoice_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_invoice_date(self, invoice_id: int):
        """
        Returns an instance of DateResult, which contains the invoicedate.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceDate

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_invoice_documents(self, invoice_id: int):
        """
        Returns an instance of StringArrayResult, which contains an array ofrelative network paths for all available invoice documents.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceDocuments

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_invoice_id(self, display_name: str, company_code_id: int):
        """
        Get the invoiceId based on the display number and company code of the invoice.

        :param display_name: str
        :param company_code_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceId

        arg = {"displayName": display_name, "companyCodeId": company_code_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_invoice_item_list(self, invoice_id: int):
        """
        Returns a list of all invoice items.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceItemList

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_invoice_nr(self, invoice_id: int):
        """
        Returns an instance of StringResult, which contains the invoicenumber.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceNr

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_invoice_object(self, invoice_id: int):
        """
        Method returns an instance of InvoiceResult, which contains aninstance of Invoice.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceObject

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_invoice_tax_types(self, invoice_id: int):
        """
        Returns a list of all tax types which are used within the transfered invoice.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceTaxTypes

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_is_invoice_exported(self, invoice_id: int):
        """
        Returns if the invoice is already exported.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getIsInvoiceExported

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_net(self, invoice_id: int):
        """
        Returns an instance of DoubleResult, which contains the net amount (in project currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getNet

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_net_by_currency_type(self, invoice_id: int, currency_type: CurrencyType):
        """
        Returns an instance of DoubleResult, which contains the net amount in the specified (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getNetByCurrencyType

        arg = {"invoiceID": invoice_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_order_i_ds(self, invoice_id: int):
        """
        Returns an instances of IntegerArrayResult, which contains the orderIDs.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getOrderIDs

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_outstanding(self, invoice_id: int):
        """
        Returns an instance of DoubleResult, which contains the outstandingamount (in project currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getOutstanding

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_outstanding_by_currency_type(
        self, invoice_id: int, currency_type: CurrencyType
    ):
        """
        Returns an instance of DoubleResult, which contains the outstandingamount in the specified (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataOutgoingInvoice30.getOutstandingByCurrencyType
        )

        arg = {"invoiceID": invoice_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_paid(self, invoice_id: int):
        """
        Returns an instance of DoubleResult, which contains the invoice amount(in project currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaid

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_paid_by_currency_type(self, invoice_id: int, currency_type: CurrencyType):
        """
        Returns an instance of DoubleResult, which contains the invoice amountin the specified (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaidByCurrencyType

        arg = {"invoiceID": invoice_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_paid_date(self, invoice_id: int):
        """
        Retuns the date the invoice is payed.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaidDate

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_payment_due_date(self, invoice_id: int):
        """
        Retuns the date the invoice is payed.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPaymentDueDate

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_po_number(self, invoice_id: int):
        """
        Returns if the PO-number

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPONumber

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_price_line_list(self, invoice_item_id: int):
        """
        Returns a list of all job related PriceLine

        :param invoice_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceLine_List

        return self.__client.make_request(proxy, invoice_item_id, unpack_dict=False)

    def get_pricelist_list(self, invoice_item_id: int):
        """
        Returns all avaliable Pricelist for this invoice item.

        :param invoice_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelist_List

        return self.__client.make_request(proxy, invoice_item_id, unpack_dict=False)

    def get_pricelist(self, invoice_item_id: int):
        """
        Returns the current selected Pricelist for the specified invoice item.

        :param invoice_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelist

        return self.__client.make_request(proxy, invoice_item_id, unpack_dict=False)

    def get_pricelist_entry_list(
        self, pricelist_id: int, source_language: str, target_language: str
    ):
        """
        Provides all price entries which are related to the Pricelistregarding the transfered source and target language.

        :param pricelist_id: int
        :param source_language: str
        :param target_language: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPricelistEntry_List

        arg = {
            "pricelistID": pricelist_id,
            "sourceLanguage": source_language,
            "targetLanguage": target_language,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit_list(self, language_code: str, service: str):
        """
        Returns a list of priceUnit related to the specified service.

        :param language_code: str
        :param service: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceUnit_List

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit(self, price_unit_id: int, language_code: str):
        """
        Returns a PriceUnitResult object.

        :param price_unit_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getPriceUnit

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_receivable_account(self, invoice_id: int):
        """
        Returns the receivable account.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getReceivableAccount

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_revenue_account(self, invoice_id: int):
        """
        Returns the revenue account.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getRevenueAccount

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_services_list(self, language_code: str):
        """
        Deprecated.Please use DataAdmin30.getAvailableServices(String, String) instead.Returns a list of all available services.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getServices_List

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_status(self, invoice_id: int):
        """
        Returns an instance of IntegerResult, which contains the status.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getStatus

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_subject(self, invoice_id: int):
        """
        Returns an instance of StringResult, which contains the subject.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getSubject

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_tax(self, invoice_id: int):
        """
        Returns an instance of DoubleResult, which contains all taxes as summed up values (in project currency).

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getTax

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def get_tax_by_currency_type(self, invoice_id: int, currency_type: CurrencyType):
        """
        Returns an instance of DoubleResult, which contains the summed up taxes in the specified (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getTaxByCurrencyType

        arg = {"invoiceID": invoice_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_tax_by_type_and_currency_type(
        self, invoice_id: int, currency_type: CurrencyType, tax_type: TaxType
    ):
        """
        Returns an instance of DoubleResult, which contains the specified TaxValue (project or home) currency.

        :param invoice_id: int
        :param currency_type: CurrencyType
        :param tax_type: TaxType

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataOutgoingInvoice30.getTaxByTypeAndCurrencyType
        )

        arg = {
            "invoiceID": invoice_id,
            "currencyType": currency_type.value,
            "taxType": tax_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_value_date(self, invoice_id: int):
        """
        Returns an instance of DateResult, which contains the value date.

        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.getValueDate

        return self.__client.make_request(proxy, invoice_id, unpack_dict=False)

    def insert_invoice_item(self, inv_item: Union[InvoiceItemIN, dict]):
        """
        Creates a new invoice item.

        :param inv_item: InvoiceItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.insertInvoiceItem

        if type(inv_item) != InvoiceItemIN:
            inv_item = InvoiceItemIN(**inv_item).dict()
        else:
            inv_item = inv_item.dict()

        return self.__client.make_request(proxy, inv_item, unpack_dict=False)

    def insert_price_line(
        self,
        invoice_item_id: int,
        price_line: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ):
        """
        Inserts a new PriceLine to the specified invoice item

        :param invoice_item_id: int
        :param price_line: PriceLineIN
        :param create_as_first_item: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.insertPriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "invoiceItemID": invoice_item_id,
            "priceLine": price_line,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Invoice, dict]):
        """


        :param search_filter: SearchFilter_Invoice

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.search

        if type(search_filter) != SearchFilter_Invoice:
            search_filter = SearchFilter_Invoice(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_address_id(self, invoice_id: int, address_id: int):
        """
        Sets the addressID which has to be related to the invoice related customer.

        :param invoice_id: int
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setAddressID

        arg = {"invoiceID": invoice_id, "addressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_brief_description(self, description: str, invoice_id: int):
        """
        Sets the brief description.

        :param description: str
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setBriefDescription

        arg = {"description": description, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_contact_person_id(self, invoice_id: int, contact_person_id: int):
        """
        Sets the customer depended contact person for the specified invoice.

        :param invoice_id: int
        :param contact_person_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setContactPersonID

        arg = {"invoiceID": invoice_id, "contactPersonID": contact_person_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, invoice_id: int):
        """
        Sets the customer ID for the specified invoice.

        :param customer_id: int
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setCustomerID

        arg = {"customerID": customer_id, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_invoice_date(self, invoice_date: datetime, invoice_id: int):
        """
        Sets the invoice date.

        :param invoice_date: datetime
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setInvoiceDate

        arg = {"invoiceDate": invoice_date, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_is_invoice_exported(self, invoice_id: int, is_exported: bool):
        """
        Defines if the invoice is already exported.

        :param invoice_id: int
        :param is_exported: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setIsInvoiceExported

        arg = {"invoiceID": invoice_id, "isExported": is_exported}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_paid_date(self, invoice_id: int, pai_date: datetime):
        """
        Defines the date the invoice is payed.

        :param invoice_id: int
        :param pai_date: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPaidDate

        arg = {"invoiceID": invoice_id, "paiDate": pai_date}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_payment_due_date(self, invoice_id: int, due_date: datetime):
        """
        Defines the date the invoice is payed.

        :param invoice_id: int
        :param due_date: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPaymentDueDate

        arg = {"invoiceID": invoice_id, "dueDate": due_date}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_po_number(self, invoice_id: int, po_number: str):
        """
        Defines if the invoice is already exported.

        :param invoice_id: int
        :param po_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPONumber

        arg = {"invoiceID": invoice_id, "poNumber": po_number}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_pricelist(self, invoice_item_id: int, price_list_id: int):
        """
        Set´s the selected Pricelist for the specified invoice item.

        :param invoice_item_id: int
        :param price_list_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setPricelist

        arg = {"InvoiceItemID": invoice_item_id, "priceListID": price_list_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_receivable_account(self, account_id: int, invoice_id: int):
        """
        Sets the receivable account.

        :param account_id: int
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setReceivableAccount

        arg = {"accountID": account_id, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_revenue_account(self, account_id: int, invoice_id: int):
        """
        Sets the revenue account.

        :param account_id: int
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setRevenueAccount

        arg = {"accountID": account_id, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, invoice_id: int):
        """
        Sets the status.

        :param status: int
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setStatus

        arg = {"Status": status, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_subject(self, subject: str, invoice_id: int):
        """
        Sets the subject.

        :param subject: str
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setSubject

        arg = {"subject": subject, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_value_date(self, value_date: datetime, invoice_id: int):
        """
        Sets the value date of the currently selected invoice.

        :param value_date: datetime
        :param invoice_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.setValueDate

        arg = {"valueDate": value_date, "invoiceID": invoice_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_invoice_item(self, inv_item: Union[InvoiceItemIN, dict], enabled: bool):
        """
        Updates a existing invoice item.

        :param inv_item: InvoiceItemIN
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.updateInvoiceItem

        if type(inv_item) != InvoiceItemIN:
            inv_item = InvoiceItemIN(**inv_item).dict()
        else:
            inv_item = inv_item.dict()

        arg = {"invItem": inv_item, "enabled": enabled}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_price_line(
        self, invoice_item_id: int, price_line: Union[PriceLineIN, dict]
    ):
        """
        Updates a existing PriceLine.

        :param invoice_item_id: int
        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataOutgoingInvoice30.updatePriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {"invoiceItemID": invoice_item_id, "priceLine": price_line}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
