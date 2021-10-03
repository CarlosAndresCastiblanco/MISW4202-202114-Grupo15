import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ClinicaService {



  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    return this.http.post<any>(`${environment.apiUrl}/login`, { nombre: username, contrasena: password });
  }

  editarHistoriaClinica() {
    return this.http.post<any>(`${environment.apiUrl}/service`, {}, {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + window.localStorage.getItem('token')
      })
    });
  }
}
