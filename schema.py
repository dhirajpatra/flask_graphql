import types
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Department as DepartmentModel, Employee as EmployeeModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class SearchResult(graphene.Union):
    class Meta:
        types = (Department, Employee)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # List field for search results
    search = graphene.List(SearchResult, q=graphene.String())

    # Allows sorting over multiple columns, by default over the primary key
    all_employees = SQLAlchemyConnectionField(Employee.connection)
    # Disable sorting over this field
    all_departments = SQLAlchemyConnectionField(
        Department.connection, sort=None)

    # def resolve_search(self, info, **args):
    #     q = args.get("q")

    #     # get queries
    #     employee_query = Employee.get_query(info)
    #     department_query = Department.get_query(info)

    #     # query employees
    #     employees = employee_query.filter((EmployeeModel.name.contains(q) | (
    #         EmployeeModel.departments.any(DepartmentModel.name.contains(q))))).all()

    #     # query departments
    #     departments = department_query.filter(
    #         DepartmentModel.name.contains(q)).all()

    #     return employees + departments


schema = graphene.Schema(query=Query)
