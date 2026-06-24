from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS 설정 (React에서 접근 가능하도록)
# 교차 출처 리소스 공유 ( 포트가 다르므로 다른 출처)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # 허용할 출처 모두 허용((*)(React 전용 : "http://localhost:5173")
    allow_credentials=True,  #(인증정보 허용, 쿠키, jWT토큰 등등)
    allow_methods=["*"],     #허용할 HTTP메서드(get, post, patch, put, delete)
    allow_headers=["*"],     #허용할 http헤더(Content-Type, Authorization)
)

# 요청 데이터 모델
class LoginRequest(BaseModel):
    userid: str
    password: str

# 모크 데이터
MOCK_USER = {
    "userid": "ujkiol1254",
    "password": "938002"
}

@app.post("/login")
async def login(request: LoginRequest):
    if request.userid != MOCK_USER["userid"]:
        msg = '사용자 아이디가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)

    if request.password != MOCK_USER["password"]:
        msg = '비밀번호가 틀렸습니다'
        raise HTTPException(status_code=401, detail=msg)

    return {"message": "로그인 성공"}