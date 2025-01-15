@extends('layouts.app')
@section('content')
<div class="container">
    <div class="row">
        <h1>Submit a Character</h1>
        <form action="/submit" method="post">
            @if ($errors->any())
            <div class="alert alert-danger" role="alert">
                Please fix the following errors
            </div>
            @endif
            {!! csrf_field() !!}
            <div class="form-group{{ $errors->has('Izena') ? ' has-error' :
'' }}">
                <label for="Izena">Ikasle Izena</label>
                <input type="text" class="form-control" id="Izena"
                    name="Izena" placeholder="Izena"
                    value="{{ old('Izena') }}">
                @if($errors->has('Izena'))
                <span class="help-block">{{ $errors->first('Izena') }}
                </span>
                @endif
            </div>
            <div class="form-group{{ $errors->has('Abizena') ? ' has-error' :
'' }}">
                <label for="Abizena">Abizena</label>
                <input type="text" class="form-control" id="Abizena"
                    name="Abizena" placeholder="Abizena"
                    value="{{ old('Abizena') }}">
                @if($errors->has('Abizena'))
                <span class="help-block">{{ $errors->first('Abizena') }}
                </span>
                @endif
            </div>
            <div class="form-group{{ $errors->has('Email') ? ' haserror' : '' }}">
                <label for="Email">Email</label>
                <textarea class="form-control" id="Email"
                    name="Email"
                    placeholder="Email">{{ old('Email')
}}</textarea>
                @if($errors->has('Email'))
                <span class="help-block">{{ $errors->first('Email') }}</span>
                @endif
            </div>
            <div class="form-group{{ $errors->has('Telefonoa') ? ' haserror' : '' }}">
                <label for="Telefonoa">Telefonoa</label>
                <textarea class="form-control" id="Telefonoa"
                    name="Telefonoa"
                    placeholder="Telefonoa">{{ old('Telefonoa')
}}</textarea>
                @if($errors->has('Telefonoa'))
                <span class="help-block">{{ $errors->first('Telefonoa') }}</span>
                @endif
            </div>
            <div class="form-group{{ $errors->has('irakasleak_id') ? ' has-error' : '' }}">
                <label for="irakasleak_id">{{ __('messages.irakasleak') }}</label>
                <select class="form-control" id="irakasleak_id" name="irakasleak_id">
                    <option value="">{{ __('messages.select_irakasleak') }}</option>
                    @foreach($irakasleaks as $irakasleak)
                    <option value="{{ $irakasleak->id }}"
                        {{ old('irakasleak_id', isset($character) ? $character->irakasleak_id : '') == $irakasleak->id ? 'selected' : '' }}>
                        {{ $irakasleak->izena }} {{ $irakasleak->abizena }}
                    </option>
                    @endforeach
                </select>
                @if($errors->has('irakasleak_id'))
                <span class="help-block">{{ $errors->first('irakasleak_id') }}</span>
                @endif
            </div>

            <button type="submit" class="btn btn-default">Submit</button>
        </form>
    </div>
</div>
@endsection