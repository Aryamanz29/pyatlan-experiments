from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field, validator

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField
from pyatlan.model.enums import IconType

from .resource import Resource


class Link(Resource):
    """Description"""

    # @classmethod
    # # @validate_arguments()
    # @init_guid
    # def create(
    #     cls, *, asset: Asset, name: str, link: str, idempotent: bool = False
    # ) -> Link:
    #     return Link(
    #         attributes=Link.Attributes.create(
    #             asset=asset, name=name, link=link, idempotent=idempotent
    #         )
    #     )

    # type_name: str = Field("Link", allow_mutation=False)

    @validator("type_name")
    def validate_type_name(cls, v):
        if v != "Link":
            raise ValueError("must be Link")
        return v

    def __setattr__(self, name, value):
        if name in Link._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # ICON: ClassVar[KeywordField] = KeywordField("icon", "icon")
    # """
    # Icon for the link.
    # """
    # ICON_TYPE: ClassVar[KeywordField] = KeywordField("iconType", "iconType")
    # """
    # Type of icon for the link, for example: image or emoji.
    # """

    # ASSET: ClassVar[RelationField] = RelationField("asset")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "icon",
        "icon_type",
        "asset",
    ]

    @property
    def icon(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.icon

    @icon.setter
    def icon(self, icon: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.icon = icon

    @property
    def icon_type(self) -> Optional[IconType]:
        return None if self.attributes is None else self.attributes.icon_type

    @icon_type.setter
    def icon_type(self, icon_type: Optional[IconType]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.icon_type = icon_type

    @property
    def asset(self) -> Optional[Asset]:
        return None if self.attributes is None else self.attributes.asset

    @asset.setter
    def asset(self, asset: Optional[Asset]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.asset = asset

    class Attributes(Resource.Attributes):
        icon: Optional[str] = Field(None, description="", alias="icon")
        icon_type: Optional[IconType] = Field(None, description="", alias="iconType")
        asset: Optional[Asset] = Field(
            None, description="", alias="asset"
        )  # relationship

        # @classmethod
        # # @validate_arguments()
        # @init_guid
        # def create(
        #     cls, *, asset: Asset, name: str, link: str, idempotent: bool
        # ) -> Link.Attributes:
        #     validate_required_fields(["asset", "name", "link"], [asset, name, link])
        #     qn = f"{asset.qualified_name}/{name}" if idempotent else str(uuid.uuid4())
        #     return Link.Attributes(
        #         qualified_name=qn,
        #         name=name,
        #         link=link,
        #         asset=asset.trim_to_reference(),
        #     )

    attributes: "Link.Attributes" = Field(
        default_factory=lambda: Link.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .asset import Asset  # noqa: E402