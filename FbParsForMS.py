from facebook_scraper import get_profile, get_posts, get_group_info

class Parser:
    def __init__(self):
        self.users, self.posts, self.groups = {}, {}, {}
        with open("exports/users.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/posts.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/groupes.txt", "w", encoding="utf-8") as file:
            file.write("\n")

    def get_user(self, url):
        request = get_profile(url, cookies="cookie.txt")
        for k, v in request.items():
            try:
                self.users[k].append(v)
            except:
                self.users[k] = []
                self.users[k].append(v)
        with open('exports/users.txt', 'a', encoding="utf-8") as file:
            file.write(f"{request}\n")

    def get_postes(self, search, il=1):
        for post in get_posts(search, pages=il, cookies="cookie.txt"):
            for k, v in post.items():
                try:
                    self.posts[k].append(v)
                except:
                    self.posts[k] = []
                    self.posts[k].append(v)

        with open('exports/posts.txt', 'a', encoding="utf-8") as file:
            file.write(f"{self.posts}\n")

    def get_group(self, url):
        request = get_group_info(url, cookies="cookie.txt")
        for k, v in request.items():
            try:
                self.groups[k].append(v)
            except:
                self.groups[k] = []
                self.groups[k].append(v)
        with open('exports/groupes.txt', 'a', encoding="utf-8") as file:
            file.write(f"{request}\n")

    def export(self):
        return([self.users, self.posts, self.groups])

if __name__ == "__main__":
    par = Parser()
    try:
        par.get_group(" ")
    except:
        pass
    par.get_user("zack")
    print(par.export())