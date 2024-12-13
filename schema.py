import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Bank, Branch, BankBranch

class BankType(SQLAlchemyObjectType):
    class Meta:
        model = Bank
        fields = ('id', 'name')

class BranchType(SQLAlchemyObjectType):
    class Meta:
        model = Branch
        fields = ('ifsc', 'branch', 'address', 'city', 'district', 'state')

class BankBranchType(SQLAlchemyObjectType):
    class Meta:
        model = BankBranch
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')

class Query(graphene.ObjectType):
    branches = graphene.List(BankBranchType)

    def resolve_branches(self, info):
        return BankBranch.query.all()

schema = graphene.Schema(query=Query)
