from __future__ import annotations

from datetime import datetime
from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class Column(SQL):
    """Description"""

    type_name: str = Field("Column", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Column":
            raise ValueError("must be Column")
        return v

    def __setattr__(self, name, value):
        if name in Column._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # DATA_TYPE: ClassVar[KeywordTextField] = KeywordTextField(
    #     "dataType", "dataType", "dataType.text"
    # )
    # """
    # TBC
    # """
    # SUB_DATA_TYPE: ClassVar[KeywordField] = KeywordField("subDataType", "subDataType")
    # """
    # TBC
    # """
    # RAW_DATA_TYPE_DEFINITION: ClassVar[KeywordField] = KeywordField(
    #     "rawDataTypeDefinition", "rawDataTypeDefinition"
    # )
    # """
    # TBC
    # """
    # ORDER: ClassVar[NumericField] = NumericField("order", "order")
    # """
    # TBC
    # """
    # NESTED_COLUMN_COUNT: ClassVar[NumericField] = NumericField(
    #     "nestedColumnCount", "nestedColumnCount"
    # )
    # """
    # TBC
    # """
    # IS_PARTITION: ClassVar[BooleanField] = BooleanField("isPartition", "isPartition")
    # """
    # TBC
    # """
    # PARTITION_ORDER: ClassVar[NumericField] = NumericField(
    #     "partitionOrder", "partitionOrder"
    # )
    # """
    # TBC
    # """
    # IS_CLUSTERED: ClassVar[BooleanField] = BooleanField("isClustered", "isClustered")
    # """
    # TBC
    # """
    # IS_PRIMARY: ClassVar[BooleanField] = BooleanField("isPrimary", "isPrimary")
    # """
    # TBC
    # """
    # IS_FOREIGN: ClassVar[BooleanField] = BooleanField("isForeign", "isForeign")
    # """
    # TBC
    # """
    # IS_INDEXED: ClassVar[BooleanField] = BooleanField("isIndexed", "isIndexed")
    # """
    # TBC
    # """
    # IS_SORT: ClassVar[BooleanField] = BooleanField("isSort", "isSort")
    # """
    # TBC
    # """
    # IS_DIST: ClassVar[BooleanField] = BooleanField("isDist", "isDist")
    # """
    # TBC
    # """
    # IS_PINNED: ClassVar[BooleanField] = BooleanField("isPinned", "isPinned")
    # """
    # TBC
    # """
    # PINNED_BY: ClassVar[KeywordField] = KeywordField("pinnedBy", "pinnedBy")
    # """
    # TBC
    # """
    # PINNED_AT: ClassVar[NumericField] = NumericField("pinnedAt", "pinnedAt")
    # """
    # TBC
    # """
    # PRECISION: ClassVar[NumericField] = NumericField("precision", "precision")
    # """
    # Total number of digits allowed
    # """
    # DEFAULT_VALUE: ClassVar[KeywordField] = KeywordField("defaultValue", "defaultValue")
    # """
    # TBC
    # """
    # IS_NULLABLE: ClassVar[BooleanField] = BooleanField("isNullable", "isNullable")
    # """
    # TBC
    # """
    # NUMERIC_SCALE: ClassVar[NumericField] = NumericField("numericScale", "numericScale")
    # """
    # TBC
    # """
    # MAX_LENGTH: ClassVar[NumericField] = NumericField("maxLength", "maxLength")
    # """
    # TBC
    # """
    # VALIDATIONS: ClassVar[KeywordField] = KeywordField("validations", "validations")
    # """
    # TBC
    # """
    # PARENT_COLUMN_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "parentColumnQualifiedName",
    #     "parentColumnQualifiedName",
    #     "parentColumnQualifiedName.text",
    # )
    # """
    # TBC
    # """
    # PARENT_COLUMN_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "parentColumnName", "parentColumnName.keyword", "parentColumnName"
    # )
    # """
    # TBC
    # """
    # COLUMN_DISTINCT_VALUES_COUNT: ClassVar[NumericField] = NumericField(
    #     "columnDistinctValuesCount", "columnDistinctValuesCount"
    # )
    # """
    # TBC
    # """
    # COLUMN_DISTINCT_VALUES_COUNT_LONG: ClassVar[NumericField] = NumericField(
    #     "columnDistinctValuesCountLong", "columnDistinctValuesCountLong"
    # )
    # """
    # TBC
    # """
    # COLUMN_HISTOGRAM: ClassVar[KeywordField] = KeywordField(
    #     "columnHistogram", "columnHistogram"
    # )
    # """
    # TBC
    # """
    # COLUMN_MAX: ClassVar[NumericField] = NumericField("columnMax", "columnMax")
    # """
    # TBC
    # """
    # COLUMN_MIN: ClassVar[NumericField] = NumericField("columnMin", "columnMin")
    # """
    # TBC
    # """
    # COLUMN_MEAN: ClassVar[NumericField] = NumericField("columnMean", "columnMean")
    # """
    # TBC
    # """
    # COLUMN_SUM: ClassVar[NumericField] = NumericField("columnSum", "columnSum")
    # """
    # TBC
    # """
    # COLUMN_MEDIAN: ClassVar[NumericField] = NumericField("columnMedian", "columnMedian")
    # """
    # TBC
    # """
    # COLUMN_STANDARD_DEVIATION: ClassVar[NumericField] = NumericField(
    #     "columnStandardDeviation", "columnStandardDeviation"
    # )
    # """
    # TBC
    # """
    # COLUMN_UNIQUE_VALUES_COUNT: ClassVar[NumericField] = NumericField(
    #     "columnUniqueValuesCount", "columnUniqueValuesCount"
    # )
    # """
    # TBC
    # """
    # COLUMN_UNIQUE_VALUES_COUNT_LONG: ClassVar[NumericField] = NumericField(
    #     "columnUniqueValuesCountLong", "columnUniqueValuesCountLong"
    # )
    # """
    # TBC
    # """
    # COLUMN_AVERAGE: ClassVar[NumericField] = NumericField(
    #     "columnAverage", "columnAverage"
    # )
    # """
    # TBC
    # """
    # COLUMN_AVERAGE_LENGTH: ClassVar[NumericField] = NumericField(
    #     "columnAverageLength", "columnAverageLength"
    # )
    # """
    # TBC
    # """
    # COLUMN_DUPLICATE_VALUES_COUNT: ClassVar[NumericField] = NumericField(
    #     "columnDuplicateValuesCount", "columnDuplicateValuesCount"
    # )
    # """
    # TBC
    # """
    # COLUMN_DUPLICATE_VALUES_COUNT_LONG: ClassVar[NumericField] = NumericField(
    #     "columnDuplicateValuesCountLong", "columnDuplicateValuesCountLong"
    # )
    # """
    # TBC
    # """
    # COLUMN_MAXIMUM_STRING_LENGTH: ClassVar[NumericField] = NumericField(
    #     "columnMaximumStringLength", "columnMaximumStringLength"
    # )
    # """
    # TBC
    # """
    # COLUMN_MAXS: ClassVar[KeywordField] = KeywordField("columnMaxs", "columnMaxs")
    # """
    # TBC
    # """
    # COLUMN_MINIMUM_STRING_LENGTH: ClassVar[NumericField] = NumericField(
    #     "columnMinimumStringLength", "columnMinimumStringLength"
    # )
    # """
    # TBC
    # """
    # COLUMN_MINS: ClassVar[KeywordField] = KeywordField("columnMins", "columnMins")
    # """
    # TBC
    # """
    # COLUMN_MISSING_VALUES_COUNT: ClassVar[NumericField] = NumericField(
    #     "columnMissingValuesCount", "columnMissingValuesCount"
    # )
    # """
    # TBC
    # """
    # COLUMN_MISSING_VALUES_COUNT_LONG: ClassVar[NumericField] = NumericField(
    #     "columnMissingValuesCountLong", "columnMissingValuesCountLong"
    # )
    # """
    # TBC
    # """
    # COLUMN_MISSING_VALUES_PERCENTAGE: ClassVar[NumericField] = NumericField(
    #     "columnMissingValuesPercentage", "columnMissingValuesPercentage"
    # )
    # """
    # TBC
    # """
    # COLUMN_UNIQUENESS_PERCENTAGE: ClassVar[NumericField] = NumericField(
    #     "columnUniquenessPercentage", "columnUniquenessPercentage"
    # )
    # """
    # TBC
    # """
    # COLUMN_VARIANCE: ClassVar[NumericField] = NumericField(
    #     "columnVariance", "columnVariance"
    # )
    # """
    # TBC
    # """
    # COLUMN_TOP_VALUES: ClassVar[KeywordField] = KeywordField(
    #     "columnTopValues", "columnTopValues"
    # )
    # """
    # TBC
    # """
    # COLUMN_DEPTH_LEVEL: ClassVar[NumericField] = NumericField(
    #     "columnDepthLevel", "columnDepthLevel"
    # )
    # """
    # Level of nesting, used for STRUCT/NESTED columns
    # """

    # SNOWFLAKE_DYNAMIC_TABLE: ClassVar[RelationField] = RelationField(
    #     "snowflakeDynamicTable"
    # )
    # """
    # TBC
    # """
    # VIEW: ClassVar[RelationField] = RelationField("view")
    # """
    # TBC
    # """
    # NESTED_COLUMNS: ClassVar[RelationField] = RelationField("nestedColumns")
    # """
    # TBC
    # """
    # DATA_QUALITY_METRIC_DIMENSIONS: ClassVar[RelationField] = RelationField(
    #     "dataQualityMetricDimensions"
    # )
    # """
    # TBC
    # """
    # DBT_MODEL_COLUMNS: ClassVar[RelationField] = RelationField("dbtModelColumns")
    # """
    # TBC
    # """
    # TABLE: ClassVar[RelationField] = RelationField("table")
    # """
    # TBC
    # """
    # COLUMN_DBT_MODEL_COLUMNS: ClassVar[RelationField] = RelationField(
    #     "columnDbtModelColumns"
    # )
    # """
    # TBC
    # """
    # MATERIALISED_VIEW: ClassVar[RelationField] = RelationField("materialisedView")
    # """
    # TBC
    # """
    # PARENT_COLUMN: ClassVar[RelationField] = RelationField("parentColumn")
    # """
    # TBC
    # """
    # QUERIES: ClassVar[RelationField] = RelationField("queries")
    # """
    # TBC
    # """
    # METRIC_TIMESTAMPS: ClassVar[RelationField] = RelationField("metricTimestamps")
    # """
    # TBC
    # """
    # FOREIGN_KEY_TO: ClassVar[RelationField] = RelationField("foreignKeyTo")
    # """
    # TBC
    # """
    # FOREIGN_KEY_FROM: ClassVar[RelationField] = RelationField("foreignKeyFrom")
    # """
    # TBC
    # """
    # DBT_METRICS: ClassVar[RelationField] = RelationField("dbtMetrics")
    # """
    # TBC
    # """
    # TABLE_PARTITION: ClassVar[RelationField] = RelationField("tablePartition")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "data_type",
        "sub_data_type",
        "raw_data_type_definition",
        "order",
        "nested_column_count",
        "is_partition",
        "partition_order",
        "is_clustered",
        "is_primary",
        "is_foreign",
        "is_indexed",
        "is_sort",
        "is_dist",
        "is_pinned",
        "pinned_by",
        "pinned_at",
        "precision",
        "default_value",
        "is_nullable",
        "numeric_scale",
        "max_length",
        "validations",
        "parent_column_qualified_name",
        "parent_column_name",
        "column_distinct_values_count",
        "column_distinct_values_count_long",
        "column_histogram",
        "column_max",
        "column_min",
        "column_mean",
        "column_sum",
        "column_median",
        "column_standard_deviation",
        "column_unique_values_count",
        "column_unique_values_count_long",
        "column_average",
        "column_average_length",
        "column_duplicate_values_count",
        "column_duplicate_values_count_long",
        "column_maximum_string_length",
        "column_maxs",
        "column_minimum_string_length",
        "column_mins",
        "column_missing_values_count",
        "column_missing_values_count_long",
        "column_missing_values_percentage",
        "column_uniqueness_percentage",
        "column_variance",
        "column_top_values",
        "column_depth_level",
        "snowflake_dynamic_table",
        "view",
        "nested_columns",
        "data_quality_metric_dimensions",
        "dbt_model_columns",
        "table",
        "column_dbt_model_columns",
        "materialised_view",
        "parent_column",
        "queries",
        "metric_timestamps",
        "foreign_key_to",
        "foreign_key_from",
        "dbt_metrics",
        "table_partition",
    ]

    @property
    def data_type(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.data_type

    @data_type.setter
    def data_type(self, data_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.data_type = data_type

    @property
    def sub_data_type(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.sub_data_type

    @sub_data_type.setter
    def sub_data_type(self, sub_data_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sub_data_type = sub_data_type

    @property
    def raw_data_type_definition(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.raw_data_type_definition
        )

    @raw_data_type_definition.setter
    def raw_data_type_definition(self, raw_data_type_definition: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.raw_data_type_definition = raw_data_type_definition

    @property
    def order(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.order

    @order.setter
    def order(self, order: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.order = order

    @property
    def nested_column_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.nested_column_count

    @nested_column_count.setter
    def nested_column_count(self, nested_column_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.nested_column_count = nested_column_count

    @property
    def is_partition(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_partition

    @is_partition.setter
    def is_partition(self, is_partition: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_partition = is_partition

    @property
    def partition_order(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.partition_order

    @partition_order.setter
    def partition_order(self, partition_order: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.partition_order = partition_order

    @property
    def is_clustered(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_clustered

    @is_clustered.setter
    def is_clustered(self, is_clustered: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_clustered = is_clustered

    @property
    def is_primary(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_primary

    @is_primary.setter
    def is_primary(self, is_primary: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_primary = is_primary

    @property
    def is_foreign(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_foreign

    @is_foreign.setter
    def is_foreign(self, is_foreign: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_foreign = is_foreign

    @property
    def is_indexed(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_indexed

    @is_indexed.setter
    def is_indexed(self, is_indexed: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_indexed = is_indexed

    @property
    def is_sort(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_sort

    @is_sort.setter
    def is_sort(self, is_sort: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_sort = is_sort

    @property
    def is_dist(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_dist

    @is_dist.setter
    def is_dist(self, is_dist: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_dist = is_dist

    @property
    def is_pinned(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_pinned

    @is_pinned.setter
    def is_pinned(self, is_pinned: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_pinned = is_pinned

    @property
    def pinned_by(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.pinned_by

    @pinned_by.setter
    def pinned_by(self, pinned_by: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.pinned_by = pinned_by

    @property
    def pinned_at(self) -> Optional[datetime]:
        return None if self.attributes is None else self.attributes.pinned_at

    @pinned_at.setter
    def pinned_at(self, pinned_at: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.pinned_at = pinned_at

    @property
    def precision(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.precision

    @precision.setter
    def precision(self, precision: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.precision = precision

    @property
    def default_value(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.default_value

    @default_value.setter
    def default_value(self, default_value: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.default_value = default_value

    @property
    def is_nullable(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_nullable = is_nullable

    @property
    def numeric_scale(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.numeric_scale

    @numeric_scale.setter
    def numeric_scale(self, numeric_scale: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.numeric_scale = numeric_scale

    @property
    def max_length(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.max_length

    @max_length.setter
    def max_length(self, max_length: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.max_length = max_length

    @property
    def validations(self) -> Optional[dict[str, str]]:
        return None if self.attributes is None else self.attributes.validations

    @validations.setter
    def validations(self, validations: Optional[dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.validations = validations

    @property
    def parent_column_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.parent_column_qualified_name
        )

    @parent_column_qualified_name.setter
    def parent_column_qualified_name(self, parent_column_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_column_qualified_name = parent_column_qualified_name

    @property
    def parent_column_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.parent_column_name

    @parent_column_name.setter
    def parent_column_name(self, parent_column_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_column_name = parent_column_name

    @property
    def column_distinct_values_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_distinct_values_count
        )

    @column_distinct_values_count.setter
    def column_distinct_values_count(self, column_distinct_values_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_distinct_values_count = column_distinct_values_count

    @property
    def column_distinct_values_count_long(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_distinct_values_count_long
        )

    @column_distinct_values_count_long.setter
    def column_distinct_values_count_long(
        self, column_distinct_values_count_long: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_distinct_values_count_long = (
            column_distinct_values_count_long
        )

    @property
    def column_max(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_max

    @column_max.setter
    def column_max(self, column_max: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_max = column_max

    @property
    def column_min(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_min

    @column_min.setter
    def column_min(self, column_min: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_min = column_min

    @property
    def column_mean(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_mean

    @column_mean.setter
    def column_mean(self, column_mean: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_mean = column_mean

    @property
    def column_sum(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_sum

    @column_sum.setter
    def column_sum(self, column_sum: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_sum = column_sum

    @property
    def column_median(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_median

    @column_median.setter
    def column_median(self, column_median: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_median = column_median

    @property
    def column_standard_deviation(self) -> Optional[float]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_standard_deviation
        )

    @column_standard_deviation.setter
    def column_standard_deviation(self, column_standard_deviation: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_standard_deviation = column_standard_deviation

    @property
    def column_unique_values_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_unique_values_count
        )

    @column_unique_values_count.setter
    def column_unique_values_count(self, column_unique_values_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_unique_values_count = column_unique_values_count

    @property
    def column_unique_values_count_long(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_unique_values_count_long
        )

    @column_unique_values_count_long.setter
    def column_unique_values_count_long(
        self, column_unique_values_count_long: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_unique_values_count_long = (
            column_unique_values_count_long
        )

    @property
    def column_average(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_average

    @column_average.setter
    def column_average(self, column_average: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_average = column_average

    @property
    def column_average_length(self) -> Optional[float]:
        return (
            None if self.attributes is None else self.attributes.column_average_length
        )

    @column_average_length.setter
    def column_average_length(self, column_average_length: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_average_length = column_average_length

    @property
    def column_duplicate_values_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_duplicate_values_count
        )

    @column_duplicate_values_count.setter
    def column_duplicate_values_count(
        self, column_duplicate_values_count: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_duplicate_values_count = column_duplicate_values_count

    @property
    def column_duplicate_values_count_long(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_duplicate_values_count_long
        )

    @column_duplicate_values_count_long.setter
    def column_duplicate_values_count_long(
        self, column_duplicate_values_count_long: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_duplicate_values_count_long = (
            column_duplicate_values_count_long
        )

    @property
    def column_maximum_string_length(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_maximum_string_length
        )

    @column_maximum_string_length.setter
    def column_maximum_string_length(self, column_maximum_string_length: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_maximum_string_length = column_maximum_string_length

    @property
    def column_maxs(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.column_maxs

    @column_maxs.setter
    def column_maxs(self, column_maxs: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_maxs = column_maxs

    @property
    def column_minimum_string_length(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_minimum_string_length
        )

    @column_minimum_string_length.setter
    def column_minimum_string_length(self, column_minimum_string_length: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_minimum_string_length = column_minimum_string_length

    @property
    def column_mins(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.column_mins

    @column_mins.setter
    def column_mins(self, column_mins: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_mins = column_mins

    @property
    def column_missing_values_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_missing_values_count
        )

    @column_missing_values_count.setter
    def column_missing_values_count(self, column_missing_values_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_missing_values_count = column_missing_values_count

    @property
    def column_missing_values_count_long(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_missing_values_count_long
        )

    @column_missing_values_count_long.setter
    def column_missing_values_count_long(
        self, column_missing_values_count_long: Optional[int]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_missing_values_count_long = (
            column_missing_values_count_long
        )

    @property
    def column_missing_values_percentage(self) -> Optional[float]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_missing_values_percentage
        )

    @column_missing_values_percentage.setter
    def column_missing_values_percentage(
        self, column_missing_values_percentage: Optional[float]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_missing_values_percentage = (
            column_missing_values_percentage
        )

    @property
    def column_uniqueness_percentage(self) -> Optional[float]:
        return (
            None
            if self.attributes is None
            else self.attributes.column_uniqueness_percentage
        )

    @column_uniqueness_percentage.setter
    def column_uniqueness_percentage(
        self, column_uniqueness_percentage: Optional[float]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_uniqueness_percentage = column_uniqueness_percentage

    @property
    def column_variance(self) -> Optional[float]:
        return None if self.attributes is None else self.attributes.column_variance

    @column_variance.setter
    def column_variance(self, column_variance: Optional[float]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_variance = column_variance

    @property
    def column_depth_level(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.column_depth_level

    @column_depth_level.setter
    def column_depth_level(self, column_depth_level: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_depth_level = column_depth_level

    # @property
    # def snowflake_dynamic_table(self) -> Optional[SnowflakeDynamicTable]:
    #     return (
    #         None if self.attributes is None else self.attributes.snowflake_dynamic_table
    #     )

    # @snowflake_dynamic_table.setter
    # def snowflake_dynamic_table(
    #     self, snowflake_dynamic_table: Optional[SnowflakeDynamicTable]
    # ):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.snowflake_dynamic_table = snowflake_dynamic_table

    @property
    def view(self) -> Optional[View]:
        return None if self.attributes is None else self.attributes.view

    @view.setter
    def view(self, view: Optional[View]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.view = view

    @property
    def nested_columns(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.nested_columns

    @nested_columns.setter
    def nested_columns(self, nested_columns: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.nested_columns = nested_columns

    @property
    def data_quality_metric_dimensions(self) -> Optional[list[Metric]]:
        return (
            None
            if self.attributes is None
            else self.attributes.data_quality_metric_dimensions
        )

    @data_quality_metric_dimensions.setter
    def data_quality_metric_dimensions(
        self, data_quality_metric_dimensions: Optional[list[Metric]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.data_quality_metric_dimensions = data_quality_metric_dimensions

    # @property
    # def dbt_model_columns(self) -> Optional[list[DbtModelColumn]]:
    #     return None if self.attributes is None else self.attributes.dbt_model_columns

    # @dbt_model_columns.setter
    # def dbt_model_columns(self, dbt_model_columns: Optional[list[DbtModelColumn]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.dbt_model_columns = dbt_model_columns

    @property
    def table(self) -> Optional[Table]:
        return None if self.attributes is None else self.attributes.table

    @table.setter
    def table(self, table: Optional[Table]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.table = table

    # @property
    # def column_dbt_model_columns(self) -> Optional[list[DbtModelColumn]]:
    #     return (
    #         None
    #         if self.attributes is None
    #         else self.attributes.column_dbt_model_columns
    #     )

    # @column_dbt_model_columns.setter
    # def column_dbt_model_columns(
    #     self, column_dbt_model_columns: Optional[list[DbtModelColumn]]
    # ):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.column_dbt_model_columns = column_dbt_model_columns

    @property
    def materialised_view(self) -> Optional[MaterialisedView]:
        return None if self.attributes is None else self.attributes.materialised_view

    @materialised_view.setter
    def materialised_view(self, materialised_view: Optional[MaterialisedView]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.materialised_view = materialised_view

    @property
    def parent_column(self) -> Optional[Column]:
        return None if self.attributes is None else self.attributes.parent_column

    @parent_column.setter
    def parent_column(self, parent_column: Optional[Column]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_column = parent_column

    @property
    def queries(self) -> Optional[list[Query]]:
        return None if self.attributes is None else self.attributes.queries

    @queries.setter
    def queries(self, queries: Optional[list[Query]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.queries = queries

    @property
    def metric_timestamps(self) -> Optional[list[Metric]]:
        return None if self.attributes is None else self.attributes.metric_timestamps

    @metric_timestamps.setter
    def metric_timestamps(self, metric_timestamps: Optional[list[Metric]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_timestamps = metric_timestamps

    @property
    def foreign_key_to(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.foreign_key_to

    @foreign_key_to.setter
    def foreign_key_to(self, foreign_key_to: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.foreign_key_to = foreign_key_to

    @property
    def foreign_key_from(self) -> Optional[Column]:
        return None if self.attributes is None else self.attributes.foreign_key_from

    @foreign_key_from.setter
    def foreign_key_from(self, foreign_key_from: Optional[Column]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.foreign_key_from = foreign_key_from

    # @property
    # def dbt_metrics(self) -> Optional[list[DbtMetric]]:
    #     return None if self.attributes is None else self.attributes.dbt_metrics

    # @dbt_metrics.setter
    # def dbt_metrics(self, dbt_metrics: Optional[list[DbtMetric]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.dbt_metrics = dbt_metrics

    @property
    def table_partition(self) -> Optional[TablePartition]:
        return None if self.attributes is None else self.attributes.table_partition

    @table_partition.setter
    def table_partition(self, table_partition: Optional[TablePartition]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.table_partition = table_partition

    class Attributes(SQL.Attributes):
        data_type: Optional[str] = Field(None, description="", alias="dataType")
        sub_data_type: Optional[str] = Field(None, description="", alias="subDataType")
        raw_data_type_definition: Optional[str] = Field(
            None, description="", alias="rawDataTypeDefinition"
        )
        order: Optional[int] = Field(None, description="", alias="order")
        nested_column_count: Optional[int] = Field(
            None, description="", alias="nestedColumnCount"
        )
        is_partition: Optional[bool] = Field(None, description="", alias="isPartition")
        partition_order: Optional[int] = Field(
            None, description="", alias="partitionOrder"
        )
        is_clustered: Optional[bool] = Field(None, description="", alias="isClustered")
        is_primary: Optional[bool] = Field(None, description="", alias="isPrimary")
        is_foreign: Optional[bool] = Field(None, description="", alias="isForeign")
        is_indexed: Optional[bool] = Field(None, description="", alias="isIndexed")
        is_sort: Optional[bool] = Field(None, description="", alias="isSort")
        is_dist: Optional[bool] = Field(None, description="", alias="isDist")
        is_pinned: Optional[bool] = Field(None, description="", alias="isPinned")
        pinned_by: Optional[str] = Field(None, description="", alias="pinnedBy")
        pinned_at: Optional[datetime] = Field(None, description="", alias="pinnedAt")
        precision: Optional[int] = Field(None, description="", alias="precision")
        default_value: Optional[str] = Field(None, description="", alias="defaultValue")
        is_nullable: Optional[bool] = Field(None, description="", alias="isNullable")
        numeric_scale: Optional[float] = Field(
            None, description="", alias="numericScale"
        )
        max_length: Optional[int] = Field(None, description="", alias="maxLength")
        validations: Optional[dict[str, str]] = Field(
            None, description="", alias="validations"
        )
        parent_column_qualified_name: Optional[str] = Field(
            None, description="", alias="parentColumnQualifiedName"
        )
        parent_column_name: Optional[str] = Field(
            None, description="", alias="parentColumnName"
        )
        column_distinct_values_count: Optional[int] = Field(
            None, description="", alias="columnDistinctValuesCount"
        )
        column_distinct_values_count_long: Optional[int] = Field(
            None, description="", alias="columnDistinctValuesCountLong"
        )
        column_max: Optional[float] = Field(None, description="", alias="columnMax")
        column_min: Optional[float] = Field(None, description="", alias="columnMin")
        column_mean: Optional[float] = Field(None, description="", alias="columnMean")
        column_sum: Optional[float] = Field(None, description="", alias="columnSum")
        column_median: Optional[float] = Field(
            None, description="", alias="columnMedian"
        )
        column_standard_deviation: Optional[float] = Field(
            None, description="", alias="columnStandardDeviation"
        )
        column_unique_values_count: Optional[int] = Field(
            None, description="", alias="columnUniqueValuesCount"
        )
        column_unique_values_count_long: Optional[int] = Field(
            None, description="", alias="columnUniqueValuesCountLong"
        )
        column_average: Optional[float] = Field(
            None, description="", alias="columnAverage"
        )
        column_average_length: Optional[float] = Field(
            None, description="", alias="columnAverageLength"
        )
        column_duplicate_values_count: Optional[int] = Field(
            None, description="", alias="columnDuplicateValuesCount"
        )
        column_duplicate_values_count_long: Optional[int] = Field(
            None, description="", alias="columnDuplicateValuesCountLong"
        )
        column_maximum_string_length: Optional[int] = Field(
            None, description="", alias="columnMaximumStringLength"
        )
        column_maxs: Optional[set[str]] = Field(
            None, description="", alias="columnMaxs"
        )
        column_minimum_string_length: Optional[int] = Field(
            None, description="", alias="columnMinimumStringLength"
        )
        column_mins: Optional[set[str]] = Field(
            None, description="", alias="columnMins"
        )
        column_missing_values_count: Optional[int] = Field(
            None, description="", alias="columnMissingValuesCount"
        )
        column_missing_values_count_long: Optional[int] = Field(
            None, description="", alias="columnMissingValuesCountLong"
        )
        column_missing_values_percentage: Optional[float] = Field(
            None, description="", alias="columnMissingValuesPercentage"
        )
        column_uniqueness_percentage: Optional[float] = Field(
            None, description="", alias="columnUniquenessPercentage"
        )
        column_variance: Optional[float] = Field(
            None, description="", alias="columnVariance"
        )
        column_depth_level: Optional[int] = Field(
            None, description="", alias="columnDepthLevel"
        )
        # snowflake_dynamic_table: Optional[SnowflakeDynamicTable] = Field(
        #     None, description="", alias="snowflakeDynamicTable"
        # )  # relationship
        view: Optional[View] = Field(None, description="", alias="view")  # relationship
        nested_columns: Optional[list[Column]] = Field(
            None, description="", alias="nestedColumns"
        )  # relationship
        data_quality_metric_dimensions: Optional[list[Metric]] = Field(
            None, description="", alias="dataQualityMetricDimensions"
        )  # relationship
        # dbt_model_columns: Optional[list[DbtModelColumn]] = Field(
        #     None, description="", alias="dbtModelColumns"
        # )  # relationship
        table: Optional[Table] = Field(
            None, description="", alias="table"
        )  # relationship
        # column_dbt_model_columns: Optional[list[DbtModelColumn]] = Field(
        #     None, description="", alias="columnDbtModelColumns"
        # )  # relationship
        materialised_view: Optional[MaterialisedView] = Field(
            None, description="", alias="materialisedView"
        )  # relationship
        parent_column: Optional[Column] = Field(
            None, description="", alias="parentColumn"
        )  # relationship
        queries: Optional[list[Query]] = Field(
            None, description="", alias="queries"
        )  # relationship
        metric_timestamps: Optional[list[Metric]] = Field(
            None, description="", alias="metricTimestamps"
        )  # relationship
        foreign_key_to: Optional[list[Column]] = Field(
            None, description="", alias="foreignKeyTo"
        )  # relationship
        foreign_key_from: Optional[Column] = Field(
            None, description="", alias="foreignKeyFrom"
        )  # relationship
        # dbt_metrics: Optional[list[DbtMetric]] = Field(
        #     None, description="", alias="dbtMetrics"
        # )  # relationship
        table_partition: Optional[TablePartition] = Field(
            None, description="", alias="tablePartition"
        )  # relationship

    attributes: Column.Attributes = Field(
        default_factory=lambda: Column.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .metric import Metric  # noqa: E402
from .table import Table  # noqa: E402
from .view import View  # noqa: E402
from .materialized_view import MaterialisedView  # noqa: E402
from .query import Query  # noqa: E402
from .table_partition import TablePartition  # noqa: E402
