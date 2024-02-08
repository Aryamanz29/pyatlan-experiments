from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, BooleanField

from .sql import SQL


class SnowflakeStream(SQL):
    """Description"""

    type_name: str = Field("SnowflakeStream", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "SnowflakeStream":
            raise ValueError("must be SnowflakeStream")
        return v

    def __setattr__(self, name, value):
        if name in SnowflakeStream._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SNOWFLAKE_STREAM_TYPE: ClassVar[KeywordField] = KeywordField(
    #     "snowflakeStreamType", "snowflakeStreamType"
    # )
    # """
    # Type of this stream, for example: standard, append-only, insert-only, etc.
    # """
    # SNOWFLAKE_STREAM_SOURCE_TYPE: ClassVar[KeywordField] = KeywordField(
    #     "snowflakeStreamSourceType", "snowflakeStreamSourceType"
    # )
    # """
    # Type of the source of this stream.
    # """
    # SNOWFLAKE_STREAM_MODE: ClassVar[KeywordField] = KeywordField(
    #     "snowflakeStreamMode", "snowflakeStreamMode"
    # )
    # """
    # Mode of this stream.
    # """
    # SNOWFLAKE_STREAM_IS_STALE: ClassVar[BooleanField] = BooleanField(
    #     "snowflakeStreamIsStale", "snowflakeStreamIsStale"
    # )
    # """
    # Whether this stream is stale (true) or not (false).
    # """
    # SNOWFLAKE_STREAM_STALE_AFTER: ClassVar[NumericField] = NumericField(
    #     "snowflakeStreamStaleAfter", "snowflakeStreamStaleAfter"
    # )
    # """
    # Time (epoch) after which this stream will be stale, in milliseconds.
    # """

    # ATLAN_SCHEMA: ClassVar[RelationField] = RelationField("atlanSchema")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "snowflake_stream_type",
        "snowflake_stream_source_type",
        "snowflake_stream_mode",
        "snowflake_stream_is_stale",
        "snowflake_stream_stale_after",
        "atlan_schema",
    ]

    @property
    def snowflake_stream_type(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.snowflake_stream_type
        )

    @snowflake_stream_type.setter
    def snowflake_stream_type(self, snowflake_stream_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_stream_type = snowflake_stream_type

    @property
    def snowflake_stream_source_type(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.snowflake_stream_source_type
        )

    @snowflake_stream_source_type.setter
    def snowflake_stream_source_type(self, snowflake_stream_source_type: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_stream_source_type = snowflake_stream_source_type

    @property
    def snowflake_stream_mode(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.snowflake_stream_mode
        )

    @snowflake_stream_mode.setter
    def snowflake_stream_mode(self, snowflake_stream_mode: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_stream_mode = snowflake_stream_mode

    @property
    def snowflake_stream_is_stale(self) -> Optional[bool]:
        return (
            None
            if self.attributes is None
            else self.attributes.snowflake_stream_is_stale
        )

    @snowflake_stream_is_stale.setter
    def snowflake_stream_is_stale(self, snowflake_stream_is_stale: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_stream_is_stale = snowflake_stream_is_stale

    @property
    def snowflake_stream_stale_after(self) -> Optional[datetime]:
        return (
            None
            if self.attributes is None
            else self.attributes.snowflake_stream_stale_after
        )

    @snowflake_stream_stale_after.setter
    def snowflake_stream_stale_after(
        self, snowflake_stream_stale_after: Optional[datetime]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.snowflake_stream_stale_after = snowflake_stream_stale_after

    @property
    def atlan_schema(self) -> Optional[Schema]:
        return None if self.attributes is None else self.attributes.atlan_schema

    @atlan_schema.setter
    def atlan_schema(self, atlan_schema: Optional[Schema]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.atlan_schema = atlan_schema

    class Attributes(SQL.Attributes):
        snowflake_stream_type: Optional[str] = Field(
            None, description="", alias="snowflakeStreamType"
        )
        snowflake_stream_source_type: Optional[str] = Field(
            None, description="", alias="snowflakeStreamSourceType"
        )
        snowflake_stream_mode: Optional[str] = Field(
            None, description="", alias="snowflakeStreamMode"
        )
        snowflake_stream_is_stale: Optional[bool] = Field(
            None, description="", alias="snowflakeStreamIsStale"
        )
        snowflake_stream_stale_after: Optional[datetime] = Field(
            None, description="", alias="snowflakeStreamStaleAfter"
        )
        atlan_schema: Optional[Schema] = Field(
            None, description="", alias="atlanSchema"
        )  # relationship

    attributes: "SnowflakeStream.Attributes" = Field(
        default_factory=lambda: SnowflakeStream.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from datetime import datetime  # noqa: E402
from .schema import Schema  # noqa: E402
