from pathlib import Path
import pandas as pd
from google.cloud import bigquery
import tomllib

SETTINGS_PATH = Path(__file__).parent / "settings.toml"


def load_settings() -> dict[str, str]:
    """Read where the auditor gets its data from."""
    with open(SETTINGS_PATH, "rb") as f:
        return tomllib.load(f)

def load_sql(path: str | Path) -> str:
    """Load SQL from a file and fill in the table and date range from the settings."""
    settings = load_settings()
    with open(path, "r") as f:
        sql = f.read()
    for key in ("table", "start_date", "end_date"):
        sql = sql.replace("{" + key + "}", settings[key])
    return sql


def run_query(sql: str) -> pd.DataFrame:
    """Run a SQL query and return the results as a pandas DataFrame."""
    client = bigquery.Client(project=load_settings()["billing_project"])
    query_job = client.query(sql)
    results = query_job.result()
    return results.to_dataframe(create_bqstorage_client=False)


if __name__ == "__main__":
    sql_path = Path(__file__).parent / "queries"/ "01_event_counts.sql"
    sql = load_sql(sql_path)

    df = run_query(sql)

    print(df)
    
    assert len(df) == 17, "Expected 17 event names"
    assert df.iloc[0]["event_name"] == "page_view"