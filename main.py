import uvicorn# this is a server which boardcast code to internet so web browser can talk to it
from fastapi import FastAPI # handel repetivity parts automatically
from pydantic import BaseModel # it follow the rule we set
app = FastAPI()# this build our web application 

class MenuItem(BaseModel):# this is a blueprint we are creating requirement type
    id: int
    name: str
    price: float

menu = [
    {"id": 1, "name": "Pizza", "price": 10.99},
    {"id": 2, "name":"Burger", "price": 8.99},
    {"id": 3, "name": "Pasta", "price": 12.99},
    {"id": 4, "name": "Salad", "price": 7.99},
    {"id": 5, "name": "Soup", "price": 5.99},
    {"id": 6, "name": "Sandwich", "price": 6.99},
    {"id": 7, "name": "Taco", "price": 9.99},
]
@app.get("/")# this is a home page of api
def home():
    return {"message":"Kitchen Management System"}
@app.get("/menu") # this will retun all the menu we have written above
def get_menu():
    return menu

@app.post("/menu")
def add_menu_item(item: MenuItem):#if some one sends post request to the address it will tigger menu function
    menu.append(item.dict()) # it take new items
    return {"message": "Menu item added successfully", "item": item}

@app.delete("/menu/{item_id}") # it tell the server if someone want to delete items
def delete_menu_item(item_id: int):
    for item in menu: # it will look every item on the menu
        if item["id"] == item_id:# it check the id we want to delete
            menu.remove(item)# if match it remove
            return {"message": "Menu item deleted successfully"}
    return {"message": "Menu item not found"} # if nothing is found it will show this

@app.put("/menu/{item_id}")# updating the existing data of item  id
def update_item(item_id: int, item : MenuItem):
    for item in menu:
        if item["id"] == item_id:
            item["name"] = update_item.name # it rewrite the old  name one to new one
            item["price"] = update_item.price # it rewrite the old price to new one
            return {"message": "Menu item updated successfully", "item": item} #it return back and ipdate new item
    return{"message": "Menu item not found"}#if didnt found matching