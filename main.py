import uvicorn# this is a server which boardcast code to internet so web browser can talk to it
from fastapi import FastAPI # handel repetivity parts automatically
from pydantic import BaseModel # it follow the rule we set
from database import engine, Base
import model

Base.metadata.create_all(bind=engine) # it create database and table for us
from database import SessionLocal # it create session for us to interact with database  
from sqlalchemy.orm import Session # it help us to interact with database
from fastapi import Depends # it help us to manage dependencies

def get_db():
    db = SessionLocal() # it create a session
    try:
        yield db # it return the session to the caller
    finally:
        db.close() # it close the session after use  

app = FastAPI()# this build our web application 

class MenuItemCreate(BaseModel):# this is a blueprint we are creating requirement type
    name: str
    price: float
class MenuItemResponse(BaseModel):
    id: int
    name: str
    price: float
    class Config:
        from_attributes = True # it will allow us to use the attribute name instead of the field name in the response


@app.get("/")# this is a home page of api
def home():
    return {"message":"Kitchen Management System"}
@app.get("/menu") # this will retun all the menu we have written above
def get_menu(db: Session = Depends(get_db)):
    items = db.query(model.MenuItem).all()
    return items# it will query all the items from database
    

@app.post("/menu")
def add_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    #if some one sends post request to the address it will tigger menu function
    db_item = model.MenuItem( name=item.name, price=item.price) # it will create a new item in database
    db.add(db_item) # it will add the item to database
    db.commit() # it will commit the changes to database
    db.refresh(db_item) # it will refresh the item to get the id from database
    return db_item # it will return the item we just added to database
@app.delete("/menu/{item_id}") # it tell the server if someone want to delete items
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first() # it will query the item with the given id
    if db_item:
        db.delete(db_item) # it will delete the item from database
        db.commit() # it will commit the changes to database
        return {"message": "Menu item deleted successfully"}
    
       
    

@app.put("/menu/{item_id}")# updating the existing data of item  id
def update_menu_item(item_id: int, item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(model.MenuItem).filter(model.MenuItem.id == item_id).first()
    if not db_item:
        return {"message": "mennu item not found"}
    db_item.name = item.name
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item
      

@app.get("/search") # it will search the food by name and return the result
def search_food(name: str, db: Session= Depends(get_db)): # it take the name of food as input
    results = db.query(model.MenuItem).filter(model.MenuItem.name.ilike(f"%{name}%")).all() 
    return {"results": results}  # it return the result of search