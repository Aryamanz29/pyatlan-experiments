from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class View(SQL):
    """Description"""

    type_name: str = Field("View", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "View":
            raise ValueError("must be View")
        return v

    def __setattr__(self, name, value):
        if name in View._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # COLUMN_COUNT: ClassVar[NumericField] = NumericField("columnCount", "columnCount")
    # """
    # TBC
    # """
    # ROW_COUNT: ClassVar[NumericField] = NumericField("rowCount", "rowCount")
    # """
    # TBC
    # """
    # SIZE_BYTES: ClassVar[NumericField] = NumericField("sizeBytes", "sizeBytes")
    # """
    # TBC
    # """
    # IS_QUERY_PREVIEW: ClassVar[BooleanField] = BooleanField(
    #     "isQueryPreview", "isQueryPreview"
    # )
    # """
    # TBC
    # """
    # QUERY_PREVIEW_CONFIG: ClassVar[KeywordField] = KeywordField(
    #     "queryPreviewConfig", "queryPreviewConfig"
    # )
    # """
    # TBC
    # """
    # ALIAS: ClassVar[KeywordField] = KeywordField("alias", "alias")
    # """
    # TBC
    # """
    # IS_TEMPORARY: ClassVar[BooleanField] = BooleanField("isTemporary", "isTemporary")
    # """
    # TBC
    # """
    # DEFINITION: ClassVar[KeywordField] = KeywordField("definition", "definition")
    # """
    # TBC
    # """

    # COLUMNS: ClassVar[RelationField] = RelationField("columns")
    # """
    # TBC
    # """
    # QUERIES: ClassVar[RelationField] = RelationField("queries")
    # """
    # TBC
    # """
    # ATLAN_SCHEMA: ClassVar[RelationField] = RelationField("atlanSchema")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "column_count",
        "row_count",
        "size_bytes",
        "is_query_preview",
        "query_preview_config",
        "alias",
        "is_temporary",
        "definition",
        "columns",
        "queries",
        "atlan_schema",
    ]

    @property
    def column_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.column_count

    @column_count.setter
    def column_count(self, column_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_count = column_count

    @property
    def row_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.row_count

    @row_count.setter
    def row_count(self, row_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.row_count = row_count

    @property
    def size_bytes(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.size_bytes = size_bytes

    @property
    def is_query_preview(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_query_preview

    @is_query_preview.setter
    def is_query_preview(self, is_query_preview: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_query_preview = is_query_preview

    @property
    def query_preview_config(self) -> Optional[dict[str, str]]:
        return None if self.attributes is None else self.attributes.query_preview_config

    @query_preview_config.setter
    def query_preview_config(self, query_preview_config: Optional[dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_preview_config = query_preview_config

    @property
    def alias(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.alias

    @alias.setter
    def alias(self, alias: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.alias = alias

    @property
    def is_temporary(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_temporary

    @is_temporary.setter
    def is_temporary(self, is_temporary: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_temporary = is_temporary

    @property
    def definition(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.definition

    @definition.setter
    def definition(self, definition: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.definition = definition

    @property
    def columns(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.columns

    @columns.setter
    def columns(self, columns: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.columns = columns

    @property
    def queries(self) -> Optional[list[Query]]:
        return None if self.attributes is None else self.attributes.queries

    @queries.setter
    def queries(self, queries: Optional[list[Query]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.queries = queries

    @property
    def atlan_schema(self) -> Optional[Schema]:
        return None if self.attributes is None else self.attributes.atlan_schema

    @atlan_schema.setter
    def atlan_schema(self, atlan_schema: Optional[Schema]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.atlan_schema = atlan_schema

    class Attributes(SQL.Attributes):
        column_count: Optional[int] = Field(None, description="", alias="columnCount")
        row_count: Optional[int] = Field(None, description="", alias="rowCount")
        size_bytes: Optional[int] = Field(None, description="", alias="sizeBytes")
        is_query_preview: Optional[bool] = Field(
            None, description="", alias="isQueryPreview"
        )
        query_preview_config: Optional[dict[str, str]] = Field(
            None, description="", alias="queryPreviewConfig"
        )
        alias: Optional[str] = Field(None, description="", alias="alias")
        is_temporary: Optional[bool] = Field(None, description="", alias="isTemporary")
        definition: Optional[str] = Field(None, description="", alias="definition")
        columns: Optional[list[Column]] = Field(
            None, description="", alias="columns"
        )  # relationship
        queries: Optional[list[Query]] = Field(
            None, description="", alias="queries"
        )  # relationship
        atlan_schema: Optional[Schema] = Field(
            None, description="", alias="atlanSchema"
        )  # relationship

    attributes: View.Attributes = Field(
        default_factory=lambda: View.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .column import Column  # noqa: E402
from .schema import Schema  # noqa: E402
from .query import Query  # noqa: E402
