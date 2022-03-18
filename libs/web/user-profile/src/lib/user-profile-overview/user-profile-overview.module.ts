import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WebUiModule } from '@challenge-registry/web/ui';
import { UserProfileOverviewComponent } from './user-profile-overview.component';

@NgModule({
  declarations: [UserProfileOverviewComponent],
  imports: [CommonModule, WebUiModule],
  exports: [UserProfileOverviewComponent],
})
export class UserProfileOverviewModule {}
