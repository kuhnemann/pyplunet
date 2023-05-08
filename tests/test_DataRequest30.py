from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        RequestResult,
        DateResult,
        RequestListResult,
        IntegerArrayResult,
        RequestIN,
        BooleanResult,
        DoubleResult,
        SearchFilter_Request,
        StringResult,
        IntegerList
)


from src.pyplunet.enums import (
        EventType
)


class test_set_DataRequest30(BaseModel):
    source_language: str
    target_language: str
    request_id: int
    subject: str
    property_name_english: str
    property_value_english: str
    request_in: RequestIN
    enable_null_or_empty_values: bool
    search_filter: SearchFilter_Request
    is_rush_request: bool
    type_of_project: str
    workflow_id: int
    order_template_id: int
    quote_template_id: int
    service: str
    customer_id: int
    server_authentication_string: str
    server_address: str
    event_type: EventType
    master_project_id: int
    status: int
    brief_description: str
    is_en15038: bool
    customer_contact_id: int
    date: datetime
    price: float
    customer_ref_no: str
    quote_id: int
    order_id: int
    customer_ref_no_previous_order: str
    ref_language: str
    unc_file_name: str
    request_number: str
    request_id_list: IntegerList
    word_count: int
    display_no: str

def get_test_set() -> test_set_DataRequest30:
    return test_set_DataRequest30(
            source_language= ,
            target_language= ,
            request_id= ,
            subject= ,
            property_name_english= ,
            property_value_english= ,
            request_in= ,
            enable_null_or_empty_values= ,
            search_filter= ,
            is_rush_request= ,
            type_of_project= ,
            workflow_id= ,
            order_template_id= ,
            quote_template_id= ,
            service= ,
            customer_id= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            master_project_id= ,
            status= ,
            brief_description= ,
            is_en15038= ,
            customer_contact_id= ,
            date= ,
            price= ,
            customer_ref_no= ,
            quote_id= ,
            order_id= ,
            customer_ref_no_previous_order= ,
            ref_language= ,
            unc_file_name= ,
            request_number= ,
            request_id_list= ,
            word_count= ,
            display_no= 
    )


def test_DataRequest30_add_language_combination(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.add_language_combination(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_add_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_add_language_combination was successful.")




def test_DataRequest30_get_subject(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_subject(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_subject was successful.")




def test_DataRequest30_set_subject(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_subject(
                subject=test_set.subject,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_subject was successful.")




def test_DataRequest30_get_creation_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_creation_date(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataRequest30_get_creation_date was successful.")




def test_DataRequest30_set_property(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_property(
                request_id=test_set.request_id,
                property_name_english=test_set.property_name_english,
                property_value_english=test_set.property_value_english
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_property failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_property was successful.")




def test_DataRequest30_get_property(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_property(
                request_id=test_set.request_id,
                property_name_english=test_set.property_name_english
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_property failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_property was successful.")




def test_DataRequest30_update(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.update(
                request_in=test_set.request_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_update was successful.")




def test_DataRequest30_delete(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.delete(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_delete was successful.")




def test_DataRequest30_insert(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.insert(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_insert was successful.")




def test_DataRequest30_search(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataRequest30_search was successful.")




def test_DataRequest30_set_rush_request(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_rush_request(
                is_rush_request=test_set.is_rush_request,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_rush_request failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_rush_request was successful.")




def test_DataRequest30_set_type_of_project(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_type_of_project(
                request_id=test_set.request_id,
                type_of_project=test_set.type_of_project
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_type_of_project failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_type_of_project was successful.")




def test_DataRequest30_get_workflow_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_workflow_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_workflow_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_workflow_id was successful.")




def test_DataRequest30_quote_request(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.quote_request(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_quote_request failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_quote_request was successful.")




def test_DataRequest30_get_type_of_project(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_type_of_project(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_type_of_project failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_type_of_project was successful.")




def test_DataRequest30_set_workflow_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_workflow_id(
                request_id=test_set.request_id,
                workflow_id=test_set.workflow_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_workflow_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_workflow_id was successful.")




def test_DataRequest30_get_rush_request(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_rush_request(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_rush_request failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataRequest30_get_rush_request was successful.")




def test_DataRequest30_order_request_by_template(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.order_request_by_template(
                request_id=test_set.request_id,
                order_template_id=test_set.order_template_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_order_request_by_template failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_order_request_by_template was successful.")




def test_DataRequest30_quote_request_by_template(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.quote_request_by_template(
                request_id=test_set.request_id,
                quote_template_id=test_set.quote_template_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_quote_request_by_template failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_quote_request_by_template was successful.")




def test_DataRequest30_add_service(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.add_service(
                service=test_set.service,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_add_service failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_add_service was successful.")




def test_DataRequest30_set_customer_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_customer_id(
                customer_id=test_set.customer_id,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_customer_id was successful.")




def test_DataRequest30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.deregister_callback_observer(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_deregister_callback_observer was successful.")




def test_DataRequest30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_register_callback_notify was successful.")




def test_DataRequest30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_deregister_callback_notify was successful.")




def test_DataRequest30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_register_callback_observer was successful.")




def test_DataRequest30_get_master_project_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_master_project_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_master_project_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_master_project_id was successful.")




def test_DataRequest30_set_master_project_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_master_project_id(
                request_id=test_set.request_id,
                master_project_id=test_set.master_project_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_master_project_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_master_project_id was successful.")




def test_DataRequest30_get_status(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_status(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_status was successful.")




def test_DataRequest30_set_status(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_status(
                status=test_set.status,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_status was successful.")




def test_DataRequest30_get_brief_description(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_brief_description(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_brief_description was successful.")




def test_DataRequest30_set_brief_description(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_brief_description(
                brief_description=test_set.brief_description,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_brief_description was successful.")




def test_DataRequest30_set_en15038_requested(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_en15038_requested(
                is_en15038=test_set.is_en15038,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_en15038_requested failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_en15038_requested was successful.")




def test_DataRequest30_get_en15038_requested(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_en15038_requested(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_en15038_requested failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataRequest30_get_en15038_requested was successful.")




def test_DataRequest30_set_customer_contact_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_customer_contact_id(
                request_id=test_set.request_id,
                customer_contact_id=test_set.customer_contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_customer_contact_id was successful.")




def test_DataRequest30_get_customer_contact_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_customer_contact_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_customer_contact_id was successful.")




def test_DataRequest30_get_order_id_list(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_order_id_list(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_order_id_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataRequest30_get_order_id_list was successful.")




def test_DataRequest30_set_delivery_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_delivery_date(
                date=test_set.date,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_delivery_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_delivery_date was successful.")




def test_DataRequest30_get_delivery_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_delivery_date(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_delivery_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataRequest30_get_delivery_date was successful.")




def test_DataRequest30_set_price(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_price(
                price=test_set.price,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_price failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_price was successful.")




def test_DataRequest30_set_quotation_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_quotation_date(
                date=test_set.date,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_quotation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_quotation_date was successful.")




def test_DataRequest30_set_customer_ref_no(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_customer_ref_no(
                customer_ref_no=test_set.customer_ref_no,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_customer_ref_no failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_customer_ref_no was successful.")




def test_DataRequest30_set_quote_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_quote_id(
                quote_id=test_set.quote_id,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_quote_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_quote_id was successful.")




def test_DataRequest30_get_quote_id_list(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_quote_id_list(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_quote_id_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataRequest30_get_quote_id_list was successful.")




def test_DataRequest30_set_creation_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_creation_date(
                date=test_set.date,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_creation_date was successful.")




def test_DataRequest30_set_order_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_order_id(
                order_id=test_set.order_id,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_order_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_order_id was successful.")




def test_DataRequest30_get_quotation_date(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_quotation_date(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_quotation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataRequest30_get_quotation_date was successful.")




def test_DataRequest30_get_request_object(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_request_object(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_request_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == RequestResult
    print(f"test_DataRequest30_get_request_object was successful.")




def test_DataRequest30_get_customer_ref_no(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_customer_ref_no(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_customer_ref_no failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_customer_ref_no was successful.")




def test_DataRequest30_get_price(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_price(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_price failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataRequest30_get_price was successful.")




def test_DataRequest30_order_request(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.order_request(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_order_request failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_order_request was successful.")




def test_DataRequest30_get_all_requests(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_all_requests(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_all_requests failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataRequest30_get_all_requests was successful.")




def test_DataRequest30_set_customer_ref_no_prev_order(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_customer_ref_no_prev_order(
                customer_ref_no_previous_order=test_set.customer_ref_no_previous_order,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_customer_ref_no_prev_order failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_customer_ref_no_prev_order was successful.")




def test_DataRequest30_get_customer_ref_no_prev_order(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_customer_ref_no_prev_order(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_customer_ref_no_prev_order failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_customer_ref_no_prev_order was successful.")




def test_DataRequest30_copy_document_to_reference_folder(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.copy_document_to_reference_folder(
                ref_language=test_set.ref_language,
                unc_file_name=test_set.unc_file_name,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_copy_document_to_reference_folder failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_copy_document_to_reference_folder was successful.")




def test_DataRequest30_copy_document_to_source_folder(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.copy_document_to_source_folder(
                source_language=test_set.source_language,
                unc_file_name=test_set.unc_file_name,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_copy_document_to_source_folder failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_copy_document_to_source_folder was successful.")




def test_DataRequest30_get_request_object2(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_request_object2(
                request_number=test_set.request_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_request_object2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == RequestResult
    print(f"test_DataRequest30_get_request_object2 was successful.")




def test_DataRequest30_get_request_no_for_view(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_request_no_for_view(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_request_no_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataRequest30_get_request_no_for_view was successful.")




def test_DataRequest30_get_request_object_list(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_request_object_list(
                request_id_list=test_set.request_id_list
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_request_object_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == RequestListResult
    print(f"test_DataRequest30_get_request_object_list was successful.")




def test_DataRequest30_insert2(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.insert2(
                request_in=test_set.request_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_insert2 was successful.")




def test_DataRequest30_set_word_count(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.set_word_count(
                word_count=test_set.word_count,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_set_word_count failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataRequest30_set_word_count was successful.")




def test_DataRequest30_get_word_count(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_word_count(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_word_count failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_word_count was successful.")




def test_DataRequest30_get_quote_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_quote_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_quote_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_quote_id was successful.")




def test_DataRequest30_get_request_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_request_id(
                display_no=test_set.display_no
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_request_id was successful.")




def test_DataRequest30_get_order_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_order_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_order_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_order_id was successful.")




def test_DataRequest30_get_customer_id(pc: PlunetClient, test_set: test_set_DataRequest30):
    try:
        resp = pc.request.get_customer_id(
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataRequest30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataRequest30_get_customer_id was successful.")



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
        test_DataRequest30_add_language_combination(pc, test_set)
        test_DataRequest30_get_subject(pc, test_set)
        test_DataRequest30_set_subject(pc, test_set)
        test_DataRequest30_get_creation_date(pc, test_set)
        test_DataRequest30_set_property(pc, test_set)
        test_DataRequest30_get_property(pc, test_set)
        test_DataRequest30_update(pc, test_set)
        test_DataRequest30_delete(pc, test_set)
        test_DataRequest30_insert(pc, test_set)
        test_DataRequest30_search(pc, test_set)
        test_DataRequest30_set_rush_request(pc, test_set)
        test_DataRequest30_set_type_of_project(pc, test_set)
        test_DataRequest30_get_workflow_id(pc, test_set)
        test_DataRequest30_quote_request(pc, test_set)
        test_DataRequest30_get_type_of_project(pc, test_set)
        test_DataRequest30_set_workflow_id(pc, test_set)
        test_DataRequest30_get_rush_request(pc, test_set)
        test_DataRequest30_order_request_by_template(pc, test_set)
        test_DataRequest30_quote_request_by_template(pc, test_set)
        test_DataRequest30_add_service(pc, test_set)
        test_DataRequest30_set_customer_id(pc, test_set)
        test_DataRequest30_deregister_callback_observer(pc, test_set)
        test_DataRequest30_register_callback_notify(pc, test_set)
        test_DataRequest30_deregister_callback_notify(pc, test_set)
        test_DataRequest30_register_callback_observer(pc, test_set)
        test_DataRequest30_get_master_project_id(pc, test_set)
        test_DataRequest30_set_master_project_id(pc, test_set)
        test_DataRequest30_get_status(pc, test_set)
        test_DataRequest30_set_status(pc, test_set)
        test_DataRequest30_get_brief_description(pc, test_set)
        test_DataRequest30_set_brief_description(pc, test_set)
        test_DataRequest30_set_en15038_requested(pc, test_set)
        test_DataRequest30_get_en15038_requested(pc, test_set)
        test_DataRequest30_set_customer_contact_id(pc, test_set)
        test_DataRequest30_get_customer_contact_id(pc, test_set)
        test_DataRequest30_get_order_id_list(pc, test_set)
        test_DataRequest30_set_delivery_date(pc, test_set)
        test_DataRequest30_get_delivery_date(pc, test_set)
        test_DataRequest30_set_price(pc, test_set)
        test_DataRequest30_set_quotation_date(pc, test_set)
        test_DataRequest30_set_customer_ref_no(pc, test_set)
        test_DataRequest30_set_quote_id(pc, test_set)
        test_DataRequest30_get_quote_id_list(pc, test_set)
        test_DataRequest30_set_creation_date(pc, test_set)
        test_DataRequest30_set_order_id(pc, test_set)
        test_DataRequest30_get_quotation_date(pc, test_set)
        test_DataRequest30_get_request_object(pc, test_set)
        test_DataRequest30_get_customer_ref_no(pc, test_set)
        test_DataRequest30_get_price(pc, test_set)
        test_DataRequest30_order_request(pc, test_set)
        test_DataRequest30_get_all_requests(pc, test_set)
        test_DataRequest30_set_customer_ref_no_prev_order(pc, test_set)
        test_DataRequest30_get_customer_ref_no_prev_order(pc, test_set)
        test_DataRequest30_copy_document_to_reference_folder(pc, test_set)
        test_DataRequest30_copy_document_to_source_folder(pc, test_set)
        test_DataRequest30_get_request_object2(pc, test_set)
        test_DataRequest30_get_request_no_for_view(pc, test_set)
        test_DataRequest30_get_request_object_list(pc, test_set)
        test_DataRequest30_insert2(pc, test_set)
        test_DataRequest30_set_word_count(pc, test_set)
        test_DataRequest30_get_word_count(pc, test_set)
        test_DataRequest30_get_quote_id(pc, test_set)
        test_DataRequest30_get_request_id(pc, test_set)
        test_DataRequest30_get_order_id(pc, test_set)
        test_DataRequest30_get_customer_id(pc, test_set)