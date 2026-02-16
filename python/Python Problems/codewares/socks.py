def get_socks(name: str, socks: list[str]) -> list[str] | list:
    
    if len(socks) < 2: return []

    socks_to_wear = []

    if name == 'Henry':
        for sock in socks:
            if socks.count(sock) >= 2:
                socks_to_wear.append(sock)
            else:
                continue   
    
    if name == 'Punky':
        for i in range(len(socks)):
            for j in range(i + 1, len(socks)):
                if socks[i] != socks[j]:
                    return [socks[i], socks[j]]
        

    return socks_to_wear
            
print(get_socks('Punky', ['red','blue','blue','green']), ['red', 'blue'])
print(get_socks('Punky', ['pink', 'argyle', 'argyle']), ['pink', 'argyle'])
