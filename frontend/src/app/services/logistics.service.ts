import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Assignment, Driver } from '../models/models';

const BASE = 'http://localhost:8000/api';

@Injectable({ providedIn: 'root' })
export class LogisticsService {
  constructor(private http: HttpClient) {}

  getAssignments(): Observable<Assignment[]> {
    return this.http.get<Assignment[]>(`${BASE}/assignments/`);
  }

  updateAssignment(id: number, data: Partial<Assignment>): Observable<Assignment> {
    return this.http.put<Assignment>(`${BASE}/assignments/${id}/`, data);
  }

  getDrivers(): Observable<Driver[]> {
    return this.http.get<Driver[]>(`${BASE}/drivers/`);
  }

  updateDriver(id: number, data: Partial<Driver>): Observable<Driver> {
    return this.http.put<Driver>(`${BASE}/drivers/${id}/`, data);
  }
}
