# this class will be used to control the database
# it will be used to create, read, update, and delete data from the database
# it will also be used to create the database
# it will be used to create the tables in the database


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, Column
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.schema import CreateTable, Column, CreateIndex
from Models import Student, Assessment, Class, StudentClass, ClassAssessment

class DatabaseController:

    def update_tables(app, db):
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        conn = engine.connect()

    # Get existing tables
        inspector = Inspector.from_engine(engine)
        existing_tables = inspector.get_table_names()

    # Get models and their tables
        models = {model.__tablename__: model for model in [Student, Class, Assessment, StudentClass, ClassAssessment]}
        metadata = db.MetaData()
        model_tables = {table_name: Table(table_name, metadata, autoload=True, autoload_with=engine) for table_name in existing_tables if table_name in models}

    # Check for missing tables and create them
        missing_tables = {table_name: models[table_name].__table__ for table_name in models if table_name not in existing_tables}
        for table_name, table in missing_tables.items():
            conn.execute(CreateTable(table))
            print(f"Created table '{table_name}'")

    # Check for missing columns and alter tables
        for table_name, table in model_tables.items():
            model = models[table_name]
            missing_columns = {column.name: column for column in model.__table__.columns if column.name not in table.columns}
            for column_name, column in missing_columns.items():
                conn.execute(f"ALTER TABLE {table_name} ADD COLUMN {column.compile(engine)}")
                print(f"Added column '{column_name}' to table '{table_name}'")


        # Check for missing indexes
        for table_name, table in model_tables.items():
            model = models[table_name]
            indexes = {index.name: index for index in model.__table__.indexes}
            for index_name, index in indexes.items():
                conn.execute(CreateIndex(index))
                print(f"Added index '{index_name}' to table '{table_name}'")

        conn.close()