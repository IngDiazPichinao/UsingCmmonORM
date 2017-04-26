""" SII Document Table Relational Object
"""
from sqlalchemy import Column
from sqlalchemy import Integer, String

from cns.orm import CommonBase, CommonMixin


class Company(CommonBase, CommonMixin):

    __tablename__  = 'companies'
    __table_args__ = {
        'schema': 'meta'
    }

    rut        = Column(Integer,    primary_key=True)
    identifier = Column(String(32), unique=True, nullable=False)
