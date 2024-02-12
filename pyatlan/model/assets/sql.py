from __future__ import annotations

from datetime import datetime
from typing import ClassVar, Optional

from pydantic.v1 import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .catalog import Catalog


class SQL(Catalog):
    """Description"""

    type_name: str = Field("SQL")  #, allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "SQL":
            raise ValueError("must be SQL")
        return v

    def __setattr__(self, name, value):
        if name in SQL._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # QUERY_COUNT: ClassVar[NumericField] = NumericField("queryCount", "queryCount")
    # """
    # TBC
    # """
    # QUERY_USER_COUNT: ClassVar[NumericField] = NumericField(
    #     "queryUserCount", "queryUserCount"
    # )
    # """
    # TBC
    # """
    # QUERY_USER_MAP: ClassVar[KeywordField] = KeywordField(
    #     "queryUserMap", "queryUserMap"
    # )
    # """
    # TBC
    # """
    # QUERY_COUNT_UPDATED_AT: ClassVar[NumericField] = NumericField(
    #     "queryCountUpdatedAt", "queryCountUpdatedAt"
    # )
    # """
    # TBC
    # """
    # DATABASE_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "databaseName", "databaseName.keyword", "databaseName"
    # )
    # """
    # TBC
    # """
    # DATABASE_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
    #     "databaseQualifiedName", "databaseQualifiedName"
    # )
    # """
    # TBC
    # """
    # SCHEMA_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "schemaName", "schemaName.keyword", "schemaName"
    # )
    # """
    # TBC
    # """
    # SCHEMA_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
    #     "schemaQualifiedName", "schemaQualifiedName"
    # )
    # """
    # TBC
    # """
    # TABLE_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "tableName", "tableName.keyword", "tableName"
    # )
    # """
    # TBC
    # """
    # TABLE_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
    #     "tableQualifiedName", "tableQualifiedName"
    # )
    # """
    # TBC
    # """
    # VIEW_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "viewName", "viewName.keyword", "viewName"
    # )
    # """
    # TBC
    # """
    # VIEW_QUALIFIED_NAME: ClassVar[KeywordField] = KeywordField(
    #     "viewQualifiedName", "viewQualifiedName"
    # )
    # """
    # TBC
    # """
    # IS_PROFILED: ClassVar[BooleanField] = BooleanField("isProfiled", "isProfiled")
    # """
    # TBC
    # """
    # LAST_PROFILED_AT: ClassVar[NumericField] = NumericField(
    #     "lastProfiledAt", "lastProfiledAt"
    # )
    # """
    # TBC
    # """

    # DBT_SOURCES: ClassVar[RelationField] = RelationField("dbtSources")
    # """
    # TBC
    # """
    # SQL_DBT_MODELS: ClassVar[RelationField] = RelationField("sqlDbtModels")
    # """
    # TBC
    # """
    # SQL_DBT_SOURCES: ClassVar[RelationField] = RelationField("sqlDBTSources")
    # """
    # TBC
    # """
    # DBT_MODELS: ClassVar[RelationField] = RelationField("dbtModels")
    # """
    # TBC
    # """
    # DBT_TESTS: ClassVar[RelationField] = RelationField("dbtTests")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "query_count",
        "query_user_count",
        "query_user_map",
        "query_count_updated_at",
        "database_name",
        "database_qualified_name",
        "schema_name",
        "schema_qualified_name",
        "table_name",
        "table_qualified_name",
        "view_name",
        "view_qualified_name",
        "is_profiled",
        "last_profiled_at",
        "dbt_sources",
        "sql_dbt_models",
        "sql_dbt_sources",
        "dbt_models",
        "dbt_tests",
    ]

    @property
    def query_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.query_count

    @query_count.setter
    def query_count(self, query_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_count = query_count

    @property
    def query_user_count(self) -> Optional[int]:
        return None if self.attributes is None else self.attributes.query_user_count

    @query_user_count.setter
    def query_user_count(self, query_user_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_user_count = query_user_count

    @property
    def query_user_map(self) -> Optional[dict[str, int]]:
        return None if self.attributes is None else self.attributes.query_user_map

    @query_user_map.setter
    def query_user_map(self, query_user_map: Optional[dict[str, int]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_user_map = query_user_map

    @property
    def query_count_updated_at(self) -> Optional[datetime]:
        return (
            None if self.attributes is None else self.attributes.query_count_updated_at
        )

    @query_count_updated_at.setter
    def query_count_updated_at(self, query_count_updated_at: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.query_count_updated_at = query_count_updated_at

    @property
    def database_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.database_name

    @database_name.setter
    def database_name(self, database_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.database_name = database_name

    @property
    def database_qualified_name(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.database_qualified_name
        )

    @database_qualified_name.setter
    def database_qualified_name(self, database_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.database_qualified_name = database_qualified_name

    @property
    def schema_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.schema_name

    @schema_name.setter
    def schema_name(self, schema_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.schema_name = schema_name

    @property
    def schema_qualified_name(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.schema_qualified_name
        )

    @schema_qualified_name.setter
    def schema_qualified_name(self, schema_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.schema_qualified_name = schema_qualified_name

    @property
    def table_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.table_name

    @table_name.setter
    def table_name(self, table_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.table_name = table_name

    @property
    def table_qualified_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.table_qualified_name

    @table_qualified_name.setter
    def table_qualified_name(self, table_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.table_qualified_name = table_qualified_name

    @property
    def view_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.view_name

    @view_name.setter
    def view_name(self, view_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.view_name = view_name

    @property
    def view_qualified_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.view_qualified_name

    @view_qualified_name.setter
    def view_qualified_name(self, view_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.view_qualified_name = view_qualified_name

    @property
    def is_profiled(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_profiled

    @is_profiled.setter
    def is_profiled(self, is_profiled: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_profiled = is_profiled

    @property
    def last_profiled_at(self) -> Optional[datetime]:
        return None if self.attributes is None else self.attributes.last_profiled_at

    @last_profiled_at.setter
    def last_profiled_at(self, last_profiled_at: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.last_profiled_at = last_profiled_at

    # @property
    # def dbt_sources(self) -> Optional[list[DbtSource]]:
    #     return None if self.attributes is None else self.attributes.dbt_sources

    # @dbt_sources.setter
    # def dbt_sources(self, dbt_sources: Optional[list[DbtSource]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.dbt_sources = dbt_sources

    # @property
    # def sql_dbt_models(self) -> Optional[list[DbtModel]]:
    #     return None if self.attributes is None else self.attributes.sql_dbt_models

    # @sql_dbt_models.setter
    # def sql_dbt_models(self, sql_dbt_models: Optional[list[DbtModel]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.sql_dbt_models = sql_dbt_models

    # @property
    # def sql_dbt_sources(self) -> Optional[list[DbtSource]]:
    #     return None if self.attributes is None else self.attributes.sql_dbt_sources

    # @sql_dbt_sources.setter
    # def sql_dbt_sources(self, sql_dbt_sources: Optional[list[DbtSource]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.sql_dbt_sources = sql_dbt_sources

    # @property
    # def dbt_models(self) -> Optional[list[DbtModel]]:
    #     return None if self.attributes is None else self.attributes.dbt_models

    # @dbt_models.setter
    # def dbt_models(self, dbt_models: Optional[list[DbtModel]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.dbt_models = dbt_models

    # @property
    # def dbt_tests(self) -> Optional[list[DbtTest]]:
    #     return None if self.attributes is None else self.attributes.dbt_tests

    # @dbt_tests.setter
    # def dbt_tests(self, dbt_tests: Optional[list[DbtTest]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.dbt_tests = dbt_tests

    class Attributes(Catalog.Attributes):
        query_count: Optional[int] = Field(None, description="", alias="queryCount")
        query_user_count: Optional[int] = Field(
            None, description="", alias="queryUserCount"
        )
        query_user_map: Optional[dict[str, int]] = Field(
            None, description="", alias="queryUserMap"
        )
        query_count_updated_at: Optional[datetime] = Field(
            None, description="", alias="queryCountUpdatedAt"
        )
        database_name: Optional[str] = Field(None, description="", alias="databaseName")
        database_qualified_name: Optional[str] = Field(
            None, description="", alias="databaseQualifiedName"
        )
        schema_name: Optional[str] = Field(None, description="", alias="schemaName")
        schema_qualified_name: Optional[str] = Field(
            None, description="", alias="schemaQualifiedName"
        )
        table_name: Optional[str] = Field(None, description="", alias="tableName")
        table_qualified_name: Optional[str] = Field(
            None, description="", alias="tableQualifiedName"
        )
        view_name: Optional[str] = Field(None, description="", alias="viewName")
        view_qualified_name: Optional[str] = Field(
            None, description="", alias="viewQualifiedName"
        )
        is_profiled: Optional[bool] = Field(None, description="", alias="isProfiled")
        last_profiled_at: Optional[datetime] = Field(
            None, description="", alias="lastProfiledAt"
        )
        # dbt_sources: Optional[list[DbtSource]] = Field(
        #     None, description="", alias="dbtSources"
        # )  # relationship
        # sql_dbt_models: Optional[list[DbtModel]] = Field(
        #     None, description="", alias="sqlDbtModels"
        # )  # relationship
        # sql_dbt_sources: Optional[list[DbtSource]] = Field(
        #     None, description="", alias="sqlDBTSources"
        # )  # relationship
        # dbt_models: Optional[list[DbtModel]] = Field(
        #     None, description="", alias="dbtModels"
        # )  # relationship
        # dbt_tests: Optional[list[DbtTest]] = Field(
        #     None, description="", alias="dbtTests"
        # )  # relationship

    attributes: SQL.Attributes = Field(
        default_factory=lambda: SQL.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )
