# flake8: noqa
import time


st = time.time()
from pyatlan.model.core import (
    AirflowDag,
    AirflowTask,
    AtlasGlossary,
    AtlasGlossaryCategory,
    AtlasGlossaryTerm,
    Column,
    ColumnProcess,
    DataDomain,
    DataProduct,
    Database,
    DbtMetric,
    DbtModel,
    DbtModelColumn,
    DbtSource,
    DbtTest,
    File,
    Folder,
    Link,
    MaterialisedView,
    MatillionComponent,
    MatillionGroup,
    MatillionJob,
    MatillionProject,
    MCIncident,
    MCMonitor,
    Metric,
    Namespace,
    Procedure,
    Process,
    Query,
    Readme,
    Schema,
    SchemaRegistry,
    SchemaRegistrySubject,
    SnowflakeDynamicTable,
    SnowflakePipe,
    SnowflakeStream,
    SnowflakeTag,
    SodaCheck,
    Table,
    TablePartition,
    Tag,
    View
)

et = time.time()
print(f"Total import time: {et - st:.2f} secs")

st = time.time()

example = AirflowDag()
example.guid = "1"
example.qualified_name = "QN"
example = AirflowTask()
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
example = Column()
example.guid = "1"
example.qualified_name = "QN"
example = ColumnProcess()
example.guid = "1"
example.qualified_name = "QN"
example = DataDomain()
example.guid = "1"
example.qualified_name = "QN"
example = DataProduct()
example.guid = "1"
example.qualified_name = "QN"
example = Database()
example.guid = "1"
example.qualified_name = "QN"
example = DbtMetric()
example.guid = "1"
example.qualified_name = "QN"
example = DbtModel()
example.guid = "1"
example.qualified_name = "QN"
example = DbtModelColumn()
example.guid = "1"
example.qualified_name = "QN"
example = DbtSource()
example.guid = "1"
example.qualified_name = "QN"
example = DbtTest()
example.guid = "1"
example.qualified_name = "QN"
example = File()
example.guid = "1"
example.qualified_name = "QN"
example = Folder()
example.guid = "1"
example.qualified_name = "QN"
example = Link()
example.guid = "1"
example.qualified_name = "QN"
example = MaterialisedView()
example.guid = "1"
example.qualified_name = "QN"
example = MatillionComponent()
example.guid = "1"
example.qualified_name = "QN"
example = MatillionGroup()
example.guid = "1"
example.qualified_name = "QN"
example = MatillionJob()
example.guid = "1"
example.qualified_name = "QN"
example = MatillionProject()
example.guid = "1"
example.qualified_name = "QN"
example = MCIncident()
example.guid = "1"
example.qualified_name = "QN"
example = MCMonitor()
example.guid = "1"
example.qualified_name = "QN"
example = Metric()
example.guid = "1"
example.qualified_name = "QN"
example = Namespace()
example.guid = "1"
example.qualified_name = "QN"
example = Procedure()
example.guid = "1"
example.qualified_name = "QN"
example = Process()
example.guid = "1"
example.qualified_name = "QN"
example = Query()
example.guid = "1"
example.qualified_name = "QN"
example = Readme()
example.guid = "1"
example.qualified_name = "QN"
example = Schema()
example.guid = "1"
example.qualified_name = "QN"
example = SchemaRegistry()
example.guid = "1"
example.qualified_name = "QN"
example = SchemaRegistrySubject()
example.guid = "1"
example.qualified_name = "QN"
example = SnowflakeDynamicTable()
example.guid = "1"
example.qualified_name = "QN"
example = SnowflakePipe()
example.guid = "1"
example.qualified_name = "QN"
example = SnowflakeStream()
example.guid = "1"
example.qualified_name = "QN"
example = SnowflakeTag()
example.guid = "1"
example.qualified_name = "QN"
example = SodaCheck()
example.guid = "1"
example.qualified_name = "QN"
example = Table()
example.guid = "1"
example.qualified_name = "QN"
example = TablePartition()
example.guid = "1"
example.qualified_name = "QN"
example = Tag()
example.guid = "1"
example.qualified_name = "QN"
example = View()
example.guid = "1"
example.qualified_name = "QN"

et = time.time()
print(f"Total instantiation time: {et - st:.2f} secs")

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
