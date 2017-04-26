""" Counties Table Relational Object
"""
from sqlalchemy     import Column, ForeignKey, UniqueConstraint
from sqlalchemy     import String
from sqlalchemy.orm import relationship

from cns.orm import CommonBase, CommonMixin

from .GeoRegion import GeoRegion


class GeoCounty(CommonBase, CommonMixin):

    __tablename__  = 'geo_comunes'
    __table_args__ = (
        UniqueConstraint('region', 'name'),
        {'schema': 'meta'}
    )

    region = Column(String(5),  ForeignKey(GeoRegion.iso), nullable=False)
    name   = Column(String(16), primary_key=True)

    ref_region = relationship(GeoRegion, backref='ref_comunes')
