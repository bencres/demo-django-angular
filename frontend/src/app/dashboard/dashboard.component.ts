import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Observable, of } from 'rxjs';
import { switchMap } from 'rxjs/operators';

import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatChipsModule } from '@angular/material/chips';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { LogisticsService } from '../services/logistics.service';
import { Assignment, Driver } from '../models/models';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatSelectModule,
    MatFormFieldModule,
    MatChipsModule,
    MatProgressSpinnerModule,
  ],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnInit {
  assignments: Assignment[] = [];
  drivers: Driver[] = [];
  loading = true;

  displayedColumns = ['id', 'start_location', 'end_location', 'distance', 'status', 'driver'];

  constructor(private svc: LogisticsService) {}

  ngOnInit(): void {
    this.svc.getAssignments().subscribe(a => {
      this.assignments = a;
      this.svc.getDrivers().subscribe(d => {
        this.drivers = d;
        this.loading = false;
      });
    });
  }

  onDriverSelected(assignmentId: number, newDriverId: number | null): void {
    const assignment = this.assignments.find(a => a.id === assignmentId)!;
    const oldDriverId = assignment.assigned_driver_id;

    if (oldDriverId === newDriverId) return;

    const unassignOld$: Observable<Driver | null> = oldDriverId
      ? this.svc.updateDriver(oldDriverId, { current_assignment: null })
      : of(null);

    unassignOld$.pipe(
      switchMap((): Observable<Driver | null> => newDriverId
        ? this.svc.updateDriver(newDriverId, { current_assignment: assignmentId })
        : of(null))
    ).subscribe(() => {
      if (oldDriverId) {
        const old = this.drivers.find(d => d.id === oldDriverId);
        if (old) old.current_assignment = null;
      }
      if (newDriverId) {
        const nw = this.drivers.find(d => d.id === newDriverId);
        if (nw) nw.current_assignment = assignmentId;
      }
      assignment.assigned_driver_id = newDriverId;
    });
  }

  statusLabel(status: string): string {
    const map: Record<string, string> = {
      pending: 'Pending',
      in_progress: 'In Progress',
      completed: 'Completed',
    };
    return map[status] ?? status;
  }
}
