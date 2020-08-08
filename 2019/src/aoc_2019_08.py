# AoC 2019 Day 8

from typing import List, Dict

YEAR = 2019
DAY = 8
WIDE = 25
TALL = 6

# Part 1
def validate_image(image: str, wide: int, tall: int) -> int:
    layer_count: Dict[int, int] = {}
    layers = create_image_layers(image, tall, wide)
    for layer in range(len(layers)):
        counter = 0
        for i in layers[layer]:
            if i == "0":
                counter += 1
        layer_count[layer] = counter
    min_count = 999999
    smallest_layer = 0
    for layer in layer_count:
        if layer_count[layer] < min_count:
            min_count = layer_count[layer]
            smallest_layer = layer
    one_count = 0
    two_count = 0
    for i in layers[smallest_layer]:
        if i == "1":
            one_count += 1
        elif i == "2":
            two_count += 1
    return one_count * two_count


# Part 2
def derive_visible_layer(layers, wide: int, tall: int):
    visible_layer: List[str] = ["" for _ in range(wide * tall)]
    for layer in layers:
        for key, pixel in enumerate(layer):
            if visible_layer[key] == "" and pixel in ("1", "0"):
                if pixel == "0":
                    visible_layer[key] = "     "
                else:
                    assert pixel == "1"
                    visible_layer[key] = "@@@@@"
    return visible_layer


# Part 2
def render_image(visible_layer: List[str], wide: int, tall: int) -> None:
    for i in range(len(visible_layer) // tall):
        print(*visible_layer[(i - 1) * wide : i * wide], sep="")


# Part 2
def create_image_layers(image: str, wide: int, tall: int) -> List[str]:
    layers: List[str] = []
    layers_in_image = int((len(image)) / (wide * tall))
    for i in range(layers_in_image):
        layer = image[i * wide * tall : (i + 1) * wide * tall]
        layers.append(layer)
    return layers


def main():
    data = open(f"input_data/input_{YEAR}_{DAY:02d}.txt", "r").readlines()
    image = data[0]
    print(validate_image(image, WIDE, TALL), "is the answer to part 1")
    layers = create_image_layers(image, WIDE, TALL)
    visible_layer = derive_visible_layer(layers, WIDE, TALL)
    render_image(visible_layer, WIDE, TALL)


if __name__ == "__main__":
    main()
