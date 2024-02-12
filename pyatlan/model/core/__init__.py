# Top-down, abstract first...
from ..assets.atlan_object import AtlanObject
from ..assets.referenceable import Referenceable
from ..assets.asset import Asset

# Any leaves of that abstract class next (these are direct-from-Asset)
from ..assets.atlas_glossary import AtlasGlossary

# Asset -> AtlasGlossaryCategory
from ..assets.atlas_glossary_category import AtlasGlossaryCategory

# Asset -> AtlasGlossaryTerm
from ..assets.atlas_glossary_term import AtlasGlossaryTerm

# Asset -> Process
from ..assets.process import Process
from ..assets.column_process import ColumnProcess

# Asset -> Namespace
from ..assets.namespace import Namespace

# Concrete leaves of these abstracts
# (these are direct-from-Namespace)
from ..assets.folder import Folder

# Then back to next-level abstracts
# Asset -> Catalog
from ..assets.catalog import Catalog

# Catalog -> SchemaRegistry
from ..assets.schema_registry import SchemaRegistry
from ..assets.schema_registry_subject import SchemaRegistrySubject

# Catalog -> Matillion
from ..assets.matillion import Matillion
from ..assets.matillion_group import MatillionGroup
from ..assets.matillion_job import MatillionJob
from ..assets.matillion_project import MatillionProject
from ..assets.matillion_component import MatillionComponent

# Catalog -> Resource
from ..assets.resource import Resource
from ..assets.link import Link

# Then to concrete leaves of these abstracts
# (these are direct-from-Resource)...
from ..assets.readme import Readme
from ..assets.file import File

# Catalog -> DataMesh
from ..assets.data_mesh import DataMesh
from ..assets.data_domain import DataDomain
from ..assets.data_product import DataProduct

# Catalog -> Tag
from ..assets.tag import Tag
from ..assets.snowflake_tag import SnowflakeTag

# Catalog -> Airflow
from ..assets.airflow import Airflow
from ..assets.airflow_task import AirflowTask
from ..assets.airflow_dag import AirflowDag

# Catalog -> SQL
from ..assets.sql import SQL

# Concrete leaves of these abstracts
# (direct-from-DataQuality)
from ..assets.database import Database
from ..assets.schema import Schema
from ..assets.table import Table
from ..assets.snowflake_dynamic_table import SnowflakeDynamicTable
from ..assets.view import View
from ..assets.materialized_view import MaterialisedView
from ..assets.table_partition import TablePartition
from ..assets.column import Column
from ..assets.query import Query
from ..assets.function import Function
from ..assets.snowflake_pipe import SnowflakePipe
from ..assets.snowflake_stream import SnowflakeStream
from ..assets.procedure import Procedure

# Catalog -> Dbt
from ..assets.dbt import Dbt
from ..assets.dbt_model_column import DbtModelColumn
from ..assets.dbt_test import DbtTest
from ..assets.dbt_model import DbtModel
from ..assets.dbt_metric import DbtMetric
from ..assets.dbt_source import DbtSource

# Catalog -> DataQuality
from ..assets.data_quality import DataQuality

# Concrete leaves of these abstracts
# (direct-from-DataQuality)
from ..assets.metric import Metric
from ..assets.monte_carlo import MonteCarlo
from ..assets.mc_incident import MCIncident
from ..assets.mc_monitor import MCMonitor
from ..assets.soda import Soda
from ..assets.soda_check import SodaCheck

# Do any model rebuilds at the very end of core of those imports...
# TODO: Rebuilding _everything_ impacts performance (significantly)
#  - so we should ONLY model_rebuild what we MUST
#  - abstract classes seem like they never need to be rebuilt (?)
#  - but concrete (leaf) classes also seem to rarely need to be rebuilt (?)
#  - for our 'try' example, we only need to rebuild Readme and Table (despite also using Views, Columns, Processes, etc)

# AtlanObject.update_forward_refs()
# Referenceable.update_forward_refs()
# Asset.update_forward_refs()
#
# AtlasGlossary.update_forward_refs()
# AtlasGlossaryCategory.update_forward_refs()
# AtlasGlossaryTerm.update_forward_refs()
# Process.update_forward_refs()
# ColumnProcess.update_forward_refs()
#
# Namespace.update_forward_refs()
# Folder.update_forward_refs()
#
# Catalog.update_forward_refs()
#
SchemaRegistry.update_forward_refs()
# SchemaRegistrySubject.update_forward_refs()
#
# Matillion.update_forward_refs()
# MatillionGroup.update_forward_refs()
# MatillionJob.update_forward_refs()
# MatillionProject.update_forward_refs()
MatillionComponent.update_forward_refs()
#
# Resource.update_forward_refs()
# Link.update_forward_refs()
#
# DataMesh.update_forward_refs()
# DataDomain.update_forward_refs()
# DataProduct.update_forward_refs()
#
Tag.update_forward_refs()
SnowflakeTag.update_forward_refs()
#
# Readme.update_forward_refs()
# File.update_forward_refs()
# Airflow.update_forward_refs()
# AirflowTask.update_forward_refs()
AirflowDag.update_forward_refs()
#
# SQL.update_forward_refs()
# Database.update_forward_refs()
# Schema.update_forward_refs()
# Table.update_forward_refs()
SnowflakeDynamicTable.update_forward_refs()
# View.update_forward_refs()
# MaterialisedView.update_forward_refs()
# TablePartition.update_forward_refs()
# Column.update_forward_refs()
# Query.update_forward_refs()
# Function.update_forward_refs()
SnowflakePipe.update_forward_refs()
SnowflakeStream.update_forward_refs()
Procedure.update_forward_refs()
#
# Dbt.update_forward_refs()
# DbtModelColumn.update_forward_refs()
# DbtTest.update_forward_refs()
# DbtModel.update_forward_refs()
DbtMetric.update_forward_refs()
# DbtSource.update_forward_refs()
#
# DataQuality.update_forward_refs()
# Metric.update_forward_refs()
# MonteCarlo.update_forward_refs()
# MCIncident.update_forward_refs()
# MCMonitor.update_forward_refs()
# Soda.update_forward_refs()
# SodaCheck.update_forward_refs()

# TODO: maybe there is a minimal "core" we can rebuild
# out of all these inter-related types? (Maybe above is it?)
