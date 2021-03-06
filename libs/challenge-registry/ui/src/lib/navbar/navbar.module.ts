import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { NavbarComponent } from './navbar.component';
import { ButtonGithubModule } from '../button-github/button-github.module';
import { UserButtonModule } from '../user-button/user-button.module';

@NgModule({
  declarations: [NavbarComponent],
  imports: [
    CommonModule,
    RouterModule,
    MatButtonModule,
    ButtonGithubModule,
    UserButtonModule,
  ],
  exports: [NavbarComponent],
})
export class NavbarModule {}
