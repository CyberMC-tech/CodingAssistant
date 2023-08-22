from ctransformers import AutoModelForCausalLM
from Options import *

model = 'Stablecode'
llm_info = Models[model]
llm = AutoModelForCausalLM.from_pretrained(**llm_info)


prompt = input('USER: ')
llm_prompt = Prompts[model].format(prompt=prompt)

print('ASSISTANT: ', end='')
generator = llm(llm_prompt, stream=True)
[print(word, end='', flush=True) for word in generator]
