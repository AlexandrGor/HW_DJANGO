import pytest
from students.models import Course, Student
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory (*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory (*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):
    #Arrange
    students = student_factory(_quantity=10)
    course = course_factory(students=students)
    #Act
    response = client.get('/courses/'+str(course.id)+'/')
    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course.name
    assert len(data['students']) == course.students.count()

@pytest.mark.django_db
def test_get_courses(client, course_factory, student_factory):
    #Arrange
    students = student_factory(_quantity=10)
    courses = course_factory(_quantity=10, students=students)
    #Act
    response = client.get('/courses/')
    #Assert
    assert response.status_code == 200
    data = response.json()
    for i,m in enumerate(data):
        assert m['name'] == courses[i].name
        assert len(m['students']) == courses[i].students.count()
@pytest.mark.django_db
def test_get_filtered_by_id_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=10)
    #Act
    response = client.get('/courses/?id='+str(courses[3].id))
    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[3].name

@pytest.mark.django_db
def test_get_filtered_by_name_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=10)
    #Act
    response = client.get('/courses/?name='+str(courses[3].name))
    #Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[3].name

@pytest.mark.django_db
def test_create_course(client):
    #Arrange
    Student.objects.create(id = 1, name = 'Alex')
    count = Course.objects.count()
    #Act
    response = client.post('/courses/', data = {'name': 'Python', 'students': [1]})
    #Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    # Arrange
    students = student_factory(_quantity=10)
    course = course_factory()
    # Act
    response = client.patch('/courses/' + str(course.id) + '/', data = {'name': 'TEST'})
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'TEST'

@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    # Arrange
    students = student_factory(_quantity=10)
    course = course_factory()
    count = Course.objects.count()
    # Act
    response = client.delete('/courses/'+str(course.id)+'/')
    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1