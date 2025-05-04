from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mysql.connector import connect

def train_predictive_model():
    conn = connect(
        host="localhost",
        user="root",
        password="rajesh",
        database="iotdb"
    )
    df = pd.read_sql("SELECT * FROM sensor_data", conn)
    if df.shape[0] < 50:
        print("Not enough data to train.")
        return
    X = df[['temperature', 'vibration', 'rpm']]
    y = df['anomaly'].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, './tmp/predictive_model.pkl')
    print("Model trained and saved.")

default_args = {
    'start_date': datetime(2024, 1, 1),
    'schedule_interval': '0 2 * * *',  # Daily at 2 AM
}

with DAG('predictive_maintenance_model_training', default_args=default_args, catchup=False) as dag:
    train_model = PythonOperator(
        task_id='train_model',
        python_callable=train_predictive_model
    )
