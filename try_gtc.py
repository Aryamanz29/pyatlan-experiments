# flake8: noqa
import time


st = time.time()
from pyatlan.model.gtc import (
    AtlasGlossaryTerm,
    AtlasGlossaryCategory,
    AtlasGlossary,
)

et = time.time()
print(f"Total import time: {et - st:.2f} secs")

st = time.time()

example = AtlasGlossary()
example.guid = "1"
example.qualified_name = "QN"
example = AtlasGlossaryCategory()
example.guid = "1"
example.qualified_name = "QN"
example = AtlasGlossaryTerm()
example.guid = "1"
example.qualified_name = "QN"
example = AtlasGlossary()
example.guid = "1"
example.qualified_name = "QN"
example = AtlasGlossaryCategory()
example.guid = "1"
example.qualified_name = "QN"
example = AtlasGlossaryTerm()
example.guid = "1"
example.qualified_name = "QN"

et = time.time()
print(f"Total instantiation time: {et - st:.2f} secs")
