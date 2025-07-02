import random
import os
from datetime import datetime, timedelta
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Article:
    def __init__(self, topic):
        self.topic = topic
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.title = self.generate_title()
        self.body = self.generate_body()
        self.author = self.generate_author()
        self.news_network = self.generate_news_network()
        self.release_date = self.generate_release_date()
        self.image_url = self.generate_image()

    def generate_title(self):
        prompt = f"""
        Write a sensational, clickbait-style news headline about: "{self.topic}"
        Make it sound like a real news headline. Return only the headline, no quotes or extra text.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return f"BREAKING: {self.topic} - You Won't Believe What Happens Next!"

    def generate_body(self):
        prompt = f"""
        Write a detailed, realistic, and creative fake news article about: "{self.topic}". The article must be at least 1000 words long. 
        - Start with a strong hook matching the headline
        - Include fake quotes from "experts" or "sources"
        - Use creative, varied, and sensational language
        - End with a dramatic conclusion
        Make it sound like a real news article. Do not write less than 1000 words. If you finish before 1000 words, continue the story with more details, quotes, and background until you reach the length.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4096
            )
            article = response.choices[0].message.content.strip()
            # Fallback: if article is too short, append a message
            if len(article.split()) < 800:
                article += "\n\n[The story continues with more shocking developments, expert opinions, and exclusive interviews. Stay tuned for updates as this story unfolds.]"
            return article
        except Exception:
            return f"In a shocking development that has left experts baffled, {self.topic} has taken an unexpected turn. Sources close to the situation reveal that this unprecedented event could have far-reaching implications for all of us. 'This changes everything,' said one anonymous insider. The implications of this story are still being analyzed by leading experts in the field."

    def generate_author(self):
        first_names = ["Sarah", "Michael", "Jennifer", "David", "Emily", "James", "Jessica", "Robert", "Amanda", "Christopher"]
        last_names = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def generate_news_network(self):
        networks = [
            "Global News Network", "International Press", "World Report", "National Daily",
            "Metro News", "City Times", "Regional Report", "Continental News",
            "Pacific Press", "Atlantic Media", "Central Broadcasting", "United News"
        ]
        return random.choice(networks)

    def generate_release_date(self):
        days_ago = random.randint(0, 90)
        return (datetime.now() - timedelta(days=days_ago)).strftime("%B %d, %Y")

    def generate_image(self):
        try:
            # Try gpt-image-1 first
            response = self.client.images.generate(
                model="gpt-image-1",
                prompt=f"{self.topic}, professional news photo, realistic, 16:9, not cartoonish.",
                size="1792x1024",
                quality="high",
                n=1,
            )
            image_url = response.data[0].url
            print("Generated image URL (gpt-image-1):", image_url)
            return image_url
        except Exception as e:
            print("gpt-image-1 error:", e)
            # Fallback to DALL-E 3
            try:
                response = self.client.images.generate(
                    model="dall-e-3",
                    prompt=f"{self.topic}, professional news photo, realistic, 16:9, not cartoonish.",
                    size="1792x1024",
                    quality="standard",
                    n=1,
                )
                image_url = response.data[0].url
                print("Generated image URL (dall-e-3):", image_url)
                return image_url
            except Exception as e2:
                print("DALL-E 3 error:", e2)
                return "https://via.placeholder.com/800x400/cccccc/666666?text=News+Image"

    def regenerate(self):
        self.title = self.generate_title()
        self.body = self.generate_body()
        self.image_url = self.generate_image()

    def regenerate_component(self, component):
        if component == "title":
            self.title = self.generate_title()
        elif component == "body":
            self.body = self.generate_body()
        elif component == "image":
            self.image_url = self.generate_image()
