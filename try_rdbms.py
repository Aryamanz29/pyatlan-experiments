# flake8: noqa
import time


st = time.time()
from pyatlan.model.rdbms import (
    Database,
    Schema,
    Table,
    View,
    MaterialisedView,
    Column,
)

et = time.time()
print(f"Total import time: {et - st:.2f} secs")

st = time.time()

example = Database()
example.guid = "1"
example.qualified_name = "QN"
example = Schema()
example.guid = "1"
example.qualified_name = "QN"
example = Table()
example.guid = "1"
example.qualified_name = "QN"
example = View()
example.guid = "1"
example.qualified_name = "QN"
example = MaterialisedView()
example.guid = "1"
example.qualified_name = "QN"
example = Column()
example.guid = "1"
example.qualified_name = "QN"

et = time.time()
print(f"Total instantiation time: {et - st:.2f} secs")
