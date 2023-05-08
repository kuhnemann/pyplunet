from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        CreditNoteListResult,
        PriceLineIN,
        CreditNoteItemIN,
        PriceLineResult,
        DateResult,
        IntegerArrayResult,
        BooleanResult,
        TaxListResult,
        DoubleResult,
        SearchFilter_CreditNote,
        StringResult
)


from src.pyplunet.enums import (
        TaxType,
        CurrencyType
)


class test_set_DataCreditNote30(BaseModel):
    credit_note_id: int
    subject: str
    search_filter: SearchFilter_CreditNote
    account_id: int
    currency_type: CurrencyType
    taxtypes: TaxType
    credit_note_item_id: int
    credit_note_item_in: CreditNoteItemIN
    customer_id: int
    address_id: int
    status: int
    description: str
    contact_person_id: int
    price_line_in: PriceLineIN
    price_line_id: int
    po_number: str
    is_exported: bool
    display_name: str
    company_code_id: int
    paid_date: datetime
    credit_date: datetime

def get_test_set() -> test_set_DataCreditNote30:
    return test_set_DataCreditNote30(
            credit_note_id= ,
            subject= ,
            search_filter= ,
            account_id= ,
            currency_type= ,
            taxtypes= ,
            credit_note_item_id= ,
            credit_note_item_in= ,
            customer_id= ,
            address_id= ,
            status= ,
            description= ,
            contact_person_id= ,
            price_line_in= ,
            price_line_id= ,
            po_number= ,
            is_exported= ,
            display_name= ,
            company_code_id= ,
            paid_date= ,
            credit_date= 
    )


def test_DataCreditNote30_get_subject(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_subject(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_subject was successful.")




def test_DataCreditNote30_set_subject(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_subject(
                subject=test_set.subject,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_subject was successful.")




def test_DataCreditNote30_search(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataCreditNote30_search was successful.")




def test_DataCreditNote30_set_receivable_account(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_receivable_account(
                account_id=test_set.account_id,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_receivable_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_receivable_account was successful.")




def test_DataCreditNote30_get_revenue_account(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_revenue_account(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_revenue_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_revenue_account was successful.")




def test_DataCreditNote30_get_receivable_account(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_receivable_account(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_receivable_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_receivable_account was successful.")




def test_DataCreditNote30_set_revenue_account(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_revenue_account(
                account_id=test_set.account_id,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_revenue_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_revenue_account was successful.")




def test_DataCreditNote30_get_tax_by_currency_type(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_tax_by_currency_type(
                credit_note_id=test_set.credit_note_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_tax_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_tax_by_currency_type was successful.")




def test_DataCreditNote30_get_tax_by_type_and_currency_type(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_tax_by_type_and_currency_type(
                credit_note_id=test_set.credit_note_id,
                currency_type=test_set.currency_type,
                taxtypes=test_set.taxtypes
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_tax_by_type_and_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_tax_by_type_and_currency_type was successful.")




def test_DataCreditNote30_delete_credit_note_item(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.delete_credit_note_item(
                credit_note_item_id=test_set.credit_note_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_delete_credit_note_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_delete_credit_note_item was successful.")




def test_DataCreditNote30_get_credit_note_item_list(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_credit_note_item_list(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_credit_note_item_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == CreditNoteListResult
    print(f"test_DataCreditNote30_get_credit_note_item_list was successful.")




def test_DataCreditNote30_insert_credit_note_item(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.insert_credit_note_item(
                credit_note_item_in=test_set.credit_note_item_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_insert_credit_note_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_insert_credit_note_item was successful.")




def test_DataCreditNote30_update_credit_note_item(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.update_credit_note_item(
                credit_note_item_id=test_set.credit_note_item_id,
                credit_note_item_in=test_set.credit_note_item_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_update_credit_note_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_update_credit_note_item was successful.")




def test_DataCreditNote30_get_net_by_currency_type(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_net_by_currency_type(
                credit_note_id=test_set.credit_note_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_net_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_net_by_currency_type was successful.")




def test_DataCreditNote30_get_gross_by_currency_type(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_gross_by_currency_type(
                credit_note_id=test_set.credit_note_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_gross_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_gross_by_currency_type was successful.")




def test_DataCreditNote30_get_outstanding_by_currency_type(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_outstanding_by_currency_type(
                credit_note_id=test_set.credit_note_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_outstanding_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_outstanding_by_currency_type was successful.")




def test_DataCreditNote30_get_currency_code(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_currency_code(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_currency_code failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_currency_code was successful.")




def test_DataCreditNote30_set_customer_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_customer_id(
                customer_id=test_set.customer_id,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_customer_id was successful.")




def test_DataCreditNote30_set_address_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_address_id(
                credit_note_id=test_set.credit_note_id,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_address_id was successful.")




def test_DataCreditNote30_get_status(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_status(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_status was successful.")




def test_DataCreditNote30_set_status(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_status(
                status=test_set.status,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_status was successful.")




def test_DataCreditNote30_get_brief_description(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_brief_description(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_brief_description was successful.")




def test_DataCreditNote30_set_brief_description(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_brief_description(
                description=test_set.description,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_brief_description was successful.")




def test_DataCreditNote30_get_contact_person_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_contact_person_id(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_contact_person_id was successful.")




def test_DataCreditNote30_set_contact_person_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_contact_person_id(
                credit_note_id=test_set.credit_note_id,
                contact_person_id=test_set.contact_person_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_contact_person_id was successful.")




def test_DataCreditNote30_update_price_line(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.update_price_line(
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_update_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_update_price_line was successful.")




def test_DataCreditNote30_insert_price_line(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.insert_price_line(
                credit_note_item_id=test_set.credit_note_item_id,
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_insert_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_insert_price_line was successful.")




def test_DataCreditNote30_delete_price_line(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.delete_price_line(
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_delete_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_delete_price_line was successful.")




def test_DataCreditNote30_set_po_number(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_po_number(
                credit_note_id=test_set.credit_note_id,
                po_number=test_set.po_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_po_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_po_number was successful.")




def test_DataCreditNote30_get_outstanding(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_outstanding(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_outstanding failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_outstanding was successful.")




def test_DataCreditNote30_get_gross(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_gross(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_gross failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_gross was successful.")




def test_DataCreditNote30_get_net(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_net(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_net failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_net was successful.")




def test_DataCreditNote30_get_tax(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_tax(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_tax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataCreditNote30_get_tax was successful.")




def test_DataCreditNote30_get_invoice_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_invoice_id(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_invoice_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_invoice_id was successful.")




def test_DataCreditNote30_get_customer_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_customer_id(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_customer_id was successful.")




def test_DataCreditNote30_get_adress_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_adress_id(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_adress_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_adress_id was successful.")




def test_DataCreditNote30_get_is_exported(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_is_exported(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_is_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataCreditNote30_get_is_exported was successful.")




def test_DataCreditNote30_set_is_exported(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_is_exported(
                credit_note_id=test_set.credit_note_id,
                is_exported=test_set.is_exported
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_is_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_is_exported was successful.")




def test_DataCreditNote30_get_paid_date(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_paid_date(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataCreditNote30_get_paid_date was successful.")




def test_DataCreditNote30_get_po_number(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_po_number(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_po_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_po_number was successful.")




def test_DataCreditNote30_get_credit_note_id(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_credit_note_id(
                display_name=test_set.display_name,
                company_code_id=test_set.company_code_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_credit_note_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_credit_note_id was successful.")




def test_DataCreditNote30_get_credit_date(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_credit_date(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_credit_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataCreditNote30_get_credit_date was successful.")




def test_DataCreditNote30_set_paid_date(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_paid_date(
                credit_note_id=test_set.credit_note_id,
                paid_date=test_set.paid_date
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_paid_date was successful.")




def test_DataCreditNote30_get_price_line(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_price_line(
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataCreditNote30_get_price_line was successful.")




def test_DataCreditNote30_set_credit_date(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.set_credit_date(
                credit_date=test_set.credit_date,
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_set_credit_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataCreditNote30_set_credit_date was successful.")




def test_DataCreditNote30_get_company_code(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_company_code(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_company_code failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataCreditNote30_get_company_code was successful.")




def test_DataCreditNote30_get_tax_types(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_tax_types(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_tax_types failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TaxListResult
    print(f"test_DataCreditNote30_get_tax_types was successful.")




def test_DataCreditNote30_get_credit_note_nr(pc: PlunetClient, test_set: test_set_DataCreditNote30):
    try:
        resp = pc.credit_note.get_credit_note_nr(
                credit_note_id=test_set.credit_note_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataCreditNote30_get_credit_note_nr failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataCreditNote30_get_credit_note_nr was successful.")



if __name__ == '__main__':
    test_clients = [
        test_client_factory.get_test_client,
        test_client_factory.get_test_client_inmemory_cache,
        test_client_factory.get_test_configured_sql_cache,
        test_client_factory.get_test_client_no_caching,
        test_client_factory.get_test_retrying_client,
        test_client_factory.get_test_retrying_client_inmemory_cache,
        test_client_factory.get_test_retrying_configured_sql_cache,
        test_client_factory.get_test_retrying_client_no_caching,
    ]
    test_set = get_test_set()
    for client in test_clients:
        print(client.__name__)
        pc = client()
        test_DataCreditNote30_get_subject(pc, test_set)
        test_DataCreditNote30_set_subject(pc, test_set)
        test_DataCreditNote30_search(pc, test_set)
        test_DataCreditNote30_set_receivable_account(pc, test_set)
        test_DataCreditNote30_get_revenue_account(pc, test_set)
        test_DataCreditNote30_get_receivable_account(pc, test_set)
        test_DataCreditNote30_set_revenue_account(pc, test_set)
        test_DataCreditNote30_get_tax_by_currency_type(pc, test_set)
        test_DataCreditNote30_get_tax_by_type_and_currency_type(pc, test_set)
        test_DataCreditNote30_delete_credit_note_item(pc, test_set)
        test_DataCreditNote30_get_credit_note_item_list(pc, test_set)
        test_DataCreditNote30_insert_credit_note_item(pc, test_set)
        test_DataCreditNote30_update_credit_note_item(pc, test_set)
        test_DataCreditNote30_get_net_by_currency_type(pc, test_set)
        test_DataCreditNote30_get_gross_by_currency_type(pc, test_set)
        test_DataCreditNote30_get_outstanding_by_currency_type(pc, test_set)
        test_DataCreditNote30_get_currency_code(pc, test_set)
        test_DataCreditNote30_set_customer_id(pc, test_set)
        test_DataCreditNote30_set_address_id(pc, test_set)
        test_DataCreditNote30_get_status(pc, test_set)
        test_DataCreditNote30_set_status(pc, test_set)
        test_DataCreditNote30_get_brief_description(pc, test_set)
        test_DataCreditNote30_set_brief_description(pc, test_set)
        test_DataCreditNote30_get_contact_person_id(pc, test_set)
        test_DataCreditNote30_set_contact_person_id(pc, test_set)
        test_DataCreditNote30_update_price_line(pc, test_set)
        test_DataCreditNote30_insert_price_line(pc, test_set)
        test_DataCreditNote30_delete_price_line(pc, test_set)
        test_DataCreditNote30_set_po_number(pc, test_set)
        test_DataCreditNote30_get_outstanding(pc, test_set)
        test_DataCreditNote30_get_gross(pc, test_set)
        test_DataCreditNote30_get_net(pc, test_set)
        test_DataCreditNote30_get_tax(pc, test_set)
        test_DataCreditNote30_get_invoice_id(pc, test_set)
        test_DataCreditNote30_get_customer_id(pc, test_set)
        test_DataCreditNote30_get_adress_id(pc, test_set)
        test_DataCreditNote30_get_is_exported(pc, test_set)
        test_DataCreditNote30_set_is_exported(pc, test_set)
        test_DataCreditNote30_get_paid_date(pc, test_set)
        test_DataCreditNote30_get_po_number(pc, test_set)
        test_DataCreditNote30_get_credit_note_id(pc, test_set)
        test_DataCreditNote30_get_credit_date(pc, test_set)
        test_DataCreditNote30_set_paid_date(pc, test_set)
        test_DataCreditNote30_get_price_line(pc, test_set)
        test_DataCreditNote30_set_credit_date(pc, test_set)
        test_DataCreditNote30_get_company_code(pc, test_set)
        test_DataCreditNote30_get_tax_types(pc, test_set)
        test_DataCreditNote30_get_credit_note_nr(pc, test_set)