# src/models/base_class.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

# Optional: Define a naming convention for constraints for Alembic
# This helps in generating consistent migration scripts.
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    It includes a default metadata object with naming conventions.
    """
    metadata = metadata_obj