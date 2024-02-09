from __future__ import annotations

from typing import ClassVar

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .catalog.catalog import Catalog


class DataQuality(Catalog):
    """Description"""

    type_name: str = Field("DataQuality", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "DataQuality":
            raise ValueError("must be DataQuality")
        return v

    def __setattr__(self, name, value):
        if name in DataQuality._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convenience_properties: ClassVar[list[str]] = []
