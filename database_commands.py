import json
filename = "data.json"

def load_data():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return "error"

def save_data(data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except:
        return "error"


# def add_post(post_id, content):
#     """افزودن پست جدید"""
#     data = load_data()
#     data["posts"].append({"id": post_id, "content": content, "likes": 0})
#     save_data(data)
#     print(f"✅ پست {post_id} ثبت شد.")

# def like_post(username, post_id):
#     """لایک کردن یک پست"""
#     data = load_data()
#     user = next((user for user in data["users"] if user["username"] == username), None)
#     post = next((post for post in data["posts"] if post["id"] == post_id), None)

#     if not user:
#         print("❌ کاربر یافت نشد!")
#         return
#     if not post:
#         print("❌ پست یافت نشد!")
#         return
#     if post_id in user["liked_posts"]:
#         print("⚠️ شما قبلاً این پست را لایک کرده‌اید!")
#         return

#     user["liked_posts"].append(post_id)
#     post["likes"] += 1
#     save_data(data)
#     print(f"❤️ {username} پست {post_id} را لایک کرد!")

