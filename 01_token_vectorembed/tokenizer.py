import tiktoken


## max gpt vocab_size

encoder = tiktoken.encoding_for_model('gpt-4o')

print('vocab size of gpt 4o', encoder.max_token_value)

# print('token encoder', encoder.encode)


text = "people set on chair" #[28963, 920, 402, 16540]
# text = "chair set on people" #[45585, 920, 402, 1665]

tokens = encoder.encode(text)

print('Tokens',tokens)

output = [28963, 920, 402, 16540,0,]

decoded = encoder.decode(output)

print('decoded tokens =>  ',decoded)