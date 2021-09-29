import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ClinicaService {



  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    return this.http.post<any>(`${environment.apiUrl}/authenticate`, { username, password });
  }

  editarHistoriaClinica() {
    return this.http.post<any>(`${environment.apiUrl}/editHC`, {});
  }
}
