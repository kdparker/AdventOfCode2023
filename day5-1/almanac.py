from __future__ import annotations
from dataclasses import dataclass

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

with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
initial_seeds = list(map(int, lines[0].split(":")[1].strip().split()))

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

def seed_to_loc(seed:int):
    soil = seed_to_soil_map.get(seed)
    fertilizer = soil_to_fertilizer_map.get(soil)
    water = fertilizer_to_water_map.get(fertilizer)
    light = water_to_light_map.get(water)
    temp = light_to_temp_map.get(light)
    hum = temp_to_hum_map.get(temp)
    return hum_to_loc_map.get(hum)

lowest_loc = seed_to_loc(initial_seeds[0])
for seed in initial_seeds[1:]:
    lowest_loc = min(lowest_loc, seed_to_loc(seed))
print(lowest_loc)