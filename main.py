from fastapi import FastAPI
app = FastAPI()
eat={1:"karthikeya"}
@app.get("/get/{mess}")
def read_course(mess):
  a=eat.get(int(mess))
  
  return {"here you go": a}

@app.post("/post/{mess}")
def rr(mess):
  eat[list(eat.keys())[-1]+1]=mess
  i=list(eat.keys())[-1]
  return {"status": "successfully posted the id is: "+str(i)}
