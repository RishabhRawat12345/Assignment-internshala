// src/app/app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component'; // make sure this path is correct

@NgModule({
  imports: [BrowserModule, AppComponent], 
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
