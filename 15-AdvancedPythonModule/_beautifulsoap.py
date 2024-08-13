html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id ="header">
        Python Kursu
    </h1>
    <div>
        <h2 class = "grup 1">
            programlar
        </h2>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>
    </div>
    <div>
        <h2 class = "grup 2">
            modüller
        </h2>
        <ul>
            <li>Menu1</li>
            <li>Menu2</li>
            <li>Menu3</li>
        </ul>
    </div>
    <img src="fred.jpg" alt="">
    
    <a class= "sister" href = "//example1.com/elsie" id= "link 1">Elsie</a>
    <a class= "sister" href = "//example2.com/elsie" id= "link 2">Elsie</a>
    <a class= "sister" href = "//example3.com/elsie" id= "link 3">Elsie</a>
    
    
</body>
</html>
"""
from bs4 import BeautifulSoup