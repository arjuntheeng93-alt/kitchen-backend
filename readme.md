## Kitchen Management System

A reset API built with fastapi and postgreSqQL for managing kitchen menu items.

## Tech Stack
- Python
-FastAPI
-PostgreSql
-SQLALchemy
-Pydantic

## Endpoint

-Get / menu - Get all item
-post /menu - Add a new menu item
-Put / menu/{id} - Update new item
-Delete /menu/{id} - Delete a menu item
-get/search - Search ,emu items by name

## How to run

1. Install dependencies : pip install - r required.text
2. Start server : uvicorn First:app --reload
3.Open docs: http: //127.0.0.1:8000/docs