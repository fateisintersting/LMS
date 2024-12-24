import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse
from .models import ContentInteraction

def generate_time_chart(request, studentid):
    interactions = ContentInteraction.objects.filter(user_id=studentid)
    content_titles = [interaction.content.title for interaction in interactions]
    durations = [interaction.duration() for interaction in interactions if interaction.duration() is not None]

    plt.figure(figsize=(10, 6))
    plt.barh(content_titles, durations, color='skyblue')
    plt.xlabel("Time Spent (minutes)")
    plt.title("Time Spent on Each Content")
    plt.tight_layout()

    # Save to buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the image as base64
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    return image_base64
