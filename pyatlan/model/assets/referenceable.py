from __future__ import annotations

from typing import Any, ClassVar, Optional

from pydantic import Field

# from .custom_metadata import CustomMetadataDict, CustomMetadataProxy
# from pyatlan.model.fields.atlan_fields import (
#     InternalKeywordField,
#     InternalKeywordTextField,
#     InternalNumericField,
#     KeywordField,
#     KeywordTextField,
#     NumericField,
# )

from .atlan_object import AtlanObject


class Referenceable(AtlanObject):
    """Description"""

    def __init__(__pydantic_self__, **data: Any) -> None:

        super().__init__(**data)
        __pydantic_self__.__fields_set__.update(["attributes", "type_name"])
        # __pydantic_self__._metadata_proxy = CustomMetadataProxy(
        #     __pydantic_self__.business_attributes
        # )

    def json(self, *args, **kwargs) -> str:
        self.business_attributes = self._metadata_proxy.business_attributes
        return super().json(**kwargs)

    def validate_required(self):
        if not self.create_time or self.created_by:
            self.attributes.validate_required()

    # def get_custom_metadata(self, name: str) -> CustomMetadataDict:
    #     return self._metadata_proxy.get_custom_metadata(name=name)

    # def set_custom_metadata(self, custom_metadata: CustomMetadataDict):
    #     return self._metadata_proxy.set_custom_metadata(custom_metadata=custom_metadata)

    # def flush_custom_metadata(self):
    #     self.business_attributes = self._metadata_proxy.business_attributes

    @classmethod
    def can_be_archived(self) -> bool:
        """
        Indicates if an asset can be archived via the asset.delete_by_guid method.
        :returns: True if archiving is supported
        """
        return True

    # @property
    # def atlan_tag_names(self) -> list[str]:
    #     from pyatlan.cache.atlan_tag_cache import AtlanTagCache
    #     from .constants import DELETED_

    #     if self.classification_names:
    #         return [
    #             AtlanTagCache.get_name_for_id(tag_id) or DELETED_
    #             for tag_id in self.classification_names
    #         ]
    #     return []

    def __setattr__(self, name, value):
        if name in Referenceable._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    _convenience_properties: ClassVar[list[str]] = [
        "qualified_name",
        "assigned_terms",
    ]

    @property
    def qualified_name(self) -> Optional[str]:
        return None if self.attributes is None else self.attributes.qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name: Optional[str]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.qualified_name = qualified_name

    @property
    def assigned_terms(self) -> Optional[list[AtlasGlossaryTerm]]:
        return None if self.attributes is None else self.attributes.meanings

    @assigned_terms.setter
    def assigned_terms(self, assigned_terms: Optional[list[AtlasGlossaryTerm]]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.meanings = assigned_terms

    class Attributes(AtlanObject):
        qualified_name: Optional[str] = Field("", description="", alias="qualifiedName")
        meanings: Optional[list[AtlasGlossaryTerm]] = Field(
            None, description="", alias="meanings"
        )  # relationship

        def validate_required(self):
            pass

    # TYPE_NAME: ClassVar[KeywordTextField] = InternalKeywordTextField(
    #     "typeName", "__typeName.keyword", "__typeName", "__typeName"
    # )
    # """Type of the asset. For example Table, Column, and so on."""
    # GUID: ClassVar[KeywordField] = InternalKeywordField("guid", "__guid", "__guid")
    # """Globally unique identifier (GUID) of any object in Atlan."""
    # CREATED_BY: ClassVar[KeywordField] = InternalKeywordField(
    #     "createdBy", "__createdBy", "__createdBy"
    # )
    # """Atlan user who created this asset."""
    # UPDATED_BY: ClassVar[KeywordField] = InternalKeywordField(
    #     "updatedBy", "__modifiedBy", "__modifiedBy"
    # )
    # """Atlan user who last updated the asset."""
    # STATUS: ClassVar[KeywordField] = InternalKeywordField(
    #     "status", "__state", "__state"
    # )
    # """Asset status in Atlan (active vs deleted)."""
    # ATLAN_TAGS: ClassVar[KeywordTextField] = InternalKeywordTextField(
    #     "classificationNames",
    #     "__traitNames",
    #     "__classificationsText",
    #     "__classificationNames",
    # )
    # """
    # All directly-assigned Atlan tags that exist on an asset, searchable by internal hashed-string ID of the Atlan tag.
    # """
    # PROPAGATED_ATLAN_TAGS: ClassVar[KeywordTextField] = InternalKeywordTextField(
    #     "classificationNames",
    #     "__propagatedTraitNames",
    #     "__classificationsText",
    #     "__propagatedClassificationNames",
    # )
    # """All propagated Atlan tags that exist on an asset, searchable by internal hashed-string ID of the Atlan tag."""
    # ASSIGNED_TERMS: ClassVar[KeywordTextField] = InternalKeywordTextField(
    #     "meanings", "__meanings", "__meaningsText", "__meanings"
    # )
    # """All terms attached to an asset, searchable by the term's qualifiedName."""
    # SUPER_TYPE_NAMES: ClassVar[KeywordTextField] = InternalKeywordTextField(
    #     "typeName", "__superTypeNames.keyword", "__superTypeNames", "__superTypeNames"
    # )
    # """All super types of an asset."""
    # CREATE_TIME: ClassVar[NumericField] = InternalNumericField(
    #     "createTime", "__timestamp", "__timestamp"
    # )
    # """Time (in milliseconds) when the asset was created."""
    # UPDATE_TIME: ClassVar[NumericField] = InternalNumericField(
    #     "updateTime", "__modificationTimestamp", "__modificationTimestamp"
    # )
    # """Time (in milliseconds) when the asset was last updated."""
    # QUALIFIED_NAME: ClassVar[KeywordTextField] = KeywordTextField(
    #     "qualifiedName", "qualifiedName", "qualifiedName.text"
    # )
    # """Unique fully-qualified name of the asset in Atlan."""

    type_name: str = Field(
        "Referenceable",
        description="Name of the type definition that defines this instance.\n",
    )
    # _metadata_proxy: CustomMetadataProxy = PrivateAttr()
    attributes: Referenceable.Attributes = Field(
        default_factory=lambda: Referenceable.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary "
        "by type, so are described in the sub-types of this schema.\n",
    )
    business_attributes: Optional[dict[str, Any]] = Field(
        None,
        description="Map of custom metadata attributes and values defined on the entity.\n",
        alias="businessAttributes",
    )
    created_by: Optional[str] = Field(
        None,
        description="Username of the user who created the object.\n",
        example="jsmith",
    )
    create_time: Optional[int] = Field(
        None,
        description="Time (epoch) at which this object was created, in milliseconds.\n",
        example=1648852296555,
    )
    delete_handler: Optional[str] = Field(
        None,
        description="Details on the handler used for deletion of the asset.",
        example="Hard",
    )
    guid: str = Field(
        "",
        description="Unique identifier of the entity instance.\n",
        example="917ffec9-fa84-4c59-8e6c-c7b114d04be3",
    )
    is_incomplete: Optional[bool] = Field(True, description="", example=True)
    labels: Optional[list[str]] = Field(None, description="Internal use only.")
    relationship_attributes: Optional[dict[str, Any]] = Field(
        None,
        description="Map of relationships for the entity. The specific keys of this map will vary by type, "
        "so are described in the sub-types of this schema.\n",
    )
    updated_by: Optional[str] = Field(
        None,
        description="Username of the user who last assets_updated the object.\n",
        example="jsmith",
    )
    update_time: Optional[int] = Field(
        None,
        description="Time (epoch) at which this object was last assets_updated, in milliseconds.\n",
        example=1649172284333,
    )
    version: Optional[int] = Field(
        None, description="Version of this object.\n", example=2
    )
    # atlan_tags: Optional[list[AtlanTag]] = Field(
    #     None, description="Atlan tags", alias="classifications"
    # )
    classification_names: Optional[list[str]] = Field(
        None, description="The names of the classifications that exist on the asset."
    )
    display_text: Optional[str] = Field(
        None,
        description="Human-readable name of the entity..\n",
    )
    entity_status: Optional[str] = Field(
        None,
        description="Status of the entity (if this is a related entity).\n",
    )
    relationship_guid: Optional[str] = Field(
        None,
        description="Unique identifier of the relationship (when this is a related entity).\n",
    )
    relationship_status: Optional[str] = Field(
        None,
        description="Status of the relationship (when this is a related entity).\n",
    )
    relationship_type: Optional[str] = Field(
        None,
        description="Status of the relationship (when this is a related entity).\n",
    )
    meaning_names: Optional[list[str]] = Field(
        None, description="Names of assigned_terms that have been linked to this asset."
    )
    # meanings: Optional[list[Meaning]] = Field(None, description="", alias="meanings")
    custom_attributes: Optional[dict[str, Any]] = Field(
        None, description="", alias="customAttributes"
    )
    scrubbed: Optional[bool] = Field(
        None, description="", alias="fields removed from results"
    )
    pending_tasks: Optional[list[str]] = Field(None)

    unique_attributes: Optional[dict[str, Any]] = Field(None)


from .asset import Asset  # noqa: E402
from .atlas_glossary_term import AtlasGlossaryTerm  # noqa: E402