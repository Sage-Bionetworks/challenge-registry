import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchViewerModule } from './search-viewer/search-viewer.module';
import { StatisticsViewerModule } from './statistics-viewer/statistics-viewer.module';
import { TopicsViewerModule } from './topics-viewer/topics-viewer.module';

@NgModule({
  imports: [CommonModule],
  declarations: [],
  exports: [SearchViewerModule, StatisticsViewerModule, TopicsViewerModule],
})
export class WebFeatureHomeModule {}
