from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class Context_Scope(Base):
    __tablename__ = 'context_scope'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    responsible = Column(String(100))
    coordinator = Column(String(100))
    start_date = Column(Date)
    end_date = Column(Date)
    last_update = Column(Date)
    service_description = Column(String)
    knowledge = Column(String)
    interfaces = Column(String)
    mission_critical = Column(String)
    support_contracts = Column(String)
    security_supplier = Column(String)
    user_amount = Column(Integer)
    scope_description = Column(String)
    risk_assessment_human = Column(String)
    risk_assessment_process = Column(String)
    risk_assessment_technological = Column(String)
    project_leader = Column(String)
    risk_owner = Column(String)
    product_owner = Column(String)
    technical_administrator = Column(String)
    security_manager = Column(String)
    incident_contact = Column(String)

class Components(Base):
    __tablename__ = 'components'
    id = Column(Integer, primary_key=True)
    bia_name = Column(Integer, ForeignKey('context_scope.name'))
    component_name = Column(String)
    processes_dependencies = Column(String)
    info_type = Column(String)
    info_owner = Column(String)
    user_type = Column(String)
    description = Column(String)

class Availability_Requirements(Base):
    __tablename__ = 'availability_requirements'
    id = Column(Integer, primary_key=True)
    component_name = Column(Integer, ForeignKey('components.component_name'))
    mtd = Column(String)
    rto = Column(String)
    rpo = Column(String)
    masl = Column(String)

class References(Base):
    __tablename__ = 'references'
    id = Column(Integer, primary_key=True)
    consequence_category = Column(String)
    consequence_small = Column(String)
    consequence_medium = Column(String)
    consequence_large = Column(String)
    consequence_huge = Column(String)

class Consequences(Base):
    __tablename__ = 'consequences'
    id = Column(Integer, primary_key=True)
    component_name = Column(Integer, ForeignKey('components.component_name'))
    category = Column(String)
    security_property = Column(String)
    consequence_worstcase = Column(String)
    justification_worstcase = Column(String)
    consequence_realisticcase = Column(String)
    justification_realisticcase = Column(String)

class ConsequenceChoices(Base):
    __tablename__ = 'consequence_choices'
    id = Column(Integer, primary_key=True)
    choice = Column(String)

class SecurityProperties(Base):
    __tablename__ = 'security_properties'
    id = Column(Integer, primary_key=True)
    choice = Column(String)