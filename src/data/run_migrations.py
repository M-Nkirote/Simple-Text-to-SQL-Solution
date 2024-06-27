from clickhouse_migrations.clickhouse_cluster import ClickhouseCluster
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("CLICKHOUSE_HOST")
db_user = os.getenv("CLICKHOUSE_USER")
db_password = os.getenv("CLICKHOUSE_PASSWORD")
db_name = os.getenv("CLICKHOUSE_DATABASE")

current_dir = Path(__file__).resolve().parent  # Get current script directory
migrations_home = current_dir.parent / "migrations"

cluster = ClickhouseCluster(db_host, db_user, db_password)
cluster.migrate(db_name, migrations_home, cluster_name=None, create_db_if_no_exists=True, multi_statement=True)