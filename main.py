from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, jobs, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rojgar Setu API",
    description="Connecting daily wage workers with local employers",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost",
    "null",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.get("/jobs-page")
def jobs_page():
    return FileResponse("frontend/jobs.html")

@app.get("/login")
def login_page():
    return FileResponse("frontend/login.html")

@app.get("/register")
def register_page():
    return FileResponse("frontend/register.html")

app.mount("/static", StaticFiles(directory="frontend"), name="static")