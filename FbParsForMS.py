from facebook_scraper import get_profile, get_posts, get_group_info


class Parser:
    def __init__(self):
        self.users = {"names": [], "ids": [], "pictures": [], "contacts": [], "place": [], "work": [
        ], "events": [], "info": [], "education": [], "relationship": [], "family": []}
        self.posts = {"post_id": [], "text": [],
                      "post_text": [], "shared_text": [], "time": [], "timestamp": [], "image": [], "image_lowquality": [], "images": [], "images_description": [], "images_lowquality": [], "images_lowquality_description": [], "video": [], "video_duration_seconds": [], "video_height": [], "video_id": [], "video_quality": [], "video_size_MB": [], "video_thumbnail": [], "video_watches": [], "video_width": [], "likes": [], "comments": [], "shares": [], "post_url": [], "link": [], "links": [], "user_id": [], "username": [], "user_url": [], "is_live": [], "factcheck": [], "shared_post_id": [], "shared_time": [], "shared_user_id": [], "shared_username": [], "shared_post_url": [], "available": [], "comments_full": [], "reactors": [], "w3_fb_url": [], "reactions": [], "reaction_count": [], "with": [], "image_id": [], "image_ids": []}
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
            if post["post_id"]:
                self.posts["post_id"].append(post["post_id"])
            else:
                self.posts["post_id"].append("~~~~")
            if post["text"]:
                self.posts["text"].append(post["text"])
            else:
                self.posts["text"].append("~~~~")
            if post["post_text"]:
                self.posts["post_text"].append(post["post_text"])
            else:
                self.posts["post_text"].append("~~~~")
            if post["shared_text"]:
                self.posts["shared_text"].append(post["shared_text"])
            else:
                self.posts["shared_text"].append("~~~~")
            if post["time"]:
                self.posts["time"].append(post["time"])
            else:
                self.posts["time"].append("~~~~")
            if post["timestamp"]:
                self.posts["timestamp"].append(post["timestamp"])
            else:
                self.posts["timestamp"].append("~~~~")
            if post["image"]:
                self.posts["image"].append(post["image"])
            else:
                self.posts["image"].append("~~~~")
            if post["image_lowquality"]:
                self.posts["image_lowquality"].append(post["image_lowquality"])
            else:
                self.posts["image_lowquality"].append("~~~~")
            if post["images"]:
                self.posts["images"].append(post["images"])
            else:
                self.posts["images"].append("~~~~")
            if post["images_description"]:
                self.posts["images_description"].append(
                    post["images_description"])
            else:
                self.posts["images_description"].append("~~~~")
            if post["images_lowquality"]:
                self.posts["images_lowquality"].append(
                    post["images_lowquality"])
            else:
                self.posts["images_lowquality"].append("~~~~")
            if post["images_lowquality_description"]:
                self.posts["images_lowquality_description"].append(
                    post["images_lowquality_description"])
            else:
                self.posts["images_lowquality_description"].append("~~~~")
            if post["video"]:
                self.posts["video"].append(post["video"])
            else:
                self.posts["video"].append("~~~~")
            if post["video_duration_seconds"]:
                self.posts["video_duration_seconds"].append(
                    post["video_duration_seconds"])
            else:
                self.posts["video_duration_seconds"].append("~~~~")
            if post["video_height"]:
                self.posts["video_height"].append(post["video_height"])
            else:
                self.posts["video_height"].append("~~~~")
            if post["video_id"]:
                self.posts["video_id"].append(post["video_id"])
            else:
                self.posts["video_id"].append("~~~~")
            if post["video_quality"]:
                self.posts["video_quality"].append(post["video_quality"])
            else:
                self.posts["video_quality"].append("~~~~")
            if post["video_size_MB"]:
                self.posts["video_size_MB"].append(post["video_size_MB"])
            else:
                self.posts["video_size_MB"].append("~~~~")
            if post["video_thumbnail"]:
                self.posts["video_thumbnail"].append(post["video_thumbnail"])
            else:
                self.posts["video_thumbnail"].append("~~~~")
            if post["video_watches"]:
                self.posts["video_watches"].append(post["video_watches"])
            else:
                self.posts["video_watches"].append("~~~~")
            if post["video_width"]:
                self.posts["video_width"].append(post["video_width"])
            else:
                self.posts["video_width"].append("~~~~")
            if post["likes"]:
                self.posts["likes"].append(post["likes"])
            else:
                self.posts["likes"].append("~~~~")
            if post["comments"]:
                self.posts["comments"].append(post["comments"])
            else:
                self.posts["comments"].append("~~~~")
            if post["shares"]:
                self.posts["shares"].append(post["shares"])
            else:
                self.posts["shares"].append("~~~~")
            if post["post_url"]:
                self.posts["post_url"].append(post["post_url"])
            else:
                self.posts["post_url"].append("~~~~")
            if post["link"]:
                self.posts["link"].append(post["link"])
            else:
                self.posts["link"].append("~~~~")
            if post["links"]:
                self.posts["links"].append(post["links"])
            else:
                self.posts["links"].append("~~~~")
            if post["user_id"]:
                self.posts["user_id"].append(post["user_id"])
            else:
                self.posts["user_id"].append("~~~~")
            if post["username"]:
                self.posts["username"].append(post["username"])
            else:
                self.posts["username"].append("~~~~")
            if post["user_url"]:
                self.posts["user_url"].append(post["user_url"])
            else:
                self.posts["user_url"].append("~~~~")
            if post["is_live"]:
                self.posts["is_live"].append(post["is_live"])
            else:
                self.posts["is_live"].append("~~~~")
            if post["factcheck"]:
                self.posts["factcheck"].append(post["factcheck"])
            else:
                self.posts["factcheck"].append("~~~~")
            if post["shared_post_id"]:
                self.posts["shared_post_id"].append(post["shared_post_id"])
            else:
                self.posts["shared_post_id"].append("~~~~")
            if post["shared_time"]:
                self.posts["shared_time"].append(post["shared_time"])
            else:
                self.posts["shared_time"].append("~~~~")
            if post["shared_user_id"]:
                self.posts["shared_user_id"].append(post["shared_user_id"])
            else:
                self.posts["shared_user_id"].append("~~~~")
            if post["shared_username"]:
                self.posts["shared_username"].append(post["shared_username"])
            else:
                self.posts["shared_username"].append("~~~~")
            if post["shared_post_url"]:
                self.posts["shared_post_url"].append(post["shared_post_url"])
            else:
                self.posts["shared_post_url"].append("~~~~")
            if post["available"]:
                self.posts["available"].append(post["available"])
            else:
                self.posts["available"].append("~~~~")
            if post["comments_full"]:
                self.posts["comments_full"].append(post["comments_full"])
            else:
                self.posts["comments_full"].append("~~~~")
            if post["reactors"]:
                self.posts["reactors"].append(post["reactors"])
            else:
                self.posts["reactors"].append("~~~~")
            if post["w3_fb_url"]:
                self.posts["w3_fb_url"].append(post["w3_fb_url"])
            else:
                self.posts["w3_fb_url"].append("~~~~")
            if post["reactions"]:
                self.posts["reactions"].append(post["reactions"])
            else:
                self.posts["reactions"].append("~~~~")
            if post["reaction_count"]:
                self.posts["reaction_count"].append(post["reaction_count"])
            else:
                self.posts["reaction_count"].append("~~~~")
            if post["with"]:
                self.posts["with"].append(post["with"])
            else:
                self.posts["with"].append("~~~~")
            if post["image_id"]:
                self.posts["image_id"].append(post["image_id"])
            else:
                self.posts["image_id"].append("~~~~")
            if post["image_ids"]:
                self.posts["image_ids"].append(post["image_ids"])
            else:
                self.posts["image_ids"].append("~~~~")

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


if __name__ == "__main__":
    par = Parser()
    par.get_group("nintendo")
    print(par.export()[2])
