from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        IntegerResult,
        ItemListResult,
        PricelistEntryList,
        PriceLineIN,
        PriceLineResult,
        ItemIN,
        PriceLineListResult,
        PricelistListResult,
        PricelistResult,
        DateResult,
        StringArrayResult,
        IntegerArrayResult,
        PriceUnitListResult,
        PriceUnitResult,
        DoubleResult,
        ItemResult,
        StringResult
)


from src.pyplunet.enums import (
        CurrencyType,
        ProjectType,
        DocumentStatus,
        EventType,
        CatType
)


class test_set_DataItem30(BaseModel):
    project_id: int
    project_type: ProjectType
    status: int
    source_language: str
    target_language: str
    item_id: int
    document_status: DocumentStatus
    language_combination_id: int
    item_in: ItemIN
    enable_null_or_empty_values: bool
    comment: str
    server_authentication_string: str
    server_address: str
    event_type: EventType
    workflow_id: int
    currency_type: CurrencyType
    language_code: str
    service: str
    current_type: CurrencyType
    pricelist_id: int
    resource_id: int
    deadline: datetime
    description: str
    reference: str
    price_line_in: PriceLineIN
    price_list_id: int
    price_unit_id: int
    create_as_first_item: bool
    price_line_id: int
    delivery_date: datetime
    file_byte_stream: bytes
    file_path_name: str
    filesize: int
    overwrite_existing_price_lines: bool
    cat_type: CatType
    copy_results_to_item: bool
    total_price: float
    path_or_url: str

def get_test_set() -> test_set_DataItem30:
    return test_set_DataItem30(
            project_id= ,
            project_type= ,
            status= ,
            source_language= ,
            target_language= ,
            item_id= ,
            document_status= ,
            language_combination_id= ,
            item_in= ,
            enable_null_or_empty_values= ,
            comment= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            workflow_id= ,
            currency_type= ,
            language_code= ,
            service= ,
            current_type= ,
            pricelist_id= ,
            resource_id= ,
            deadline= ,
            description= ,
            reference= ,
            price_line_in= ,
            price_list_id= ,
            price_unit_id= ,
            create_as_first_item= ,
            price_line_id= ,
            delivery_date= ,
            file_byte_stream= ,
            file_path_name= ,
            filesize= ,
            overwrite_existing_price_lines= ,
            cat_type= ,
            copy_results_to_item= ,
            total_price= ,
            path_or_url= 
    )


def test_DataItem30_get_items_by_status2(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status2(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                status=test_set.status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status2 was successful.")




def test_DataItem30_add_language_combination(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.add_language_combination(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                project_type=test_set.project_type,
                project_id=test_set.project_id,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_add_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_add_language_combination was successful.")




def test_DataItem30_get_items_by_status3(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status3(
                project_type=test_set.project_type,
                status=test_set.status,
                document_status=test_set.document_status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status3 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status3 was successful.")




def test_DataItem30_get_source_language(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_source_language(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_source_language failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataItem30_get_source_language was successful.")




def test_DataItem30_seek_language_combination(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.seek_language_combination(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                project_type=test_set.project_type,
                project_id=test_set.project_id,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_seek_language_combination failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_seek_language_combination was successful.")




def test_DataItem30_get_jobs_with_status(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_jobs_with_status(
                status=test_set.status,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_jobs_with_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataItem30_get_jobs_with_status was successful.")




def test_DataItem30_get_all_item_objects(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_all_item_objects(
                project_id=test_set.project_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_all_item_objects failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_all_item_objects was successful.")




def test_DataItem30_get_target_language(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_target_language(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_target_language failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataItem30_get_target_language was successful.")




def test_DataItem30_set_language_combination_id(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_language_combination_id(
                language_combination_id=test_set.language_combination_id,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_language_combination_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_language_combination_id was successful.")




def test_DataItem30_get_items_by_status1(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status1(
                project_type=test_set.project_type,
                status=test_set.status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status1 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status1 was successful.")




def test_DataItem30_get_items_by_status4(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status4(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                status=test_set.status,
                document_status=test_set.document_status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status4 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status4 was successful.")




def test_DataItem30_update(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.update(
                item_in=test_set.item_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_update was successful.")




def test_DataItem30_delete(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.delete(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_delete was successful.")




def test_DataItem30_insert(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.insert(
                project_id=test_set.project_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_insert was successful.")




def test_DataItem30_get_comment(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_comment(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_comment failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataItem30_get_comment was successful.")




def test_DataItem30_set_comment(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_comment(
                comment=test_set.comment,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_comment failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_comment was successful.")




def test_DataItem30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.deregister_callback_observer(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_deregister_callback_observer was successful.")




def test_DataItem30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_register_callback_notify was successful.")




def test_DataItem30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_deregister_callback_notify was successful.")




def test_DataItem30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_register_callback_observer was successful.")




def test_DataItem30_add_language_combination2(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.add_language_combination2(
                source_language=test_set.source_language,
                target_language=test_set.target_language,
                project_type=test_set.project_type,
                project_id=test_set.project_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_add_language_combination2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_add_language_combination2 was successful.")




def test_DataItem30_copy_jobs_from_workflow(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.copy_jobs_from_workflow(
                workflow_id=test_set.workflow_id,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_copy_jobs_from_workflow failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_copy_jobs_from_workflow was successful.")




def test_DataItem30_get_price_line_list(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_price_line_list(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_price_line_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataItem30_get_price_line_list was successful.")




def test_DataItem30_get_language_independent_item_object(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_language_independent_item_object(
                project_type=test_set.project_type,
                project_id=test_set.project_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_language_independent_item_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemResult
    print(f"test_DataItem30_get_language_independent_item_object was successful.")




def test_DataItem30_get_price_unit_list(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_price_unit_list(
                language_code=test_set.language_code,
                service=test_set.service
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_price_unit_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitListResult
    print(f"test_DataItem30_get_price_unit_list was successful.")




def test_DataItem30_insert_language_independent_item(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.insert_language_independent_item(
                item_in=test_set.item_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_insert_language_independent_item failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_insert_language_independent_item was successful.")




def test_DataItem30_get_items_by_status3_by_currency_type(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status3_by_currency_type(
                project_type=test_set.project_type,
                status=test_set.status,
                document_status=test_set.document_status,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status3_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status3_by_currency_type was successful.")




def test_DataItem30_get_total_price_by_currency_type(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_total_price_by_currency_type(
                project_type=test_set.project_type,
                item_id=test_set.item_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_total_price_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataItem30_get_total_price_by_currency_type was successful.")




def test_DataItem30_get_items_by_status4_by_currency_type(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_items_by_status4_by_currency_type(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                status=test_set.status,
                document_status=test_set.document_status,
                current_type=test_set.current_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_items_by_status4_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_items_by_status4_by_currency_type was successful.")




def test_DataItem30_get_default_contact_person(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_default_contact_person(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_default_contact_person failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_default_contact_person was successful.")




def test_DataItem30_get_all_item_objects_by_currency(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_all_item_objects_by_currency(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_all_item_objects_by_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemListResult
    print(f"test_DataItem30_get_all_item_objects_by_currency was successful.")




def test_DataItem30_get_pricelist_entry_list(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_pricelist_entry_list(
                pricelist_id=test_set.pricelist_id,
                source_language=test_set.source_language,
                target_language=test_set.target_language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_pricelist_entry_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistEntryList
    print(f"test_DataItem30_get_pricelist_entry_list was successful.")




def test_DataItem30_get_item_object_by_currency_type(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_item_object_by_currency_type(
                project_type=test_set.project_type,
                item_id=test_set.item_id,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_item_object_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemResult
    print(f"test_DataItem30_get_item_object_by_currency_type was successful.")




def test_DataItem30_get_pricelist_list(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_pricelist_list(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_pricelist_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistListResult
    print(f"test_DataItem30_get_pricelist_list was successful.")




def test_DataItem30_get_price_line_list_by_currency(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_price_line_list_by_currency(
                item_id=test_set.item_id,
                project_type=test_set.project_type,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_price_line_list_by_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataItem30_get_price_line_list_by_currency was successful.")




def test_DataItem30_set_default_contact_person(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_default_contact_person(
                project_type=test_set.project_type,
                item_id=test_set.item_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_default_contact_person failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_default_contact_person was successful.")




def test_DataItem30_get_status(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_status(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_status was successful.")




def test_DataItem30_set_status(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_status(
                status=test_set.status,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_status was successful.")




def test_DataItem30_get_brief_description(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_brief_description(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataItem30_get_brief_description was successful.")




def test_DataItem30_set_document_status(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_document_status(
                document_status=test_set.document_status,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_document_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_document_status was successful.")




def test_DataItem30_set_delivery_deadline(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_delivery_deadline(
                deadline=test_set.deadline,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_delivery_deadline failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_delivery_deadline was successful.")




def test_DataItem30_set_brief_description(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_brief_description(
                description=test_set.description,
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_brief_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_brief_description was successful.")




def test_DataItem30_get_document_status(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_document_status(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_document_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_document_status was successful.")




def test_DataItem30_get_delivery_deadline(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_delivery_deadline(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_delivery_deadline failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataItem30_get_delivery_deadline was successful.")




def test_DataItem30_get_best_pricelist(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_best_pricelist(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_best_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_best_pricelist was successful.")




def test_DataItem30_set_item_reference(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_item_reference(
                project_type=test_set.project_type,
                item_id=test_set.item_id,
                reference=test_set.reference
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_item_reference failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_item_reference was successful.")




def test_DataItem30_update_price_line(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.update_price_line(
                item_id=test_set.item_id,
                project_type=test_set.project_type,
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_update_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataItem30_update_price_line was successful.")




def test_DataItem30_get_pricelist(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_pricelist(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistResult
    print(f"test_DataItem30_get_pricelist was successful.")




def test_DataItem30_set_pricelist(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_pricelist(
                item_id=test_set.item_id,
                project_type=test_set.project_type,
                price_list_id=test_set.price_list_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_pricelist was successful.")




def test_DataItem30_get_item_reference(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_item_reference(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_item_reference failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataItem30_get_item_reference was successful.")




def test_DataItem30_get_services_list(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_services_list(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_services_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataItem30_get_services_list was successful.")




def test_DataItem30_get_price_unit(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_price_unit(
                price_unit_id=test_set.price_unit_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_price_unit failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitResult
    print(f"test_DataItem30_get_price_unit was successful.")




def test_DataItem30_get_by_language(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_by_language(
                project_type=test_set.project_type,
                project_id=test_set.project_id,
                source_language=test_set.source_language,
                target_language=test_set.target_language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_by_language failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_by_language was successful.")




def test_DataItem30_insert_price_line(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.insert_price_line(
                item_id=test_set.item_id,
                project_type=test_set.project_type,
                price_line_in=test_set.price_line_in,
                create_as_first_item=test_set.create_as_first_item
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_insert_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataItem30_insert_price_line was successful.")




def test_DataItem30_delete_price_line(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.delete_price_line(
                item_id=test_set.item_id,
                project_type=test_set.project_type,
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_delete_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_delete_price_line was successful.")




def test_DataItem30_set_delivery_date(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_delivery_date(
                delivery_date=test_set.delivery_date,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_delivery_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_delivery_date was successful.")




def test_DataItem30_get_delivery_date(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_delivery_date(
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_delivery_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataItem30_get_delivery_date was successful.")




def test_DataItem30_insert2(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.insert2(
                item_in=test_set.item_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_insert2 was successful.")




def test_DataItem30_get_order_id(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_order_id(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_order_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_order_id was successful.")




def test_DataItem30_set_cat_report2(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_cat_report2(
                file_byte_stream=test_set.file_byte_stream,
                file_path_name=test_set.file_path_name,
                filesize=test_set.filesize,
                overwrite_existing_price_lines=test_set.overwrite_existing_price_lines,
                cat_type=test_set.cat_type,
                project_type=test_set.project_type,
                copy_results_to_item=test_set.copy_results_to_item,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_cat_report2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_cat_report2 was successful.")




def test_DataItem30_get_invoice_id(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_invoice_id(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_invoice_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataItem30_get_invoice_id was successful.")




def test_DataItem30_set_total_price(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_total_price(
                project_type=test_set.project_type,
                total_price=test_set.total_price,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_total_price failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_total_price was successful.")




def test_DataItem30_set_cat_report(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.set_cat_report(
                path_or_url=test_set.path_or_url,
                overwrite_existing_price_lines=test_set.overwrite_existing_price_lines,
                cat_type=test_set.cat_type,
                project_type=test_set.project_type,
                copy_results_to_item=test_set.copy_results_to_item,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_set_cat_report failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataItem30_set_cat_report was successful.")




def test_DataItem30_get_item_object(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_item_object(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_item_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == ItemResult
    print(f"test_DataItem30_get_item_object was successful.")




def test_DataItem30_get_jobs(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_jobs(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_jobs failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataItem30_get_jobs was successful.")




def test_DataItem30_get_total_price(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_total_price(
                project_type=test_set.project_type,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_total_price failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DoubleResult
    print(f"test_DataItem30_get_total_price was successful.")




def test_DataItem30_get_all_items(pc: PlunetClient, test_set: test_set_DataItem30):
    try:
        resp = pc.item.get_all_items(
                project_type=test_set.project_type,
                project_id=test_set.project_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataItem30_get_all_items failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataItem30_get_all_items was successful.")



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
        test_DataItem30_get_items_by_status2(pc, test_set)
        test_DataItem30_add_language_combination(pc, test_set)
        test_DataItem30_get_items_by_status3(pc, test_set)
        test_DataItem30_get_source_language(pc, test_set)
        test_DataItem30_seek_language_combination(pc, test_set)
        test_DataItem30_get_jobs_with_status(pc, test_set)
        test_DataItem30_get_all_item_objects(pc, test_set)
        test_DataItem30_get_target_language(pc, test_set)
        test_DataItem30_set_language_combination_id(pc, test_set)
        test_DataItem30_get_items_by_status1(pc, test_set)
        test_DataItem30_get_items_by_status4(pc, test_set)
        test_DataItem30_update(pc, test_set)
        test_DataItem30_delete(pc, test_set)
        test_DataItem30_insert(pc, test_set)
        test_DataItem30_get_comment(pc, test_set)
        test_DataItem30_set_comment(pc, test_set)
        test_DataItem30_deregister_callback_observer(pc, test_set)
        test_DataItem30_register_callback_notify(pc, test_set)
        test_DataItem30_deregister_callback_notify(pc, test_set)
        test_DataItem30_register_callback_observer(pc, test_set)
        test_DataItem30_add_language_combination2(pc, test_set)
        test_DataItem30_copy_jobs_from_workflow(pc, test_set)
        test_DataItem30_get_price_line_list(pc, test_set)
        test_DataItem30_get_language_independent_item_object(pc, test_set)
        test_DataItem30_get_price_unit_list(pc, test_set)
        test_DataItem30_insert_language_independent_item(pc, test_set)
        test_DataItem30_get_items_by_status3_by_currency_type(pc, test_set)
        test_DataItem30_get_total_price_by_currency_type(pc, test_set)
        test_DataItem30_get_items_by_status4_by_currency_type(pc, test_set)
        test_DataItem30_get_default_contact_person(pc, test_set)
        test_DataItem30_get_all_item_objects_by_currency(pc, test_set)
        test_DataItem30_get_pricelist_entry_list(pc, test_set)
        test_DataItem30_get_item_object_by_currency_type(pc, test_set)
        test_DataItem30_get_pricelist_list(pc, test_set)
        test_DataItem30_get_price_line_list_by_currency(pc, test_set)
        test_DataItem30_set_default_contact_person(pc, test_set)
        test_DataItem30_get_status(pc, test_set)
        test_DataItem30_set_status(pc, test_set)
        test_DataItem30_get_brief_description(pc, test_set)
        test_DataItem30_set_document_status(pc, test_set)
        test_DataItem30_set_delivery_deadline(pc, test_set)
        test_DataItem30_set_brief_description(pc, test_set)
        test_DataItem30_get_document_status(pc, test_set)
        test_DataItem30_get_delivery_deadline(pc, test_set)
        test_DataItem30_get_best_pricelist(pc, test_set)
        test_DataItem30_set_item_reference(pc, test_set)
        test_DataItem30_update_price_line(pc, test_set)
        test_DataItem30_get_pricelist(pc, test_set)
        test_DataItem30_set_pricelist(pc, test_set)
        test_DataItem30_get_item_reference(pc, test_set)
        test_DataItem30_get_services_list(pc, test_set)
        test_DataItem30_get_price_unit(pc, test_set)
        test_DataItem30_get_by_language(pc, test_set)
        test_DataItem30_insert_price_line(pc, test_set)
        test_DataItem30_delete_price_line(pc, test_set)
        test_DataItem30_set_delivery_date(pc, test_set)
        test_DataItem30_get_delivery_date(pc, test_set)
        test_DataItem30_insert2(pc, test_set)
        test_DataItem30_get_order_id(pc, test_set)
        test_DataItem30_set_cat_report2(pc, test_set)
        test_DataItem30_get_invoice_id(pc, test_set)
        test_DataItem30_set_total_price(pc, test_set)
        test_DataItem30_set_cat_report(pc, test_set)
        test_DataItem30_get_item_object(pc, test_set)
        test_DataItem30_get_jobs(pc, test_set)
        test_DataItem30_get_total_price(pc, test_set)
        test_DataItem30_get_all_items(pc, test_set)