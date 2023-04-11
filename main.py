import requests
class fg:
  black = "\u001b[30m"
  red = "\u001b[31m"
  green = "\u001b[32m"
  yellow = "\u001b[33m"
  blue = "\u001b[34m"
  magenta = "\u001b[35m"
  cyan = "\u001b[36m"
  white = "\u001b[37m"
  reset = "\u001b[0m"
notwhanet = []
banner = f"""{fg.yellow}

  _____                 _                   _____    _               _____                           _             
 |  __ \               | |                 |_   _|  | |             / ____|                         | |            
 | |__) |__ _ _ __   __| | ___  _ __ ___     | |  __| | ___  __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \    | | / _` |/ _ \/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | | \ \ (_| | | | | (_| | (_) | | | | | |  _| || (_| |  __/ (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_| |_____\__,_|\___|\__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                   
                                                                                                                   
                    {fg.reset}                       
"""
def logic():
    baseurl="https://what-to-code.com/api/ideas/random"
    #GET method
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0"

    }
    res = requests.get(baseurl, headers=headers)
    if res.status_code == 200:
        a = res.json()["description"]
        b = res.json()["title"]
        c = res.json()["id"]
        d = res.json()["likes"]
        e = res.json()["tags"] if res.json()["tags"] else "None"
        final =f"""
{fg.yellow}Title: {fg.reset}{b}\n{fg.red}Description:{fg.reset}{a}\n{fg.blue}ID: {fg.reset}{c}\n{fg.green}Likes: {fg.reset}{d}\n{fg.magenta}Tags: {fg.reset}{e}
        """
        return final
    else:
        raise f"{fg.red}Unexpectd error, status code: " + res.status_code + fg.reset
def generate():
    
    import os
    os.system("cls" if os.name == "nt" else "clear")
    print(banner)
    idea = logic()
    if idea in notwhanet:
        generate()
    print(idea)
    print(f"\n\n{fg.yellow}Do you want to do this idea or choose other?{fg.reset} \n{fg.yellow}[{fg.reset}1{fg.yellow}] Use This Idea \n{fg.yellow}[{fg.reset}2{fg.yellow}] Choose Another Idea{fg.reset}:")
    choice = input()
    if choice == "1":
        print(f"{fg.magenta} Go on using this!{fg.reset}")
    else:
        title=idea.split("\n")
        
        title = title[1].replace("Title: ", "")
        
        
        notwhanet.append(title)
        
        generate()
def main():
    import os
    os.system("cls" if os.name == "nt" else "clear")
    print(f""" {fg.yellow}


  _____                 _                   _____    _               _____                           _             
 |  __ \               | |                 |_   _|  | |             / ____|                         | |            
 | |__) |__ _ _ __   __| | ___  _ __ ___     | |  __| | ___  __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \    | | / _` |/ _ \/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | | \ \ (_| | | | | (_| | (_) | | | | | |  _| || (_| |  __/ (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_| |_____\__,_|\___|\__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                   
                                                                                                                   
                                                                                                                                                                            
{fg.yellow}[{fg.reset}1{fg.yellow}] Generate
{fg.yellow}[{fg.reset}2{fg.yellow}] Exit{fg.reset}
    """)
    choice = input(f"{fg.cyan}Pick one: {fg.reset}")
    if choice == "1":
        generate()
    elif choice == "2":
        import sys
        sys.exit()
    else:
        print(f"{fg.red}Invalid choice.{fg.reset}")
        main()

main()
