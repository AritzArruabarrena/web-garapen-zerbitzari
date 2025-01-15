<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ikaslea extends Controller
{
    public function show()
    {
        $characters = \App\Models\Ikaslea::all();
        return view('ikaslea-list', ['characters' => $characters]);
    }

    public function showFiltered(Request $request)
    {
        $query = \App\Models\Ikaslea::where('Izena', $request->query('Izena'));
        $characters = $query->get();
        return view('ikaslea-list', ['characters' => $characters]);
    }

 
    public function destroy($id)
    {
        $character = \App\Models\Ikaslea::findOrFail($id);
        $character->delete();
        return redirect('/')->with('success', 'Registro eliminado con éxito.');
    }

}
