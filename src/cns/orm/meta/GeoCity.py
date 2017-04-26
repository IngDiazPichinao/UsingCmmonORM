""" Cities Table Relational Object
"""
from sqlalchemy     import Column, ForeignKey, UniqueConstraint
from sqlalchemy     import String
from sqlalchemy.orm import relationship

from cns.orm import CommonBase, CommonMixin

from .GeoRegion import GeoRegion
from .GeoCounty import GeoCounty


class GeoCity(CommonBase, CommonMixin):

    __tablename__  = 'geo_cities'
    __table_args__ = (
        UniqueConstraint('region', 'county', 'name'),
        {'schema': 'meta'}
    )

    region = Column(String(5),  ForeignKey(GeoRegion.iso),  nullable=False)
    county = Column(String(5),  ForeignKey(GeoCounty.name), nullable=False)
    name   = Column(String(16), primary_key=True)

    ref_region = relationship(GeoRegion, backref='ref_cities')
    ref_county = relationship(GeoCounty, backref='ref_cities')
