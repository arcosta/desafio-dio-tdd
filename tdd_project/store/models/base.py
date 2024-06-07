from bson import Decimal128
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, UUID4, model_serializer
from typing import Any
import uuid


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @model_serializer
    def set_mode(self) -> dict[str, Any]:
        for key, value in self.__dict__.items():
            if isinstance(value, Decimal):
                self.__dict__[key] = Decimal128(str(value))

        return self.__dict__
