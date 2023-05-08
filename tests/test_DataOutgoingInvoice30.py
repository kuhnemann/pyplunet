from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        InvoiceItemResult,
        PriceLineListResult,
        PricelistListResult,
        DateResult,
        InvoiceResult,
        SearchFilter_Invoice,
        Result,
        PricelistEntryList,
        PriceLineIN,
        PriceLineResult,
        PricelistResult,
        IntegerArrayResult,
        BooleanResult,
        IntegerResult,
        StringArrayResult,
        InvoiceItemIN,
        PriceUnitListResult,
        PriceUnitResult,
        TaxListResult,
        DoubleResult,
        StringResult
)


from src.pyplunet.enums import (
        TaxType,
        CurrencyType
)


class test_set_DataOutgoingInvoice30(BaseModel):
    invoice_id: int
    subject: str
    search_filter: SearchFilter_Invoice
    account_id: int
    template: str
    format_id: int
    is_exported: bool
    invoice_item: InvoiceItemIN
    enable_null_or_empty_values: bool
    currency_type: CurrencyType
    taxtypes: TaxType
    due_date: datetime
    invoice_item_id: int
    display_name: str
    company_code_id: int
    customer_id: int
    address_id: int
    language_code: str
    service: str
    pricelist_id: int
    source_language: str
    target_language: str
    status: int
    description: str
    contact_person_id: int
    price_line_in: PriceLineIN
    price_list_id: int
    price_unit_id: int
    create_as_first_item: bool
    price_line_id: int
    po_number: str
    invoice_date: datetime
    value_date: datetime
    paid_date: datetime

def get_test_set() -> test_set_DataOutgoingInvoice30:
    return test_set_DataOutgoingInvoice30(
            invoice_id= ,
            subject= ,
            search_filter= ,
            account_id= ,
            template= ,
            format_id= ,
            is_exported= ,
            invoice_item= ,
            enable_null_or_empty_values= ,
            currency_type= ,
            taxtypes= ,
            due_date= ,
            invoice_item_id= ,
            display_name= ,
            company_code_id= ,
            customer_id= ,
            address_id= ,
            language_code= ,
            service= ,
            pricelist_id= ,
            source_language= ,
            target_language= ,
            status= ,
            description= ,
            contact_person_id= ,
            price_line_in= ,
            price_list_id= ,
            price_unit_id= ,
            create_as_first_item= ,
            price_line_id= ,
            po_number= ,
            invoice_date= ,
            value_date= ,
            paid_date= 
    )


def test_DataOutgoingInvoice30_get_subject(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_subject(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_subject was successful.")




def test_DataOutgoingInvoice30_set_subject(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_subject(
                subject=test_set.subject,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_subject was successful.")




def test_DataOutgoingInvoice30_delete(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.delete(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_delete was successful.")




def test_DataOutgoingInvoice30_search(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataOutgoingInvoice30_search was successful.")




def test_DataOutgoingInvoice30_get_invoice_documents(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_documents(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_documents failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOutgoingInvoice30_get_invoice_documents was successful.")




def test_DataOutgoingInvoice30_set_receivable_account(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_receivable_account(
                account_id=test_set.account_id,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_receivable_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_receivable_account was successful.")




def test_DataOutgoingInvoice30_get_revenue_account(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_revenue_account(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_revenue_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_revenue_account was successful.")




def test_DataOutgoingInvoice30_create_invoice_document(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.create_invoice_document(
                template=test_set.template,
                format_id=test_set.format_id,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_create_invoice_document failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_create_invoice_document was successful.")




def test_DataOutgoingInvoice30_get_receivable_account(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_receivable_account(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_receivable_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_receivable_account was successful.")




def test_DataOutgoingInvoice30_set_revenue_account(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_revenue_account(
                account_id=test_set.account_id,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_revenue_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_revenue_account was successful.")




def test_DataOutgoingInvoice30_set_is_invoice_exported(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_is_invoice_exported(
                invoice_id=test_set.invoice_id,
                is_exported=test_set.is_exported
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_is_invoice_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_is_invoice_exported was successful.")




def test_DataOutgoingInvoice30_insert_invoice_item(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.insert_invoice_item(
                invoice_item=test_set.invoice_item
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_insert_invoice_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_insert_invoice_item was successful.")




def test_DataOutgoingInvoice30_update_invoice_item(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.update_invoice_item(
                invoice_item=test_set.invoice_item,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_update_invoice_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_update_invoice_item was successful.")




def test_DataOutgoingInvoice30_get_paid_by_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_paid_by_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_paid_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_paid_by_currency_type was successful.")




def test_DataOutgoingInvoice30_get_tax_by_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_tax_by_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_tax_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_tax_by_currency_type was successful.")




def test_DataOutgoingInvoice30_get_tax_by_type_and_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_tax_by_type_and_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type,
                taxtypes=test_set.taxtypes
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_tax_by_type_and_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_tax_by_type_and_currency_type was successful.")




def test_DataOutgoingInvoice30_get_payment_due_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_payment_due_date(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_payment_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOutgoingInvoice30_get_payment_due_date was successful.")




def test_DataOutgoingInvoice30_get_net_by_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_net_by_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_net_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_net_by_currency_type was successful.")




def test_DataOutgoingInvoice30_get_gross_by_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_gross_by_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_gross_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_gross_by_currency_type was successful.")




def test_DataOutgoingInvoice30_get_outstanding_by_currency_type(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_outstanding_by_currency_type(
                invoice_id=test_set.invoice_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_outstanding_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_outstanding_by_currency_type was successful.")




def test_DataOutgoingInvoice30_set_payment_due_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_payment_due_date(
                invoice_id=test_set.invoice_id,
                due_date=test_set.due_date
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_payment_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_payment_due_date was successful.")




def test_DataOutgoingInvoice30_get_is_invoice_exported(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_is_invoice_exported(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_is_invoice_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataOutgoingInvoice30_get_is_invoice_exported was successful.")




def test_DataOutgoingInvoice30_get_invoice_tax_types(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_tax_types(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_tax_types failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TaxListResult
    print(f"test_DataOutgoingInvoice30_get_invoice_tax_types was successful.")




def test_DataOutgoingInvoice30_get_invoice_item_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_item_list(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_item_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == InvoiceItemResult
    print(f"test_DataOutgoingInvoice30_get_invoice_item_list was successful.")




def test_DataOutgoingInvoice30_delete_invoice_item(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.delete_invoice_item(
                invoice_item_id=test_set.invoice_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_delete_invoice_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_delete_invoice_item was successful.")




def test_DataOutgoingInvoice30_get_currency_code(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_currency_code(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_currency_code failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_currency_code was successful.")




def test_DataOutgoingInvoice30_get_invoice_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_id(
                display_name=test_set.display_name,
                company_code_id=test_set.company_code_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_invoice_id was successful.")




def test_DataOutgoingInvoice30_set_customer_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_customer_id(
                customer_id=test_set.customer_id,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_customer_id was successful.")




def test_DataOutgoingInvoice30_set_address_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_address_id(
                invoice_id=test_set.invoice_id,
                address_id=test_set.address_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_address_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_address_id was successful.")




def test_DataOutgoingInvoice30_get_price_line_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_price_line_list(
                invoice_item_id=test_set.invoice_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_price_line_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataOutgoingInvoice30_get_price_line_list was successful.")




def test_DataOutgoingInvoice30_get_price_unit_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_price_unit_list(
                language_code=test_set.language_code,
                service=test_set.service
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_price_unit_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitListResult
    print(f"test_DataOutgoingInvoice30_get_price_unit_list was successful.")




def test_DataOutgoingInvoice30_get_pricelist_entry_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_pricelist_entry_list(
                pricelist_id=test_set.pricelist_id,
                source_language=test_set.source_language,
                target_language=test_set.target_language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_pricelist_entry_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistEntryList
    print(f"test_DataOutgoingInvoice30_get_pricelist_entry_list was successful.")




def test_DataOutgoingInvoice30_get_pricelist_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_pricelist_list(
                invoice_item_id=test_set.invoice_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_pricelist_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistListResult
    print(f"test_DataOutgoingInvoice30_get_pricelist_list was successful.")




def test_DataOutgoingInvoice30_get_status(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_status(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_status was successful.")




def test_DataOutgoingInvoice30_set_status(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_status(
                status=test_set.status,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_status was successful.")




def test_DataOutgoingInvoice30_get_brief_description(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_brief_description(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_brief_description was successful.")




def test_DataOutgoingInvoice30_set_brief_description(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_brief_description(
                description=test_set.description,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_brief_description was successful.")




def test_DataOutgoingInvoice30_get_contact_person_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_contact_person_id(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_contact_person_id was successful.")




def test_DataOutgoingInvoice30_set_contact_person_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_contact_person_id(
                invoice_id=test_set.invoice_id,
                contact_person_id=test_set.contact_person_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_contact_person_id was successful.")




def test_DataOutgoingInvoice30_update_price_line(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.update_price_line(
                invoice_item_id=test_set.invoice_item_id,
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_update_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataOutgoingInvoice30_update_price_line was successful.")




def test_DataOutgoingInvoice30_get_pricelist(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_pricelist(
                invoice_item_id=test_set.invoice_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistResult
    print(f"test_DataOutgoingInvoice30_get_pricelist was successful.")




def test_DataOutgoingInvoice30_set_pricelist(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_pricelist(
                invoice_item_id=test_set.invoice_item_id,
                price_list_id=test_set.price_list_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_pricelist was successful.")




def test_DataOutgoingInvoice30_get_services_list(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_services_list(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_services_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOutgoingInvoice30_get_services_list was successful.")




def test_DataOutgoingInvoice30_get_price_unit(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_price_unit(
                price_unit_id=test_set.price_unit_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_price_unit failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitResult
    print(f"test_DataOutgoingInvoice30_get_price_unit was successful.")




def test_DataOutgoingInvoice30_insert_price_line(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.insert_price_line(
                invoice_item_id=test_set.invoice_item_id,
                price_line_in=test_set.price_line_in,
                create_as_first_item=test_set.create_as_first_item
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_insert_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataOutgoingInvoice30_insert_price_line was successful.")




def test_DataOutgoingInvoice30_delete_price_line(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.delete_price_line(
                invoice_item_id=test_set.invoice_item_id,
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_delete_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_delete_price_line was successful.")




def test_DataOutgoingInvoice30_set_po_number(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_po_number(
                invoice_id=test_set.invoice_id,
                po_number=test_set.po_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_po_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_po_number was successful.")




def test_DataOutgoingInvoice30_get_outstanding(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_outstanding(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_outstanding failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_outstanding was successful.")




def test_DataOutgoingInvoice30_get_gross(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_gross(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_gross failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_gross was successful.")




def test_DataOutgoingInvoice30_get_order_i_ds(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_order_i_ds(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_order_i_ds failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataOutgoingInvoice30_get_order_i_ds was successful.")




def test_DataOutgoingInvoice30_get_net(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_net(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_net failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_net was successful.")




def test_DataOutgoingInvoice30_get_paid(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_paid(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_paid failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_paid was successful.")




def test_DataOutgoingInvoice30_get_value_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_value_date(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_value_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOutgoingInvoice30_get_value_date was successful.")




def test_DataOutgoingInvoice30_get_invoice_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_date(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOutgoingInvoice30_get_invoice_date was successful.")




def test_DataOutgoingInvoice30_get_invoice_nr(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_nr(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_nr failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_invoice_nr was successful.")




def test_DataOutgoingInvoice30_set_invoice_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_invoice_date(
                invoice_date=test_set.invoice_date,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_invoice_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_invoice_date was successful.")




def test_DataOutgoingInvoice30_get_tax(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_tax(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_tax failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOutgoingInvoice30_get_tax was successful.")




def test_DataOutgoingInvoice30_get_invoice_object(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_invoice_object(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_invoice_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == InvoiceResult
    print(f"test_DataOutgoingInvoice30_get_invoice_object was successful.")




def test_DataOutgoingInvoice30_set_value_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_value_date(
                value_date=test_set.value_date,
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_value_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_value_date was successful.")




def test_DataOutgoingInvoice30_get_customer_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_customer_id(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_customer_id was successful.")




def test_DataOutgoingInvoice30_get_adress_id(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_adress_id(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_adress_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_adress_id was successful.")




def test_DataOutgoingInvoice30_get_paid_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_paid_date(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOutgoingInvoice30_get_paid_date was successful.")




def test_DataOutgoingInvoice30_get_po_number(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_po_number(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_po_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOutgoingInvoice30_get_po_number was successful.")




def test_DataOutgoingInvoice30_set_paid_date(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.set_paid_date(
                invoice_id=test_set.invoice_id,
                paid_date=test_set.paid_date
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_set_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOutgoingInvoice30_set_paid_date was successful.")




def test_DataOutgoingInvoice30_get_company_code(pc: PlunetClient, test_set: test_set_DataOutgoingInvoice30):
    try:
        resp = pc.outgoing_invoice.get_company_code(
                invoice_id=test_set.invoice_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOutgoingInvoice30_get_company_code failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOutgoingInvoice30_get_company_code was successful.")



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
        test_DataOutgoingInvoice30_get_subject(pc, test_set)
        test_DataOutgoingInvoice30_set_subject(pc, test_set)
        test_DataOutgoingInvoice30_delete(pc, test_set)
        test_DataOutgoingInvoice30_search(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_documents(pc, test_set)
        test_DataOutgoingInvoice30_set_receivable_account(pc, test_set)
        test_DataOutgoingInvoice30_get_revenue_account(pc, test_set)
        test_DataOutgoingInvoice30_create_invoice_document(pc, test_set)
        test_DataOutgoingInvoice30_get_receivable_account(pc, test_set)
        test_DataOutgoingInvoice30_set_revenue_account(pc, test_set)
        test_DataOutgoingInvoice30_set_is_invoice_exported(pc, test_set)
        test_DataOutgoingInvoice30_insert_invoice_item(pc, test_set)
        test_DataOutgoingInvoice30_update_invoice_item(pc, test_set)
        test_DataOutgoingInvoice30_get_paid_by_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_get_tax_by_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_get_tax_by_type_and_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_get_payment_due_date(pc, test_set)
        test_DataOutgoingInvoice30_get_net_by_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_get_gross_by_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_get_outstanding_by_currency_type(pc, test_set)
        test_DataOutgoingInvoice30_set_payment_due_date(pc, test_set)
        test_DataOutgoingInvoice30_get_is_invoice_exported(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_tax_types(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_item_list(pc, test_set)
        test_DataOutgoingInvoice30_delete_invoice_item(pc, test_set)
        test_DataOutgoingInvoice30_get_currency_code(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_id(pc, test_set)
        test_DataOutgoingInvoice30_set_customer_id(pc, test_set)
        test_DataOutgoingInvoice30_set_address_id(pc, test_set)
        test_DataOutgoingInvoice30_get_price_line_list(pc, test_set)
        test_DataOutgoingInvoice30_get_price_unit_list(pc, test_set)
        test_DataOutgoingInvoice30_get_pricelist_entry_list(pc, test_set)
        test_DataOutgoingInvoice30_get_pricelist_list(pc, test_set)
        test_DataOutgoingInvoice30_get_status(pc, test_set)
        test_DataOutgoingInvoice30_set_status(pc, test_set)
        test_DataOutgoingInvoice30_get_brief_description(pc, test_set)
        test_DataOutgoingInvoice30_set_brief_description(pc, test_set)
        test_DataOutgoingInvoice30_get_contact_person_id(pc, test_set)
        test_DataOutgoingInvoice30_set_contact_person_id(pc, test_set)
        test_DataOutgoingInvoice30_update_price_line(pc, test_set)
        test_DataOutgoingInvoice30_get_pricelist(pc, test_set)
        test_DataOutgoingInvoice30_set_pricelist(pc, test_set)
        test_DataOutgoingInvoice30_get_services_list(pc, test_set)
        test_DataOutgoingInvoice30_get_price_unit(pc, test_set)
        test_DataOutgoingInvoice30_insert_price_line(pc, test_set)
        test_DataOutgoingInvoice30_delete_price_line(pc, test_set)
        test_DataOutgoingInvoice30_set_po_number(pc, test_set)
        test_DataOutgoingInvoice30_get_outstanding(pc, test_set)
        test_DataOutgoingInvoice30_get_gross(pc, test_set)
        test_DataOutgoingInvoice30_get_order_i_ds(pc, test_set)
        test_DataOutgoingInvoice30_get_net(pc, test_set)
        test_DataOutgoingInvoice30_get_paid(pc, test_set)
        test_DataOutgoingInvoice30_get_value_date(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_date(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_nr(pc, test_set)
        test_DataOutgoingInvoice30_set_invoice_date(pc, test_set)
        test_DataOutgoingInvoice30_get_tax(pc, test_set)
        test_DataOutgoingInvoice30_get_invoice_object(pc, test_set)
        test_DataOutgoingInvoice30_set_value_date(pc, test_set)
        test_DataOutgoingInvoice30_get_customer_id(pc, test_set)
        test_DataOutgoingInvoice30_get_adress_id(pc, test_set)
        test_DataOutgoingInvoice30_get_paid_date(pc, test_set)
        test_DataOutgoingInvoice30_get_po_number(pc, test_set)
        test_DataOutgoingInvoice30_set_paid_date(pc, test_set)
        test_DataOutgoingInvoice30_get_company_code(pc, test_set)