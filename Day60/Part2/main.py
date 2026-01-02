from flask import Flask, render_template, request
import requests
import smtplib
import json

smtp_server = "smtp.gmail.com"
smtp_port = 587
receiver_email = "murilomatsuora@gmail.com"
with open("sensitive_data.json") as file:
    sensitive_data = json.load(file)

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    print(request.method)
    if request.method == 'POST':
        return do_the_login(contact_info=request.form)
    else:
        return render_template("contact.html")
    
def do_the_login(contact_info):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sensitive_data["sender_data"]["email"], sensitive_data["sender_data"]["password"])
            
            email_content = (
                f"Subject: Message from {contact_info['name']}\n\n"
                f"Name: {contact_info['name']}\n"
                f"Email: {contact_info['email']}\n"
                f"Phone: {contact_info['phone']}\n\n"
                f"Message:\n{contact_info['message']}"
            )
            
            server.sendmail(
                from_addr=sensitive_data["sender_data"]["email"], 
                to_addrs=receiver_email, 
                msg=email_content
            )
        
        print("Email sent successfully!")
        return render_template("contact_successfull.html")

    except Exception as e:
        print(f"Error: {e}")

        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
