import torch, joblib, re

job_token = joblib.load('mytokenizer')

job_model = joblib.load('bart_model')


class Summarizer():
    def __init__(self, text_to_summ:str):
      self.text_to_summ = text_to_summ
      
    def clean_text(self, text):
      """To clean the input text
      params:
      text: text to be summarised  
      """
    
      ### Command for removing EMOJI
      RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
      text = RE_EMOJI.sub(r'', self.text_to_summ)
    
      ### Command for removing links
      text = re.sub(r'https?://[A-Za-z0-9./]+', '', text)
    
      ### Command for removing symbols/punctuation 
    #   text = re.sub(r'[^\w\s]','',text)
    
      return text

    def summarize_text(self) -> str:
      input_text = self.clean_text(self.text_to_summ)
      inputs = job_token([input_text], return_tensors="pt")
      summary_ids_model = job_model.generate(inputs['input_ids'], max_length=500, early_stopping=False)
      output = [job_token.decode(g, skip_special_tokens=True) for g in summary_ids_model]

      return " ".join(output)


# summ = Summarizer(text_to_summ=text_to_summarize)

# print(summ.summarize_text())