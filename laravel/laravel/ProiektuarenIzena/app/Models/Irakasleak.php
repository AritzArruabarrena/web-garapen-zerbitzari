<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Irakasleak extends Model
{
    /** @use HasFactory<\Database\Factories\IrakasleakFactory> */
    use HasFactory;

    protected $fillable = [
        'id',
        'izena',
        'abizena',
        'email',
    ];
}
