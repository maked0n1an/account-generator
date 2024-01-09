from abc import ABC, abstractmethod
from pathlib import Path

class Writer(ABC):
    header = ['Address', 'Private Key', 'Mnemonic']
    folder_name = 'results'
    
    @classmethod
    def create_folder(cls):
        relative_path = Path(cls.folder_name)        
        relative_path.mkdir(parents=True, exist_ok=True)
    
    @abstractmethod
    def write_data(self, data):
        pass
    