export interface Assignment {
  id: number;
  start_location: string;
  end_location: string;
  distance: number;
  status: 'pending' | 'in_progress' | 'completed';
  assigned_driver_id: number | null;
}

export interface Driver {
  id: number;
  first_name: string;
  last_name: string;
  current_assignment: number | null;
}
