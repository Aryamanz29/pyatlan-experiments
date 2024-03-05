from custom.model.assets import Process, AlteryxWorkflow

# To extend the SDK with custom typedefs:
# eg: python3 class_generator.py --with-custom-typedefs
# It will generate custom/model/assets/

p1 = Process()
p1.name = "process-1"
print(p1)

p2 = Process()
p2.name = "process-2"
print(p2)

aw = AlteryxWorkflow()
aw.name = "alteryx-workflow-1"
aw.attributes.alteryx_transformations = [p1, p2]
print(aw.alteryx_transformations[0].name, aw.alteryx_transformations[1].name)

p3 = Process()
p3.name = "process-3"
p3.outputs = [p2]
p3.alteryx_workflow = aw
print(p3.alteryx_workflow.name, p3.outputs[0].name)
