from bs4 import BeautifulSoup

with open('home.html', 'r') as code:
    content = code.read()

    soup = BeautifulSoup(content, 'lxml')

    CourseCards = soup.find_all('div', class_='card')

    for course in CourseCards:
        CourseName = course.h5.text
        CoursePrice = course.a.text.split()[2]
        print(f'The name of the course is {CourseName} and it is priced for {CoursePrice}')