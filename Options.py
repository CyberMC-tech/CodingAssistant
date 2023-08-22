
Prompts = {
    'Stablecode': '###Instruction:\n{prompt}\n\n###Response:',
    'Llama': '''[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

{prompt} [/INST]
'''
}


Models = {
    'Stablecode': {
        'model_path_or_repo_id': 'models/stablecode-instruct-alpha-3b.ggmlv1.q4_1.bin',
        'model_type': 'gpt-neox',
        'local_files_only': True
        },

    'Llama': {
        'model_path_or_repo_id': 'TheBloke/Llama-2-7B-Chat-GGML',
        'model_type': 'llama',
        'model_file': 'llama-2-7b-chat.ggmlv3.q2_K.bin'
    }
}
