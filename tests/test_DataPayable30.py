from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        PriceLineIN,
        PriceLineResult,
        PriceLineListResult,
        PayableItemIN,
        DateResult,
        StringArrayResult,
        IntegerArrayResult,
        PriceUnitListResult,
        PriceUnitResult,
        TaxListResult,
        BooleanResult,
        PayableItemResultList,
        DoubleResult,
        StringResult,
        SearchFilter_Payable
)


from src.pyplunet.enums import (
        TaxType
)


class test_set_DataPayable30(BaseModel):
    search_filter: SearchFilter_Payable
    payables_id: int
    due_date: datetime
    account_id: str
    accountstatement: str
    currency_tpe: int
    tax_type: TaxType
    payment_item_in: PayableItemIN
    payment_item_id: int
    enable_null_or_empty_values: bool
    external_number: str
    payables_item_id: int
    language_code: str
    service: str
    status: int
    price_line_in: PriceLineIN
    price_unit_id: int
    create_as_first_item: bool
    price_line_id: int
    item_id: int
    invoice_date: datetime
    value_date: datetime
    is_exported: bool
    memo: str
    paid_date: datetime

def get_test_set() -> test_set_DataPayable30:
    return test_set_DataPayable30(
            search_filter= ,
            payables_id= ,
            due_date= ,
            account_id= ,
            accountstatement= ,
            currency_tpe= ,
            tax_type= ,
            payment_item_in= ,
            payment_item_id= ,
            enable_null_or_empty_values= ,
            external_number= ,
            payables_item_id= ,
            language_code= ,
            service= ,
            status= ,
            price_line_in= ,
            price_unit_id= ,
            create_as_first_item= ,
            price_line_id= ,
            item_id= ,
            invoice_date= ,
            value_date= ,
            is_exported= ,
            memo= ,
            paid_date= 
    )


def test_DataPayable30_search(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataPayable30_search was successful.")




def test_DataPayable30_get_payment_due_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_payment_due_date(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_payment_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataPayable30_get_payment_due_date was successful.")




def test_DataPayable30_set_payment_due_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_payment_due_date(
                payables_id=test_set.payables_id,
                due_date=test_set.due_date
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_payment_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_payment_due_date was successful.")




def test_DataPayable30_get_invoice_tax_types(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_invoice_tax_types(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_invoice_tax_types failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TaxListResult
    print(f"test_DataPayable30_get_invoice_tax_types was successful.")




def test_DataPayable30_get_creditor_account(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_creditor_account(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_creditor_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_creditor_account was successful.")




def test_DataPayable30_get_external_invoice_number(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_external_invoice_number(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_external_invoice_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_external_invoice_number was successful.")




def test_DataPayable30_set_creditor_account(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_creditor_account(
                account_id=test_set.account_id,
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_creditor_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_creditor_account was successful.")




def test_DataPayable30_set_account_statement(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_account_statement(
                payables_id=test_set.payables_id,
                accountstatement=test_set.accountstatement
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_account_statement failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_account_statement was successful.")




def test_DataPayable30_get_total_tax_amount(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_total_tax_amount(
                payables_id=test_set.payables_id,
                currency_tpe=test_set.currency_tpe,
                tax_type=test_set.tax_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_total_tax_amount failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataPayable30_get_total_tax_amount was successful.")




def test_DataPayable30_get_total_net_amount(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_total_net_amount(
                payables_id=test_set.payables_id,
                currency_tpe=test_set.currency_tpe
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_total_net_amount failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataPayable30_get_total_net_amount was successful.")




def test_DataPayable30_update_payment_item(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.update_payment_item(
                payment_item_in=test_set.payment_item_in,
                payment_item_id=test_set.payment_item_id,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_update_payment_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_update_payment_item was successful.")




def test_DataPayable30_delete_payment_item(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.delete_payment_item(
                payment_item_id=test_set.payment_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_delete_payment_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_delete_payment_item was successful.")




def test_DataPayable30_get_expense_account(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_expense_account(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_expense_account failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_expense_account was successful.")




def test_DataPayable30_get_payment_item_list(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_payment_item_list(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_payment_item_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PayableItemResultList
    print(f"test_DataPayable30_get_payment_item_list was successful.")




def test_DataPayable30_get_account_statement(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_account_statement(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_account_statement failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_account_statement was successful.")




def test_DataPayable30_insert_payment_item(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.insert_payment_item(
                payment_item_in=test_set.payment_item_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_insert_payment_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_insert_payment_item was successful.")




def test_DataPayable30_get_payment_creator_resource_id(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_payment_creator_resource_id(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_payment_creator_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_payment_creator_resource_id was successful.")




def test_DataPayable30_set_external_invoice_number(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_external_invoice_number(
                payables_id=test_set.payables_id,
                external_number=test_set.external_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_external_invoice_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_external_invoice_number was successful.")




def test_DataPayable30_get_currency(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_currency(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_currency was successful.")




def test_DataPayable30_get_payment_method(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_payment_method(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_payment_method failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_payment_method was successful.")




def test_DataPayable30_get_price_line_list(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_price_line_list(
                payables_item_id=test_set.payables_item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_price_line_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataPayable30_get_price_line_list was successful.")




def test_DataPayable30_get_price_unit_list(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_price_unit_list(
                language_code=test_set.language_code,
                service=test_set.service
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_price_unit_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitListResult
    print(f"test_DataPayable30_get_price_unit_list was successful.")




def test_DataPayable30_get_status(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_status(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_status was successful.")




def test_DataPayable30_set_status(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_status(
                status=test_set.status,
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_status was successful.")




def test_DataPayable30_update_price_line(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.update_price_line(
                payables_item_id=test_set.payables_item_id,
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_update_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataPayable30_update_price_line was successful.")




def test_DataPayable30_get_services_list(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_services_list(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_services_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataPayable30_get_services_list was successful.")




def test_DataPayable30_get_price_unit(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_price_unit(
                price_unit_id=test_set.price_unit_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_price_unit failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitResult
    print(f"test_DataPayable30_get_price_unit was successful.")




def test_DataPayable30_insert_price_line(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.insert_price_line(
                payables_item_id=test_set.payables_item_id,
                price_line_in=test_set.price_line_in,
                create_as_first_item=test_set.create_as_first_item
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_insert_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataPayable30_insert_price_line was successful.")




def test_DataPayable30_delete_price_line(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.delete_price_line(
                payables_item_id=test_set.payables_item_id,
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_delete_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_delete_price_line was successful.")




def test_DataPayable30_get_payable_id(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_payable_id(
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_payable_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_payable_id was successful.")




def test_DataPayable30_get_value_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_value_date(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_value_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataPayable30_get_value_date was successful.")




def test_DataPayable30_get_invoice_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_invoice_date(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_invoice_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataPayable30_get_invoice_date was successful.")




def test_DataPayable30_set_invoice_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_invoice_date(
                invoice_date=test_set.invoice_date,
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_invoice_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_invoice_date was successful.")




def test_DataPayable30_set_value_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_value_date(
                value_date=test_set.value_date,
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_value_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_value_date was successful.")




def test_DataPayable30_get_resource_id(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_resource_id(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_resource_id was successful.")




def test_DataPayable30_get_is_exported(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_is_exported(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_is_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataPayable30_get_is_exported was successful.")




def test_DataPayable30_set_is_exported(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_is_exported(
                payables_id=test_set.payables_id,
                is_exported=test_set.is_exported
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_is_exported failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_is_exported was successful.")




def test_DataPayable30_get_memo(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_memo(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataPayable30_get_memo was successful.")




def test_DataPayable30_get_paid_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_paid_date(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataPayable30_get_paid_date was successful.")




def test_DataPayable30_set_memo(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_memo(
                payables_id=test_set.payables_id,
                memo=test_set.memo
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_memo was successful.")




def test_DataPayable30_set_paid_date(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.set_paid_date(
                payables_id=test_set.payables_id,
                paid_date=test_set.paid_date
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_set_paid_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataPayable30_set_paid_date was successful.")




def test_DataPayable30_get_company_code(pc: PlunetClient, test_set: test_set_DataPayable30):
    try:
        resp = pc.payable.get_company_code(
                payables_id=test_set.payables_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataPayable30_get_company_code failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataPayable30_get_company_code was successful.")



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
        test_DataPayable30_search(pc, test_set)
        test_DataPayable30_get_payment_due_date(pc, test_set)
        test_DataPayable30_set_payment_due_date(pc, test_set)
        test_DataPayable30_get_invoice_tax_types(pc, test_set)
        test_DataPayable30_get_creditor_account(pc, test_set)
        test_DataPayable30_get_external_invoice_number(pc, test_set)
        test_DataPayable30_set_creditor_account(pc, test_set)
        test_DataPayable30_set_account_statement(pc, test_set)
        test_DataPayable30_get_total_tax_amount(pc, test_set)
        test_DataPayable30_get_total_net_amount(pc, test_set)
        test_DataPayable30_update_payment_item(pc, test_set)
        test_DataPayable30_delete_payment_item(pc, test_set)
        test_DataPayable30_get_expense_account(pc, test_set)
        test_DataPayable30_get_payment_item_list(pc, test_set)
        test_DataPayable30_get_account_statement(pc, test_set)
        test_DataPayable30_insert_payment_item(pc, test_set)
        test_DataPayable30_get_payment_creator_resource_id(pc, test_set)
        test_DataPayable30_set_external_invoice_number(pc, test_set)
        test_DataPayable30_get_currency(pc, test_set)
        test_DataPayable30_get_payment_method(pc, test_set)
        test_DataPayable30_get_price_line_list(pc, test_set)
        test_DataPayable30_get_price_unit_list(pc, test_set)
        test_DataPayable30_get_status(pc, test_set)
        test_DataPayable30_set_status(pc, test_set)
        test_DataPayable30_update_price_line(pc, test_set)
        test_DataPayable30_get_services_list(pc, test_set)
        test_DataPayable30_get_price_unit(pc, test_set)
        test_DataPayable30_insert_price_line(pc, test_set)
        test_DataPayable30_delete_price_line(pc, test_set)
        test_DataPayable30_get_payable_id(pc, test_set)
        test_DataPayable30_get_value_date(pc, test_set)
        test_DataPayable30_get_invoice_date(pc, test_set)
        test_DataPayable30_set_invoice_date(pc, test_set)
        test_DataPayable30_set_value_date(pc, test_set)
        test_DataPayable30_get_resource_id(pc, test_set)
        test_DataPayable30_get_is_exported(pc, test_set)
        test_DataPayable30_set_is_exported(pc, test_set)
        test_DataPayable30_get_memo(pc, test_set)
        test_DataPayable30_get_paid_date(pc, test_set)
        test_DataPayable30_set_memo(pc, test_set)
        test_DataPayable30_set_paid_date(pc, test_set)
        test_DataPayable30_get_company_code(pc, test_set)