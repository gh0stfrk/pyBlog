from html.parser import HTMLParser

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime


class HTMLTextExtractor(HTMLParser):
    """Extracts Text from html markup"""

    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, d):
        self.result.append(d)

    def get_text(self):
        return "".join(self.result)


def send_recommendation_email(
    recommender_name,
    recommender_email,
    post_title,
    post_url,
    recipient_email,
    comments=None,
):
    subject = f"Reading Recommendation from {recommender_name} ({recommender_email}), read '{post_title}'"
    html_message = render_to_string(
        "blog/post/mail.html",
        {
            "recommender_name": recommender_name,
            "recommender_email": recommender_email,
            "post_title": post_title,
            "post_url": post_url,
            "year": datetime.now().year,
            "comments": comments,
        },
    )
    plain_message = strip_tags(html_message)
    from_email = "your-email@example.com"
    send_mail(
        subject, plain_message, from_email, [recipient_email], html_message=html_message
    )
