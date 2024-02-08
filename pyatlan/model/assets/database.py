from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class Database(SQL):
    """Description"""

    type_name: str = Field("Database", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Database":
            raise ValueError("must be Database")
        return v

    def __setattr__(self, name, value):
        if name in Database._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SCHEMA_COUNT: ClassVar[NumericField] = NumericField("schemaCount", "schemaCount")
    # """
    # TBC
    # """

    # SCHEMAS: ClassVar[RelationField] = RelationField("schemas")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "schema_count",
        "schemas",
    ]

    @property
    def schema_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.schema_count

    @schema_count.setter
    def schema_count(self, schema_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.schema_count = schema_count

    @property
    def schemas(self) -> Optional[list[Schema]]:
        return None if self.attributes is None else self.attributes.schemas

    @schemas.setter
    def schemas(self, schemas: Optional[list[Schema]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.schemas = schemas

    class Attributes(SQL.Attributes):
        schema_count: Optional[int] = Field(None, description="", alias="schemaCount")
        schemas: Optional[list[Schema]] = Field(
            None, description="", alias="schemas"
        )  # relationship

    attributes: Database.Attributes = Field(
        default_factory=lambda: Database.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .schema import Schema  # noqa: E402
