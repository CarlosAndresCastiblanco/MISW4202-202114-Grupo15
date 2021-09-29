import { Component, OnInit } from '@angular/core';
import { ClinicaService } from '../_services/clinica-service/clinica.service';

@Component({
  selector: 'app-historia-clinica',
  templateUrl: './historia-clinica.component.html',
  styleUrls: ['./historia-clinica.component.scss']
})
export class HistoriaClinicaComponent {

  loading = false;
  constructor(
    private clinicaService: ClinicaService
  ) { }



  editarHistoriaClinica(): void {

    this.loading = true;
    this.clinicaService.editarHistoriaClinica()
      .subscribe(
        (data: any) => {
          alert('Usuario puede modificar la historia clínica');
        },
        (error: any) => {
          alert('Usuario NO puede modificar la historia clínica');
          this.loading = false;
        });

  }

}
