from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class Table(SQL):
    """Description"""

    type_name: str = Field("Table", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Table":
            raise ValueError("must be Table")
        return v

    def __setattr__(self, name, value):
        if name in Table._convenience_properties:
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
    # ALIAS: ClassVar[KeywordField] = KeywordField("alias", "alias")
    # """
    # TBC
    # """
    # IS_TEMPORARY: ClassVar[BooleanField] = BooleanField("isTemporary", "isTemporary")
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
    # EXTERNAL_LOCATION: ClassVar[KeywordField] = KeywordField(
    #     "externalLocation", "externalLocation"
    # )
    # """
    # TBC
    # """
    # EXTERNAL_LOCATION_REGION: ClassVar[KeywordField] = KeywordField(
    #     "externalLocationRegion", "externalLocationRegion"
    # )
    # """
    # TBC
    # """
    # EXTERNAL_LOCATION_FORMAT: ClassVar[KeywordField] = KeywordField(
    #     "externalLocationFormat", "externalLocationFormat"
    # )
    # """
    # TBC
    # """
    # IS_PARTITIONED: ClassVar[BooleanField] = BooleanField(
    #     "isPartitioned", "isPartitioned"
    # )
    # """
    # TBC
    # """
    # PARTITION_STRATEGY: ClassVar[KeywordField] = KeywordField(
    #     "partitionStrategy", "partitionStrategy"
    # )
    # """
    # TBC
    # """
    # PARTITION_COUNT: ClassVar[NumericField] = NumericField(
    #     "partitionCount", "partitionCount"
    # )
    # """
    # TBC
    # """
    # PARTITION_LIST: ClassVar[KeywordField] = KeywordField(
    #     "partitionList", "partitionList"
    # )
    # """
    # TBC
    # """

    # COLUMNS: ClassVar[RelationField] = RelationField("columns")
    # """
    # TBC
    # """
    # FACTS: ClassVar[RelationField] = RelationField("facts")
    # """
    # TBC
    # """
    # ATLAN_SCHEMA: ClassVar[RelationField] = RelationField("atlanSchema")
    # """
    # TBC
    # """
    # PARTITIONS: ClassVar[RelationField] = RelationField("partitions")
    # """
    # TBC
    # """
    # QUERIES: ClassVar[RelationField] = RelationField("queries")
    # """
    # TBC
    # """
    # DIMENSIONS: ClassVar[RelationField] = RelationField("dimensions")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "column_count",
        "row_count",
        "size_bytes",
        "alias",
        "is_temporary",
        "is_query_preview",
        "query_preview_config",
        "external_location",
        "external_location_region",
        "external_location_format",
        "is_partitioned",
        "partition_strategy",
        "partition_count",
        "partition_list",
        "columns",
        "facts",
        "atlan_schema",
        "partitions",
        "queries",
        "dimensions",
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
    def external_location(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.external_location

    @external_location.setter
    def external_location(self, external_location: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location = external_location

    @property
    def external_location_region(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.external_location_region
        )

    @external_location_region.setter
    def external_location_region(self, external_location_region: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location_region = external_location_region

    @property
    def external_location_format(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.external_location_format
        )

    @external_location_format.setter
    def external_location_format(self, external_location_format: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.external_location_format = external_location_format

    @property
    def is_partitioned(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_partitioned

    @is_partitioned.setter
    def is_partitioned(self, is_partitioned: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_partitioned = is_partitioned

    @property
    def partition_strategy(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.partition_strategy

    @partition_strategy.setter
    def partition_strategy(self, partition_strategy: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_strategy = partition_strategy

    @property
    def partition_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.partition_count

    @partition_count.setter
    def partition_count(self, partition_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_count = partition_count

    @property
    def partition_list(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.partition_list

    @partition_list.setter
    def partition_list(self, partition_list: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_list = partition_list

    @property
    def columns(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.columns

    @columns.setter
    def columns(self, columns: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.columns = columns

    @property
    def facts(self) -> Optional[list[Table]]:
        return None if self.attributes is None else self.attributes.facts

    @facts.setter
    def facts(self, facts: Optional[list[Table]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.facts = facts

    @property
    def atlan_schema(self) -> Optional[Schema]:
        return None if self.attributes is None else self.attributes.atlan_schema

    @atlan_schema.setter
    def atlan_schema(self, atlan_schema: Optional[Schema]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.atlan_schema = atlan_schema

    @property
    def partitions(self) -> Optional[list[TablePartition]]:
        return None if self.attributes is None else self.attributes.partitions

    @partitions.setter
    def partitions(self, partitions: Optional[list[TablePartition]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partitions = partitions

    @property
    def queries(self) -> Optional[list[Query]]:
        return None if self.attributes is None else self.attributes.queries

    @queries.setter
    def queries(self, queries: Optional[list[Query]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.queries = queries

    @property
    def dimensions(self) -> Optional[list[Table]]:
        return None if self.attributes is None else self.attributes.dimensions

    @dimensions.setter
    def dimensions(self, dimensions: Optional[list[Table]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dimensions = dimensions

    class Attributes(SQL.Attributes):
        column_count: Optional[int] = Field(None, description="", alias="columnCount")
        row_count: Optional[int] = Field(None, description="", alias="rowCount")
        size_bytes: Optional[int] = Field(None, description="", alias="sizeBytes")
        alias: Optional[str] = Field(None, description="", alias="alias")
        is_temporary: Optional[bool] = Field(None, description="", alias="isTemporary")
        is_query_preview: Optional[bool] = Field(
            None, description="", alias="isQueryPreview"
        )
        query_preview_config: Optional[dict[str, str]] = Field(
            None, description="", alias="queryPreviewConfig"
        )
        external_location: Optional[str] = Field(
            None, description="", alias="externalLocation"
        )
        external_location_region: Optional[str] = Field(
            None, description="", alias="externalLocationRegion"
        )
        external_location_format: Optional[str] = Field(
            None, description="", alias="externalLocationFormat"
        )
        is_partitioned: Optional[bool] = Field(
            None, description="", alias="isPartitioned"
        )
        partition_strategy: Optional[str] = Field(
            None, description="", alias="partitionStrategy"
        )
        partition_count: Optional[int] = Field(
            None, description="", alias="partitionCount"
        )
        partition_list: Optional[str] = Field(
            None, description="", alias="partitionList"
        )
        columns: Optional[list[Column]] = Field(
            None, description="", alias="columns"
        )  # relationship
        facts: Optional[list[Table]] = Field(
            None, description="", alias="facts"
        )  # relationship
        atlan_schema: Optional[Schema] = Field(
            None, description="", alias="atlanSchema"
        )  # relationship
        partitions: Optional[list[TablePartition]] = Field(
            None, description="", alias="partitions"
        )  # relationship
        queries: Optional[list[Query]] = Field(
            None, description="", alias="queries"
        )  # relationship
        dimensions: Optional[list[Table]] = Field(
            None, description="", alias="dimensions"
        )  # relationship

    attributes: Table.Attributes = Field(
        default_factory=lambda: Table.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .column import Column  # noqa: E402
from .schema import Schema  # noqa: E402
from .query import Query  # noqa: E402
from .table_partition import TablePartition  # noqa: E402
