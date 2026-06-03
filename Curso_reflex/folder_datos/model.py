import reflex as rx
from datetime import datetime
import sqlmodel


class Dato(sqlmodel.SQLModel,table=True):
    """"Modelo para representar una tarea"""

    id:int | None = sqlmodel.Field(default=None, primary_key=True)

    title:str 
    description:str
    completed: bool = False

    #Establecer la fecha 
    crated_at: datetime = sqlmodel.Field(
        default_factory= datetime.now,
        sa_column= sqlmodel.Column(
        sqlmodel.DateTime(timezone=True),
        sever_default= sqlmodel.func.now()
        )
    )