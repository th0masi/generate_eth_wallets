# generate_eth_wallets
Массово генерирует кошельки, сохраняет сразу в 4 файла. Запустите, введите количество.  
  
```wallets.txt``` - только кошельки  
```private_key.txt``` - только приватники  
```seeds.txt``` - только сид-фразы  

```wallets.csv``` - таблица, в формате address_wallet:private_key:seed

# Установка

необходимо 2 библиотеки, можно установить 2 способами:  
```pip install pandas``` (для таблицы)  
```pip install eth_account bip_utils```  

или:  

```pip install -r requirements.txt``` (установит автоматически из requirements.txt)
