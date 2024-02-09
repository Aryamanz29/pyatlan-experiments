from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .base.asset import Asset


class Namespace(Asset):
    """Description"""

    type_name: str = Field("Namespace", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "Namespace":
            raise ValueError("must be Namespace")
        return v

    def __setattr__(self, name, value):
        if name in Namespace._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # CHILDREN_QUERIES: ClassVar[RelationField] = RelationField("childrenQueries")
    # """
    # TBC
    # """
    # CHILDREN_FOLDERS: ClassVar[RelationField] = RelationField("childrenFolders")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "children_queries",
        "children_folders",
    ]

    @property
    def children_queries(self) -> Optional[list[Query]]:
        return None if self.attributes is None else self.attributes.children_queries

    @children_queries.setter
    def children_queries(self, children_queries: Optional[list[Query]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.children_queries = children_queries

    @property
    def children_folders(self) -> Optional[list[Folder]]:
        return None if self.attributes is None else self.attributes.children_folders

    @children_folders.setter
    def children_folders(self, children_folders: Optional[list[Folder]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.children_folders = children_folders

    class Attributes(Asset.Attributes):
        children_queries: Optional[list[Query]] = Field(
            None, description="", alias="childrenQueries"
        )  # relationship
        children_folders: Optional[list[Folder]] = Field(
            None, description="", alias="childrenFolders"
        )  # relationship

    attributes: Namespace.Attributes = Field(
        default_factory=lambda: Namespace.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .query import Query  # noqa: E402
from .folder import Folder  # noqa: E402
