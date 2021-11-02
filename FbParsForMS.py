from facebook_scraper import get_profile, get_posts, get_group_info
import requests


class Setings:
    def __init__(self):
        self.settings = {}
        with open("additional_files/settings.txt", "r", encoding="utf-8") as file:
            self.file = file.read()
        self.settingsF = self.file.split('\n')
        for setingF in self.settingsF:
            set = setingF.split("=")
            self.settings[set[0]] = set[1]

    def get(self):
        return(self.settings)


class Cookies:
    def __init__(self, s):
        self.loging = s["cokie_loggining"]
        self.login = s["login"]
        self.passwd = s["passwd"]

    def get(self):
        session = requests.Session()
        if self.loging:
            session.auth = (self.login, self.passwd)
        response = session.get('http://facebook.com')
        kok = []
        for c in session.cookies:
            kok.append({'name': c.name, 'value': c.value,
                        'domain': c.domain, 'path': c.path, 'secure': c.secure})
        with open("additional_files/cookie.txt", "w", encoding="utf-8") as file:
            file.write(str(kok))


class Parser:
    def __init__(self):
        self.users, self.posts, self.groups = {}, {}, {}
        with open("exports/users.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/posts.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/groupes.txt", "w", encoding="utf-8") as file:
            file.write("\n")

    def get_user(self, url, c=0):
        if c:
            request = get_profile(url, cookies="additional_files/cookie.txt")
        else:
            request = get_profile(url)
        for k, v in request.items():
            try:
                self.users[k].append(v)
            except:
                self.users[k] = []
                self.users[k].append(v)
        with open('exports/users.txt', 'a', encoding="utf-8") as file:
            file.write(f"{request}\n")

    def get_postes(self, search, il=1, c=0):
        if c:
            posts = get_posts(search, pages=il, cookies="additional_files/cookie.txt")
        else:
            posts = get_posts(search, pages=il)
        for post in posts:
            for k, v in post.items():
                try:
                    self.posts[k].append(v)
                except:
                    self.posts[k] = []
                    self.posts[k].append(v)

        with open('exports/posts.txt', 'a', encoding="utf-8") as file:
            file.write(f"{self.posts}\n")

    def get_group(self, url, c=0):
        if c:
            request = get_group_info(url, cookies="additional_files/cookie.txt")
        else:
            request = get_group_info(url)
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
    set = Setings()
