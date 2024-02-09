# flake8: noqa
import os
import importlib
import inspect
import time


print("--- try.py import start ---\n")
st = time.time()

from pyatlan.model.assets.atlas import AtlasGlossary
from pyatlan.model.assets.atlas import AtlasGlossaryTerm
from pyatlan.model.assets.atlas import AtlasGlossaryCategory
from pyatlan.model.assets.airflow import Airflow  # this fails
from pyatlan.model.assets.process import Process
from pyatlan.model.assets.process import ColumnProcess
from pyatlan.model.assets.catalog import Catalog
from pyatlan.model.assets.dbt import Dbt
from pyatlan.model.assets.dbt import DbtMetric
from pyatlan.model.assets.dbt import DbtTest
from pyatlan.model.assets.dbt import DbtSource
from pyatlan.model.assets.dbt import DbtModel
from pyatlan.model.assets.dbt import DbtModelColumn
from pyatlan.model.assets.data_mesh import DataMesh
from pyatlan.model.assets.data_mesh import DataDomain
from pyatlan.model.assets.data_mesh import DataProduct

et = time.time()
print("\n--- try.py import end ---")
print(f"Total import time: {et - st:.2f} secs")

st = time.time()

example = AtlasGlossary()
example.guid = "1"
example.qualified_name = "QN"
gt = AtlasGlossaryTerm()
gc = AtlasGlossaryCategory()
# af = Airflow()
pro = Process()
cp = ColumnProcess()
ct = Catalog()

# dbt = Dbt()
# dt = DbtTest()
# dmt = DbtMetric()
# ds = DbtSource()
# dm = DbtModel()
# dmc = DbtModelColumn()

# data_m = DataMesh()
data_d = DataDomain()
data_pro = DataProduct()

et = time.time()
print(f"Total instantiation time: {et - st:.2f} secs")

# example = AtlasGlossaryCategory()
# example.guid = "1"
# example.qualified_name = "QN"
# example = AtlasGlossaryTerm()
# example.guid = "1"
# example.qualified_name = "QN"

# example = AtlasGlossary()
# example.guid = "1"
# example.qualified_name = "QN"
# example = AtlasGlossaryCategory()
# example.guid = "1"
# example.qualified_name = "QN"
# example = AtlasGlossaryTerm()
# example.guid = "1"
# example.qualified_name = "QN"

# af = Airflow()

# st = time.time()
# from pyatlan.model.assets import *

# et = time.time()

# models_directory = "pyatlan/model/assets"
# model_files = [f for f in os.listdir(models_directory) if f.endswith(".py")]

# instances = {}
# for model_file in model_files:
#     model_module_name = model_file[:-3]
#     full_path = f"{'.'.join(models_directory.split('/'))}.{model_module_name}"

#     model_module = importlib.import_module(full_path, package=__name__)
#     model_classes = [
#         obj
#         for name, obj in inspect.getmembers(model_module, inspect.isclass)
#         if issubclass(obj, AtlanObject) and obj.__module__ == full_path
#     ]
#     # Create instances
#     for model_class in model_classes:
#         class_name = model_class.__name__
#         class_instance = model_class()
#         instances[class_name] = class_instance

# for model_name, instance in instances.items():
#     print(f"\n Created: {model_name}()")
# print(f"\nTotal models: {len(instances.items())}")
# print(f"Total import time: {et - st:.2f} secs")


# start = time.time()
# r = Readme()
# print(r)
# r.guid = "abc123"
# r.qualified_name = "readmeQN"
# g = AtlasGlossary()
# g.guid = "def456"
# g.qualified_name = "glossaryQN"
# g.readme = r
# cat = AtlasGlossaryCategory()
# cat.guid = "cat"
# cat.qualified_name = "catQN"
# t1 = AtlasGlossaryTerm()
# t1.guid = "x"
# t1.qualified_name = "t1QN"
# t2 = AtlasGlossaryTerm()
# t2.guid = "y"
# t2.qualified_name = "t2QN"
# g.terms = [t1, t2]
# g.categories = [cat]
# print(g.model_dump_json(by_alias=True, exclude_unset=True, indent=2))
# end = time.time()
# print(f"Glossary took: {end - start}")

# start = time.time()
# lineage = Process()
# lineage.guid = "lineage"
# lineage.qualified_name = "lineageQN"
# d1 = Database()
# d1.guid = "d1"
# d1.qualified_name = "d1QN"
# s1 = Schema()
# s1.guid = "s1"
# s1.qualified_name = "s1QN"
# s1.database = d1
# t1 = Table()
# t1.guid = "t1"
# t1.qualified_name = "t1QN"
# t1.atlan_schema = s1
# v2 = View()
# v2.guid = "v2"
# v2.qualified_name = "v2QN"
# v2.atlan_schema = s1
# lineage.inputs = [t1]
# lineage.outputs = [v2]
# col_lineage = ColumnProcess()
# col_lineage.guid = "cl"
# col_lineage.qualified_name = "clQN"
# c1 = Column()
# c1.guid = "c1"
# c1.qualified_name = "c1QN"
# c2 = Column()
# c2.guid = "c2"
# c2.qualified_name = "c2QN"
# col_lineage.inputs = [c1]
# col_lineage.outputs = [c2]
# lineage.column_processes = [col_lineage]
# print(lineage.model_dump_json(by_alias=True, exclude_unset=True, indent=2))
# end = time.time()
# print(f"Lineage took: {end - start}")
