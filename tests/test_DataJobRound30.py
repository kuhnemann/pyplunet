from __future__ import annotations
from tests import test_client_factory
from datetime import datetime
from pydantic import BaseModel
from src.pyplunet import PlunetClient
from src.pyplunet.exceptions import PlunetAPIError


from src.pyplunet.models import (
        Result,
        JobRoundSearchcriteriaResult,
        IntegerResult,
        JobRoundRankingMethodList,
        JobRoundSearchCriteriaIN,
        IntegerArrayResult,
        JobRoundRankingMethodListResult,
        JobRoundIN,
        JobRoundResult
)


from src.pyplunet.enums import (
        ProjectType
)


class test_set_DataJobRound30(BaseModel):
    round_id: int
    resource_id: int
    resource_contact_id: int
    job_round_search_criteria_in: JobRoundSearchCriteriaIN
    job_round_ranking_method_list: JobRoundRankingMethodList
    job_id: int
    project_type: ProjectType
    round_in: JobRoundIN
    job_round_in: JobRoundIN

def get_test_set() -> test_set_DataJobRound30:
    return test_set_DataJobRound30(
            round_id= ,
            resource_id= ,
            resource_contact_id= ,
            job_round_search_criteria_in= ,
            job_round_ranking_method_list= ,
            job_id= ,
            project_type= ,
            round_in= ,
            job_round_in= 
    )


def test_DataJobRound30_delete(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.delete(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_delete failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_delete was successful.")




def test_DataJobRound30_get_ranking_methods(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_ranking_methods(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_ranking_methods failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobRoundRankingMethodListResult
    print(f"test_DataJobRound30_get_ranking_methods was successful.")




def test_DataJobRound30_get_resources_for_round(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_resources_for_round(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_resources_for_round failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataJobRound30_get_resources_for_round was successful.")




def test_DataJobRound30_set_resource_for_review(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.set_resource_for_review(
                resource_id=test_set.resource_id,
                resource_contact_id=test_set.resource_contact_id,
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_set_resource_for_review failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_set_resource_for_review was successful.")




def test_DataJobRound30_assign_resource_in_review(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.assign_resource_in_review(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_assign_resource_in_review failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_assign_resource_in_review was successful.")




def test_DataJobRound30_get_search_criteria(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_search_criteria(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_search_criteria failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobRoundSearchcriteriaResult
    print(f"test_DataJobRound30_get_search_criteria was successful.")




def test_DataJobRound30_set_search_criteria(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.set_search_criteria(
                job_round_search_criteria_in=test_set.job_round_search_criteria_in,
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_set_search_criteria failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_set_search_criteria was successful.")




def test_DataJobRound30_set_ranking_methods(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.set_ranking_methods(
                job_round_ranking_method_list=test_set.job_round_ranking_method_list,
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_set_ranking_methods failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_set_ranking_methods was successful.")




def test_DataJobRound30_get_assigned_round_id(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_assigned_round_id(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_assigned_round_id failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJobRound30_get_assigned_round_id was successful.")




def test_DataJobRound30_get_round_object(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_round_object(
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_round_object failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == JobRoundResult
    print(f"test_DataJobRound30_get_round_object was successful.")




def test_DataJobRound30_assign_resource(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.assign_resource(
                resource_id=test_set.resource_id,
                resource_contact_id=test_set.resource_contact_id,
                round_id=test_set.round_id
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_assign_resource failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_assign_resource was successful.")




def test_DataJobRound30_update_round(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.update_round(
                round_in=test_set.round_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_update_round failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == Result
    print(f"test_DataJobRound30_update_round was successful.")




def test_DataJobRound30_add_round(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.add_round(
                job_id=test_set.job_id,
                project_type=test_set.project_type,
                job_round_in=test_set.job_round_in
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_add_round failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerResult
    print(f"test_DataJobRound30_add_round was successful.")




def test_DataJobRound30_get_all_round_i_ds(pc: PlunetClient, test_set: test_set_DataJobRound30):
    try:
        resp = pc.job_round.get_all_round_i_ds(
                job_id=test_set.job_id,
                project_type=test_set.project_type
        )
    except PlunetAPIError as e:
        error = e
        print(f"test_DataJobRound30_get_all_round_i_ds failed with error {type(e)} that was suppressed since it is a valid PlunetAPIError")
        return
    assert type(resp) == IntegerArrayResult
    print(f"test_DataJobRound30_get_all_round_i_ds was successful.")



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
        test_DataJobRound30_delete(pc, test_set)
        test_DataJobRound30_get_ranking_methods(pc, test_set)
        test_DataJobRound30_get_resources_for_round(pc, test_set)
        test_DataJobRound30_set_resource_for_review(pc, test_set)
        test_DataJobRound30_assign_resource_in_review(pc, test_set)
        test_DataJobRound30_get_search_criteria(pc, test_set)
        test_DataJobRound30_set_search_criteria(pc, test_set)
        test_DataJobRound30_set_ranking_methods(pc, test_set)
        test_DataJobRound30_get_assigned_round_id(pc, test_set)
        test_DataJobRound30_get_round_object(pc, test_set)
        test_DataJobRound30_assign_resource(pc, test_set)
        test_DataJobRound30_update_round(pc, test_set)
        test_DataJobRound30_add_round(pc, test_set)
        test_DataJobRound30_get_all_round_i_ds(pc, test_set)