from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()
# Define the Employee class mapped to the 'employees' table
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    # Add more attributes as needed

# Create the table in the database
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
# Create a new employee
new_employee = Employee(name='John Doe', department='Engineering')
# Add the new employee to the session
session.add(new_employee)
# Commit the changes to the database
session.commit()
employees = session.query(Employee).all()
# Print the employees
for employee in employees:
    print(f"ID: {employee.id}, Name: {employee.name}, Department: {employee.department}")
