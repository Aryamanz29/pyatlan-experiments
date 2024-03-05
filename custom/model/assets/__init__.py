from .process import Process
from .alteryx_workflow import AlteryxWorkflow

# Update asset forward references:
localns = locals()
Process.Attributes.update_forward_refs(**localns)
AlteryxWorkflow.Attributes.update_forward_refs(**localns)
