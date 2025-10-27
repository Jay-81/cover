# Ex.06 Book Front Cover Page Design
## Date: 27-10-25

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:
book.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Book Cover - Whispers of the Mind</title>
<style>

  body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #1f1c2c, #928dab, #1f4037, #99f2c8);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .book {
    width: 320px;
    height: 480px;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    overflow: hidden;
    position: relative;
    color: #f0f0f0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 20px;
  }
  .title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 10px;
    color: #ffd166;
  }
  .tagline {
    font-size: 14px;
    margin-top: 14px;
    color: #ffe8a1;
  }
  .author-info {
    position: absolute;
    bottom: 20px;
    right: 20px;
    text-align: right;
  }
  .author-pic {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    border: 2px solid #ffd166;
    display: block;
    margin-bottom: 6px;
  }
  .author {
    font-size: 14px;
    font-style: italic;
    color: #ffe8a1;
  }
  .footer {
    position: absolute;
    bottom: 12px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 12px;
    color: #ffd166;
    letter-spacing: 1px;
  }
</style>
</head>
<body>
<div class="book">
  <h1 class="title">Whispers of the Mind</h1>
  <p class="tagline">“A quiet storm of thoughts untold.”</p>
  <div class="author-info">
    <img src="{% static 'jai profile.jpg' %}" alt="Author Photo" class="author-pic">
    <p class="author">by Jayani K</p>
  </div>
  <div class="footer">The Modern Tales Collection</div>
</div>
</body>
</html>

```
urls.py
```

from django.contrib import admin
from django.urls import path
from bookapp.views import book_cover

urlpatterns = [
    path('', book_cover, name='book-cover'),
    path('admin/', admin.site.urls),
    path('book/', book_cover),
]


```
views.py
```
from django.shortcuts import render

def book_cover(request):
    return render(request, "book.html")

```
## OUTPUT:
![alt text](<Screenshot (113).png>)

## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
