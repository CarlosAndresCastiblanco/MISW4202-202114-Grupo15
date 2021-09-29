import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClinicaService } from '../_services/clinica-service/clinica.service';

@Component({
  selector: 'app-inicio-sesion',
  templateUrl: './inicio-sesion.component.html',
  styleUrls: ['./inicio-sesion.component.scss']
})
export class InicioSesionComponent {
  loginForm: FormGroup;
  loading = false;
  submitted = false;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private clinicaService: ClinicaService
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  get f() { return this.loginForm.controls; }

  onSubmit() {
    this.submitted = true;

    this.router.navigate(['/historiaClinica']);
    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;
    this.clinicaService.login(this.f.username.value, this.f.password.value)
      .subscribe(
        (data: any) => {
          this.router.navigate(['/historiaClinica']);
        },
        (error: any) => {
          this.loading = false;
        });
  }
}
