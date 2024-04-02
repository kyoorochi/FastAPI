from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_db
from schemas import ItemCreate, ItemUpdate
from sqlalchemy.orm import Session
import crud_orm, schemas

router = APIRouter(prefix='/api/v1/user', tags=['Items'])
# api/v1/item

# api/v1/item/{item_id}
@router.get('/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud_orm.get_item()

@router.get('/')
def get_items(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    return crud_orm.get_items(db, skip, limit)

@router.post('/')
def create_item(owner_id:int, item_create: schemas.ItemCreate, db: Session=Depends(get_db)):
    return crud_orm.create_item(db, item_create, owner_id=owner_id)

@router.put('/{item_id}')
def update_item(item_id: int, item_update: ItemUpdate, db: Session=Depends(get_db)):
    return crud_orm.update_item(db, item_update, item_id)

@router.delete('/{item_id}')
def delete_item(item_id:int, db: Session=Depends(get_db)):    
    is_success = crud_orm.delete_item(db, item_id)

    if not is_success:
        raise HTTPException(404, 'Item not found. Fail to delete item')
    return {'msg': 'Item delete success'}