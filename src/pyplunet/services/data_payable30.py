from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import TaxType
from ..models import (
    BooleanResult,
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerResult,
    PayableItemIN,
    PayableItemResultList,
    PriceLineIN,
    PriceLineListResult,
    PriceLineResult,
    PriceUnitListResult,
    PriceUnitResult,
    Result,
    SearchFilter_Payable,
    StringArrayResult,
    StringResult,
    TaxListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataPayable30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def search(
        self, search_filter: Union[SearchFilter_Payable, dict]
    ) -> IntegerArrayResult:
        """
        No description of search in docs.


        :param search_filter: SearchFilter_Payable
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataPayable30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_Payable:
            search_filter = SearchFilter_Payable(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_due_date(self, payables_id: int) -> DateResult:
        """
        Retuns the date the invoice is payed.


        :param payables_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentDueDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_payment_due_date(self, payables_id: int, due_date: datetime) -> Result:
        """
        Defines the date the invoice is payed.


        :param payables_id: int
        :param due_date: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setPaymentDueDate
        response_model = Result

        arg = {"payablesID": payables_id, "dueDate": due_date}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_invoice_tax_types(self, payables_id: int) -> TaxListResult:
        """
        Returns a list of all tax types which are used within the transfered invoice..
        Possible currency codes can be configured over Admin|Settings|Comany Code


        :param payables_id: int
        :return: TaxListResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getInvoiceTaxTypes
        response_model = TaxListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_creditor_account(self, payables_id: int) -> StringResult:
        """
        Returns the creditor account.


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getCreditorAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_external_invoice_number(self, payables_id: int) -> StringResult:
        """
        Returns the revenue account.


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getExternalInvoiceNumber
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_creditor_account(self, account_id: str, payables_id: int) -> Result:
        """
        Defines the creditor account.


        :param account_id: str
        :param payables_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setCreditorAccount
        response_model = Result

        arg = {"accountID": account_id, "payablesID": payables_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_account_statement(self, payables_id: int, accountstatement: str) -> Result:
        """
        Defines the po number of the related credit note.


        :param payables_id: int
        :param accountstatement: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setAccountStatement
        response_model = Result

        arg = {"payablesID": payables_id, "accountstatement": accountstatement}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_total_tax_amount(
        self, payables_id: int, currency_tpe: int, tax_type: Union[TaxType, int]
    ) -> DoubleResult:
        """
        Returns the total tax price of the payment.


        :param payables_id: int
        :param currency_tpe: int
        :param tax_type: TaxType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getTotalTaxAmount
        response_model = DoubleResult

        if type(tax_type) == TaxType:
            tax_type = tax_type.value
        elif type(tax_type) == int:
            tax_type = tax_type
        else:
            tax_type = int(tax_type)

        arg = {
            "payablesID": payables_id,
            "currencyTpe": currency_tpe,
            "taxType": tax_type,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_total_net_amount(self, payables_id: int, currency_tpe: int) -> DoubleResult:
        """
        Returns the total net price of the payment,


        :param payables_id: int
        :param currency_tpe: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getTotalNetAmount
        response_model = DoubleResult

        arg = {"payablesID": payables_id, "currencyTpe": currency_tpe}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_payment_item(
        self,
        payment_item_in: Union[PayableItemIN, dict],
        payment_item_id: int,
        enable_null_or_empty_values: bool,
    ) -> Result:
        """
        Updates an existung payment item


        :param payment_item_in: PayableItemIN
        :param payment_item_id: int
        :param enable_null_or_empty_values: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.updatePaymentItem
        response_model = Result

        if type(payment_item_in) != PayableItemIN:
            payment_item_in = PayableItemIN(**payment_item_in).dict()
        else:
            payment_item_in = payment_item_in.dict()

        arg = {
            "PaymentItemIN": payment_item_in,
            "PaymentItemID": payment_item_id,
            "enableNullOrEmptyValues": enable_null_or_empty_values,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_payment_item(self, payment_item_id: int) -> Result:
        """
        Deletes an payment Item


        :param payment_item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.deletePaymentItem
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payment_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_expense_account(self, payables_id: int) -> StringResult:
        """
        Returns the expense account.


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getExpenseAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_item_list(self, payables_id: int) -> PayableItemResultList:
        """
        Retuns a list of all paymentent relevant items


        :param payables_id: int
        :return: PayableItemResultList
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentItemList
        response_model = PayableItemResultList

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_account_statement(self, payables_id: int) -> StringResult:
        """
        Returns the account statement.


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getAccountStatement
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert_payment_item(
        self, payment_item_in: Union[PayableItemIN, dict]
    ) -> IntegerResult:
        """
        Inserts a new payment item


        :param payment_item_in: PayableItemIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.insertPaymentItem
        response_model = IntegerResult

        if type(payment_item_in) != PayableItemIN:
            payment_item_in = PayableItemIN(**payment_item_in).dict()
        else:
            payment_item_in = payment_item_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payment_item_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_creator_resource_id(self, payables_id: int) -> IntegerResult:
        """
        Returns the resourceID of the for the creation responsible resource.


        :param payables_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentCreatorResourceID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_external_invoice_number(
        self, payables_id: int, external_number: str
    ) -> Result:
        """
        Defines the revenue account.


        :param payables_id: int
        :param external_number: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setExternalInvoiceNumber
        response_model = Result

        arg = {"payablesID": payables_id, "externalNumber": external_number}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_currency(self, payables_id: int) -> StringResult:
        """
        Returns the currency of the payable.


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getCurrency
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_payment_method(self, payables_id: int) -> IntegerResult:
        """
        Returns the payment method, represented by its FA value.

        See Admin | Miscellaneous | Payment method | FA value.


        :param payables_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaymentMethod
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_price_line_list(self, payables_item_id: int) -> PriceLineListResult:
        """
        Returns a list of all job related PriceLine


        :param payables_item_id: int
        :return: PriceLineListResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPriceLine_List
        response_model = PriceLineListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_item_id,
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

        proxy = self.__client.plunet_server.DataPayable30.getPriceUnit_List
        response_model = PriceUnitListResult

        arg = {"languageCode": language_code, "service": service}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(self, payables_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        PayableStatus.


        :param payables_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, payables_id: int) -> Result:
        """
        Defines the PayableStatus.


        :param status: int
        :param payables_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setStatus
        response_model = Result

        arg = {"Status": status, "payablesID": payables_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_price_line(
        self, payables_item_id: int, price_line_in: Union[PriceLineIN, dict]
    ) -> PriceLineResult:
        """
        Updates a existing PriceLine.


        :param payables_item_id: int
        :param price_line_in: PriceLineIN
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataPayable30.updatePriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        arg = {"payablesItemID": payables_item_id, "priceLineIN": price_line_in}

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

        proxy = self.__client.plunet_server.DataPayable30.getServices_List
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
        Possible PriceUnitÂ´s can be obtained over DataItem30.getPriceUnit_List(String, String, String)


        :param price_unit_id: int
        :param language_code: str
        :return: PriceUnitResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPriceUnit
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
        payables_item_id: int,
        price_line_in: Union[PriceLineIN, dict],
        create_as_first_item: bool,
    ) -> PriceLineResult:
        """
        Inserts a new PriceLine to the specified invoice item


        :param payables_item_id: int
        :param price_line_in: PriceLineIN
        :param create_as_first_item: bool
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataPayable30.insertPriceLine
        response_model = PriceLineResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        arg = {
            "payablesItemID": payables_item_id,
            "priceLineIN": price_line_in,
            "createAsFirstItem": create_as_first_item,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_price_line(self, payables_item_id: int, price_line_id: int) -> Result:
        """
        Deletes an existing PriceLine


        :param payables_item_id: int
        :param price_line_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.deletePriceLine
        response_model = Result

        arg = {"payablesItemID": payables_item_id, "priceLineID": price_line_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_payable_id(self, item_id: int) -> IntegerResult:
        """
        Returns the payable ID the item is related to.


        :param item_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPayableID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_value_date(self, payables_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the value date.


        :param payables_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getValueDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_date(self, payables_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the invoice
        date.


        :param payables_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getInvoiceDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_invoice_date(self, invoice_date: datetime, payables_id: int) -> Result:
        """
        Defines the invoice date.


        :param invoice_date: datetime
        :param payables_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setInvoiceDate
        response_model = Result

        arg = {"invoiceDate": invoice_date, "payablesID": payables_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_value_date(self, value_date: datetime, payables_id: int) -> Result:
        """
        Defines the value date of the currently selected invoice.


        :param value_date: datetime
        :param payables_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setValueDate
        response_model = Result

        arg = {"valueDate": value_date, "payablesID": payables_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_resource_id(self, payables_id: int) -> IntegerResult:
        """
        Returns the resourceID the payment is related to.


        :param payables_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getResourceID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_is_exported(self, payables_id: int) -> BooleanResult:
        """
        Returns if the invoice is already exported.


        :param payables_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getIsExported
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_is_exported(self, payables_id: int, is_exported: bool) -> Result:
        """
        Defines if the invoice is already exported.


        :param payables_id: int
        :param is_exported: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setIsExported
        response_model = Result

        arg = {"payablesID": payables_id, "isExported": is_exported}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_memo(self, payables_id: int) -> StringResult:
        """
        Returns the memo field value


        :param payables_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getMemo
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_paid_date(self, payables_id: int) -> DateResult:
        """
        Retuns the date the invoice is payed.


        :param payables_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getPaidDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_memo(self, payables_id: int, memo: str) -> Result:
        """
        Defines the memo field value


        :param payables_id: int
        :param memo: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setMemo
        response_model = Result

        arg = {"payablesID": payables_id, "memo": memo}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_paid_date(self, payables_id: int, paid_date: datetime) -> Result:
        """
        Defines the date the invoice is payed.


        :param payables_id: int
        :param paid_date: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataPayable30.setPaidDate
        response_model = Result

        arg = {"payablesID": payables_id, "paidDate": paid_date}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_company_code(self, payables_id: int) -> IntegerResult:
        """
        Returns the type dependent company code, related to the specified
        invoice.


        :param payables_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataPayable30.getCompanyCode
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=payables_id,
            response_model=response_model,
            unpack_dict=False,
        )
