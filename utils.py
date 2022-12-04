def read_data(data_path: str, encoding_type='utf-8-sig') -> list:
    
    with open(data_path, encoding=encoding_type, mode='r') as file:
        data = file.read().splitlines()
        file.close()
    
    return data