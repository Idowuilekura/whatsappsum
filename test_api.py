text_to_summarize = """
A GLIMPSE INTO THE META-LIFE


Some days are indelible in my heart because either someone dear to me was born or died.


November 9th is one of those days for me because it was the day Myles Munroe died in a plane crash together with his wife and some others.


MYLES MUNROE was a Kingdom General known for his teachings on purpose and kingdom advancement.


Years away from now, "YOU" will die. Your body will be lifeless with YOU out of it. Just at that moment, there will be tears erupting out as the news of your death will flood social media.


At that moment for YOU, the physical will be totally gone and the metaphysical will be as real as anything you have ever known. Your greatest concern will be how much of your physical activity translated to metaphysical profit.


How will it be for you? Death is something that is inevitable yet we don't wanna think of it for a second.


YOU will stand before your creator for "judgement." Did that sound scary? Probably. How prepared are YOU for that day?


Probably, it will be in an examination format with lots of questions, both objective and theory.


Some of the questions would be like: Did you discover your specific purpose while you lived on earth? Did you fulfill the purpose why you were born? What percentage of humanity did you impact with your life? What percentage of your life was wasted? Did you use your purpose for selfish gain or kingdom advancement?


Myles Munroe lived a life of purpose and I was impacted by his lifestyle, a psychospiritual life.


It's exactly seven years since he went to glory.


Sleep on Dr. Myles Munroe. 


"It is better to go to a house of mourning than to go to a house of feasting, for death is the destiny of everyone; the living should take this to heart." Eccl.7:2
"""

url = "https://whatsappsumm.azurewebsites.net/summarize_post"

# text_to_summarize = (text_to_summarize.strip().split('\n'))

text_to_summarize = [text_to_summarize]

data = {'text_to_summ': text_to_summarize}
import requests
resp = requests.post(url=url, json = data)

print(resp.json())

# print(text_to_summarize)