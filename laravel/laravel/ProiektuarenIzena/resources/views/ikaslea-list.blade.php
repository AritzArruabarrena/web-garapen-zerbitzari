@extends('layouts.app')
@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-10 col-md-offset-1">
            <div class="panel panel-success">
                <div class="panel-heading">Ikasle Lista</div>
                @if(Auth::check())
                <!-- Table -->
                <table class="table">
                    <tr>
                        <th>Izena</th>
                        <th>Abizena</th>
                        <th>Email</th>
                        <th>Telefonoa</th>
                        <th>irakasleak_id</th>
                        <th>Editatu</th>
                        <th>Ezabatu</th>
                    </tr>
                    @foreach($characters as $character)
                    <tr>
                        <td>{{ $character->Izena }}</td>
                        <td>{{ $character->Abizena }}</td>
                        <td>{{ $character->Email }}</td>
                        <td>{{ $character->Telefonoa }}</td>
                        <td>{{ $character->Irakasleak->Izena }}</td>
                        <td><a href="{{ url('/ikaslea/' . $character->id . '/edit') }}" class="btn btn-warning">Editar</a></td>
                        <td><form action="/ikaslea/{{ $character->id }}" method="POST" style="display:inline;">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="btn btn-danger btn-sm" onclick="return confirm('¿Seguro que deseas eliminar este registro?')">Eliminar</button>
                            </form></td>
                    </tr>
                    @endforeach
                </table>
                <a href="/submit" class="btn btn-info"> You need to login to
                add ikaslea>></a> 
                @endif
            </div>
            @if(Auth::guest())
            <a href="/login" class="btn btn-info"> You need to login to
                see the list >></a> 😜😜
            @endif
        </div>
    </div>
</div>
@endsection