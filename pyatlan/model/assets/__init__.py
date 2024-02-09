print("super-init called...")

# Top-down, abstract first...
from .atlan_object import AtlanObject
from .referenceable import Referenceable
from .asset import Asset

# Asset relationship classes
from .schema_registry_subject import SchemaRegistrySubject
from .mc_monitor import MCMonitor
from .data_mesh.data_product import DataProduct
from .file import File
from .mc_incident import MCIncident
from .link import Link
from .metric import Metric
from .readme import Readme
from .soda_check import SodaCheck
from .process.process import Process
from .airflow.airflow_task import AirflowTask


Referenceable.model_rebuild()
print("super-init end...")

# # Any leaves of that abstract class next (these are direct-from-Asset)
# from .atlas_glossary import AtlasGlossary

# # Asset -> AtlasGlossaryCategory
# from .atlas_glossary_category import AtlasGlossaryCategory

# # Asset -> AtlasGlossaryTerm
# from .atlas_glossary_term import AtlasGlossaryTerm

# # Asset -> Process
# from .process import Process
# from .column_process import ColumnProcess

# # Asset -> Namespace
# from .namespace import Namespace

# # Concrete leaves of these abstracts
# # (these are direct-from-Namespace)
# from .folder import Folder

# # Then back to next-level abstracts
# # Asset -> Catalog
# from .catalog import Catalog

# # Catalog -> SchemaRegistry
# from .schema_registry import SchemaRegistry
# from .schema_registry_subject import SchemaRegistrySubject

# # Catalog -> Matillion
# from .matillion import Matillion
# from .matillion_group import MatillionGroup
# from .matillion_job import MatillionJob
# from .matillion_project import MatillionProject
# from .matillion_component import MatillionComponent

# # Catalog -> Resource
# from .resource import Resource
# from .link import Link

# # Then to concrete leaves of these abstracts
# # (these are direct-from-Resource)...
# from .readme import Readme
# from .file import File

# # Catalog -> DataMesh
# from .data_mesh import DataMesh
# from .data_domain import DataDomain
# from .data_product import DataProduct

# # Catalog -> Tag
# from .tag import Tag
# from .snowflake_tag import SnowflakeTag

# # Catalog -> Airflow
# from .airflow import Airflow
# from .airflow_task import AirflowTask
# from .airflow_dag import AirflowDag

# # Catalog -> SQL
# from .sql import SQL

# # Concrete leaves of these abstracts
# # (direct-from-DataQuality)
# from .database import Database
# from .schema import Schema
# from .table import Table
# from .snowflake_dynamic_table import SnowflakeDynamicTable
# from .view import View
# from .materialized_view import MaterialisedView
# from .table_partition import TablePartition
# from .column import Column
# from .query import Query
# from .function import Function
# from .snowflake_pipe import SnowflakePipe
# from .snowflake_stream import SnowflakeStream
# from .procedure import Procedure

# # Catalog -> Dbt
# from .dbt import Dbt
# from .dbt_model_column import DbtModelColumn
# from .dbt_test import DbtTest
# from .dbt_model import DbtModel
# from .dbt_metric import DbtMetric
# from .dbt_source import DbtSource

# # Catalog -> DataQuality
# from .data_quality import DataQuality

# # Concrete leaves of these abstracts
# # (direct-from-DataQuality)
# from .metric import Metric
# from .monte_carlo import MonteCarlo
# from .mc_incident import MCIncident
# from .mc_monitor import MCMonitor
# from .soda import Soda
# from .soda_check import SodaCheck

# # Do any model rebuilds at the very end of core of those imports...
# # TODO: Rebuilding _everything_ impacts performance (significantly)
# #  - so we should ONLY model_rebuild what we MUST
# #  - abstract classes seem like they never need to be rebuilt (?)
# #  - but concrete (leaf) classes also seem to rarely need to be rebuilt (?)
# #  - for our 'try' example, we only need to rebuild Readme and Table (despite also using Views, Columns, Processes, etc)

# AtlanObject.model_rebuild()
# Referenceable.model_rebuild()
# Asset.model_rebuild()

# AtlasGlossary.model_rebuild()
# AtlasGlossaryCategory.model_rebuild()
# AtlasGlossaryTerm.model_rebuild()
# Process.model_rebuild()
# ColumnProcess.model_rebuild()

# Namespace.model_rebuild()
# Folder.model_rebuild()

# Catalog.model_rebuild()

# SchemaRegistry.model_rebuild()
# SchemaRegistrySubject.model_rebuild()

# Matillion.model_rebuild()
# MatillionGroup.model_rebuild()
# MatillionJob.model_rebuild()
# MatillionProject.model_rebuild()
# MatillionComponent.model_rebuild()

# Resource.model_rebuild()
# Link.model_rebuild()

# DataMesh.model_rebuild()
# DataDomain.model_rebuild()
# DataProduct.model_rebuild()

# Tag.model_rebuild()
# SnowflakeTag.model_rebuild()

# Readme.model_rebuild()
# File.model_rebuild()
# Airflow.model_rebuild()
# AirflowTask.model_rebuild()
# AirflowDag.model_rebuild()

# SQL.model_rebuild()
# Database.model_rebuild()
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

# Dbt.model_rebuild()
# DbtModelColumn.model_rebuild()
# DbtTest.model_rebuild()
# DbtModel.model_rebuild()
# DbtMetric.model_rebuild()
# DbtSource.model_rebuild()

# DataQuality.model_rebuild()
# Metric.model_rebuild()
# MonteCarlo.model_rebuild()
# MCIncident.model_rebuild()
# MCMonitor.model_rebuild()
# Soda.model_rebuild()
# SodaCheck.model_rebuild()

# # TODO: maybe there is a minimal "core" we can rebuild
# # out of all these inter-related types? (Maybe above is it?)
