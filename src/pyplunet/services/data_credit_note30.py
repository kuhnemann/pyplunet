from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CurrencyType, TaxType
from ..models import (
    BooleanResult,
    CreditNoteItemIN,
    CreditNoteListResult,
    DateResult,
    DoubleResult,
    IntegerArrayResult,
    IntegerResult,
    PriceLineIN,
    PriceLineResult,
    Result,
    SearchFilter_CreditNote,
    StringResult,
    TaxListResult,
)

if TYPE_CHECKING:
    from ..client import PlunetClient
    from ..retrying_client import RetryingPlunetClient


class DataCreditNote30:
    def __init__(self, client: Union[PlunetClient, RetryingPlunetClient]):
        self.__client = client

    def get_subject(self, credit_note_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the subject.


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getSubject
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_subject(self, subject: str, credit_note_id: int) -> Result:
        """
        Defines the subject.


        :param subject: str
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setSubject
        response_model = Result

        arg = {"subject": subject, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def search(
        self, search_filter: Union[SearchFilter_CreditNote, dict]
    ) -> IntegerArrayResult:
        """
        Search implementation to filter for any existing credit note based on
        the search filter.


        :param search_filter: SearchFilter_CreditNote
        :return: IntegerArrayResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.search
        response_model = IntegerArrayResult

        if type(search_filter) != SearchFilter_CreditNote:
            search_filter = SearchFilter_CreditNote(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=search_filter,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_receivable_account(self, account_id: int, credit_note_id: int) -> Result:
        """
        Sets the receivable account.


        :param account_id: int
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setReceivableAccount
        response_model = Result

        arg = {"accountID": account_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_revenue_account(self, credit_note_id: int) -> StringResult:
        """
        Returns the revenue account.


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getRevenueAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_receivable_account(self, credit_note_id: int) -> StringResult:
        """
        Returns the receivable account.


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getReceivableAccount
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_revenue_account(self, account_id: int, credit_note_id: int) -> Result:
        """
        Sets the revenue account.


        :param account_id: int
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setRevenueAccount
        response_model = Result

        arg = {"accountID": account_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_tax_by_currency_type(
        self, credit_note_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the summed up taxes in the specified (project or home) currency.
        Default currency is the project currency.


        :param credit_note_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_tax_by_type_and_currency_type(
        self,
        credit_note_id: int,
        currency_type: Union[CurrencyType, int],
        taxtypes: Union[TaxType, int],
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the specified TaxValue (project or home) currency.
        Possible


        :param credit_note_id: int
        :param currency_type: CurrencyType
        :param taxtypes: TaxType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxByTypeAndCurrencyType
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
            "creditNoteID": credit_note_id,
            "currencyType": currency_type,
            "taxtypes": taxtypes,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_credit_note_item(self, credit_note_item_id: int) -> Result:
        """
        Deletes an credit note item.


        :param credit_note_item_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.deleteCreditNoteItem
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_item_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_credit_note_item_list(self, credit_note_id: int) -> CreditNoteListResult:
        """
        Retunrs a list of all credit note items.


        :param credit_note_id: int
        :return: CreditNoteListResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteItemList
        response_model = CreditNoteListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert_credit_note_item(
        self, credit_note_item_in: Union[CreditNoteItemIN, dict]
    ) -> IntegerResult:
        """
        Inserts a new credit note item.


        :param credit_note_item_in: CreditNoteItemIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.insertCreditNoteItem
        response_model = IntegerResult

        if type(credit_note_item_in) != CreditNoteItemIN:
            credit_note_item_in = CreditNoteItemIN(**credit_note_item_in).dict()
        else:
            credit_note_item_in = credit_note_item_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_item_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def update_credit_note_item(
        self,
        credit_note_item_id: int,
        credit_note_item_in: Union[CreditNoteItemIN, dict],
    ) -> Result:
        """
        Updates a existing credit note item.


        :param credit_note_item_id: int
        :param credit_note_item_in: CreditNoteItemIN
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.updateCreditNoteItem
        response_model = Result

        if type(credit_note_item_in) != CreditNoteItemIN:
            credit_note_item_in = CreditNoteItemIN(**credit_note_item_in).dict()
        else:
            credit_note_item_in = credit_note_item_in.dict()

        arg = {
            "creditNoteItemID": credit_note_item_id,
            "creditNoteItemIN": credit_note_item_in,
        }

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_net_by_currency_type(
        self, credit_note_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the net amount in the specified (project or home) currency.
        Default currency is the project currency.


        :param credit_note_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getNetByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_gross_by_currency_type(
        self, credit_note_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the credit note amount in the specified (project or home) currency.
        Default currency is the project currency.


        :param credit_note_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getGrossByCurrencyType
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_outstanding_by_currency_type(
        self, credit_note_id: int, currency_type: Union[CurrencyType, int]
    ) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the outstanding
        amount in the specified (project or home) currency.
        Default currency is the project currency.


        :param credit_note_id: int
        :param currency_type: CurrencyType
        :return: DoubleResult
        """

        proxy = (
            self.__client.plunet_server.DataCreditNote30.getOutstandingByCurrencyType
        )
        response_model = DoubleResult

        if type(currency_type) == CurrencyType:
            currency_type = currency_type.value
        elif type(currency_type) == int:
            currency_type = currency_type
        else:
            currency_type = int(currency_type)

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_currency_code(self, credit_note_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the currency code
        of the specified credit note (the amount is standard currency).


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCurrencyCode
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_customer_id(self, customer_id: int, credit_note_id: int) -> Result:
        """
        Sets the customer ID for the specified credit note.


        :param customer_id: int
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setCustomerID
        response_model = Result

        arg = {"customerID": customer_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def set_address_id(self, credit_note_id: int, address_id: int) -> Result:
        """
        Sets the addressID which has to be related to the credit note related customer.
        Address information can be obtained over
        DataCustomerAddress30


        :param credit_note_id: int
        :param address_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setAddressID
        response_model = Result

        arg = {"creditNoteID": credit_note_id, "addressID": address_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_status(self, credit_note_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        CreditNoteStatus.


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getStatus
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_status(self, status: int, credit_note_id: int) -> Result:
        """
        Defines the CreditNoteStatus.


        :param status: int
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setStatus
        response_model = Result

        arg = {"Status": status, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_brief_description(self, credit_note_id: int) -> StringResult:
        """
        Returns the brief description.


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getBriefDescription
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_brief_description(self, description: str, credit_note_id: int) -> Result:
        """
        Sets the brief description.


        :param description: str
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setBriefDescription
        response_model = Result

        arg = {"description": description, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_contact_person_id(self, credit_note_id: int) -> IntegerResult:
        """
        Returns the id to the credit note related contact person
        (resource).

        Contact Person details can be obtained over
        DataCustomerContact30


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getContactPersonID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_contact_person_id(
        self, credit_note_id: int, contact_person_id: int
    ) -> Result:
        """
        Sets the customer depended contact person for the specified credit note.
        Contact Person details can be obtained over
        DataCustomerContact30


        :param credit_note_id: int
        :param contact_person_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setContactPersonID
        response_model = Result

        arg = {"creditNoteID": credit_note_id, "contactPersonID": contact_person_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def update_price_line(self, price_line_in: Union[PriceLineIN, dict]) -> Result:
        """
        Updates a existing PriceLine.


        :param price_line_in: PriceLineIN
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.updatePriceLine
        response_model = Result

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=price_line_in,
            response_model=response_model,
            unpack_dict=False,
        )

    def insert_price_line(
        self, credit_note_item_id: int, price_line_in: Union[PriceLineIN, dict]
    ) -> IntegerResult:
        """
        Inserts a new PriceLineIN to the specified credit note
        item.


        :param credit_note_item_id: int
        :param price_line_in: PriceLineIN
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.insertPriceLine
        response_model = IntegerResult

        if type(price_line_in) != PriceLineIN:
            price_line_in = PriceLineIN(**price_line_in).dict()
        else:
            price_line_in = price_line_in.dict()

        arg = {"creditNoteItemID": credit_note_item_id, "priceLineIN": price_line_in}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def delete_price_line(self, price_line_id: int) -> Result:
        """
        Deletes an existing PriceLine.


        :param price_line_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.deletePriceLine
        response_model = Result

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=price_line_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_po_number(self, credit_note_id: int, po_number: str) -> Result:
        """
        Defines the po number of the related credit note.


        :param credit_note_id: int
        :param po_number: str
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setPONumber
        response_model = Result

        arg = {"creditNoteID": credit_note_id, "poNumber": po_number}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_outstanding(self, credit_note_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the outstanding
        amount (in project currency).


        :param credit_note_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getOutstanding
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_gross(self, credit_note_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the credit note amount (in project currency).


        :param credit_note_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getGross
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_net(self, credit_note_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains the net amount (in project currency).


        :param credit_note_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getNet
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_tax(self, credit_note_id: int) -> DoubleResult:
        """
        Returns an instance of DoubleResult, which contains all taxes as summed up values (in project currency).


        :param credit_note_id: int
        :return: DoubleResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTax
        response_model = DoubleResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_invoice_id(self, credit_note_id: int) -> IntegerResult:
        """
        Returns the credit note related invoice ID.


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getInvoiceID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_customer_id(self, credit_note_id: int) -> IntegerResult:
        """
        Returns an instance of IntegerResult, which contains the
        customer ID.


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCustomerID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_adress_id(self, credit_note_id: int) -> IntegerResult:
        """
        Return the ID of the customer address entry this credit note is mapped to.
        Address information can be obtained over
        DataCustomerAddress30


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getAdressID
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_is_exported(self, credit_note_id: int) -> BooleanResult:
        """
        Returns if the credit note is already exported.


        :param credit_note_id: int
        :return: BooleanResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getIsExported
        response_model = BooleanResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_is_exported(self, credit_note_id: int, is_exported: bool) -> Result:
        """
        Defines if the credit note is already exported.


        :param credit_note_id: int
        :param is_exported: bool
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setIsExported
        response_model = Result

        arg = {"creditNoteID": credit_note_id, "isExported": is_exported}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_paid_date(self, credit_note_id: int) -> DateResult:
        """
        Retuns the date the credit note is payed.


        :param credit_note_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPaidDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_po_number(self, credit_note_id: int) -> StringResult:
        """
        Returns the PO-number


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPONumber
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_credit_note_id(
        self, display_name: str, company_code_id: int
    ) -> IntegerResult:
        """
        Get the creditNoteId based on the display name and company code of the credit note.


        :param display_name: str
        :param company_code_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteId
        response_model = IntegerResult

        arg = {"displayName": display_name, "companyCodeId": company_code_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_credit_date(self, credit_note_id: int) -> DateResult:
        """
        Returns an instance of DateResult, which contains the credit note date.


        :param credit_note_id: int
        :return: DateResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditDate
        response_model = DateResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_paid_date(self, credit_note_id: int, paid_date: datetime) -> Result:
        """
        Defines the date the credit note is payed.


        :param credit_note_id: int
        :param paid_date: datetime
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setPaidDate
        response_model = Result

        arg = {"creditNoteID": credit_note_id, "paidDate": paid_date}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_price_line(self, price_line_id: int) -> PriceLineResult:
        """
        Returns an existing PriceLine.


        :param price_line_id: int
        :return: PriceLineResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPriceLine
        response_model = PriceLineResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=price_line_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def set_credit_date(self, credit_date: datetime, credit_note_id: int) -> Result:
        """
        Defines the credit date.


        :param credit_date: datetime
        :param credit_note_id: int
        :return: Result
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setCreditDate
        response_model = Result

        arg = {"creditDate": credit_date, "creditNoteID": credit_note_id}

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=arg,
            response_model=response_model,
            unpack_dict=True,
        )

    def get_company_code(self, credit_note_id: int) -> IntegerResult:
        """
        Returns the type dependent company code, related to the specified
        credit note.


        :param credit_note_id: int
        :return: IntegerResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCompanyCode
        response_model = IntegerResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_tax_types(self, credit_note_id: int) -> TaxListResult:
        """
        Returns a list of all tax types which are used within the transfered credit note.
        Possible currency codes can be configured over Admin|Settings|Comany Code


        :param credit_note_id: int
        :return: TaxListResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxTypes
        response_model = TaxListResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )

    def get_credit_note_nr(self, credit_note_id: int) -> StringResult:
        """
        Returns an instance of StringResult, which contains the credit note
        number.


        :param credit_note_id: int
        :return: StringResult
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteNr
        response_model = StringResult

        return self.__client.make_request(
            operation_proxy=proxy,
            argument=credit_note_id,
            response_model=response_model,
            unpack_dict=False,
        )
