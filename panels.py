# Gets the maximum number of rectangles a * b that can fit horizontally in a rectangle x * y
def max_rectangles_horizontal(a: int, b: int, x: int, y: int) -> int:
    return (x // a) * (y // b)

# Gets the maximum number of rectangles a * b that can fit vertically in a rectangle x * y
def max_rectangles_vertical(a: int, b: int, x: int, y: int) -> int:
    return (x // b) * (y // a)

# Gets the maximum number of panels that can fit in the roof horizontally, using the remaining space available
def get_full_horizontal_fit(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    horizontal_fit = max_rectangles_horizontal(panel_width, panel_height, roof_width, roof_height)
    remaining_width = roof_width % panel_width
    remaining_fit_horizontal = max_rectangles_vertical(panel_width, panel_height, remaining_width, roof_height)
    return horizontal_fit + remaining_fit_horizontal

# Gets the maximum number of panels that can fit in the roof vertically, using the remaining space available
def get_full_vertical_fit(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    vertical_fit = max_rectangles_vertical(panel_width, panel_height, roof_width, roof_height)
    remaining_height = roof_height % panel_height
    remaining_fit_vertical = max_rectangles_horizontal(panel_width, panel_height, roof_width, remaining_height)
    return vertical_fit + remaining_fit_vertical

# Gets the max number of panels that can fit in the roof
def get_max_panels_in_roof(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    # Set the width of the roof and panels as the larger value to simplify code
    real_roof_width = max(roof_height, roof_width)
    real_roof_height = min(roof_height, roof_width)
    real_panel_width = max(panel_height, panel_width)
    real_panel_height = min(panel_height, panel_width)

    panels_in_horizontal_fit = get_full_horizontal_fit(real_panel_width, real_panel_height, real_roof_width, real_roof_height)
    panels_in_vertical_fit = get_full_vertical_fit(real_panel_width, real_panel_height, real_roof_width, real_roof_height)

    return max(panels_in_horizontal_fit, panels_in_vertical_fit)

if __name__ == "__main__":
    # Test cases: (panel_width, panel_height, roof_width, roof_height), result
    test_cases = [[(1, 2, 3, 5), 7], [(1, 2, 2, 4), 4],  [(2, 2, 1, 10), 0]]
    for test_case, expected_result in test_cases:
        result = get_max_panels_in_roof(*test_case)
        assert result == expected_result
        print(f"Test passed: {test_case} -> {result}")