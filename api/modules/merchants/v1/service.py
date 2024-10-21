from typing import Optional
from fastapi import Depends

from api.modules.merchants.v1.repository import MerchantRepository
from api.modules.merchants.v1.dtos.merchant import MerchantDto
from api.modules.merchants.v1.entities.merchant import Merchant


class MerchantService:
    def __init__(self, merchatn_repository: MerchantRepository = Depends()) -> None:
        self.merchatn_repository = merchatn_repository

    async def read_one(self, parameters: MerchantDto.ReadOne.Parameters) -> Optional[Merchant]:
        return await self.merchatn_repository.read_one(parameters)
