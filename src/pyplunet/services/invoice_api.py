from __future__ import annotations
from datetime import datetime
from typing import List, Union

from ..models import SearchFilter_Invoice, SelectionEntry_TimeFrame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import PlunetClient

from ..enums import CatType, InvoiceStatusType, ProjectType, TimeFrameRelation_Invoice


class DataOutgoingInvoice30:
    def __init__(self, client: PlunetClient):
        self.__client = client

    def search_for_invoice_ids_by_invoice_date(
        self, from_date: datetime, to_date: datetime, status: InvoiceStatusType
    ) -> List[int]:

        timeframe = SelectionEntry_TimeFrame(
            dateFrom=from_date,
            dateTo=to_date,
            dateRelation=TimeFrameRelation_Invoice.INVOICE_DATE,
        )

        searchfilter_invoice = SearchFilter_Invoice(
            timeFrame=timeframe, invoiceStatus=status
        )
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.search,
            searchfilter_invoice.dict(),
        )

    def get_invoice_object(self, invoice_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.getInvoiceObject,
            invoice_id,
        )

    def get_invoice_company_code(self, invoice_id: int):
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.getCompanyCode, invoice_id
        )

    def get_invoice_receivable_account(self, invoice_id: int) -> str:
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.getReceivableAccount,
            invoice_id,
        )

    def get_invoice_revenue_account(self, invoice_id: int) -> str:
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.getRevenueAccount,
            invoice_id,
        )

    def get_invoice_payment_due_date(self, invoice_id: int) -> datetime:
        return self.__client.make_request(
            self.__client.plunet_server.DataOutgoingInvoice30.getPaymentDueDate,
            invoice_id,
        )
