from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .data_quality import DataQuality


class Metric(DataQuality):
    """Description"""

    type_name: str = Field("Metric", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Metric":
            raise ValueError("must be Metric")
        return v

    def __setattr__(self, name, value):
        if name in Metric._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # METRIC_TYPE: ClassVar[KeywordField] = KeywordField("metricType", "metricType")
    # """
    # TBC
    # """
    # METRIC_SQL: ClassVar[KeywordField] = KeywordField("metricSQL", "metricSQL")
    # """
    # TBC
    # """
    # METRIC_FILTERS: ClassVar[TextField] = TextField("metricFilters", "metricFilters")
    # """
    # TBC
    # """
    # METRIC_TIME_GRAINS: ClassVar[TextField] = TextField(
    #     "metricTimeGrains", "metricTimeGrains"
    # )
    # """
    # TBC
    # """

    # METRIC_TIMESTAMP_COLUMN: ClassVar[RelationField] = RelationField(
    #     "metricTimestampColumn"
    # )
    # """
    # TBC
    # """
    # ASSETS: ClassVar[RelationField] = RelationField("assets")
    # """
    # TBC
    # """
    # METRIC_DIMENSION_COLUMNS: ClassVar[RelationField] = RelationField(
    #     "metricDimensionColumns"
    # )
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "metric_type",
        "metric_s_q_l",
        "metric_filters",
        "metric_time_grains",
        "metric_timestamp_column",
        "assets",
        "metric_dimension_columns",
    ]

    @property
    def metric_type(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.metric_type

    @metric_type.setter
    def metric_type(self, metric_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_type = metric_type

    @property
    def metric_s_q_l(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.metric_s_q_l

    @metric_s_q_l.setter
    def metric_s_q_l(self, metric_s_q_l: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_s_q_l = metric_s_q_l

    @property
    def metric_filters(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.metric_filters

    @metric_filters.setter
    def metric_filters(self, metric_filters: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_filters = metric_filters

    @property
    def metric_time_grains(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.metric_time_grains

    @metric_time_grains.setter
    def metric_time_grains(self, metric_time_grains: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_time_grains = metric_time_grains

    @property
    def metric_timestamp_column(self) -> Optional[Column]:
        return (
            None if self.attributes is None else self.attributes.metric_timestamp_column
        )

    @metric_timestamp_column.setter
    def metric_timestamp_column(self, metric_timestamp_column: Optional[Column]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_timestamp_column = metric_timestamp_column

    @property
    def assets(self) -> Optional[list[Asset]]:
        return None if self.attributes is None else self.attributes.assets

    @assets.setter
    def assets(self, assets: Optional[list[Asset]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.assets = assets

    @property
    def metric_dimension_columns(self) -> Optional[list[Column]]:
        return (
            None
            if self.attributes is None
            else self.attributes.metric_dimension_columns
        )

    @metric_dimension_columns.setter
    def metric_dimension_columns(
        self, metric_dimension_columns: Optional[list[Column]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.metric_dimension_columns = metric_dimension_columns

    class Attributes(DataQuality.Attributes):
        metric_type: Optional[str] = Field(None, description="", alias="metricType")
        metric_s_q_l: Optional[str] = Field(None, description="", alias="metricSQL")
        metric_filters: Optional[str] = Field(
            None, description="", alias="metricFilters"
        )
        metric_time_grains: Optional[set[str]] = Field(
            None, description="", alias="metricTimeGrains"
        )
        metric_timestamp_column: Optional[Column] = Field(
            None, description="", alias="metricTimestampColumn"
        )  # relationship
        assets: Optional[list[Asset]] = Field(
            None, description="", alias="assets"
        )  # relationship
        metric_dimension_columns: Optional[list[Column]] = Field(
            None, description="", alias="metricDimensionColumns"
        )  # relationship

    attributes: "Metric.Attributes" = Field(
        default_factory=lambda: Metric.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .column import Column  # noqa: E402
from .asset import Asset  # noqa: E402
