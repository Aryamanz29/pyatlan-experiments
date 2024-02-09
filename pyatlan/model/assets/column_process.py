from __future__ import annotations

from typing import ClassVar, Optional

from pydantic import Field

# from pyatlan.model.fields.atlan_fields import KeywordField, RelationField

from .process.process import Process


class ColumnProcess(Process):
    """Description"""

    type_name: str = Field("ColumnProcess", allow_mutation=False)

    def validate_type_name(cls, v):
        if v != "ColumnProcess":
            raise ValueError("must be ColumnProcess")
        return v

    def __setattr__(self, name, value):
        if name in ColumnProcess._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    # OUTPUTS: ClassVar[RelationField] = RelationField("outputs")
    # """
    # TBC
    # """
    # PROCESS: ClassVar[RelationField] = RelationField("process")
    # """
    # TBC
    # """
    # INPUTS: ClassVar[RelationField] = RelationField("inputs")
    # """
    # TBC
    # """

    _convenience_properties: ClassVar[list[str]] = [
        "outputs",
        "process",
        "inputs",
    ]

    @property
    def process(self) -> Optional[Process]:
        return None if self.attributes is None else self.attributes.process

    @process.setter
    def process(self, process: Optional[Process]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.process = process

    class Attributes(Process.Attributes):
        process: Optional[Process] = Field(
            None, description="", alias="process"
        )  # relationship

    attributes: ColumnProcess.Attributes = Field(
        default_factory=lambda: ColumnProcess.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )
