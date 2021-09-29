import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [{ path: '', loadChildren: () => import('./inicio-sesion/inicio-sesion.module').then(m => m.InicioSesionModule) }, { path: 'historiaClinica', loadChildren: () => import('./historia-clinica/historia-clinica.module').then(m => m.HistoriaClinicaModule) }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
