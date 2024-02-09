from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

from .resource import Resource


class Readme(Resource):
    """Description"""

    @property
    def description(self) -> Optional[str]:
        return self.attributes.description

    @description.setter
    def description(self, description: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.description = description

    type_name: str = Field("Readme", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Readme":
            raise ValueError("must be Readme")
        return v

    def __setattr__(self, name, value):
        if name in Readme._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SEE_ALSO: ClassVar[RelationField] = RelationField("seeAlso")
    # """
    # TBC
    # """
    # ASSET: ClassVar[RelationField] = RelationField("asset")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "see_also",
        "asset",
    ]

    @property
    def see_also(self) -> Optional[list[Readme]]:
        return None if self.attributes is None else self.attributes.see_also

    @see_also.setter
    def see_also(self, see_also: Optional[list[Readme]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.see_also = see_also

    @property
    def asset(self) -> Optional[Asset]:
        return None if self.attributes is None else self.attributes.asset

    @asset.setter
    def asset(self, asset: Optional[Asset]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.asset = asset

    class Attributes(Resource.Attributes):
        see_also: Optional[list[Readme]] = Field(
            None, description="", alias="seeAlso"
        )  # relationship
        asset: Optional[Asset] = Field(
            None, description="", alias="asset"
        )  # relationship

    attributes: Readme.Attributes = Field(
        default_factory=lambda: Readme.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .base.asset import Asset  # noqa: E402
