from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .sql import SQL


class Query(SQL):
    """Description"""

    type_name: str = Field("Query", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Query":
            raise ValueError("must be Query")
        return v

    def __setattr__(self, name, value):
        if name in Query._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # RAW_QUERY: ClassVar[KeywordField] = KeywordField("rawQuery", "rawQuery")
    # """
    # TBC
    # """
    # LONG_RAW_QUERY: ClassVar[KeywordField] = KeywordField(
    #     "longRawQuery", "longRawQuery"
    # )
    # """
    # TBC
    # """
    # RAW_QUERY_TEXT: ClassVar[RelationField] = RelationField("rawQueryText")
    # """
    # TBC
    # """
    # DEFAULT_SCHEMA_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "defaultSchemaQualifiedName",
    #     "defaultSchemaQualifiedName",
    #     "defaultSchemaQualifiedName.text",
    # )
    # """
    # TBC
    # """
    # DEFAULT_DATABASE_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "defaultDatabaseQualifiedName",
    #     "defaultDatabaseQualifiedName",
    #     "defaultDatabaseQualifiedName.text",
    # )
    # """
    # TBC
    # """
    # VARIABLES_SCHEMA_BASE64: ClassVar[KeywordField] = KeywordField(
    #     "variablesSchemaBase64", "variablesSchemaBase64"
    # )
    # """
    # TBC
    # """
    # IS_PRIVATE: ClassVar[BooleanField] = BooleanField("isPrivate", "isPrivate")
    # """
    # TBC
    # """
    # IS_SQL_SNIPPET: ClassVar[BooleanField] = BooleanField(
    #     "isSqlSnippet", "isSqlSnippet"
    # )
    # """
    # TBC
    # """
    # PARENT_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "parentQualifiedName", "parentQualifiedName", "parentQualifiedName.text"
    # )
    # """
    # TBC
    # """
    # COLLECTION_QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "collectionQualifiedName",
    #     "collectionQualifiedName",
    #     "collectionQualifiedName.text",
    # )
    # """
    # TBC
    # """
    # IS_VISUAL_QUERY: ClassVar[BooleanField] = BooleanField(
    #     "isVisualQuery", "isVisualQuery"
    # )
    # """
    # TBC
    # """
    # VISUAL_BUILDER_SCHEMA_BASE64: ClassVar[KeywordField] = KeywordField(
    #     "visualBuilderSchemaBase64", "visualBuilderSchemaBase64"
    # )
    # """
    # TBC
    # """

    # PARENT: ClassVar[RelationField] = RelationField("parent")
    # """
    # TBC
    # """
    # COLUMNS: ClassVar[RelationField] = RelationField("columns")
    # """
    # TBC
    # """
    # TABLES: ClassVar[RelationField] = RelationField("tables")
    # """
    # TBC
    # """
    # VIEWS: ClassVar[RelationField] = RelationField("views")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "raw_query",
        "long_raw_query",
        "raw_query_text",
        "default_schema_qualified_name",
        "default_database_qualified_name",
        "variables_schema_base64",
        "is_private",
        "is_sql_snippet",
        "parent_qualified_name",
        "collection_qualified_name",
        "is_visual_query",
        "visual_builder_schema_base64",
        "parent",
        "columns",
        "tables",
        "views",
    ]

    @property
    def raw_query(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.raw_query

    @raw_query.setter
    def raw_query(self, raw_query: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.raw_query = raw_query

    @property
    def long_raw_query(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.long_raw_query

    @long_raw_query.setter
    def long_raw_query(self, long_raw_query: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.long_raw_query = long_raw_query

    @property
    def raw_query_text(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.raw_query_text

    @raw_query_text.setter
    def raw_query_text(self, raw_query_text: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.raw_query_text = raw_query_text

    @property
    def default_schema_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.default_schema_qualified_name
        )

    @default_schema_qualified_name.setter
    def default_schema_qualified_name(
        self, default_schema_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.default_schema_qualified_name = default_schema_qualified_name

    @property
    def default_database_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.default_database_qualified_name
        )

    @default_database_qualified_name.setter
    def default_database_qualified_name(
        self, default_database_qualified_name: Optional[str]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.default_database_qualified_name = (
            default_database_qualified_name
        )

    @property
    def variables_schema_base64(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.variables_schema_base64
        )

    @variables_schema_base64.setter
    def variables_schema_base64(self, variables_schema_base64: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.variables_schema_base64 = variables_schema_base64

    @property
    def is_private(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_private

    @is_private.setter
    def is_private(self, is_private: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_private = is_private

    @property
    def is_sql_snippet(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_sql_snippet

    @is_sql_snippet.setter
    def is_sql_snippet(self, is_sql_snippet: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_sql_snippet = is_sql_snippet

    @property
    def parent_qualified_name(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.parent_qualified_name
        )

    @parent_qualified_name.setter
    def parent_qualified_name(self, parent_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_qualified_name = parent_qualified_name

    @property
    def collection_qualified_name(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.collection_qualified_name
        )

    @collection_qualified_name.setter
    def collection_qualified_name(self, collection_qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.collection_qualified_name = collection_qualified_name

    @property
    def is_visual_query(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_visual_query

    @is_visual_query.setter
    def is_visual_query(self, is_visual_query: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_visual_query = is_visual_query

    @property
    def visual_builder_schema_base64(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.visual_builder_schema_base64
        )

    @visual_builder_schema_base64.setter
    def visual_builder_schema_base64(self, visual_builder_schema_base64: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.visual_builder_schema_base64 = visual_builder_schema_base64

    @property
    def parent(self) -> Optional[Namespace]:
        return None if self.attributes is None else self.attributes.parent

    @parent.setter
    def parent(self, parent: Optional[Namespace]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent = parent

    @property
    def columns(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.columns

    @columns.setter
    def columns(self, columns: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.columns = columns

    @property
    def tables(self) -> Optional[list[Table]]:
        return None if self.attributes is None else self.attributes.tables

    @tables.setter
    def tables(self, tables: Optional[list[Table]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.tables = tables

    # @property
    # def views(self) -> Optional[list[View]]:
    #     return None if self.attributes is None else self.attributes.views

    # @views.setter
    # def views(self, views: Optional[list[View]]):
    #     if self.attributes is None:
    #         self.attributes = self.Attributes()
    #     self.attributes.views = views

    class Attributes(SQL.Attributes):
        raw_query: Optional[str] = Field(None, description="", alias="rawQuery")
        long_raw_query: Optional[str] = Field(
            None, description="", alias="longRawQuery"
        )
        raw_query_text: Optional[str] = Field(
            None, description="", alias="rawQueryText"
        )
        default_schema_qualified_name: Optional[str] = Field(
            None, description="", alias="defaultSchemaQualifiedName"
        )
        default_database_qualified_name: Optional[str] = Field(
            None, description="", alias="defaultDatabaseQualifiedName"
        )
        variables_schema_base64: Optional[str] = Field(
            None, description="", alias="variablesSchemaBase64"
        )
        is_private: Optional[bool] = Field(None, description="", alias="isPrivate")
        is_sql_snippet: Optional[bool] = Field(
            None, description="", alias="isSqlSnippet"
        )
        parent_qualified_name: Optional[str] = Field(
            None, description="", alias="parentQualifiedName"
        )
        collection_qualified_name: Optional[str] = Field(
            None, description="", alias="collectionQualifiedName"
        )
        is_visual_query: Optional[bool] = Field(
            None, description="", alias="isVisualQuery"
        )
        visual_builder_schema_base64: Optional[str] = Field(
            None, description="", alias="visualBuilderSchemaBase64"
        )
        parent: Optional[Namespace] = Field(
            None, description="", alias="parent"
        )  # relationship
        columns: Optional[list[Column]] = Field(
            None, description="", alias="columns"
        )  # relationship
        tables: Optional[list[Table]] = Field(
            None, description="", alias="tables"
        )  # relationship
        # views: Optional[list[View]] = Field(
        #     None, description="", alias="views"
        # )  # relationship

    attributes: Query.Attributes = Field(
        default_factory=lambda: Query.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .namespace import Namespace  # noqa: E402
from .column import Column  # noqa: E402
from .table import Table  # noqa: E402
