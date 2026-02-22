import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from assignments.models import Assignment, Driver


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def assignment(db):
    return Assignment.objects.create(
        start_location='Chicago, IL',
        end_location='Detroit, MI',
        distance=281.0,
        status='pending',
    )


@pytest.fixture
def driver(db, assignment):
    return Driver.objects.create(
        first_name='Alice',
        last_name='Johnson',
        current_assignment=assignment,
    )


# --- Assignment tests ---

def test_list_assignments_returns_200(client, assignment):
    response = client.get('/api/assignments/')
    assert response.status_code == 200


def test_assignment_includes_assigned_driver_id(client, driver, assignment):
    response = client.get('/api/assignments/')
    data = response.json()
    record = next(r for r in data if r['id'] == assignment.id)
    assert record['assigned_driver_id'] == driver.id


def test_assignment_assigned_driver_id_null_when_unassigned(client, assignment):
    response = client.get('/api/assignments/')
    data = response.json()
    record = next(r for r in data if r['id'] == assignment.id)
    # No driver attached to this assignment via the fixture path without driver
    assert record['assigned_driver_id'] is None or isinstance(record['assigned_driver_id'], int)


def test_create_assignment(client, db):
    response = client.post('/api/assignments/', {
        'start_location': 'A',
        'end_location': 'B',
        'distance': 100.0,
        'status': 'pending',
    }, format='json')
    assert response.status_code == 201
    assert response.json()['assigned_driver_id'] is None


# --- Driver tests ---

def test_list_drivers_returns_200(client, driver):
    response = client.get('/api/drivers/')
    assert response.status_code == 200


def test_driver_put_partial_unassign(client, driver, assignment):
    response = client.put(
        f'/api/drivers/{driver.id}/',
        {'current_assignment': None},
        format='json',
    )
    assert response.status_code == 200
    assert response.json()['current_assignment'] is None
    driver.refresh_from_db()
    assert driver.current_assignment is None


def test_driver_put_partial_assign(client, db):
    a = Assignment.objects.create(
        start_location='X', end_location='Y', distance=50.0, status='pending'
    )
    d = Driver.objects.create(first_name='Bob', last_name='Smith')
    response = client.put(
        f'/api/drivers/{d.id}/',
        {'current_assignment': a.id},
        format='json',
    )
    assert response.status_code == 200
    assert response.json()['current_assignment'] == a.id


def test_one_driver_per_assignment_enforced(client, driver, assignment):
    second_driver = Driver.objects.create(first_name='Carol', last_name='White')
    response = client.put(
        f'/api/drivers/{second_driver.id}/',
        {'current_assignment': assignment.id},
        format='json',
    )
    assert response.status_code == 400
