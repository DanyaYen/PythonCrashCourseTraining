crypto_shit_list = ['Bitcoin', 'Etherium', 'Toncoin', 'Solana', 'Toncoin', 'Avalanche', 'Ripple']
i_have = []
x  = ', '.join(crypto_shit_list)
print(f'i need to buy {x}')
while 'Toncoin' in crypto_shit_list:
    crypto_shit_list.remove('Toncoin')
print("damn all Toncoins sold out")
while crypto_shit_list:
    current_crypto = crypto_shit_list.pop()
    print(f"Buying crypto: {current_crypto}")
    i_have.append(current_crypto)
print("\nThe following crypto has been bought:")
for crypto in i_have:
    print(crypto)