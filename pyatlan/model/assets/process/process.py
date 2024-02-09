from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from ..base.asset import Asset


class Process(Asset):
    """Description"""

    type_name: str = Field("Process", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Process":
            raise ValueError("must be Process")
        return v

    def __setattr__(self, name, value):
        if name in Process._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # CODE: ClassVar[KeywordField] = KeywordField("code", "code")
    # """
    # TBC
    # """
    # SQL: ClassVar[KeywordField] = KeywordField("sql", "sql")
    # """
    # TBC
    # """
    # AST: ClassVar[KeywordField] = KeywordField("ast", "ast")
    # """
    # TBC
    # """

    # MATILLION_COMPONENT: ClassVar[RelationField] = RelationField("matillionComponent")
    # """
    # TBC
    # """
    # AIRFLOW_TASKS: ClassVar[RelationField] = RelationField("airflowTasks")
    # """
    # TBC
    # """
    # COLUMN_PROCESSES: ClassVar[RelationField] = RelationField("columnProcesses")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "inputs",
        "outputs",
        "code",
        "sql",
        "ast",
        "matillion_component",
        "airflow_tasks",
        "column_processes",
    ]

    @property
    def inputs(self) -> Optional[list[Catalog]]:
        return None if self.attributes is None else self.attributes.inputs

    @inputs.setter
    def inputs(self, inputs: Optional[list[Catalog]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.inputs = inputs

    @property
    def outputs(self) -> Optional[list[Catalog]]:
        return None if self.attributes is None else self.attributes.outputs

    @outputs.setter
    def outputs(self, outputs: Optional[list[Catalog]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.outputs = outputs

    @property
    def code(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.code

    @code.setter
    def code(self, code: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.code = code

    @property
    def sql(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.sql

    @sql.setter
    def sql(self, sql: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sql = sql

    @property
    def ast(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.ast

    @ast.setter
    def ast(self, ast: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.ast = ast

    # @property
    # def matillion_component(self) -> Optional[MatillionComponent]:
    #     return None if self.attributes is None else self.attributes.matillion_component

    # @matillion_component.setter
    # def matillion_component(self, matillion_component: Optional[MatillionComponent]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.matillion_component = matillion_component

    @property
    def airflow_tasks(self) -> Optional[list[AirflowTask]]:
        return None if self.attributes is None else self.attributes.airflow_tasks

    @airflow_tasks.setter
    def airflow_tasks(self, airflow_tasks: Optional[list[AirflowTask]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.airflow_tasks = airflow_tasks

    @property
    def column_processes(self) -> Optional[list[ColumnProcess]]:
        return None if self.attributes is None else self.attributes.column_processes

    @column_processes.setter
    def column_processes(self, column_processes: Optional[list[ColumnProcess]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.column_processes = column_processes

    class Attributes(Asset.Attributes):
        inputs: Optional[list[Catalog]] = Field(None, description="", alias="inputs")
        outputs: Optional[list[Catalog]] = Field(None, description="", alias="outputs")
        code: Optional[str] = Field(None, description="", alias="code")
        sql: Optional[str] = Field(None, description="", alias="sql")
        ast: Optional[str] = Field(None, description="", alias="ast")
        # matillion_component: Optional[MatillionComponent] = Field(
        #     None, description="", alias="matillionComponent"
        # )  # relationship
        airflow_tasks: Optional[list[AirflowTask]] = Field(
            None, description="", alias="airflowTasks"
        )  # relationship
        column_processes: Optional[list[ColumnProcess]] = Field(
            None, description="", alias="columnProcesses"
        )  # relationship

        @staticmethod
        def generate_qualified_name(
            name: str,
            connection_qualified_name: str,
            inputs: list[Catalog],
            outputs: list[Catalog],
            parent: Optional[Process] = None,
            process_id: Optional[str] = None,
        ) -> str:
            if process_id and process_id.strip():
                return f"{connection_qualified_name}/{process_id}"
            return "blah"

    attributes: Process.Attributes = Field(
        default_factory=lambda: Process.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from ..catalog.catalog import Catalog  # noqa: E402
from ..airflow_task import AirflowTask  # noqa: E402
from ..column_process import ColumnProcess  # noqa: E402
