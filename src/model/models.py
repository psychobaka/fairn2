"""
Python `peewee` objects representing the FairN2 MySQL database.  This code was
almost entirely generated using the "pwiz" utility provided by `peewee`.
"""

from peewee import *

####NON-PEEWEE CUSTOMIZED CODE##################################################
from getpass import getpass




usr = input("MySQL DB Username:")
database = MySQLDatabase(
    'fairn2',
    host='localhost',
    port=3306,
    user=usr,
    password=getpass(),
)
####END NON-PEEWEE CUSTOMIZED CODE##############################################

class BaseModel(Model):
    class Meta:
        database = database

class TblExpensetype(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'tbl_expensetype'

class TblAccounttype(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'tbl_accounttype'

class TblAccount(BaseModel):
    accountype = ForeignKeyField(db_column='accountype_id', rel_model=TblAccounttype, to_field='id')
    datecreated = DateTimeField()
    expensetype = ForeignKeyField(db_column='expensetype_id', null=True, rel_model=TblExpensetype, to_field='id')
    household_account = ForeignKeyField(db_column='household_account_id', null=True, rel_model='self', to_field='id')
    name = CharField()

    class Meta:
        db_table = 'tbl_account'

class TblPerson(BaseModel):
    datecreated = DateTimeField()
    e-mail = CharField(null=True)
    firstname = CharField()
    lastname = CharField()

    class Meta:
        db_table = 'tbl_person'

class TblAccountPerson(BaseModel):
    account = ForeignKeyField(db_column='account_id', rel_model=TblAccount, to_field='id')
    person = ForeignKeyField(db_column='person_id', rel_model=TblPerson, to_field='id')

    class Meta:
        db_table = 'tbl_account_person'

class TblSplittype(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'tbl_splittype'

class TblSplit(BaseModel):
    splittype = ForeignKeyField(db_column='splittype_id', rel_model=TblSplittype, to_field='id')

    class Meta:
        db_table = 'tbl_split'

class TblExpensesplitdefault(BaseModel):
    expense_account = ForeignKeyField(db_column='expense_account_id', rel_model=TblAccount, to_field='id')
    split = ForeignKeyField(db_column='split_id', rel_model=TblSplit, to_field='id')
    user_account = ForeignKeyField(db_column='user_account_id', null=True, rel_model=TblAccount, related_name='tbl_account_user_account_set', to_field='id')

    class Meta:
        db_table = 'tbl_expensesplitdefault'

class TblLedger(BaseModel):
    amount = DecimalField()
    datecreated = DateTimeField()
    dateupdated = DateTimeField(null=True)
    dst_account = ForeignKeyField(db_column='dst_account_id', rel_model=TblAccount, to_field='id')
    notes = CharField(null=True)
    parent_ledger = ForeignKeyField(db_column='parent_ledger_id', null=True, rel_model='self', to_field='id')
    split = ForeignKeyField(db_column='split_id', null=True, rel_model=TblSplit, to_field='id')
    src_account = ForeignKeyField(db_column='src_account_id', rel_model=TblAccount, related_name='tbl_account_src_account_set', to_field='id')

    class Meta:
        db_table = 'tbl_ledger'

class TblSplitcustpercent(BaseModel):
    account = ForeignKeyField(db_column='account_id', rel_model=TblAccount, to_field='id')
    percentage = DecimalField()
    split = ForeignKeyField(db_column='split_id', rel_model=TblSplit, to_field='id')

    class Meta:
        db_table = 'tbl_splitcustpercent'
