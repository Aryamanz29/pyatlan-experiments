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

# AtlanObject.model_rebuild()
# Referenceable.model_rebuild()
# Asset.model_rebuild()
#
# AtlasGlossary.model_rebuild()
# AtlasGlossaryCategory.model_rebuild()
# AtlasGlossaryTerm.model_rebuild()
# Process.model_rebuild()
# ColumnProcess.model_rebuild()
#
# Namespace.model_rebuild()
# Folder.model_rebuild()
#
# Catalog.model_rebuild()
#
# SchemaRegistry.model_rebuild()
# SchemaRegistrySubject.model_rebuild()
#
# Matillion.model_rebuild()
# MatillionGroup.model_rebuild()
# MatillionJob.model_rebuild()
# MatillionProject.model_rebuild()
# MatillionComponent.model_rebuild()
#
# Resource.model_rebuild()
# Link.model_rebuild()
#
# DataMesh.model_rebuild()
# DataDomain.model_rebuild()
# DataProduct.model_rebuild()
#
# Tag.model_rebuild()
# SnowflakeTag.model_rebuild()
#
# Readme.model_rebuild()
# File.model_rebuild()
# Airflow.model_rebuild()
# AirflowTask.model_rebuild()
# AirflowDag.model_rebuild()
#
# SQL.model_rebuild()
Database.model_rebuild()
# Schema.model_rebuild()
# Table.model_rebuild()
# SnowflakeDynamicTable.model_rebuild()
# View.model_rebuild()
# MaterialisedView.model_rebuild()
# TablePartition.model_rebuild()
# Column.model_rebuild()
# Query.model_rebuild()
# Function.model_rebuild()
# SnowflakePipe.model_rebuild()
# SnowflakeStream.model_rebuild()
# Procedure.model_rebuild()
#
# Dbt.model_rebuild()
# DbtModelColumn.model_rebuild()
# DbtTest.model_rebuild()
# DbtModel.model_rebuild()
# DbtMetric.model_rebuild()
# DbtSource.model_rebuild()
#
# DataQuality.model_rebuild()
# Metric.model_rebuild()
# MonteCarlo.model_rebuild()
# MCIncident.model_rebuild()
# MCMonitor.model_rebuild()
# Soda.model_rebuild()
# SodaCheck.model_rebuild()

# TODO: maybe there is a minimal "core" we can rebuild
# out of all these inter-related types? (Maybe above is it?)
