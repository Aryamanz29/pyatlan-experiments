from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .airflow.airflow import Airflow


class AirflowTask(Airflow):
    """Description"""

    type_name: str = Field("AirflowTask", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "AirflowTask":
            raise ValueError("must be AirflowTask")
        return v

    def __setattr__(self, name, value):
        if name in AirflowTask._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # AIRFLOW_TASK_OPERATOR_CLASS: ClassVar[KeywordTextField] = KeywordTextField(
    #     "airflowTaskOperatorClass",
    #     "airflowTaskOperatorClass.keyword",
    #     "airflowTaskOperatorClass",
    # )
    # """
    # TBC
    # """
    # AIRFLOW_DAG_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "airflowDagName", "airflowDagName.keyword", "airflowDagName"
    # )
    # """
    # TBC
    # """
    # AIRFLOW_DAG_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
    #     "airflowDagQualifiedName", "airflowDagQualifiedName"
    # )
    # """
    # TBC
    # """
    # AIRFLOW_TASK_CONNECTION_ID: ClassVar[KeywordTextField] = KeywordTextField(
    #     "airflowTaskConnectionId",
    #     "airflowTaskConnectionId.keyword",
    #     "airflowTaskConnectionId",
    # )
    # """
    # TBC
    # """
    # AIRFLOW_TASK_SQL: ClassVar[KeywordField] = KeywordField(
    #     "airflowTaskSql", "airflowTaskSql"
    # )
    # """
    # TBC
    # """
    # AIRFLOW_TASK_RETRY_NUMBER: ClassVar[NumericField] = NumericField(
    #     "airflowTaskRetryNumber", "airflowTaskRetryNumber"
    # )
    # """
    # Retry required for the run
    # """
    # AIRFLOW_TASK_POOL: ClassVar[KeywordField] = KeywordField(
    #     "airflowTaskPool", "airflowTaskPool"
    # )
    # """
    # Pool on which this run happened
    # """
    # AIRFLOW_TASK_POOL_SLOTS: ClassVar[NumericField] = NumericField(
    #     "airflowTaskPoolSlots", "airflowTaskPoolSlots"
    # )
    # """
    # Pool slots used for the run
    # """
    # AIRFLOW_TASK_QUEUE: ClassVar[KeywordField] = KeywordField(
    #     "airflowTaskQueue", "airflowTaskQueue"
    # )
    # """
    # Queue on which this run happened
    # """
    # AIRFLOW_TASK_PRIORITY_WEIGHT: ClassVar[NumericField] = NumericField(
    #     "airflowTaskPriorityWeight", "airflowTaskPriorityWeight"
    # )
    # """
    # Priority weight of the run
    # """
    # AIRFLOW_TASK_TRIGGER_RULE: ClassVar[KeywordField] = KeywordField(
    #     "airflowTaskTriggerRule", "airflowTaskTriggerRule"
    # )
    # """
    # Trigger rule of the run
    # """

    # OUTPUTS: ClassVar[RelationField] = RelationField("outputs")
    # """
    # TBC
    # """
    # PROCESS: ClassVar[RelationField] = RelationField("process")
    # """
    # TBC
    # """
    # INPUTS: ClassVar[RelationField] = RelationField("inputs")
    # """
    # TBC
    # """
    # AIRFLOW_DAG: ClassVar[RelationField] = RelationField("airflowDag")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "airflow_task_operator_class",
        "airflow_dag_name",
        "airflow_dag_qualified_name",
        "airflow_task_connection_id",
        "airflow_task_sql",
        "airflow_task_retry_number",
        "airflow_task_pool",
        "airflow_task_pool_slots",
        "airflow_task_queue",
        "airflow_task_priority_weight",
        "airflow_task_trigger_rule",
        "outputs",
        "process",
        "inputs",
        "airflow_dag",
    ]

    @property
    def airflow_task_operator_class(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_task_operator_class
        )

    @airflow_task_operator_class.setter
    def airflow_task_operator_class(self, airflow_task_operator_class: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_operator_class = airflow_task_operator_class

    @property
    def airflow_dag_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_dag_name

    @airflow_dag_name.setter
    def airflow_dag_name(self, airflow_dag_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_dag_name = airflow_dag_name

    @property
    def airflow_dag_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_dag_qualified_name
        )

    @airflow_dag_qualified_name.setter
    def airflow_dag_qualified_name(self, airflow_dag_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_dag_qualified_name = airflow_dag_qualified_name

    @property
    def airflow_task_connection_id(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_task_connection_id
        )

    @airflow_task_connection_id.setter
    def airflow_task_connection_id(self, airflow_task_connection_id: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_connection_id = airflow_task_connection_id

    @property
    def airflow_task_sql(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_task_sql

    @airflow_task_sql.setter
    def airflow_task_sql(self, airflow_task_sql: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_sql = airflow_task_sql

    @property
    def airflow_task_retry_number(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_task_retry_number
        )

    @airflow_task_retry_number.setter
    def airflow_task_retry_number(self, airflow_task_retry_number: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_retry_number = airflow_task_retry_number

    @property
    def airflow_task_pool(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_task_pool

    @airflow_task_pool.setter
    def airflow_task_pool(self, airflow_task_pool: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_pool = airflow_task_pool

    @property
    def airflow_task_pool_slots(self) -> Optional[int]:
        return (
            None if self.attributes is None else self.attributes.airflow_task_pool_slots
        )

    @airflow_task_pool_slots.setter
    def airflow_task_pool_slots(self, airflow_task_pool_slots: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_pool_slots = airflow_task_pool_slots

    @property
    def airflow_task_queue(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.airflow_task_queue

    @airflow_task_queue.setter
    def airflow_task_queue(self, airflow_task_queue: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_queue = airflow_task_queue

    @property
    def airflow_task_priority_weight(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_task_priority_weight
        )

    @airflow_task_priority_weight.setter
    def airflow_task_priority_weight(self, airflow_task_priority_weight: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_priority_weight = airflow_task_priority_weight

    @property
    def airflow_task_trigger_rule(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.airflow_task_trigger_rule
        )

    @airflow_task_trigger_rule.setter
    def airflow_task_trigger_rule(self, airflow_task_trigger_rule: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_task_trigger_rule = airflow_task_trigger_rule

    @property
    def outputs(self) -> Optional[list[Catalog]]:
        return None if self.attributes is None else self.attributes.outputs

    @outputs.setter
    def outputs(self, outputs: Optional[list[Catalog]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.outputs = outputs

    @property
    def process(self) -> Optional[Process]:
        return None if self.attributes is None else self.attributes.process

    @process.setter
    def process(self, process: Optional[Process]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.process = process

    @property
    def inputs(self) -> Optional[list[Catalog]]:
        return None if self.attributes is None else self.attributes.inputs

    @inputs.setter
    def inputs(self, inputs: Optional[list[Catalog]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.inputs = inputs

    @property
    def airflow_dag(self) -> Optional[AirflowDag]:
        return None if self.attributes is None else self.attributes.airflow_dag

    @airflow_dag.setter
    def airflow_dag(self, airflow_dag: Optional[AirflowDag]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_dag = airflow_dag

    class Attributes(Airflow.Attributes):
        airflow_task_operator_class: Optional[str] = Field(
            None, description="", alias="airflowTaskOperatorClass"
        )
        airflow_dag_name: Optional[str] = Field(
            None, description="", alias="airflowDagName"
        )
        airflow_dag_qualified_name: Optional[str] = Field(
            None, description="", alias="airflowDagQualifiedName"
        )
        airflow_task_connection_id: Optional[str] = Field(
            None, description="", alias="airflowTaskConnectionId"
        )
        airflow_task_sql: Optional[str] = Field(
            None, description="", alias="airflowTaskSql"
        )
        airflow_task_retry_number: Optional[int] = Field(
            None, description="", alias="airflowTaskRetryNumber"
        )
        airflow_task_pool: Optional[str] = Field(
            None, description="", alias="airflowTaskPool"
        )
        airflow_task_pool_slots: Optional[int] = Field(
            None, description="", alias="airflowTaskPoolSlots"
        )
        airflow_task_queue: Optional[str] = Field(
            None, description="", alias="airflowTaskQueue"
        )
        airflow_task_priority_weight: Optional[int] = Field(
            None, description="", alias="airflowTaskPriorityWeight"
        )
        airflow_task_trigger_rule: Optional[str] = Field(
            None, description="", alias="airflowTaskTriggerRule"
        )
        outputs: Optional[list[Catalog]] = Field(
            None, description="", alias="outputs"
        )  # relationship
        process: Optional[Process] = Field(
            None, description="", alias="process"
        )  # relationship
        inputs: Optional[list[Catalog]] = Field(
            None, description="", alias="inputs"
        )  # relationship
        airflow_dag: Optional[AirflowDag] = Field(
            None, description="", alias="airflowDag"
        )  # relationship

    attributes: "AirflowTask.Attributes" = Field(
        default_factory=lambda: AirflowTask.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .catalog.catalog import Catalog  # noqa: E402
from .process.process import Process  # noqa: E402
from .airflow_dag import AirflowDag  # noqa: E402