import questionary

from questionary import Choice

from modules import EthAccount, WriterFactor
from utils import center_output, format_input


def get_word_count() -> int:
    result = questionary.select(
        "Select count of words in mnemonics", 
        choices=[
            Choice("1) 12", 12),
            Choice("2) 15", 15),
            Choice("3) 18", 18),
            Choice("4) 21", 21),
            Choice("5) 24", 24),
        ],
        qmark="| ⚙️ ",
        pointer="✅ "
    ).ask()
    
    return result

def get_file_format() -> str:
    result = questionary.select(
        "Select file format to save mnemonics", 
        choices=[
            Choice("1) Excel", 'Excel'),
            Choice("2) CSV", 'CSV')
        ],
        qmark="| ⚙️ ",
        pointer="✅ "
    ).ask()
    
    return result
    

def greetings():
    name_label = "========= Wallet Creator ========="
    brand_label = "========== Author: M A K E D 0 N 1 A N =========="
    telegram = "======== https://t.me/crypto_maked0n1an ========" 
    
    print("")
    center_output(name_label)
    center_output(brand_label)
    center_output(telegram)
    
def main():
    greetings()
    word_number = get_word_count()
    wallet_num = int(format_input("Please type the number of wallets to generate: "))
    file_format = get_file_format()
    
    data = []
    
    for _ in range(wallet_num):
        account = EthAccount.generate_account(word_number)
        data.append(account)
    
    writer = WriterFactor.create_writer(file_format, "accounts")
    writer.write_data(data)
    
    center_output("✅ The accounts has been created successfully!")
    

if __name__ == '__main__':
    main()