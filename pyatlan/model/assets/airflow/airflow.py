from __future__ import annotations

from datetime import datetime
from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from ..catalog.catalog import Catalog


class Airflow(Catalog):
    """Description"""

    type_name: str = Field("Airflow", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Airflow":
            raise ValueError("must be Airflow")
        return v

    def __setattr__(self, name, value):
        if name in Airflow._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # AIRFLOW_TAGS: ClassVar[KeywordField] = KeywordField("airflowTags", "airflowTags")
    # """
    # TBC
    # """
    # AIRFLOW_RUN_VERSION: ClassVar[KeywordField] = KeywordField(
    #     "airflowRunVersion", "airflowRunVersion"
    # )
    # """
    # Airflow Version of the run
    # """
    # AIRFLOW_RUN_OPEN_LINEAGE_VERSION: ClassVar[KeywordField] = KeywordField(
    #     "airflowRunOpenLineageVersion", "airflowRunOpenLineageVersion"
    # )
    # """
    # OpenLineage Version of the run
    # """
    # AIRFLOW_RUN_NAME: ClassVar[KeywordField] = KeywordField(
    #     "airflowRunName", "airflowRunName"
    # )
    # """
    # Name of the run
    # """
    # AIRFLOW_RUN_TYPE: ClassVar[KeywordField] = KeywordField(
    #     "airflowRunType", "airflowRunType"
    # )
    # """
    # Type of the run
    # """
    # AIRFLOW_RUN_START_TIME: ClassVar[NumericField] = NumericField(
    #     "airflowRunStartTime", "airflowRunStartTime"
    # )
    # """
    # Start time of the run
    # """
    # AIRFLOW_RUN_END_TIME: ClassVar[NumericField] = NumericField(
    #     "airflowRunEndTime", "airflowRunEndTime"
    # )
    # """
    # End time of the run
    # """
    # AIRFLOW_RUN_OPEN_LINEAGE_STATE: ClassVar[KeywordField] = KeywordField(
    #     "airflowRunOpenLineageState", "airflowRunOpenLineageState"
    # )
    # """
    # OpenLineage state of the run
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "airflow_tags",
        "airflow_run_version",
        "airflow_run_open_lineage_version",
        "airflow_run_name",
        "airflow_run_type",
        "airflow_run_start_time",
        "airflow_run_end_time",
        "airflow_run_open_lineage_state",
    ]

    @property
    def airflow_tags(self) -> Optional[set[str]]:
        return None if self.attributes is None else self.attributes.airflow_tags

    @airflow_tags.setter
    def airflow_tags(self, airflow_tags: Optional[set[str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_tags = airflow_tags

    @property
    def airflow_run_version(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_run_version

    @airflow_run_version.setter
    def airflow_run_version(self, airflow_run_version: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_version = airflow_run_version

    @property
    def airflow_run_open_lineage_version(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_run_open_lineage_version
        )

    @airflow_run_open_lineage_version.setter
    def airflow_run_open_lineage_version(
        self, airflow_run_open_lineage_version: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_open_lineage_version = (
            airflow_run_open_lineage_version
        )

    @property
    def airflow_run_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_run_name

    @airflow_run_name.setter
    def airflow_run_name(self, airflow_run_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_name = airflow_run_name

    @property
    def airflow_run_type(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_run_type

    @airflow_run_type.setter
    def airflow_run_type(self, airflow_run_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_type = airflow_run_type

    @property
    def airflow_run_start_time(self) -> Optional[datetime]:
        return (
            None if self.attributes is None else self.attributes.airflow_run_start_time
        )

    @airflow_run_start_time.setter
    def airflow_run_start_time(self, airflow_run_start_time: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_start_time = airflow_run_start_time

    @property
    def airflow_run_end_time(self) -> Optional[datetime]:
        return None if self.attributes is None else self.attributes.airflow_run_end_time

    @airflow_run_end_time.setter
    def airflow_run_end_time(self, airflow_run_end_time: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_run_end_time = airflow_run_end_time

    class Attributes(Catalog.Attributes):
        airflow_tags: Optional[set[str]] = Field(
            None, description="", alias="airflowTags"
        )
        airflow_run_version: Optional[str] = Field(
            None, description="", alias="airflowRunVersion"
        )
        airflow_run_open_lineage_version: Optional[str] = Field(
            None, description="", alias="airflowRunOpenLineageVersion"
        )
        airflow_run_name: Optional[str] = Field(
            None, description="", alias="airflowRunName"
        )
        airflow_run_type: Optional[str] = Field(
            None, description="", alias="airflowRunType"
        )
        airflow_run_start_time: Optional[datetime] = Field(
            None, description="", alias="airflowRunStartTime"
        )
        airflow_run_end_time: Optional[datetime] = Field(
            None, description="", alias="airflowRunEndTime"
        )

    attributes: Airflow.Attributes = Field(
        default_factory=lambda: Airflow.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )
