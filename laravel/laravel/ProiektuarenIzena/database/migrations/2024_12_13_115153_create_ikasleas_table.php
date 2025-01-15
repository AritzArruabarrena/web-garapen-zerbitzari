<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('ikasleas', function (Blueprint $table) {
            $table->id();
            $table->string('Izena');
            $table->string('Abizena');
            $table->string('Email')->unique();
            $table->string('Telefonoa');
            $table->timestamps();

        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('ikasleas');
    }
};
