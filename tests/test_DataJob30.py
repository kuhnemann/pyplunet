from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        JobTrackingTimeIN,
        PriceLineListResult,
        PricelistListResult,
        DateResult,
        Result,
        PricelistEntryList,
        PriceLineIN,
        PriceLineResult,
        JobTrackingTimeResult,
        JobIN,
        PricelistResult,
        JobListResult,
        JobTrackingTimeListIN,
        IntegerResult,
        StringArrayResult,
        PriceUnitResult,
        PriceUnitListResult,
        JobResult,
        StringResult,
        JobMetricResult
)


from src.pyplunet.enums import (
        CurrencyType,
        CatType,
        ProjectType,
        EventType
)


class test_set_DataJob30(BaseModel):
    project_type: ProjectType
    job_id: int
    item_id: int
    job_in: JobIN
    enable_null_or_empty_values: bool
    project_id: int
    job_type_abbrevation: str
    comment: str
    resource_id: int
    description: str
    server_authentication_string: str
    server_address: str
    event_type: EventType
    language_code: str
    service: str
    pricelist_id: int
    source_language: str
    target_language: str
    job_tracking_time_in: JobTrackingTimeIN
    job_i_ds: str
    contact_id: int
    job_tracking_time_list_in: JobTrackingTimeListIN
    currency_type: CurrencyType
    target_file_name: str
    price_line_in: PriceLineIN
    user_id: int
    action_link_type: int
    price_list_id: int
    price_unit_id: int
    create_as_first_item: bool
    price_line_id: int
    note: str
    job_type_short: str
    start_date: datetime
    due_date: datetime
    status: int
    file_byte_stream: bytes
    file_path_name: str
    filesize: int
    cat_type: CatType
    analyze_and_copy_result_to_job: bool
    path_or_url: str
    overwrite_existing_price_lines: bool

def get_test_set() -> test_set_DataJob30:
    return test_set_DataJob30(
            project_type= ,
            job_id= ,
            item_id= ,
            job_in= ,
            enable_null_or_empty_values= ,
            project_id= ,
            job_type_abbrevation= ,
            comment= ,
            resource_id= ,
            description= ,
            server_authentication_string= ,
            server_address= ,
            event_type= ,
            language_code= ,
            service= ,
            pricelist_id= ,
            source_language= ,
            target_language= ,
            job_tracking_time_in= ,
            job_i_ds= ,
            contact_id= ,
            job_tracking_time_list_in= ,
            currency_type= ,
            target_file_name= ,
            price_line_in= ,
            user_id= ,
            action_link_type= ,
            price_list_id= ,
            price_unit_id= ,
            create_as_first_item= ,
            price_line_id= ,
            note= ,
            job_type_short= ,
            start_date= ,
            due_date= ,
            status= ,
            file_byte_stream= ,
            file_path_name= ,
            filesize= ,
            cat_type= ,
            analyze_and_copy_result_to_job= ,
            path_or_url= ,
            overwrite_existing_price_lines= 
    )


def test_DataJob30_get_creation_date(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_creation_date(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_creation_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataJob30_get_creation_date was successful.")




def test_DataJob30_set_item_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_item_id(
                project_type=test_set.project_type,
                item_id=test_set.item_id,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_item_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_item_id was successful.")




def test_DataJob30_update(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.update(
                job_in=test_set.job_in,
                enable_null_or_empty_values=test_set.enable_null_or_empty_values
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_update failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_update was successful.")




def test_DataJob30_insert(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.insert(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                job_type_abbrevation=test_set.job_type_abbrevation
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_insert failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_insert was successful.")




def test_DataJob30_get_comment(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_comment(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_comment failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_comment was successful.")




def test_DataJob30_set_comment(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_comment(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                comment=test_set.comment
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_comment failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_comment was successful.")




def test_DataJob30_get_currency(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_currency(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_currency failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_currency was successful.")




def test_DataJob30_set_resource_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_resource_id(
                project_type=test_set.project_type,
                resource_id=test_set.resource_id,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_resource_id was successful.")




def test_DataJob30_get_description(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_description(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_description was successful.")




def test_DataJob30_set_description(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_description(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                description=test_set.description
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_description failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_description was successful.")




def test_DataJob30_deregister_callback_observer(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.deregister_callback_observer(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_deregister_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_deregister_callback_observer was successful.")




def test_DataJob30_register_callback_notify(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.register_callback_notify(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_register_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_register_callback_notify was successful.")




def test_DataJob30_deregister_callback_notify(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.deregister_callback_notify(
                event_type=test_set.event_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_deregister_callback_notify failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_deregister_callback_notify was successful.")




def test_DataJob30_register_callback_observer(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.register_callback_observer(
                server_authentication_string=test_set.server_authentication_string,
                server_address=test_set.server_address,
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_register_callback_observer failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_register_callback_observer was successful.")




def test_DataJob30_get_price_line_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_price_line_list(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_price_line_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataJob30_get_price_line_list was successful.")




def test_DataJob30_get_price_unit_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_price_unit_list(
                language_code=test_set.language_code,
                service=test_set.service
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_price_unit_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitListResult
    print(f"test_DataJob30_get_price_unit_list was successful.")




def test_DataJob30_get_pricelist_entry_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_pricelist_entry_list(
                pricelist_id=test_set.pricelist_id,
                source_language=test_set.source_language,
                target_language=test_set.target_language
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_pricelist_entry_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistEntryList
    print(f"test_DataJob30_get_pricelist_entry_list was successful.")




def test_DataJob30_get_pricelist_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_pricelist_list(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_pricelist_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistListResult
    print(f"test_DataJob30_get_pricelist_list was successful.")




def test_DataJob30_get_contact_person_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_contact_person_id(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_get_contact_person_id was successful.")




def test_DataJob30_get_job_type_long_name(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_type_long_name(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_type_long_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_job_type_long_name was successful.")




def test_DataJob30_add_job_tracking_time(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.add_job_tracking_time(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                job_tracking_time_in=test_set.job_tracking_time_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_add_job_tracking_time failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_add_job_tracking_time was successful.")




def test_DataJob30_set_contact_person_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_contact_person_id(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_contact_person_id was successful.")




def test_DataJob30_get_job_list_for_view(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_list_for_view(
                job_i_ds=test_set.job_i_ds,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_list_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobListResult
    print(f"test_DataJob30_get_job_list_for_view was successful.")




def test_DataJob30_get_resource_contact_person_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_resource_contact_person_id(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_resource_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_get_resource_contact_person_id was successful.")




def test_DataJob30_get_item_independent_jobs(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_item_independent_jobs(
                project_type=test_set.project_type,
                project_id=test_set.project_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_item_independent_jobs failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobListResult
    print(f"test_DataJob30_get_item_independent_jobs was successful.")




def test_DataJob30_get_job_tracking_times_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_tracking_times_list(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_tracking_times_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobTrackingTimeResult
    print(f"test_DataJob30_get_job_tracking_times_list was successful.")




def test_DataJob30_get_job_list_of_item_for_view(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_list_of_item_for_view(
                item_id=test_set.item_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_list_of_item_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobListResult
    print(f"test_DataJob30_get_job_list_of_item_for_view was successful.")




def test_DataJob30_get_job_type_short_name(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_type_short_name(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_type_short_name failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_job_type_short_name was successful.")




def test_DataJob30_set_resource_contact_person_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_resource_contact_person_id(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                contact_id=test_set.contact_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_resource_contact_person_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_resource_contact_person_id was successful.")




def test_DataJob30_add_job_tracking_times_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.add_job_tracking_times_list(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                job_tracking_time_list_in=test_set.job_tracking_time_list_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_add_job_tracking_times_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_add_job_tracking_times_list was successful.")




def test_DataJob30_get_price_line_list_by_currency_type(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_price_line_list_by_currency_type(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                currency_type=test_set.currency_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_price_line_list_by_currency_type failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineListResult
    print(f"test_DataJob30_get_price_line_list_by_currency_type was successful.")




def test_DataJob30_get_download_url_source_data(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_download_url_source_data(
                target_file_name=test_set.target_file_name,
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_download_url_source_data failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_download_url_source_data was successful.")




def test_DataJob30_update_price_line(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.update_price_line(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                price_line_in=test_set.price_line_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_update_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataJob30_update_price_line was successful.")




def test_DataJob30_get_action_link(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_action_link(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                user_id=test_set.user_id,
                action_link_type=test_set.action_link_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_action_link failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_action_link was successful.")




def test_DataJob30_get_pricelist(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_pricelist(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PricelistResult
    print(f"test_DataJob30_get_pricelist was successful.")




def test_DataJob30_set_pricelist(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_pricelist(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                price_list_id=test_set.price_list_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_pricelist failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_pricelist was successful.")




def test_DataJob30_get_services_list(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_services_list(
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_services_list failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringArrayResult
    print(f"test_DataJob30_get_services_list was successful.")




def test_DataJob30_get_price_unit(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_price_unit(
                price_unit_id=test_set.price_unit_id,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_price_unit failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceUnitResult
    print(f"test_DataJob30_get_price_unit was successful.")




def test_DataJob30_insert_price_line(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.insert_price_line(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                price_line_in=test_set.price_line_in,
                create_as_first_item=test_set.create_as_first_item
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_insert_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == PriceLineResult
    print(f"test_DataJob30_insert_price_line was successful.")




def test_DataJob30_delete_price_line(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.delete_price_line(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                price_line_id=test_set.price_line_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_delete_price_line failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_delete_price_line was successful.")




def test_DataJob30_get_delivery_date(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_delivery_date(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_delivery_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataJob30_get_delivery_date was successful.")




def test_DataJob30_set_delivery_note(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_delivery_note(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                note=test_set.note
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_delivery_note failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_delivery_note was successful.")




def test_DataJob30_get_payable_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_payable_id(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_payable_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_get_payable_id was successful.")




def test_DataJob30_get_job_number(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_number(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_number failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_job_number was successful.")




def test_DataJob30_run_automatic_job(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.run_automatic_job(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_run_automatic_job failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_run_automatic_job was successful.")




def test_DataJob30_insert3(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.insert3(
                job_in=test_set.job_in,
                job_type_short=test_set.job_type_short
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_insert3 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_insert3 was successful.")




def test_DataJob30_delete_job(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.delete_job(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_delete_job failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_delete_job was successful.")




def test_DataJob30_set_price_liste_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_price_liste_id(
                project_type=test_set.project_type,
                price_list_id=test_set.price_list_id,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_price_liste_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_price_liste_id was successful.")




def test_DataJob30_assign_job(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.assign_job(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                resource_id=test_set.resource_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_assign_job failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_assign_job was successful.")




def test_DataJob30_set_start_date(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_start_date(
                project_type=test_set.project_type,
                start_date=test_set.start_date,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_start_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_start_date was successful.")




def test_DataJob30_set_due_date(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_due_date(
                project_type=test_set.project_type,
                due_date=test_set.due_date,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_due_date was successful.")




def test_DataJob30_get_job_for_view(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_for_view(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_for_view failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobResult
    print(f"test_DataJob30_get_job_for_view was successful.")




def test_DataJob30_set_job_status(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_job_status(
                project_type=test_set.project_type,
                job_id=test_set.job_id,
                status=test_set.status
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_job_status failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_job_status was successful.")




def test_DataJob30_get_delivery_note(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_delivery_note(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_delivery_note failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == StringResult
    print(f"test_DataJob30_get_delivery_note was successful.")




def test_DataJob30_get_due_date(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_due_date(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_due_date failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == DateResult
    print(f"test_DataJob30_get_due_date was successful.")




def test_DataJob30_get_job_metrics(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_job_metrics(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                language_code=test_set.language_code
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_job_metrics failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobMetricResult
    print(f"test_DataJob30_get_job_metrics was successful.")




def test_DataJob30_insert2(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.insert2(
                project_id=test_set.project_id,
                project_type=test_set.project_type,
                job_type_abbrevation=test_set.job_type_abbrevation,
                item_id=test_set.item_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_insert2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_insert2 was successful.")




def test_DataJob30_get_resource_id(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.get_resource_id(
                project_type=test_set.project_type,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_get_resource_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJob30_get_resource_id was successful.")




def test_DataJob30_set_cat_report2(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_cat_report2(
                file_byte_stream=test_set.file_byte_stream,
                file_path_name=test_set.file_path_name,
                filesize=test_set.filesize,
                cat_type=test_set.cat_type,
                project_type=test_set.project_type,
                analyze_and_copy_result_to_job=test_set.analyze_and_copy_result_to_job,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_cat_report2 failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_cat_report2 was successful.")




def test_DataJob30_set_cat_report(pc: PlunetClient, test_set: test_set_DataJob30):
    try:
        resp = pc.job.set_cat_report(
                path_or_url=test_set.path_or_url,
                overwrite_existing_price_lines=test_set.overwrite_existing_price_lines,
                cat_type=test_set.cat_type,
                project_type=test_set.project_type,
                analyze_and_copy_result_to_job=test_set.analyze_and_copy_result_to_job,
                job_id=test_set.job_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJob30_set_cat_report failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJob30_set_cat_report was successful.")



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
        test_DataJob30_get_creation_date(pc, test_set)
        test_DataJob30_set_item_id(pc, test_set)
        test_DataJob30_update(pc, test_set)
        test_DataJob30_insert(pc, test_set)
        test_DataJob30_get_comment(pc, test_set)
        test_DataJob30_set_comment(pc, test_set)
        test_DataJob30_get_currency(pc, test_set)
        test_DataJob30_set_resource_id(pc, test_set)
        test_DataJob30_get_description(pc, test_set)
        test_DataJob30_set_description(pc, test_set)
        test_DataJob30_deregister_callback_observer(pc, test_set)
        test_DataJob30_register_callback_notify(pc, test_set)
        test_DataJob30_deregister_callback_notify(pc, test_set)
        test_DataJob30_register_callback_observer(pc, test_set)
        test_DataJob30_get_price_line_list(pc, test_set)
        test_DataJob30_get_price_unit_list(pc, test_set)
        test_DataJob30_get_pricelist_entry_list(pc, test_set)
        test_DataJob30_get_pricelist_list(pc, test_set)
        test_DataJob30_get_contact_person_id(pc, test_set)
        test_DataJob30_get_job_type_long_name(pc, test_set)
        test_DataJob30_add_job_tracking_time(pc, test_set)
        test_DataJob30_set_contact_person_id(pc, test_set)
        test_DataJob30_get_job_list_for_view(pc, test_set)
        test_DataJob30_get_resource_contact_person_id(pc, test_set)
        test_DataJob30_get_item_independent_jobs(pc, test_set)
        test_DataJob30_get_job_tracking_times_list(pc, test_set)
        test_DataJob30_get_job_list_of_item_for_view(pc, test_set)
        test_DataJob30_get_job_type_short_name(pc, test_set)
        test_DataJob30_set_resource_contact_person_id(pc, test_set)
        test_DataJob30_add_job_tracking_times_list(pc, test_set)
        test_DataJob30_get_price_line_list_by_currency_type(pc, test_set)
        test_DataJob30_get_download_url_source_data(pc, test_set)
        test_DataJob30_update_price_line(pc, test_set)
        test_DataJob30_get_action_link(pc, test_set)
        test_DataJob30_get_pricelist(pc, test_set)
        test_DataJob30_set_pricelist(pc, test_set)
        test_DataJob30_get_services_list(pc, test_set)
        test_DataJob30_get_price_unit(pc, test_set)
        test_DataJob30_insert_price_line(pc, test_set)
        test_DataJob30_delete_price_line(pc, test_set)
        test_DataJob30_get_delivery_date(pc, test_set)
        test_DataJob30_set_delivery_note(pc, test_set)
        test_DataJob30_get_payable_id(pc, test_set)
        test_DataJob30_get_job_number(pc, test_set)
        test_DataJob30_run_automatic_job(pc, test_set)
        test_DataJob30_insert3(pc, test_set)
        test_DataJob30_delete_job(pc, test_set)
        test_DataJob30_set_price_liste_id(pc, test_set)
        test_DataJob30_assign_job(pc, test_set)
        test_DataJob30_set_start_date(pc, test_set)
        test_DataJob30_set_due_date(pc, test_set)
        test_DataJob30_get_job_for_view(pc, test_set)
        test_DataJob30_set_job_status(pc, test_set)
        test_DataJob30_get_delivery_note(pc, test_set)
        test_DataJob30_get_due_date(pc, test_set)
        test_DataJob30_get_job_metrics(pc, test_set)
        test_DataJob30_insert2(pc, test_set)
        test_DataJob30_get_resource_id(pc, test_set)
        test_DataJob30_set_cat_report2(pc, test_set)
        test_DataJob30_set_cat_report(pc, test_set)