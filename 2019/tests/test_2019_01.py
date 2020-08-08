from aoc_2019_01 import calculate_fuel_for_mass, calculate_fuel_for_mass_recursive


def test_calculate_fuel_for_mass():
    assert calculate_fuel_for_mass(12) == 2
    assert calculate_fuel_for_mass(14) == 2
    assert calculate_fuel_for_mass(1969) == 654
    assert calculate_fuel_for_mass(100756) == 33583


def test_calculate_fuel_for_mass_part2():
    assert calculate_fuel_for_mass_recursive(14) == 2
    assert calculate_fuel_for_mass_recursive(1969) == 966
    assert calculate_fuel_for_mass_recursive(100756) == 50346
