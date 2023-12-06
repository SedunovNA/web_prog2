from typing import Union

from fastapi import FastAPI,Depends, HTTPException

from app.models.vallet import Vallet, Currency, Category, Transaction

from app.config.database import engine, get_db, Base

from app.schemas.vallet_schema import CreateRequestVallet,Response, CreateRequestCurrency, CreateRequestCategory, CreateRequestTransaction

from sqlalchemy.orm import Session

from array import *

#Vallet.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

curs_usd = array('f',[0.0, 92.8, 1.0, 0.93])


@app.get("/")
def hello():

    return "Hello"

@app.get("/vallets")
async def get_vallets(vallets = list[Vallet], db:Session = Depends(get_db) ):

    vallets = db.query(Vallet).all()
    return Response(code=200,
        message="Success",
        data=vallets)



@app.get("/vallets/{id}")
async def get_vallets_id(id: int, db:Session = Depends(get_db)):
        vallet = db.query(Vallet).get(id)

        if not vallet:
            raise HTTPException(status_code=404, detail=f"vallet item with id {id} not found")
        return vallet



@app.post("/vallets/create")
async def vallets(vallet: CreateRequestVallet, db:Session = Depends(get_db)):

    currency = db.query(Currency).get(vallet.currency_id)

    print(
        'vallet', currency
    )

    if not currency:
        return Response(
            code=404,
            message="Currency not found",
            data=None
        )
    
    w=Vallet(**vallet.dict())

    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )


@app.post("/currency/add")
async def add_currency(currency: CreateRequestCurrency, db:Session = Depends(get_db)):

    w=Currency(**currency.dict())

    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )

@app.post("/category/add")
async def add_category(category: CreateRequestCategory, db:Session = Depends(get_db)):

    w=Category(**category.dict())

    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )

@app.post("/transaction/add")
async def add_transaction(transaction: CreateRequestTransaction, db:Session = Depends(get_db)):

    w=Transaction(**transaction.dict())
    vallet1 = db.query(Vallet).get(w.vallet_id_1)
    vallet2 = db.query(Vallet).get(w.vallet_id_2)

    if(w.currency_id!=vallet2.currency_id):
        babki = w.symma * curs_usd[w.vallet_id_1]
    else: babki = w.symma
        

    if(vallet1!=vallet2):
        vallet1.amount -= w.symma
        vallet2.amount += babki
        db.commit()
    else: 
        vallet1.amount -= babki
        db.commit()


    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )


@app.delete("/vallets/delete/{id}")
async def delete_vallet(id: int, db:Session = Depends(get_db)):
 
    # get the given id
    vallet = db.query(Vallet).get(id)
 
    # if item with given id exists, delete it from the database. Otherwise raise 404 error
    if vallet:
        db.delete(vallet)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail=f"vallet item with id {id} not found")
 
    return Response(
        code=200,
        message="Delete Succes vallet id = "+f" {id}",
        data=vallet
    )


@app.put("/vallets/update/{id}")
async def update_vallet(id: int, request:CreateRequestVallet, db:Session = Depends(get_db)):
     
     vallet = db.query(Vallet).get(id)

     if vallet:
          vallet.currency_id = request.currency_id
          vallet.amount = request.amount
          db.commit()

     if not vallet:
        raise HTTPException(status_code=404, detail=f"vallet item with id {id} not found")
    
     return Response(
        code=200,
        message="Update Succes vallet id = "+f" {id} ",
        data= vallet
    )

@app.put("/vallets/trans/{id}/{summa}")
async def transaction(id: int, summa: int, db:Session = Depends(get_db)):
     
     vallet = db.query(Vallet).get(id)
     curr_id = vallet.currency_id


     if vallet:
          vallet.amount += summa
          db.commit()

     if not vallet:
        raise HTTPException(status_code=404, detail=f"vallet item with id {id} not found")
    
     return Response(
        code=200,
        message="Update Succes vallet id = "+f" {id}" + "Cur_id = "+ f"{curr_id}"+ "Ha Symmy = "+ f"{summa}",
        data= vallet
    )

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}