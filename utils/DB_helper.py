import boto3


class DatabaseConnection:
    def __init__(self, resource_name: str, table_name: str):
        self.client = None
        self.resource_name = resource_name
        self.table_name = table_name

    def __enter__(self):
        self.client = boto3.resource(self.resource_name, endpoint_url='http://127.0.0.1:8000/')
        table = self.client.Table(self.table_name)
        return table

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
