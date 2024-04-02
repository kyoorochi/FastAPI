from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

# 동기용 데이터베이스 접속 명령여
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:0521@localhost/oz-fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 접속 명령어(aiomysql)
# 무거운 I/O 요청이 먼저 와도, 뒤에 가벼운 I/O 작업 요청이 들어오면 더 빨리 끝나는 녀석이 응답한다.
ASYNC_SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://root:0521@localhost/oz-fastapi'
engine = create_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

Base = declarative_base()