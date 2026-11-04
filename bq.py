from pathlib import Path
import pandas as pd
from google.cloud import bigquery

PROJECT_ID = "tracking-auditor-513612"


def load_sql(path: str| Path) -> str:
    """Load SQL from a file."""
    with open(path, "r") as f:
        return f.read()


def run_query(sql: str) -> pd.DataFrame:
    """Run a SQL query and return the results as a pandas DataFrame."""
    client = bigquery.Client(project=PROJECT_ID)
    query_job = client.query(sql)
    results = query_job.result()
    return results.to_dataframe()


if __name__ == "__main__":
    sql_path = Path(__file__).parent / "queries"/ "01_event_counts.sql"
    sql = load_sql(sql_path)

    df = run_query(sql)

    print(df)
    
    assert len(df) == 17, "Expected 17 event names"
    assert df.iloc[0]["event_name"] == "page_view"