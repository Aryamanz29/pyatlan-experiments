from __future__ import annotations

from typing import ClassVar, Optional

from pydantic.v1 import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .asset import Asset


class AtlasGlossaryCategory(Asset):
    """Description"""

    @classmethod
    def can_be_archived(self) -> bool:
        """
        Indicates if an asset can be archived via the asset.delete_by_guid method.
        :returns: True if archiving is supported
        """
        return False

    def _set_qualified_name_fallback(cls, values):
        if (
            "attributes" in values
            and values["attributes"]
            and not values["attributes"].qualified_name
        ):
            values["attributes"].qualified_name = values["guid"]
        return values

    def trim_to_required(self) -> AtlasGlossaryCategory:
        if self.anchor is None or not self.anchor.guid:
            raise ValueError("anchor.guid must be available")
        return self.create_for_modification(
            qualified_name=self.qualified_name or "",
            name=self.name or "",
            glossary_guid=self.anchor.guid,
        )

    # ANCHOR: ClassVar[KeywordField] = KeywordField("anchor", "__glossary")
    # """Glossary in which the category is contained, searchable by the qualifiedName of the glossary."""
    # PARENT_CATEGORY: ClassVar[KeywordField] = KeywordField(
    #     "parentCategory", "__parentCategory"
    # )
    # """Parent category in which a subcategory is contained, searchable by the qualifiedName of the category."""

    type_name: str = Field("AtlasGlossaryCategory")  #, allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "AtlasGlossaryCategory":
            raise ValueError("must be AtlasGlossaryCategory")
        return v

    def __setattr__(self, name, value):
        if name in AtlasGlossaryCategory._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # SHORT_DESCRIPTION: ClassVar[KeywordField] = KeywordField(
    #     "shortDescription", "shortDescription"
    # )
    # """
    # TBC
    # """
    # LONG_DESCRIPTION: ClassVar[KeywordField] = KeywordField(
    #     "longDescription", "longDescription"
    # )
    # """
    # TBC
    # """
    # ADDITIONAL_ATTRIBUTES: ClassVar[KeywordField] = KeywordField(
    #     "additionalAttributes", "additionalAttributes"
    # )
    # """
    # TBC
    # """
    # CATEGORY_TYPE: ClassVar[KeywordField] = KeywordField("categoryType", "categoryType")
    # """
    # TBC
    # """
    # TERMS: ClassVar[RelationField] = RelationField("terms")
    # """
    # TBC
    # """
    # CHILDREN_CATEGORIES: ClassVar[RelationField] = RelationField("childrenCategories")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "short_description",
        "long_description",
        "additional_attributes",
        "category_type",
        "terms",
        "anchor",
        "parent_category",
        "children_categories",
    ]

    @property
    def short_description(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.short_description

    @short_description.setter
    def short_description(self, short_description: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.short_description = short_description

    @property
    def long_description(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.long_description

    @long_description.setter
    def long_description(self, long_description: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.long_description = long_description

    @property
    def additional_attributes(self) -> Optional[dict[str, str]]:
        return (
            None if self.attributes is None else self.attributes.additional_attributes
        )

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes: Optional[dict[str, str]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.additional_attributes = additional_attributes

    @property
    def terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.terms

    @terms.setter
    def terms(self, terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.terms = terms

    @property
    def anchor(self) -> Optional[AtlasGlossary]:
        return None if self.attributes is None else self.attributes.anchor

    @anchor.setter
    def anchor(self, anchor: Optional[AtlasGlossary]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.anchor = anchor

    @property
    def parent_category(self) -> Optional[AtlasGlossaryCategory]:
        return None if self.attributes is None else self.attributes.parent_category

    @parent_category.setter
    def parent_category(self, parent_category: Optional[AtlasGlossaryCategory]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.parent_category = parent_category

    @property
    def children_categories(self) -> Optional[list[AtlasGlossaryCategory]]:
        return None if self.attributes is None else self.attributes.children_categories

    @children_categories.setter
    def children_categories(
        self, children_categories: Optional[list[AtlasGlossaryCategory]]
    ):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.children_categories = children_categories

    class Attributes(Asset.Attributes):
        short_description: Optional[str] = Field(
            None, description="", alias="shortDescription"
        )
        long_description: Optional[str] = Field(
            None, description="", alias="longDescription"
        )
        additional_attributes: Optional[dict[str, str]] = Field(
            None, description="", alias="additionalAttributes"
        )
        terms: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="terms"
        )  # relationship
        anchor: Optional[AtlasGlossary] = Field(
            None, description="", alias="anchor"
        )  # relationship
        parent_category: Optional[AtlasGlossaryCategory] = Field(
            None, description="", alias="parentCategory"
        )  # relationship
        children_categories: Optional[list[AtlasGlossaryCategory]] = Field(
            None, description="", alias="childrenCategories"
        )  # relationship

    attributes: AtlasGlossaryCategory.Attributes = Field(
        default_factory=lambda: AtlasGlossaryCategory.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .atlas_glossary import AtlasGlossary  # noqa: E402
from .atlas_glossary_term import AtlasGlossaryTerm  # noqa: E402
