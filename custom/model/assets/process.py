from __future__ import annotations

from typing import Optional, ClassVar, List
from pydantic.v1 import Field
from pyatlan.model.fields.atlan_fields import RelationField
from pyatlan.model.assets import Process as BaseProcess


class Process(BaseProcess):
    ALTERYX_WORKFLOW: ClassVar[RelationField] = RelationField("alteryxWorkflow")
    """
    TBC
    """
    _convenience_properties: ClassVar[List[str]] = (
        BaseProcess._convenience_properties + ["alteryx_workflow"]
    )

    def __setattr__(self, name, value):
        if name in Process._convenience_properties:
            return object.__setattr__(self, name, value)
        super().__setattr__(name, value)

    @property
    def alteryx_workflow(self) -> Optional[AlteryxWorkflow]:
        return None if self.attributes is None else self.attributes.alteryx_workflow

    @alteryx_workflow.setter
    def alteryx_workflow(self, alteryx_workflow: Optional[AlteryxWorkflow]):
        if self.attributes is None:
            self.attributes = self.Attributes()
        self.attributes.alteryx_workflow = alteryx_workflow

    class Attributes(BaseProcess.Attributes):
        alteryx_workflow: Optional[AlteryxWorkflow] = Field(
            default=None, description=""
        )  # relationship

    attributes: "Process.Attributes" = Field(
        default_factory=lambda: Process.Attributes(),
        description="Map of attributes in the instance and their values. The specific keys of this map will vary by "
        "type, so are described in the sub-types of this schema.\n",
    )


from .alteryx_workflow import AlteryxWorkflow  # noqa
