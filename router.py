from fastapi import APIRouter
from repository import BookRepo
from model import Book , Response

router= APIRouter()

@router.get("/book/")
async def get_all():
    _booklist = await BookRepo.retrieve()
    return Response(code=200,status="ok",message="successfull",result=_booklist).dict(exclude_none=True)


@router.post("/book/create")
async def create(book : Book):
    await BookRepo.insert(book)
    return Response(code=200,status="ok",massage="success save data").dict(exclude_none=True)

@router.get("/book/{id}")
async def get_id(id:str):
    _book = await BookRepo.retrieve_id(id)
    return Response(code=200,status="ok",massage="success retrieve data",result=__annotations__).dict(exclude_none=True)

@router.post("/book/update")
async def update(book:Book):
    return Response(code=200,status="ok",massage="success retrieve data").dict(exclude_none=True)

@router.delete("/book/{id}")
async def delete(id:str):
    await BookRepo.delete(id)
    return Response(code=200,status="ok",massage="success delete data").dict(exclude_none=True)

