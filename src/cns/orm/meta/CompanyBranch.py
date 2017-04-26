""" Company Branch Table Relational Object
"""
from sqlalchemy     import Column, ForeignKey, UniqueConstraint
from sqlalchemy     import Integer, String
from sqlalchemy.orm import relationship

from cns.orm import CommonBase, CommonMixin


class CompanyBranch(CommonBase, CommonMixin):

    __tablename__  = 'meta.company_branches'
    __table_args__ = (
        UniqueConstraint('company', 'identifier'),
        {'schema': 'meta'}
    )

    company    = Column(Integer,  ForeignKey('meta.companies.rut'))
    identifier = Column(String(32), nullable=False)

    address = Column(String(32), nullable=False)  # NOT NULL,
    county  = Column(String(16), nullable=False)  # REFERENCES meta.geo_counties(name) NOT NULL,
    city    = Column(String(16), nullable=False)  # REFERENCES meta.geo_cities(name)   NOT NULL,

    sii_code = Column(Integer, primary_key=True)

    ref_company = relationship('Company', backref='ref_company_branches')
