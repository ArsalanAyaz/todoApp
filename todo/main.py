from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session

class Todo(SQLModel):
    id : int | None = Field(default=None, primary_key=Truel)
    content : str = Field(index=True, max_length={20}, min_length={4})
    is_completed : bool = Field()
    

connection_string = str(setting.BD_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode":"require"}, pool_recycle=500, pool_size=10)

async def get_session():
    with Session(engine) as session:
        yield session
        
        
async def create_tables():
    SQLModel.metadata.create_all(engine)        
        
@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()        
    
    
    

app : FastAPI = FastAPI(lifespan=lifespan)

@app.get("/")
async def mainMessage():
    return {"message":"Hello world"}


@app.post("/todos")
async def create_todo():
    ...
    