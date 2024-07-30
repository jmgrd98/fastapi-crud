from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17
    },
    2: {
        "name": "Jane",
        "age": 18
    },
    3: {
        "name": "Jack",
        "age": 19
    }
}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/student/{student_id}")
async def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0, lt=4)):
    return students[student_id]


