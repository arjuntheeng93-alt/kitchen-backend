import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#lets make a blue print our menu and write requiremnt\
class MenuItem(BaseModel):
    id: int
    name: str
    price: float # this are our requirement
    
menu = [ {"id": 1, "name": "Pizza", "price": 10.99},
    {"id": 2, "name":"Burger", "price": 8.99},
    {"id": 3, "name": "Pasta", "price": 12.99},
    {"id": 4, "name": "Salad", "price": 7.99},
    {"id": 5, "name": "Soup", "price": 5.99},
    {"id": 6, "name": "Sandwich", "price": 6.99},] 
# this are our menu 
@app.get("/")# now we are creating our home page
def home():# we have make home function
    return{"message": "hello thank you for visiting"}
@app.get("/menu") # we request for data inside the menuitem
def get_menu(): # we make menu function
    return menu

@app.post("/menu")
def add_menu_item(item:MenuItem)
    