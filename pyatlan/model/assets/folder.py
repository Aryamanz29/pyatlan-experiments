from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .namespace import Namespace


class Folder(Namespace):
    """Description"""

    type_name: str = Field("Folder")  #, allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Folder":
            raise ValueError("must be Folder")
        return v

    def __setattr__(self, name, value):
        if name in Folder._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

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

    # PARENT: ClassVar[RelationField] = RelationField("parent")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "parent_qualified_name",
        "collection_qualified_name",
        "parent",
    ]

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
    def parent(self) -> Optional[Namespace]:
        return None if self.attributes is None else self.attributes.parent

    @parent.setter
    def parent(self, parent: Optional[Namespace]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent = parent

    class Attributes(Namespace.Attributes):
        parent_qualified_name: Optional[str] = Field(
            None, description="", alias="parentQualifiedName"
        )
        collection_qualified_name: Optional[str] = Field(
            None, description="", alias="collectionQualifiedName"
        )
        parent: Optional[Namespace] = Field(
            None, description="", alias="parent"
        )  # relationship

    attributes: Folder.Attributes = Field(
        default_factory=lambda: Folder.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )
