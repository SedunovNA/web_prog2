from typing import Union

from fastapi import FastAPI,Depends, HTTPException

from app.models.vallet import Vallet

from app.config.database import engine, get_db

from app.schemas.vallet_schema import CreateRequestVallet,Response

from sqlalchemy.orm import Session

Vallet.metadata.create_all(bind=engine)

app = FastAPI()



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
    w=Vallet(**vallet.dict())

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
          vallet.currency = request.currency
          vallet.amount = request.amount
          db.commit()

     if not vallet:
        raise HTTPException(status_code=404, detail=f"vallet item with id {id} not found")
    
     return Response(
        code=200,
        message="Update Succes vallet id = "+f" {id} ",
        data= vallet
    )


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}