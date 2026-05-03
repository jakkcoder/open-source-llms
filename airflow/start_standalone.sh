#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export AIRFLOW_HOME="${ROOT}/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="${ROOT}/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES="False"

cd "${ROOT}"
uv sync

echo ""
echo "Starting Airflow in standalone mode (SQLite + embedded scheduler + webserver)."
echo "AIRFLOW_HOME=${AIRFLOW_HOME}"
echo "DAGs folder: ${AIRFLOW__CORE__DAGS_FOLDER}"
echo "On first run, watch the console for the auto-created admin password."
echo ""

exec uv run airflow standalone
