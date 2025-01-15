<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Ikaslea;
use App\Models\Irakasleak;

class FormularioaIkasleakGehitu extends Controller
{
    // Mostrar formulario para crear un nuevo Ikaslea
    public function show()
    {
        // Obtener todos los Irakasleak para pasarlos a la vista
        $irakasleaks = Irakasleak::all();
        return view('FormularioaIkasleakBista', compact('irakasleaks'));
    }

    // Guardar un nuevo Ikaslea
    public function save(Request $request)
    {
        // Validar los datos del formulario
        $data = $request->validate([
            'izena' => 'required|max:255',
            'abizena' => 'required|max:255',
            'email' => 'required|max:255|email|unique:ikasleas,email',
            'telefonoa' => 'required|numeric',
            'irakasleak_id' => 'required|exists:irakasleaks,id', // Validar que el irakasleak_id sea válido
        ]);

        // Crear un nuevo Ikaslea con los datos validados
        $character = new Ikaslea($data);
        $character->save();

        // Redirigir al índice con un mensaje de éxito
        return redirect('/')->with('success', 'Ikaslea creado correctamente.');
    }

    // Mostrar formulario para editar un Ikaslea
    public function edit($id)
    {
        // Obtener el Ikaslea por su ID
        $character = Ikaslea::findOrFail($id);
        
        // Obtener todos los Irakasleak para el select
        $irakasleaks = Irakasleak::all();
        
        // Pasar el Ikaslea y los Irakasleak a la vista
        return view('FormularioaIkasleakBista', compact('character', 'irakasleaks'));
    }

    // Actualizar un Ikaslea
    public function update(Request $request, $id)
    {
        // Validar los datos del formulario
        $data = $request->validate([
            'izena' => 'required|max:255',
            'abizena' => 'required|max:255',
            'email' => 'required|max:255|email|unique:ikasleas,email,' . $id, // Permitir el email actual
            'telefonoa' => 'required|numeric',
            'irakasleak_id' => 'required|exists:irakasleaks,id', // Validar que el irakasleak_id sea válido
        ]);

        // Buscar y actualizar el Ikaslea
        $character = Ikaslea::findOrFail($id);
        $character->update($data);

        // Redirigir al índice con un mensaje de éxito
        return redirect('/')->with('success', 'Ikaslea actualizado correctamente.');
    }
}
