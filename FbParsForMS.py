from facebook_scraper import get_profile, get_posts, get_group_info


class Parser:
    def __init__(self):
        self.users = {"names": [], "ids": [], "pictures": [], "contacts": [], "place": [], "work": [
        ], "events": [], "info": [], "education": [], "relationship": [], "family": []}
        self.posts = {}
        self.groups = {'admins': [], 'id': [],
                       'members': [], 'name': [], 'type': []}
        with open("exports/users.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/posts.txt", "w", encoding="utf-8") as file:
            file.write("\n")
        with open("exports/groupes.txt", "w", encoding="utf-8") as file:
            file.write("\n")

    def get_user(self, url):
        request = get_profile(url, cookies="cookie.txt")
        try:
            self.users["names"].append(request['Name'])
        except:
            self.users["names"].append("~~~~")
        try:
            self.users["ids"].append(request['id'])
        except:
            self.users["ids"].append("~~~~")
        try:
            self.users["pictures"].append(request['profile_picture'])
        except:
            self.users["pictures"].append("~~~~")
        try:
            self.users["contacts"].append(request['Contact Info'])
        except:
            self.users["contacts"].append("~~~~")
        try:
            self.users["place"].append(request['Places Lived'])
        except:
            self.users["place"].append("~~~~")
        try:
            self.users["work"].append(request['Work'])
        except:
            self.users["work"].append("~~~~")
        try:
            self.users["events"].append(request['Life Events'])
        except:
            self.users["events"].append("~~~~")
        try:
            self.users["info"].append(request['Basic Info'])
        except:
            self.users["info"].append("~~~~")
        try:
            self.users["education"].append(request['Education'])
        except:
            self.users["education"].append("~~~~")
        try:
            self.users["relationship"].append(request['Relationship'])
        except:
            self.users["relationship"].append("~~~~")
        try:
            self.users["family"].append(request['Family Members'])
        except:
            self.users["family"].append("~~~~")
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
        try:
            self.groups["admins"].append(request['admins'])
        except:
            self.groups["admins"].append("~~~~")
        try:
            self.groups["id"].append(request['id'])
        except:
            self.groups["id"].append("~~~~")
        try:
            self.groups["members"].append(request['members'])
        except:
            self.groups["members"].append("~~~~")
        try:
            self.groups["name"].append(request['name'])
        except:
            self.groups["name"].append("~~~~")
        try:
            self.groups["type"].append(request['type'])
        except:
            self.groups["type"].append("~~~~")
        with open('exports/groupes.txt', 'a', encoding="utf-8") as file:
            file.write(f"{request}\n")

    def export(self):
        return([self.users, self.posts, self.groups])

    def test(self):
        for post in get_posts("zack", pages=1, cookies="cookie.txt"):
            for k, v in post.items():
                try:
                    self.posts[k].append(v)
                except:
                    self.posts[k] = []
                    self.posts[k].append(v)
        for k, v in self.posts.items():
            print(f"Key: {k}\nV: {v}")


if __name__ == "__main__":
    par = Parser()
    try:
        par.get_group(" ")
    except:
        pass
    par.test()
