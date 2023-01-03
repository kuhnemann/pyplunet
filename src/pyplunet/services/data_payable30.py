from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CurrencyType
from ..models import PayableItemIN, PriceLineIN, SearchFilter_Payable

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataPayable30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete_payment_item(self, payment_item_id: int):
        """
        Deletes an payment Item

        :param payment_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.deletePaymentItem

        return self.__client.make_request(proxy, payment_item_id, unpack_dict=False)

    def delete_price_line(self, payables_item_id: int, price_line: int):
        """
        Deletes an existing PriceLine

        :param payables_item_id: int
        :param price_line: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.deletePriceLine

        arg = {"payablesItemID": payables_item_id, "priceLine": price_line}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_account_statement(self, payables_id: int):
        """
        Returns the account statement.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getAccountStatement

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_company_code(self, payables_id: int):
        """
        Returns the type dependent company code, related to the specifiedinvoice.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getCompanyCode

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_creditor_account(self, payables_id: int):
        """
        Returns the creditor account.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getCreditorAccount

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_currency(self, payables_id: int):
        """
        Returns the currency of the payable.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getCurrency

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_expense_account(self, payables_id: int):
        """
        Returns the expense account.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getExpenseAccount

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_external_invoice_number(self, payables_id: int):
        """
        Returns the revenue account.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getExternalInvoiceNumber

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_invoice_date(self, payables_id: int):
        """
        Returns an instance of DateResult, which contains the invoicedate.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getInvoiceDate

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_invoice_tax_types(self, payables_id: int):
        """
        Returns a list of all tax types which are used within the transfered invoice.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getInvoiceTaxTypes

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_is_exported(self, payables_id: int):
        """
        Returns if the invoice is already exported.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getIsExported

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_memo(self, payables_id: int):
        """
        Returns the memo field value

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getMemo

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_paid_date(self, payables_id: int):
        """
        Retuns the date the invoice is payed.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaidDate

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_payable_id(self, item_id: int):
        """
        Returns the payable ID the item is related to.

        :param item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPayableID

        return self.__client.make_request(proxy, item_id, unpack_dict=False)

    def get_payment_creator_resource_id(self, payables_id: int):
        """
        Returns the resourceID of the for the creation responsible resource.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentCreatorResourceID

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_payment_due_date(self, payables_id: int):
        """
        Retuns the date the invoice is payed.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentDueDate

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_payment_item_list(self, payables_id: int):
        """
        Retuns a list of all paymentent relevant items

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentItemList

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_payment_method(self, payables_id: int):
        """
        Returns the payment method, represented by its FA value.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentMethod

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_price_line_list(self, payables_item_id: int):
        """
        Returns a list of all job related PriceLine

        :param payables_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPriceLine_List

        return self.__client.make_request(proxy, payables_item_id, unpack_dict=False)

    def get_price_unit_list(self, language_code: str, service: str):
        """
        Returns a list of priceUnit related to the specified service.

        :param language_code: str
        :param service: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPriceUnit_List

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_price_unit(self, price_unit_id: int, language_code: str):
        """
        Returns a PriceUnitResult object.

        :param price_unit_id: int
        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getPriceUnit

        arg = {"PriceUnitID": price_unit_id, "languageCode": language_code}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_resource_id(self, payables_id: int):
        """
        Returns the resourceID the payment is related to.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getResourceID

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_services_list(self, language_code: str):
        """
        Deprecated.Please use DataAdmin30.getAvailableServices(String, String) instead.Returns a list of all available services.

        :param language_code: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getServices_List

        return self.__client.make_request(proxy, language_code, unpack_dict=False)

    def get_status(self, payables_id: int):
        """
        Returns an instance of IntegerResult, which contains thePayableStatus.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getStatus

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def get_total_net_amount(self, payables_id: int, currency_type: CurrencyType):
        """
        Returns the total net price of the payment,

        :param payables_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getTotalNetAmount

        arg = {"payablesID": payables_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_total_tax_amount(
        self, payables_id: int, currency_type: CurrencyType, tax_id: int
    ):
        """
        Returns the total tax price of the payment.

        :param payables_id: int
        :param currency_type: CurrencyType
        :param tax_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getTotalTaxAmount

        arg = {
            "payablesID": payables_id,
            "currencyType": currency_type.value,
            "taxID": tax_id,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_value_date(self, payables_id: int):
        """
        Returns an instance of DateResult, which contains the value date.

        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.getValueDate

        return self.__client.make_request(proxy, payables_id, unpack_dict=False)

    def insert_payment_item(self, payment_item: Union[PayableItemIN, dict]):
        """
        Inserts a new payment item

        :param payment_item: PayableItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.insertPaymentItem

        if type(payment_item) != PayableItemIN:
            payment_item = PayableItemIN(**payment_item).dict()
        else:
            payment_item = payment_item.dict()

        return self.__client.make_request(proxy, payment_item, unpack_dict=False)

    def insert_price_line(
        self,
        payables_item_id: int,
        price_line: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ):
        """
        Inserts a new PriceLine to the specified invoice item

        :param payables_item_id: int
        :param price_line: PriceLineIN
        :param create_as_first_item: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.insertPriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {
            "payablesItemID": payables_item_id,
            "priceLine": price_line,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_Payable, dict]):
        """


        :param search_filter: SearchFilter_Payable

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.search

        if type(search_filter) != SearchFilter_Payable:
            search_filter = SearchFilter_Payable(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_account_statement(self, payables_id: int, accountstatement: str):
        """
        Defines the po number of the related credit note.

        :param payables_id: int
        :param accountstatement: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setAccountStatement

        arg = {"payablesID": payables_id, "accountstatement": accountstatement}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_creditor_account(self, account_id: str, payables_id: int):
        """
        Defines the creditor account.

        :param account_id: str
        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setCreditorAccount

        arg = {"accountID": account_id, "payablesID": payables_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_external_invoice_number(self, payables_id: int, external_number: str):
        """
        Defines the revenue account.

        :param payables_id: int
        :param external_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setExternalInvoiceNumber

        arg = {"payablesID": payables_id, "externalNumber": external_number}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_invoice_date(self, invoice_date: datetime, payables_id: int):
        """
        Defines the invoice date.

        :param invoice_date: datetime
        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setInvoiceDate

        arg = {"invoiceDate": invoice_date, "payablesID": payables_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_is_exported(self, payables_id: int, is_exported: bool):
        """
        Defines if the invoice is already exported.

        :param payables_id: int
        :param is_exported: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setIsExported

        arg = {"payablesID": payables_id, "isExported": is_exported}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_memo(self, payables_id: int, memo: str):
        """
        Defines the memo field value

        :param payables_id: int
        :param memo: str

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setMemo

        arg = {"payablesID": payables_id, "memo": memo}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_paid_date(self, payables_id: int, pai_date: datetime):
        """
        Defines the date the invoice is payed.

        :param payables_id: int
        :param pai_date: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setPaidDate

        arg = {"payablesID": payables_id, "paiDate": pai_date}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_payment_due_date(self, payables_id: int, due_date: datetime):
        """
        Defines the date the invoice is payed.

        :param payables_id: int
        :param due_date: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setPaymentDueDate

        arg = {"payablesID": payables_id, "dueDate": due_date}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, payables_id: int):
        """
        Defines the PayableStatus.

        :param status: int
        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setStatus

        arg = {"Status": status, "payablesID": payables_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_value_date(self, value_date: datetime, payables_id: int):
        """
        Defines the value date of the currently selected invoice.

        :param value_date: datetime
        :param payables_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.setValueDate

        arg = {"valueDate": value_date, "payablesID": payables_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_payment_item(
        self,
        payment_item: Union[PayableItemIN, dict],
        payment_item_id: int,
        enabled: bool,
    ):
        """
        Updates an existung payment item

        :param payment_item: PayableItemIN
        :param payment_item_id: int
        :param enabled: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.updatePaymentItem

        if type(payment_item) != PayableItemIN:
            payment_item = PayableItemIN(**payment_item).dict()
        else:
            payment_item = payment_item.dict()

        arg = {
            "paymentItem": payment_item,
            "paymentItemID": payment_item_id,
            "enabled": enabled,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_price_line(
        self, payables_item_id: int, price_line: Union[PriceLineIN, dict]
    ):
        """
        Updates a existing PriceLine.

        :param payables_item_id: int
        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataPayable30.updatePriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {"payablesItemID": payables_item_id, "priceLine": price_line}

        return self.__client.make_request(proxy, arg, unpack_dict=True)
