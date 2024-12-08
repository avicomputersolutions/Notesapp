from sqlalchemy import create_engine,String,Text
from sqlalchemy.orm import declarative_base,Mapped,mapped_column
engine = create_engine("sqlite:///notes.db")

base=declarative_base()

class Notes(base):
    __tablename__="notes"
    id:Mapped[int]= mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String(256))
    description:Mapped[str]=mapped_column(Text)

    def __init__(self,title,description):
        self.title=title
        self.description=description


base.metadata.create_all(engine)
