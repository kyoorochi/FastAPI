from fastapi import FastAPI, APIRouter

# 로컬 메모리 DB - 서버를 종료하면 데이터가 사라진다.
BOOKS = [
    {
        'id': 1,
        'title': '퍼펙트 게임',
        'author': '장이',
        'url': 'https://www.yes24.com/퍼펙트게임'
    }
]

app = FastAPI()
router = APIRouter()

# 루트 페이지
@router.get('/', status_code=200)
def main():
    return {'Message':'Welcome to the Book World!'}

# 전체 책 데이터 조회
@router.get('/api/v1/books', status_code=200)
def get_all_books() -> list:
    return BOOKS

# 특정 책 데이터 조회
@router.get('/api/v1/books/{book_id}')
def get_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         book
    #         break 과 같은 개념

    if book:
        return book
    return {'error':f'Book not found, ID: {book_id}'}
  
# 책 생성
@router.post('/api/v1/books/')
def create_book(book: dict):
    #{'id':2, 'title':'' ...}
    BOOKS.append(book)
    return book

# 책 수정
@router.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book_update: dict):
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    for key, value in book_update.items():
        if key in book:
            book[key] = value
    return book

# 책 삭제
@router.delete('/api/v1/books/{book_id}')
def delete_book(book_id: int):
    global BOOKS
    BOOKS = [item for item in BOOKS if item['id'] != book_id]
    # for item in BOOKS:
    #     if item['id'] != book_id:
    #         item
    return {'message': f'Successfully deleted book, ID: {book_id}'}

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('books:app', port=8001, reload=True)