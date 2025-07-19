from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings.'

    def handle(self, *args, **kwargs):
        # Ensure at least one user exists
        if not User.objects.exists():
            User.objects.create_user(username='testuser', password='password123')

        user = User.objects.first()

        sample_titles = [
            "Beach House", "Mountain Cabin", "City Apartment", "Safari Lodge", "Lakeview Cottage"
        ]

        for i in range(10):
            Listing.objects.create(
                title=random.choice(sample_titles) + f" {i}",
                description="A beautiful place to stay with modern amenities.",
                location=random.choice(["Nairobi", "Mombasa", "Naivasha", "Kisumu", "Diani"]),
                price_per_night=random.randint(30, 300),
                owner=user
            )

        self.stdout.write(self.style.SUCCESS("✅ Successfully seeded the database."))

