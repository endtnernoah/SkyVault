"""
    Settings for the postgres database
"""
database_type = 'postgresql'
database_user = 'skyvault'
database_pass = 'bvuqGIciWQbN8D7I3VQiOi'
database_host = 'localhost'
database_port = '5432'
database_name = 'vault'


database_url = f'{database_type}://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}'
