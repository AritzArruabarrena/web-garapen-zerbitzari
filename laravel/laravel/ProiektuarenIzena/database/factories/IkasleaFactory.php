<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Ikaslea>
 */
class IkasleaFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        $irakasleak = \App\Models\Irakasleak::pluck('id')->toArray();
        return [
            'izena' => $this->faker->firstName(),
            'abizena' => $this->faker->lastName(),
            'email' => $this->faker->unique()->safeEmail(),
            'telefonoa' => $this->faker->numerify('##########'),
            'irakasleak_id' => $this->faker->randomElement($irakasleak),
        ];
    }
}
