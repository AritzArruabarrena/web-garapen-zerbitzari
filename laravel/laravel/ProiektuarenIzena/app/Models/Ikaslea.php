<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Ikaslea extends Model
{
    /** @use HasFactory<\Database\Factories\IkasleaFactory> */
    use HasFactory;

    protected $fillable = [
        'izena',
        'abizena',
        'email',
        'telefonoa',
        'irakasleak_id',
    ];

    public function irakasleak()
    {
        return $this->belongsTo(Irakasleak::class, 'irakasleak_id');
    }
}
