from __future__ import annotations

from pydantic.v1 import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


def encoders():
    from datetime import datetime

    return {
        datetime: lambda v: int(v.timestamp() * 1000),
    }


class AtlanObject(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
        json_encoders=encoders(),
        validate_assignment=True,
    )
