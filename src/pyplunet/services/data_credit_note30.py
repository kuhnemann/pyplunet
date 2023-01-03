from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, List, Union

from ..enums import CurrencyType, TaxType
from ..models import CreditNoteItemIN, PriceLineIN, SearchFilter_CreditNote

if TYPE_CHECKING:
    from ..client import PlunetClient


class DataCreditNote30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def delete_credit_note_item(self, create_note_item_id: int):
        """
        Deletes an credit note item.

        :param create_note_item_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.deleteCreditNoteItem

        return self.__client.make_request(proxy, create_note_item_id, unpack_dict=False)

    def delete_price_line(self, price_line_id: int):
        """
        Deletes an existing PriceLine.

        :param price_line_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.deletePriceLine

        return self.__client.make_request(proxy, price_line_id, unpack_dict=False)

    def get_adress_id(self, credit_note_id: int):
        """
        Return the ID of the customer address entry this credit note is mapped to.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getAdressID

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_brief_description(self, credit_note_id: int):
        """
        Returns the brief description.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getBriefDescription

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_company_code(self, credit_note_id: int):
        """
        Returns the type dependent company code, related to the specifiedcredit note.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCompanyCode

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_contact_person_id(self, credit_note_id: int):
        """
        Returns the id to the credit note related contact person(resource).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getContactPersonID

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_credit_date(self, credit_note_id: int):
        """
        Returns an instance of DateResult, which contains the credit note date.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditDate

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_credit_note_id(self, display_name: str, company_code_id: int):
        """
        Get the creditNoteId based on the display name and company code of the credit note.

        :param display_name: str
        :param company_code_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteId

        arg = {"displayName": display_name, "companyCodeId": company_code_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_credit_note_item_list(self, credit_note_id: int):
        """
        Retunrs a list of all credit note items.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteItemList

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_credit_note_nr(self, credit_note_id: int):
        """
        Returns an instance of StringResult, which contains the credit notenumber.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCreditNoteNr

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_currency_code(self, credit_note_id: int):
        """
        Returns an instance of StringResult, which contains the currency codeof the specified credit note (the amount is standard currency).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCurrencyCode

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_customer_id(self, credit_note_id: int):
        """
        Returns an instance of IntegerResult, which contains thecustomer ID.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getCustomerID

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_gross(self, credit_note_id: int):
        """
        Returns an instance of DoubleResult, which contains the credit note amount (in project currency).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getGross

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_gross_by_currency_type(
        self, credit_note_id: int, currency_type: CurrencyType
    ):
        """
        Returns an instance of DoubleResult, which contains the credit note amount in the specified (project or home) currency.

        :param credit_note_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getGrossByCurrencyType

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_invoice_id(self, credit_note_id: int):
        """
        Returns the credit note related invoice ID.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getInvoiceID

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_is_exported(self, credit_note_id: int):
        """
        Returns if the credit note is already exported.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getIsExported

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_net(self, credit_note_id: int):
        """
        Returns an instance of DoubleResult, which contains the net amount (in project currency).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getNet

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_net_by_currency_type(
        self, credit_note_id: int, currency_type: CurrencyType
    ):
        """
        Returns an instance of DoubleResult, which contains the net amount in the specified (project or home) currency.

        :param credit_note_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getNetByCurrencyType

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_outstanding(self, credit_note_id: int):
        """
        Returns an instance of DoubleResult, which contains the outstandingamount (in project currency).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getOutstanding

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_outstanding_by_currency_type(
        self, credit_note_id: int, currency_type: CurrencyType
    ):
        """
        Returns an instance of DoubleResult, which contains the outstandingamount in the specified (project or home) currency.

        :param credit_note_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = (
            self.__client.plunet_server.DataCreditNote30.getOutstandingByCurrencyType
        )

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_paid_date(self, credit_note_id: int):
        """
        Retuns the date the credit note is payed.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPaidDate

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_po_number(self, credit_note_id: int):
        """
        Returns the PO-number

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPONumber

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_price_line(self, price_line_id: int):
        """
        Returns an existing PriceLine.

        :param price_line_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getPriceLine

        return self.__client.make_request(proxy, price_line_id, unpack_dict=False)

    def get_receivable_account(self, credit_note_id: int):
        """
        Returns the receivable account.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getReceivableAccount

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_revenue_account(self, credit_note_id: int):
        """
        Returns the revenue account.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getRevenueAccount

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_status(self, credit_note_id: int):
        """
        Returns an instance of IntegerResult, which contains theCreditNoteStatus.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getStatus

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_subject(self, credit_note_id: int):
        """
        Returns an instance of StringResult, which contains the subject.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getSubject

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_tax(self, credit_note_id: int):
        """
        Returns an instance of DoubleResult, which contains all taxes as summed up values (in project currency).

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTax

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def get_tax_by_currency_type(
        self, credit_note_id: int, currency_type: CurrencyType
    ):
        """
        Returns an instance of DoubleResult, which contains the summed up taxes in the specified (project or home) currency.

        :param credit_note_id: int
        :param currency_type: CurrencyType

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxByCurrencyType

        arg = {"creditNoteID": credit_note_id, "currencyType": currency_type.value}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_tax_by_type_and_currency_type(
        self, credit_note_id: int, currency_type: CurrencyType, tax_type: TaxType
    ):
        """
        Returns an instance of DoubleResult, which contains the specified TaxValue (project or home) currency.

        :param credit_note_id: int
        :param currency_type: CurrencyType
        :param tax_type: TaxType

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxByTypeAndCurrencyType

        arg = {
            "creditNoteID": credit_note_id,
            "currencyType": currency_type.value,
            "taxType": tax_type.value,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def get_tax_types(self, credit_note_id: int):
        """
        Returns a list of all tax types which are used within the transfered credit note.

        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.getTaxTypes

        return self.__client.make_request(proxy, credit_note_id, unpack_dict=False)

    def insert_credit_note_item(self, credit_note_item: Union[CreditNoteItemIN, dict]):
        """
        Inserts a new credit note item.

        :param credit_note_item: CreditNoteItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.insertCreditNoteItem

        if type(credit_note_item) != CreditNoteItemIN:
            credit_note_item = CreditNoteItemIN(**credit_note_item).dict()
        else:
            credit_note_item = credit_note_item.dict()

        return self.__client.make_request(proxy, credit_note_item, unpack_dict=False)

    def insert_price_line(
        self, credit_note_item_id: int, price_line: Union[PriceLineIN, dict]
    ):
        """
        Inserts a new PriceLineIN to the specified credit noteitem.

        :param credit_note_item_id: int
        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.insertPriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        arg = {"creditNoteItemID": credit_note_item_id, "priceLine": price_line}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def search(self, search_filter: Union[SearchFilter_CreditNote, dict]):
        """
        Search implementation to filter for any existing credit note based onthe search filter.

        :param search_filter: SearchFilter_CreditNote

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.search

        if type(search_filter) != SearchFilter_CreditNote:
            search_filter = SearchFilter_CreditNote(**search_filter).dict()
        else:
            search_filter = search_filter.dict()

        return self.__client.make_request(proxy, search_filter, unpack_dict=False)

    def set_address_id(self, credit_note_id: int, address_id: int):
        """
        Sets the addressID which has to be related to the credit note related customer.

        :param credit_note_id: int
        :param address_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setAddressID

        arg = {"creditNoteID": credit_note_id, "addressID": address_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_brief_description(self, description: str, credit_note_id: int):
        """
        Sets the brief description.

        :param description: str
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setBriefDescription

        arg = {"description": description, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_contact_person_id(self, credit_note_id: int, contact_person_id: int):
        """
        Sets the customer depended contact person for the specified credit note.

        :param credit_note_id: int
        :param contact_person_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setContactPersonID

        arg = {"creditNoteID": credit_note_id, "contactPersonID": contact_person_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_credit_date(self, credit_date: datetime, credit_note_id: int):
        """
        Defines the credit date.

        :param credit_date: datetime
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setCreditDate

        arg = {"creditDate": credit_date, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_customer_id(self, customer_id: int, credit_note_id: int):
        """
        Sets the customer ID for the specified credit note.

        :param customer_id: int
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setCustomerID

        arg = {"customerID": customer_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_is_exported(self, credit_note_id: int, is_exported: bool):
        """
        Defines if the credit note is already exported.

        :param credit_note_id: int
        :param is_exported: bool

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setIsExported

        arg = {"creditNoteID": credit_note_id, "isExported": is_exported}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_paid_date(self, credit_note_id: int, paid_date: datetime):
        """
        Defines the date the credit note is payed.

        :param credit_note_id: int
        :param paid_date: datetime

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setPaidDate

        arg = {"creditNoteID": credit_note_id, "paidDate": paid_date}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_po_number(self, credit_note_id: int, po_number: str):
        """
        Defines the po number of the related credit note.

        :param credit_note_id: int
        :param po_number: str

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setPONumber

        arg = {"creditNoteID": credit_note_id, "poNumber": po_number}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_receivable_account(self, account_id: int, credit_note_id: int):
        """
        Sets the receivable account.

        :param account_id: int
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setReceivableAccount

        arg = {"accountID": account_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_revenue_account(self, account_id: int, credit_note_id: int):
        """
        Sets the revenue account.

        :param account_id: int
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setRevenueAccount

        arg = {"accountID": account_id, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_status(self, status: int, credit_note_id: int):
        """
        Defines the CreditNoteStatus.

        :param status: int
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setStatus

        arg = {"Status": status, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def set_subject(self, subject: str, credit_note_id: int):
        """
        Defines the subject.

        :param subject: str
        :param credit_note_id: int

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.setSubject

        arg = {"subject": subject, "creditNoteID": credit_note_id}

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_credit_note_item(
        self, create_note_item_id: int, credit_note_item: Union[CreditNoteItemIN, dict]
    ):
        """
        Updates a existing credit note item.

        :param create_note_item_id: int
        :param credit_note_item: CreditNoteItemIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.updateCreditNoteItem

        if type(credit_note_item) != CreditNoteItemIN:
            credit_note_item = CreditNoteItemIN(**credit_note_item).dict()
        else:
            credit_note_item = credit_note_item.dict()

        arg = {
            "createNoteItemID": create_note_item_id,
            "creditNoteItem": credit_note_item,
        }

        return self.__client.make_request(proxy, arg, unpack_dict=True)

    def update_price_line(self, price_line: Union[PriceLineIN, dict]):
        """
        Updates a existing PriceLine.

        :param price_line: PriceLineIN

        :return:
        """

        proxy = self.__client.plunet_server.DataCreditNote30.updatePriceLine

        if type(price_line) != PriceLineIN:
            price_line = PriceLineIN(**price_line).dict()
        else:
            price_line = price_line.dict()

        return self.__client.make_request(proxy, price_line, unpack_dict=False)
