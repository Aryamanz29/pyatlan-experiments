from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, NumericField, RelationField

from .soda import Soda


class SodaCheck(Soda):
    """Description"""

    type_name: str = Field("SodaCheck", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "SodaCheck":
            raise ValueError("must be SodaCheck")
        return v

    def __setattr__(self, name, value):
        if name in SodaCheck._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SODA_CHECK_ID: ClassVar[KeywordField] = KeywordField("sodaCheckId", "sodaCheckId")
    # """
    # Identifier of the check in Soda.
    # """
    # SODA_CHECK_EVALUATION_STATUS: ClassVar[KeywordField] = KeywordField(
    #     "sodaCheckEvaluationStatus", "sodaCheckEvaluationStatus"
    # )
    # """
    # Status of the check in Soda.
    # """
    # SODA_CHECK_DEFINITION: ClassVar[KeywordField] = KeywordField(
    #     "sodaCheckDefinition", "sodaCheckDefinition"
    # )
    # """
    # Definition of the check in Soda.
    # """
    # SODA_CHECK_LAST_SCAN_AT: ClassVar[NumericField] = NumericField(
    #     "sodaCheckLastScanAt", "sodaCheckLastScanAt"
    # )
    # """

    # """
    # SODA_CHECK_INCIDENT_COUNT: ClassVar[NumericField] = NumericField(
    #     "sodaCheckIncidentCount", "sodaCheckIncidentCount"
    # )
    # """

    # """

    # SODA_CHECK_COLUMNS: ClassVar[RelationField] = RelationField("sodaCheckColumns")
    # """
    # TBC
    # """
    # SODA_CHECK_ASSETS: ClassVar[RelationField] = RelationField("sodaCheckAssets")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "soda_check_id",
        "soda_check_evaluation_status",
        "soda_check_definition",
        "soda_check_last_scan_at",
        "soda_check_incident_count",
        "soda_check_columns",
        "soda_check_assets",
    ]

    @property
    def soda_check_id(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.soda_check_id

    @soda_check_id.setter
    def soda_check_id(self, soda_check_id: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_id = soda_check_id

    @property
    def soda_check_evaluation_status(self) -> Optional[str]:
        return (
            None
            if self.attributes is None
            else self.attributes.soda_check_evaluation_status
        )

    @soda_check_evaluation_status.setter
    def soda_check_evaluation_status(self, soda_check_evaluation_status: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_evaluation_status = soda_check_evaluation_status

    @property
    def soda_check_definition(self) -> Optional[str]:
        return (
            None if self.attributes is None else self.attributes.soda_check_definition
        )

    @soda_check_definition.setter
    def soda_check_definition(self, soda_check_definition: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_definition = soda_check_definition

    @property
    def soda_check_last_scan_at(self) -> Optional[datetime]:
        return (
            None if self.attributes is None else self.attributes.soda_check_last_scan_at
        )

    @soda_check_last_scan_at.setter
    def soda_check_last_scan_at(self, soda_check_last_scan_at: Optional[datetime]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_last_scan_at = soda_check_last_scan_at

    @property
    def soda_check_incident_count(self) -> Optional[int]:
        return (
            None
            if self.attributes is None
            else self.attributes.soda_check_incident_count
        )

    @soda_check_incident_count.setter
    def soda_check_incident_count(self, soda_check_incident_count: Optional[int]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_incident_count = soda_check_incident_count

    @property
    def soda_check_columns(self) -> Optional[list[Column]]:
        return None if self.attributes is None else self.attributes.soda_check_columns

    @soda_check_columns.setter
    def soda_check_columns(self, soda_check_columns: Optional[list[Column]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_columns = soda_check_columns

    @property
    def soda_check_assets(self) -> Optional[list[Asset]]:
        return None if self.attributes is None else self.attributes.soda_check_assets

    @soda_check_assets.setter
    def soda_check_assets(self, soda_check_assets: Optional[list[Asset]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.soda_check_assets = soda_check_assets

    class Attributes(Soda.Attributes):
        soda_check_id: Optional[str] = Field(None, description="", alias="sodaCheckId")
        soda_check_evaluation_status: Optional[str] = Field(
            None, description="", alias="sodaCheckEvaluationStatus"
        )
        soda_check_definition: Optional[str] = Field(
            None, description="", alias="sodaCheckDefinition"
        )
        soda_check_last_scan_at: Optional[datetime] = Field(
            None, description="", alias="sodaCheckLastScanAt"
        )
        soda_check_incident_count: Optional[int] = Field(
            None, description="", alias="sodaCheckIncidentCount"
        )
        soda_check_columns: Optional[list[Column]] = Field(
            None, description="", alias="sodaCheckColumns"
        )  # relationship
        soda_check_assets: Optional[list[Asset]] = Field(
            None, description="", alias="sodaCheckAssets"
        )  # relationship

    attributes: "SodaCheck.Attributes" = Field(
        default_factory=lambda: SodaCheck.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from datetime import datetime  # noqa: E402
from .column import Column  # noqa: E402
from .base.asset import Asset  # noqa: E402
