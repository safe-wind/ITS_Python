def is_valid_ipv4(address: str) -> bool:

    numeri = address.split('.')
    if len(numeri) != 4:
        return False

    for i in numeri:
        if not i.isdigit():
            return False
        i = int(i)
        if 0 <= i <=255:
            continue
        else:
            return False
        
    return True