import uvicorn, whatsappsum
from fastapi import FastAPI 
from pydantic_file import WhatsappSum


app = FastAPI()

@app.get("/")
def index():
    return {"message":"Welcome to Whatsappsummarizer"}


@app.post("/summarize_post")
def summarize_post(whatsapppost : WhatsappSum):
    summarizer = whatsappsum.Summarizer(whatsapppost.text_to_summ[0])
    return {'summarized_text': summarizer.summarize_text()}



if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)




