from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .catalog import Catalog


class Resource(Catalog):
    """Description"""

    type_name: str = Field("Resource")  #, allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Resource":
            raise ValueError("must be Resource")
        return v

    def __setattr__(self, name, value):
        if name in Resource._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # LINK: ClassVar[KeywordField] = KeywordField("link", "link")
    # """
    # TBC
    # """
    # IS_GLOBAL: ClassVar[BooleanField] = BooleanField("isGlobal", "isGlobal")
    # """
    # TBC
    # """
    # REFERENCE: ClassVar[KeywordField] = KeywordField("reference", "reference")
    # """
    # TBC
    # """
    # RESOURCE_METADATA: ClassVar[KeywordField] = KeywordField(
    #     "resourceMetadata", "resourceMetadata"
    # )
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "link",
        "is_global",
        "reference",
        "resource_metadata",
    ]

    @property
    def link(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.link

    @link.setter
    def link(self, link: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.link = link

    @property
    def is_global(self) -> Optional[bool]:
        return None if self.attributes is None else self.attributes.is_global

    @is_global.setter
    def is_global(self, is_global: Optional[bool]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.is_global = is_global

    @property
    def reference(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.reference

    @reference.setter
    def reference(self, reference: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.reference = reference

    @property
    def resource_metadata(self) -> Optional[dict[str, str]]:
        return None if self.attributes is None else self.attributes.resource_metadata

    @resource_metadata.setter
    def resource_metadata(self, resource_metadata: Optional[dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.resource_metadata = resource_metadata

    class Attributes(Catalog.Attributes):
        link: Optional[str] = Field(None, description="", alias="link")
        is_global: Optional[bool] = Field(None, description="", alias="isGlobal")
        reference: Optional[str] = Field(None, description="", alias="reference")
        resource_metadata: Optional[dict[str, str]] = Field(
            None, description="", alias="resourceMetadata"
        )

    attributes: Resource.Attributes = Field(
        default_factory=lambda: Resource.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )
