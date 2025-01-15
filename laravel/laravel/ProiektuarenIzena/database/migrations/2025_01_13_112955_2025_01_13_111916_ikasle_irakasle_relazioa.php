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
        Schema::table('ikasleas', function (Blueprint $table) {
            $table->unsignedBigInteger('irakasleak_id'); // Asegúrate del nombre correcto
            $table->index('irakasleak_id');

            $table->foreign('irakasleak_id') // Llave foránea
                ->references('id')
                ->on('irakasleaks')
                ->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('ikasleas', function (Blueprint $table) {
            if (Schema::hasColumn('ikasleas', 'irakasleak_id')) {
                $table->dropForeign(['irakasleak_id']); // Nombre correcto de la llave foránea
                $table->dropIndex(['irakasleak_id']);  // Elimina el índice
                $table->dropColumn('irakasleak_id');   // Elimina la columna
            }
        });
    }
};
