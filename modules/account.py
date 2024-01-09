from eth_account import Account

from utils.exceptions import ValidationException


class EthAccount():
    VALID_WORD_COUNTS = [12, 15, 18, 21, 24]
    
    @staticmethod
    def generate_account(word_count: int) -> list[str]:
        if word_count not in EthAccount.VALID_WORD_COUNTS:
            raise ValidationException(
                f"Invalid choice for number of words: {word_count}, should be one of "
                f"{EthAccount.VALID_WORD_COUNTS}"
            )
        
        Account.enable_unaudited_hdwallet_features()
        account, mnemonic = Account.create_with_mnemonic(num_words=word_count)
        
        return [account.address, account.key.hex(), mnemonic]