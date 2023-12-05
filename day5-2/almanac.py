from __future__ import annotations
from dataclasses import dataclass

def split_ranges(range_min, range_max, source_min, source_max):
    range_a = (range_min, max(source_min, range_min) - 1)
    intersection = (max(source_min, range_min), min(source_max, range_max))
    range_b = (min(source_max, range_max) + 1, range_max)
    return range_a, intersection, range_b

@dataclass
class TranslationMap:
    entries: list[tuple[int, int, int]]

    def get(self, index:int):
        for entry in self.entries:
            destination = entry[0]
            source = entry[1]
            length = entry[2]
            if index >= source and index <= source + length - 1:
                return destination + (index-source)
        return index
    
    def translate_ranges(self, ranges: list[tuple(int, int)]) -> list[tuple(int, int)]:
        new_ranges  = []
        ranges_to_translate = ranges.copy()
        while ranges_to_translate:
            range_to_translate = ranges_to_translate.pop()
            range_min = range_to_translate[0]
            range_length = range_to_translate[1]
            range_max = range_min + range_length-1
            found_translation = False
            for entry in self.entries:
                destination = entry[0]
                source_min = entry[1]
                length = entry[2]
                source_max = source_min+length - 1
                range_a, intersection, range_b = split_ranges(range_min, range_max, source_min, source_max)
                if intersection[0] <= intersection[1]:
                    if range_a[0] <= range_a[1]:
                        ranges_to_translate.append((range_a[0], range_a[1] - range_a[0] + 1))
                    if range_b[0] <= range_b[1]:
                        ranges_to_translate.append((range_b[0], range_b[1] - range_b[0] + 1))
                    new_ranges.append((intersection[0] + (destination-source_min), intersection[1] - intersection[0] + 1))
                    found_translation = True
                    break
            if not found_translation:
                new_ranges.append(range_to_translate)
        return new_ranges

with open("input_given.txt") as f:
    input = f.read()

lines = input.splitlines()
initial_seed_numbers = list(map(int, lines[0].split(":")[1].strip().split()))

initial_seeds: list[tuple(int, int)] = []
for i in range(0, len(initial_seed_numbers), 2):
    initial_seeds.append((initial_seed_numbers[i], initial_seed_numbers[i+1]))

def create_translation_map(start_line_index: int) -> tuple(dict[int, int], int):
    next_map_start = 0
    entries = []
    for line_no, line in enumerate(lines[start_line_index:]):
        numbers = list(map(int, line.split()))
        if len(numbers) != 3:
            next_map_start = line_no + start_line_index + 2
            break
        entries.append(tuple(numbers))
    return TranslationMap(entries=entries), next_map_start

seed_to_soil_map, soil_to_fertilizer_start = create_translation_map(3)
soil_to_fertilizer_map, fertilizer_to_water_start = create_translation_map(soil_to_fertilizer_start)
fertilizer_to_water_map, water_to_light_start = create_translation_map(fertilizer_to_water_start)
water_to_light_map, light_to_temp_start = create_translation_map(water_to_light_start)
light_to_temp_map, temp_to_hum_start = create_translation_map(light_to_temp_start)
temp_to_hum_map, hum_to_loc_start = create_translation_map(temp_to_hum_start)
hum_to_loc_map, _ = create_translation_map(hum_to_loc_start)

def seed_to_loc_ranges(seed_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    soil_ranges = seed_to_soil_map.translate_ranges(seed_ranges)
    fertilizer_ranges = soil_to_fertilizer_map.translate_ranges(soil_ranges)
    water_ranges = fertilizer_to_water_map.translate_ranges(fertilizer_ranges)
    light_ranges = water_to_light_map.translate_ranges(water_ranges)
    temp_ranges = light_to_temp_map.translate_ranges(light_ranges)
    hum_ranges = temp_to_hum_map.translate_ranges(temp_ranges)
    return hum_to_loc_map.translate_ranges(hum_ranges)

loc_ranges = seed_to_loc_ranges(initial_seeds)
print(min(map(lambda x: x[0], loc_ranges)))