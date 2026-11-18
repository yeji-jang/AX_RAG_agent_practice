"""
shared/core 모듈 동작 확인용 테스트

- 실행방법 :
    1) cd src
    2) uv run python -m scripts.db_core
"""

# 테스트 함수 가져오기
from shared.core.vector_store import (
    get_raw_db_connection,
    get_vector_store,
    get_embeddings,
    get_llm
)


# 테스트 함수 정의하기

"""1. DB 연결 확인"""
def test_db() :
    pass
    # conn = get_raw_db_connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT current_database()")
    # print(" 1. DB 연결 : ", cursor.)


"""2. 벡터 스토어"""
def test_vector_store() : 
    pass


"""3. 임베딩 벡터 길이"""
def test_embeddings() :
    pass


"""4. LLM 모델의 응답 품질"""


def test_llm() :
    pass
#     answer = get_llm().invoke("")


# if __name__ == "__main__" : 
#     test_db()
#     test_vector_store()
#     test_embeddings()
#     test_llm()

