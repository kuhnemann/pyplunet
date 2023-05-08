from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        OrderIN,
        LinkListResult,
        SearchFilter_Order,
        TemplateListResult,
        DateResult,
        StringArrayResult,
        IntegerArrayResult,
        BooleanResult,
        OrderResult,
        DoubleResult,
        OrderListResult,
        StringResult,
        IntegerList
)


from src.pyplunet.enums import (
        ProjectType,
        EventType
)


class test_set_DataOrder30(BaseModel):
    source_language: str
    target_language: str
    order_id: int
    name: str
    subject: str
    request_id: int
    property_name_english: str
    property_value_english: str
    order_in: OrderIN
    enable_null_or_empty_values: bool
    search_filter: SearchFilter_Order
    source_order_id: int
    target_id: int
    project_type: ProjectType
    is_bidirectional: bool
    memo: str
    reference: str
    project_category: str
    system_language_code: str
    customer_id: int
    server_authentication_string: str
    server_address: str
    event_type: EventType
    template_id: int
    master_project_id: int
    delivery_deadline: datetime
    is_en15038: bool
    order_id_list: IntegerList
    resource_id: int
    order_number: str
    customer_contact_id: int
    project_status: int
    user_id: int
    action_link_type: int
    order_date: datetime
    creation_date: datetime
    currency_iso_code: str
    rate: float
    template: str
    format_id: int
    external_id: str
    display_no: str
    language: str

def get_test_set() -> test_set_DataOrder30:
    return test_set_DataOrder30(
            source_language= ,
            target_language= ,
            order_id= ,
            name= ,
            subject= ,
            request_id= ,
            property_name_english= ,
            property_value_english= ,
            order_in= ,
            enable_null_or_empty_values= ,
            search_filter= ,
            source_order_id= ,
            target_id= ,
            project_type= ,
            is_bidirectional= ,
            memo= ,
            reference= ,
            project_category= ,
            system_language_code= ,
            customer_id= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            template_id= ,
            master_project_id= ,
            delivery_deadline= ,
            is_en15038= ,
            order_id_list= ,
            resource_id= ,
            order_number= ,
            customer_contact_id= ,
            project_status= ,
            user_id= ,
            action_link_type= ,
            order_date= ,
            creation_date= ,
            currency_iso_code= ,
            rate= ,
            template= ,
            format_id= ,
            external_id= ,
            display_no= ,
            language= 
    )


def test_DataOrder30_add_language_combination(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.add_language_combination(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_add_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_add_language_combination was successful.")




def test_DataOrder30_get_rate(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_rate(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_rate failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataOrder30_get_rate was successful.")




def test_DataOrder30_get_request_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_request_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_request_id was successful.")




def test_DataOrder30_set_project_name(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_project_name(
                name=test_set.name,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_project_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_project_name was successful.")




def test_DataOrder30_get_subject(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_subject(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_subject was successful.")




def test_DataOrder30_set_subject(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_subject(
                subject=test_set.subject,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_subject failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_subject was successful.")




def test_DataOrder30_get_project_name(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_project_name(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_project_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_project_name was successful.")




def test_DataOrder30_set_request_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_request_id(
                order_id=test_set.order_id,
                request_id=test_set.request_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_request_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_request_id was successful.")




def test_DataOrder30_get_creation_date(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_creation_date(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOrder30_get_creation_date was successful.")




def test_DataOrder30_set_property(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_property(
                order_id=test_set.order_id,
                property_name_english=test_set.property_name_english,
                property_value_english=test_set.property_value_english
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_property failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_property was successful.")




def test_DataOrder30_get_property(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_property(
                order_id=test_set.order_id,
                property_name_english=test_set.property_name_english
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_property failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_property was successful.")




def test_DataOrder30_update(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.update(
                order_in=test_set.order_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_update was successful.")




def test_DataOrder30_delete(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.delete(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_delete was successful.")




def test_DataOrder30_insert(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.insert(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_insert was successful.")




def test_DataOrder30_search(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.search(
                search_filter=test_set.search_filter
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_search failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataOrder30_search was successful.")




def test_DataOrder30_create_link(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.create_link(
                source_order_id=test_set.source_order_id,
                target_id=test_set.target_id,
                project_type=test_set.project_type,
                is_bidirectional=test_set.is_bidirectional,
                memo=test_set.memo
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_create_link failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_create_link was successful.")




def test_DataOrder30_get_currency(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_currency(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_currency was successful.")




def test_DataOrder30_set_reference_number(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_reference_number(
                order_id=test_set.order_id,
                reference=test_set.reference
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_reference_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_reference_number was successful.")




def test_DataOrder30_set_project_category(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_project_category(
                project_category=test_set.project_category,
                system_language_code=test_set.system_language_code,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_project_category failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_project_category was successful.")




def test_DataOrder30_get_project_category(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_project_category(
                system_language_code=test_set.system_language_code,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_project_category failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_project_category was successful.")




def test_DataOrder30_set_customer_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_customer_id(
                customer_id=test_set.customer_id,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_customer_id was successful.")




def test_DataOrder30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.deregister_callback_observer(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_deregister_callback_observer was successful.")




def test_DataOrder30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_register_callback_notify was successful.")




def test_DataOrder30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_deregister_callback_notify was successful.")




def test_DataOrder30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_register_callback_observer was successful.")




def test_DataOrder30_insert_by_template(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.insert_by_template(
                order_in=test_set.order_in,
                template_id=test_set.template_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_insert_by_template failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_insert_by_template was successful.")




def test_DataOrder30_get_reference_number(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_reference_number(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_reference_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_reference_number was successful.")




def test_DataOrder30_get_project_manager_memo(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_project_manager_memo(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_project_manager_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_project_manager_memo was successful.")




def test_DataOrder30_get_master_project_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_master_project_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_master_project_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_master_project_id was successful.")




def test_DataOrder30_set_master_project_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_master_project_id(
                order_id=test_set.order_id,
                master_project_id=test_set.master_project_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_master_project_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_master_project_id was successful.")




def test_DataOrder30_set_project_manager_memo(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_project_manager_memo(
                order_id=test_set.order_id,
                memo=test_set.memo
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_project_manager_memo failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_project_manager_memo was successful.")




def test_DataOrder30_set_delivery_deadline(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_delivery_deadline(
                delivery_deadline=test_set.delivery_deadline,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_delivery_deadline failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_delivery_deadline was successful.")




def test_DataOrder30_get_delivery_deadline(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_delivery_deadline(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_delivery_deadline failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOrder30_get_delivery_deadline was successful.")




def test_DataOrder30_get_order_confirmations(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_confirmations(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_confirmations failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_order_confirmations was successful.")




def test_DataOrder30_set_en15038_requested(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_en15038_requested(
                is_en15038=test_set.is_en15038,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_en15038_requested failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_en15038_requested was successful.")




def test_DataOrder30_get_language_combination(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_language_combination(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_language_combination was successful.")




def test_DataOrder30_get_delivery_comment(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_delivery_comment(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_delivery_comment failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_delivery_comment was successful.")




def test_DataOrder30_get_order_object_list(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_object_list(
                order_id_list=test_set.order_id_list
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_object_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == OrderListResult
    print(f"test_DataOrder30_get_order_object_list was successful.")




def test_DataOrder30_get_projectmanager_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_projectmanager_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_projectmanager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_projectmanager_id was successful.")




def test_DataOrder30_get_order_closing_date(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_closing_date(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_closing_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOrder30_get_order_closing_date was successful.")




def test_DataOrder30_set_projectmanager_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_projectmanager_id(
                resource_id=test_set.resource_id,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_projectmanager_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_projectmanager_id was successful.")




def test_DataOrder30_get_en15038_requested(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_en15038_requested(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_en15038_requested failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataOrder30_get_en15038_requested was successful.")




def test_DataOrder30_get_order_object(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_object(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == OrderResult
    print(f"test_DataOrder30_get_order_object was successful.")




def test_DataOrder30_get_order_object2(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_object2(
                order_number=test_set.order_number
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_object2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == OrderResult
    print(f"test_DataOrder30_get_order_object2 was successful.")




def test_DataOrder30_get_template_list(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_template_list(
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_template_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == TemplateListResult
    print(f"test_DataOrder30_get_template_list was successful.")




def test_DataOrder30_set_customer_contact_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_customer_contact_id(
                customer_contact_id=test_set.customer_contact_id,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_customer_contact_id was successful.")




def test_DataOrder30_get_customer_contact_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_customer_contact_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_customer_contact_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_customer_contact_id was successful.")




def test_DataOrder30_set_project_status(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_project_status(
                order_id=test_set.order_id,
                project_status=test_set.project_status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_project_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_project_status was successful.")




def test_DataOrder30_get_project_status(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_project_status(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_project_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_project_status was successful.")




def test_DataOrder30_get_action_link(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_action_link(
                order_id=test_set.order_id,
                user_id=test_set.user_id,
                action_link_type=test_set.action_link_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_action_link failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_action_link was successful.")




def test_DataOrder30_get_links(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_links(
                order_id=test_set.order_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_links failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == LinkListResult
    print(f"test_DataOrder30_get_links was successful.")




def test_DataOrder30_get_order_date(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_date(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataOrder30_get_order_date was successful.")




def test_DataOrder30_set_order_date(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_order_date(
                order_date=test_set.order_date,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_order_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_order_date was successful.")




def test_DataOrder30_check_en15038(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.check_en15038(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_check_en15038 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == BooleanResult
    print(f"test_DataOrder30_check_en15038 was successful.")




def test_DataOrder30_set_creation_date(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_creation_date(
                creation_date=test_set.creation_date,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_creation_date was successful.")




def test_DataOrder30_get_order_no_for_view(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_no_for_view(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_no_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_order_no_for_view was successful.")




def test_DataOrder30_set_currency_and_rate(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_currency_and_rate(
                order_id=test_set.order_id,
                currency_iso_code=test_set.currency_iso_code,
                rate=test_set.rate
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_currency_and_rate failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_currency_and_rate was successful.")




def test_DataOrder30_get_documents_within_source_folder(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_documents_within_source_folder(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_documents_within_source_folder failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_documents_within_source_folder was successful.")




def test_DataOrder30_get_documents_within_final_folder(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_documents_within_final_folder(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_documents_within_final_folder failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_documents_within_final_folder was successful.")




def test_DataOrder30_create_order_confirmation(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.create_order_confirmation(
                template=test_set.template,
                format_id=test_set.format_id,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_create_order_confirmation failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_create_order_confirmation was successful.")




def test_DataOrder30_insert2(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.insert2(
                order_in=test_set.order_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_insert2 was successful.")




def test_DataOrder30_set_external_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.set_external_id(
                order_id=test_set.order_id,
                external_id=test_set.external_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_set_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataOrder30_set_external_id was successful.")




def test_DataOrder30_get_external_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_external_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_external_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataOrder30_get_external_id was successful.")




def test_DataOrder30_get_order_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_order_id(
                display_no=test_set.display_no
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_order_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_order_id was successful.")




def test_DataOrder30_get_documents_within_reference_folder(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_documents_within_reference_folder(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_documents_within_reference_folder failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_documents_within_reference_folder was successful.")




def test_DataOrder30_get_documents_within_source_folder_by_language(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_documents_within_source_folder_by_language(
                language=test_set.language,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_documents_within_source_folder_by_language failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_documents_within_source_folder_by_language was successful.")




def test_DataOrder30_get_documents_within_reference_folder_by_language(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_documents_within_reference_folder_by_language(
                language=test_set.language,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_documents_within_reference_folder_by_language failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataOrder30_get_documents_within_reference_folder_by_language was successful.")




def test_DataOrder30_get_customer_id(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_customer_id(
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_customer_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_customer_id was successful.")




def test_DataOrder30_get_item_status(pc: PlunetClient, test_set: test_set_DataOrder30):
    try:
        resp = pc.order.get_item_status(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                order_id=test_set.order_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataOrder30_get_item_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataOrder30_get_item_status was successful.")



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
        test_DataOrder30_add_language_combination(pc, test_set)
        test_DataOrder30_get_rate(pc, test_set)
        test_DataOrder30_get_request_id(pc, test_set)
        test_DataOrder30_set_project_name(pc, test_set)
        test_DataOrder30_get_subject(pc, test_set)
        test_DataOrder30_set_subject(pc, test_set)
        test_DataOrder30_get_project_name(pc, test_set)
        test_DataOrder30_set_request_id(pc, test_set)
        test_DataOrder30_get_creation_date(pc, test_set)
        test_DataOrder30_set_property(pc, test_set)
        test_DataOrder30_get_property(pc, test_set)
        test_DataOrder30_update(pc, test_set)
        test_DataOrder30_delete(pc, test_set)
        test_DataOrder30_insert(pc, test_set)
        test_DataOrder30_search(pc, test_set)
        test_DataOrder30_create_link(pc, test_set)
        test_DataOrder30_get_currency(pc, test_set)
        test_DataOrder30_set_reference_number(pc, test_set)
        test_DataOrder30_set_project_category(pc, test_set)
        test_DataOrder30_get_project_category(pc, test_set)
        test_DataOrder30_set_customer_id(pc, test_set)
        test_DataOrder30_deregister_callback_observer(pc, test_set)
        test_DataOrder30_register_callback_notify(pc, test_set)
        test_DataOrder30_deregister_callback_notify(pc, test_set)
        test_DataOrder30_register_callback_observer(pc, test_set)
        test_DataOrder30_insert_by_template(pc, test_set)
        test_DataOrder30_get_reference_number(pc, test_set)
        test_DataOrder30_get_project_manager_memo(pc, test_set)
        test_DataOrder30_get_master_project_id(pc, test_set)
        test_DataOrder30_set_master_project_id(pc, test_set)
        test_DataOrder30_set_project_manager_memo(pc, test_set)
        test_DataOrder30_set_delivery_deadline(pc, test_set)
        test_DataOrder30_get_delivery_deadline(pc, test_set)
        test_DataOrder30_get_order_confirmations(pc, test_set)
        test_DataOrder30_set_en15038_requested(pc, test_set)
        test_DataOrder30_get_language_combination(pc, test_set)
        test_DataOrder30_get_delivery_comment(pc, test_set)
        test_DataOrder30_get_order_object_list(pc, test_set)
        test_DataOrder30_get_projectmanager_id(pc, test_set)
        test_DataOrder30_get_order_closing_date(pc, test_set)
        test_DataOrder30_set_projectmanager_id(pc, test_set)
        test_DataOrder30_get_en15038_requested(pc, test_set)
        test_DataOrder30_get_order_object(pc, test_set)
        test_DataOrder30_get_order_object2(pc, test_set)
        test_DataOrder30_get_template_list(pc, test_set)
        test_DataOrder30_set_customer_contact_id(pc, test_set)
        test_DataOrder30_get_customer_contact_id(pc, test_set)
        test_DataOrder30_set_project_status(pc, test_set)
        test_DataOrder30_get_project_status(pc, test_set)
        test_DataOrder30_get_action_link(pc, test_set)
        test_DataOrder30_get_links(pc, test_set)
        test_DataOrder30_get_order_date(pc, test_set)
        test_DataOrder30_set_order_date(pc, test_set)
        test_DataOrder30_check_en15038(pc, test_set)
        test_DataOrder30_set_creation_date(pc, test_set)
        test_DataOrder30_get_order_no_for_view(pc, test_set)
        test_DataOrder30_set_currency_and_rate(pc, test_set)
        test_DataOrder30_get_documents_within_source_folder(pc, test_set)
        test_DataOrder30_get_documents_within_final_folder(pc, test_set)
        test_DataOrder30_create_order_confirmation(pc, test_set)
        test_DataOrder30_insert2(pc, test_set)
        test_DataOrder30_set_external_id(pc, test_set)
        test_DataOrder30_get_external_id(pc, test_set)
        test_DataOrder30_get_order_id(pc, test_set)
        test_DataOrder30_get_documents_within_reference_folder(pc, test_set)
        test_DataOrder30_get_documents_within_source_folder_by_language(pc, test_set)
        test_DataOrder30_get_documents_within_reference_folder_by_language(pc, test_set)
        test_DataOrder30_get_customer_id(pc, test_set)
        test_DataOrder30_get_item_status(pc, test_set)