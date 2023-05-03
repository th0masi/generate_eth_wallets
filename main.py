import pandas as pd
from eth_account import Account
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def generate_ethereum_wallets(count):
    wallets = []

    for _ in range(count):
        mnemonic_generator = Bip39MnemonicGenerator()
        mnemonic = mnemonic_generator.FromWordsNumber(words_num=12)
        seed = Bip39SeedGenerator(mnemonic).Generate()
        bip_obj = Bip44.FromSeed(seed, Bip44Coins.ETHEREUM)

        private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey().Raw().ToBytes()
        account = Account.from_key(private_key)

        wallets.append({
            'address': account.address,
            'private_key': private_key.hex(),
            'mnemonic': mnemonic,
        })

    return wallets

def save_wallets_to_csv(wallets, file_name):
    df = pd.DataFrame(wallets, columns=['address', 'private_key', 'mnemonic'])
    df.columns = ['Wallets', 'Private Key', 'Seed Phrases']
    df.to_csv(file_name, index=False)

def save_wallets_to_files(wallets):
    with open('wallets.txt', 'w') as f:
        for wallet in wallets:
            f.write(f"{wallet['address']}\n")

    with open('private_key.txt', 'w') as f:
        for wallet in wallets:
            f.write(f"{wallet['private_key']}\n")

    with open('seeds.txt', 'w') as f:
        for wallet in wallets:
            f.write(f"{wallet['mnemonic']}\n")

if __name__ == '__main__':
    count = int(input("Введите количество кошельков для генерации: "))
    wallets = generate_ethereum_wallets(count)
    save_wallets_to_csv(wallets, 'wallets.csv')
    save_wallets_to_files(wallets)
    print(f"\n>>> Сгенерировано {count} кошельков Ethereum и сохранено в файлах wallets.csv, wallets.txt, private_key.txt и seeds.txt")
