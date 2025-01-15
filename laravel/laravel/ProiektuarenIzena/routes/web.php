<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/', 'App\Http\Controllers\Ikaslea@show');

Route::get('/ikaslea/{id}/edit', 'App\Http\Controllers\FormularioaIkasleakGehitu@edit');// Mostrar formulario de edición
Route::put('/ikaslea/{id}', 'App\Http\Controllers\FormularioaIkasleakGehitu@update')->name('ikaslea.update');   // Actualizar registro
Route::delete('/ikaslea/{id}', 'App\Http\Controllers\Ikaslea@destroy'); // Eliminar registro

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');


Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::get('/submit', 'App\Http\Controllers\FormularioaIkasleakGehitu@show');
Route::post('/submit', 'App\Http\Controllers\FormularioaIkasleakGehitu@save');

