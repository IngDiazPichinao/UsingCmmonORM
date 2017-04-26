""" Regions Table Relational Object
"""
from sqlalchemy import Column
from sqlalchemy import String

from cns.orm import CommonBase, CommonMixin


class GeoRegion(CommonBase, CommonMixin):

    __tablename__  = 'geo_regions'
    __table_args__ = {
        'schema': 'meta'
    }

    iso   = Column(String(5),  primary_key=True)
    roman = Column(String(4),  nullable=False)
    name  = Column(String(64), nullable=False)
