from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        SearchFilter_Quote,
        QuoteListResult,
        QuoteIN,
        TemplateListResult,
        DateResult,
        QuoteResult,
        IntegerArrayResult,
        DoubleResult,
        StringResult,
        IntegerList
)


from src.pyplunet.enums import (
        ProjectClassType,
        EventType
)


class test_set_DataQuote30(BaseModel):
    source_language: str
    target_language: str
    quote_id: int
    project_name: str
    subject: str
    request_id: int
    quote_in: QuoteIN
    enable_null_or_empty_values: bool
    search_filter: SearchFilter_Quote
    project_class_type: ProjectClassType
    reference: str
    project_category: str
    system_language_code: str
    customer_id: int
    server_authentication_string: str
    server_address: str
    event_type: EventType
    template_id: int
    memo: str
    status: int
    resource_id: int
    customer_contact_id: int
    project_status: int
    date: datetime
    quote_number: str
    quote_id_list: IntegerList
    template: str
    format_id: int
    external_id: str
    display_no: str

def get_test_set() -> test_set_DataQuote30:
    return test_set_DataQuote30(
            source_language= ,
            target_language= ,
            quote_id= ,
            project_name= ,
            subject= ,
            request_id= ,
            quote_in= ,
            enable_null_or_empty_values= ,
            search_filter= ,
            project_class_type= ,
            reference= ,
            project_category= ,
            system_language_code= ,
            customer_id= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            template_id= ,
            memo= ,
            status= ,
            resource_id= ,
            customer_contact_id= ,
            project_status= ,
            date= ,
            quote_number= ,
            quote_id_list= ,
            template= ,
            format_id= ,
            external_id= ,
            display_no= 
    )


def test_DataQuote30_add_language_combination(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.add_language_combination(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_add_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_add_language_combination was successful.")




def test_DataQuote30_get_rate(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_rate(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_rate failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataQuote30_get_rate was successful.")




def test_DataQuote30_get_request_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_request_id(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_request_id was successful.")




def test_DataQuote30_set_project_name(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_project_name(
                project_name=test_set.project_name,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_project_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_project_name was successful.")




def test_DataQuote30_get_subject(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_subject(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_subject was successful.")




def test_DataQuote30_set_subject(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_subject(
                subject=test_set.subject,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_subject was successful.")




def test_DataQuote30_get_project_name(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_project_name(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_project_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_project_name was successful.")




def test_DataQuote30_set_request_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_request_id(
                quote_id=test_set.quote_id,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_request_id was successful.")




def test_DataQuote30_get_creation_date(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_creation_date(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataQuote30_get_creation_date was successful.")




def test_DataQuote30_update(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.update(
                quote_in=test_set.quote_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_update was successful.")




def test_DataQuote30_delete(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.delete(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_delete was successful.")




def test_DataQuote30_insert(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.insert(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_insert was successful.")




def test_DataQuote30_search(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataQuote30_search was successful.")




def test_DataQuote30_request_order(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.request_order(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_request_order failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_request_order was successful.")




def test_DataQuote30_request_quote(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.request_quote(
                project_class_type=test_set.project_class_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_request_quote failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_request_quote was successful.")




def test_DataQuote30_get_currency(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_currency(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_currency was successful.")




def test_DataQuote30_set_reference_number(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_reference_number(
                quote_id=test_set.quote_id,
                reference=test_set.reference
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_reference_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_reference_number was successful.")




def test_DataQuote30_set_project_category(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_project_category(
                project_category=test_set.project_category,
                system_language_code=test_set.system_language_code,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_project_category failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_project_category was successful.")




def test_DataQuote30_get_project_category(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_project_category(
                system_language_code=test_set.system_language_code,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_project_category failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_project_category was successful.")




def test_DataQuote30_set_customer_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_customer_id(
                customer_id=test_set.customer_id,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_customer_id was successful.")




def test_DataQuote30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.deregister_callback_observer(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_deregister_callback_observer was successful.")




def test_DataQuote30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_register_callback_notify was successful.")




def test_DataQuote30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_deregister_callback_notify was successful.")




def test_DataQuote30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_register_callback_observer was successful.")




def test_DataQuote30_insert_by_template(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.insert_by_template(
                quote_in=test_set.quote_in,
                template_id=test_set.template_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_insert_by_template failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_insert_by_template was successful.")




def test_DataQuote30_get_reference_number(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_reference_number(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_reference_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_reference_number was successful.")




def test_DataQuote30_get_project_manager_memo(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_project_manager_memo(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_project_manager_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_project_manager_memo was successful.")




def test_DataQuote30_set_project_manager_memo(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_project_manager_memo(
                quote_id=test_set.quote_id,
                memo=test_set.memo
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_project_manager_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_project_manager_memo was successful.")




def test_DataQuote30_get_status(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_status(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_status was successful.")




def test_DataQuote30_set_status(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_status(
                status=test_set.status,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_status was successful.")




def test_DataQuote30_get_projectmanager_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_projectmanager_id(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_projectmanager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_projectmanager_id was successful.")




def test_DataQuote30_set_projectmanager_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_projectmanager_id(
                resource_id=test_set.resource_id,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_projectmanager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_projectmanager_id was successful.")




def test_DataQuote30_get_template_list(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_template_list(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_template_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TemplateListResult
    print(f"test_DataQuote30_get_template_list was successful.")




def test_DataQuote30_set_customer_contact_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_customer_contact_id(
                customer_contact_id=test_set.customer_contact_id,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_customer_contact_id was successful.")




def test_DataQuote30_get_customer_contact_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_customer_contact_id(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_customer_contact_id was successful.")




def test_DataQuote30_set_project_status(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_project_status(
                quote_id=test_set.quote_id,
                project_status=test_set.project_status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_project_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_project_status was successful.")




def test_DataQuote30_get_project_status(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_project_status(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_project_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_project_status was successful.")




def test_DataQuote30_get_quote_object(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_object(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == QuoteResult
    print(f"test_DataQuote30_get_quote_object was successful.")




def test_DataQuote30_get_quote_document(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_document(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_document failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_quote_document was successful.")




def test_DataQuote30_set_creation_date(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_creation_date(
                date=test_set.date,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_creation_date was successful.")




def test_DataQuote30_get_quote_object2(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_object2(
                quote_number=test_set.quote_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_object2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == QuoteResult
    print(f"test_DataQuote30_get_quote_object2 was successful.")




def test_DataQuote30_get_order_id_first_item(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_order_id_first_item(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_order_id_first_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_order_id_first_item was successful.")




def test_DataQuote30_get_quote_no_for_view(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_no_for_view(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_no_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_quote_no_for_view was successful.")




def test_DataQuote30_get_quote_object_list(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_object_list(
                quote_id_list=test_set.quote_id_list
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_object_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == QuoteListResult
    print(f"test_DataQuote30_get_quote_object_list was successful.")




def test_DataQuote30_create_quote_document(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.create_quote_document(
                template=test_set.template,
                format_id=test_set.format_id,
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_create_quote_document failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_create_quote_document was successful.")




def test_DataQuote30_insert2(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.insert2(
                quote_in=test_set.quote_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_insert2 was successful.")




def test_DataQuote30_set_external_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.set_external_id(
                quote_id=test_set.quote_id,
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_set_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataQuote30_set_external_id was successful.")




def test_DataQuote30_get_external_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_external_id(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataQuote30_get_external_id was successful.")




def test_DataQuote30_get_quote_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_quote_id(
                display_no=test_set.display_no
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_quote_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_quote_id was successful.")




def test_DataQuote30_get_customer_id(pc: PlunetClient, test_set: test_set_DataQuote30):
    try:
        resp = pc.quote.get_customer_id(
                quote_id=test_set.quote_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataQuote30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataQuote30_get_customer_id was successful.")



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
        test_DataQuote30_add_language_combination(pc, test_set)
        test_DataQuote30_get_rate(pc, test_set)
        test_DataQuote30_get_request_id(pc, test_set)
        test_DataQuote30_set_project_name(pc, test_set)
        test_DataQuote30_get_subject(pc, test_set)
        test_DataQuote30_set_subject(pc, test_set)
        test_DataQuote30_get_project_name(pc, test_set)
        test_DataQuote30_set_request_id(pc, test_set)
        test_DataQuote30_get_creation_date(pc, test_set)
        test_DataQuote30_update(pc, test_set)
        test_DataQuote30_delete(pc, test_set)
        test_DataQuote30_insert(pc, test_set)
        test_DataQuote30_search(pc, test_set)
        test_DataQuote30_request_order(pc, test_set)
        test_DataQuote30_request_quote(pc, test_set)
        test_DataQuote30_get_currency(pc, test_set)
        test_DataQuote30_set_reference_number(pc, test_set)
        test_DataQuote30_set_project_category(pc, test_set)
        test_DataQuote30_get_project_category(pc, test_set)
        test_DataQuote30_set_customer_id(pc, test_set)
        test_DataQuote30_deregister_callback_observer(pc, test_set)
        test_DataQuote30_register_callback_notify(pc, test_set)
        test_DataQuote30_deregister_callback_notify(pc, test_set)
        test_DataQuote30_register_callback_observer(pc, test_set)
        test_DataQuote30_insert_by_template(pc, test_set)
        test_DataQuote30_get_reference_number(pc, test_set)
        test_DataQuote30_get_project_manager_memo(pc, test_set)
        test_DataQuote30_set_project_manager_memo(pc, test_set)
        test_DataQuote30_get_status(pc, test_set)
        test_DataQuote30_set_status(pc, test_set)
        test_DataQuote30_get_projectmanager_id(pc, test_set)
        test_DataQuote30_set_projectmanager_id(pc, test_set)
        test_DataQuote30_get_template_list(pc, test_set)
        test_DataQuote30_set_customer_contact_id(pc, test_set)
        test_DataQuote30_get_customer_contact_id(pc, test_set)
        test_DataQuote30_set_project_status(pc, test_set)
        test_DataQuote30_get_project_status(pc, test_set)
        test_DataQuote30_get_quote_object(pc, test_set)
        test_DataQuote30_get_quote_document(pc, test_set)
        test_DataQuote30_set_creation_date(pc, test_set)
        test_DataQuote30_get_quote_object2(pc, test_set)
        test_DataQuote30_get_order_id_first_item(pc, test_set)
        test_DataQuote30_get_quote_no_for_view(pc, test_set)
        test_DataQuote30_get_quote_object_list(pc, test_set)
        test_DataQuote30_create_quote_document(pc, test_set)
        test_DataQuote30_insert2(pc, test_set)
        test_DataQuote30_set_external_id(pc, test_set)
        test_DataQuote30_get_external_id(pc, test_set)
        test_DataQuote30_get_quote_id(pc, test_set)
        test_DataQuote30_get_customer_id(pc, test_set)