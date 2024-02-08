from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .airflow import Airflow


class AirflowDag(Airflow):
    """Description"""

    type_name: str = Field("AirflowDag", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "AirflowDag":
            raise ValueError("must be AirflowDag")
        return v

    def __setattr__(self, name, value):
        if name in AirflowDag._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # AIRFLOW_DAG_SCHEDULE: ClassVar[KeywordField] = KeywordField(
    #     "airflowDagSchedule", "airflowDagSchedule"
    # )
    # """
    # TBC
    # """
    # AIRFLOW_DAG_SCHEDULE_DELTA: ClassVar[NumericField] = NumericField(
    #     "airflowDagScheduleDelta", "airflowDagScheduleDelta"
    # )
    # """
    # Duration between scheduled runs in seconds
    # """

    # AIRFLOW_TASKS: ClassVar[RelationField] = RelationField("airflowTasks")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "airflow_dag_schedule",
        "airflow_dag_schedule_delta",
        "airflow_tasks",
    ]

    @property
    def airflow_dag_schedule(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_dag_schedule

    @airflow_dag_schedule.setter
    def airflow_dag_schedule(self, airflow_dag_schedule: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_dag_schedule = airflow_dag_schedule

    @property
    def airflow_dag_schedule_delta(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_dag_schedule_delta
        )

    @airflow_dag_schedule_delta.setter
    def airflow_dag_schedule_delta(self, airflow_dag_schedule_delta: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_dag_schedule_delta = airflow_dag_schedule_delta

    @property
    def airflow_tasks(self) -> Optional[list[AirflowTask]]:
        return None if self.attributes is None else self.attributes.airflow_tasks

    @airflow_tasks.setter
    def airflow_tasks(self, airflow_tasks: Optional[list[AirflowTask]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_tasks = airflow_tasks

    class Attributes(Airflow.Attributes):
        airflow_dag_schedule: Optional[str] = Field(
            None, description="", alias="airflowDagSchedule"
        )
        airflow_dag_schedule_delta: Optional[int] = Field(
            None, description="", alias="airflowDagScheduleDelta"
        )
        airflow_tasks: Optional[list[AirflowTask]] = Field(
            None, description="", alias="airflowTasks"
        )  # relationship

    attributes: "AirflowDag.Attributes" = Field(
        default_factory=lambda: AirflowDag.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .airflow_task import AirflowTask  # noqa: E402