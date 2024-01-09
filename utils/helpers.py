def center_output(message: str):
    print(f"| {message:^59}|")
    
    
def format_input(message: str) -> str:
    print(f"| {message:^59}|", end='\n| ', flush=True)    
    value = input()
    
    return value