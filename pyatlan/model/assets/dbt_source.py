from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .dbt import Dbt


class DbtSource(Dbt):
    """Description"""

    type_name: str = Field("DbtSource", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "DbtSource":
            raise ValueError("must be DbtSource")
        return v

    def __setattr__(self, name, value):
        if name in DbtSource._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # DBT_STATE: ClassVar[KeywordField] = KeywordField("dbtState", "dbtState")
    # """

    # """
    # DBT_FRESHNESS_CRITERIA: ClassVar[KeywordField] = KeywordField(
    #     "dbtFreshnessCriteria", "dbtFreshnessCriteria"
    # )
    # """

    # """

    # SQL_ASSETS: ClassVar[RelationField] = RelationField("sqlAssets")
    # """
    # TBC
    # """
    # DBT_TESTS: ClassVar[RelationField] = RelationField("dbtTests")
    # """
    # TBC
    # """
    # SQL_ASSET: ClassVar[RelationField] = RelationField("sqlAsset")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "dbt_state",
        "dbt_freshness_criteria",
        "sql_assets",
        "dbt_tests",
        "sql_asset",
    ]

    @property
    def dbt_state(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.dbt_state

    @dbt_state.setter
    def dbt_state(self, dbt_state: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_state = dbt_state

    @property
    def dbt_freshness_criteria(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.dbt_freshness_criteria
        )

    @dbt_freshness_criteria.setter
    def dbt_freshness_criteria(self, dbt_freshness_criteria: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_freshness_criteria = dbt_freshness_criteria

    @property
    def sql_assets(self) -> Optional[list[SQL]]:
        return None if self.attributes is None else self.attributes.sql_assets

    @sql_assets.setter
    def sql_assets(self, sql_assets: Optional[list[SQL]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sql_assets = sql_assets

    @property
    def dbt_tests(self) -> Optional[list[DbtTest]]:
        return None if self.attributes is None else self.attributes.dbt_tests

    @dbt_tests.setter
    def dbt_tests(self, dbt_tests: Optional[list[DbtTest]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.dbt_tests = dbt_tests

    @property
    def sql_asset(self) -> Optional[SQL]:
        return None if self.attributes is None else self.attributes.sql_asset

    @sql_asset.setter
    def sql_asset(self, sql_asset: Optional[SQL]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.sql_asset = sql_asset

    class Attributes(Dbt.Attributes):
        dbt_state: Optional[str] = Field(None, description="", alias="dbtState")
        dbt_freshness_criteria: Optional[str] = Field(
            None, description="", alias="dbtFreshnessCriteria"
        )
        sql_assets: Optional[list[SQL]] = Field(
            None, description="", alias="sqlAssets"
        )  # relationship
        dbt_tests: Optional[list[DbtTest]] = Field(
            None, description="", alias="dbtTests"
        )  # relationship
        sql_asset: Optional[SQL] = Field(
            None, description="", alias="sqlAsset"
        )  # relationship

    attributes: "DbtSource.Attributes" = Field(
        default_factory=lambda: DbtSource.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .sql import SQL  # noqa: E402
from .dbt_test import DbtTest  # noqa: E402