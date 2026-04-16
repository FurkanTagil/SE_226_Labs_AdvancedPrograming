import geometry_utils as gu

print("Availabe shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter(e.g, circle_area)")

operation = input("Enter the operation you want to perform: ")

functions = {
    "circle_area": gu.circle_area,
    "circle_perimeter": gu.circle_perimeter,
    "rectangle_area": gu.rectangle_area,
    "rectangle_perimeter": gu.rectangle_perimeter,
    "triangle_area": gu.triangle_area
}

if operation not in functions:
    print("invalid operation.")
else:
    if("circle") in operation:
        r = float(input("Enter radius: "))
        result = functions[operation](r)
    elif "rectangle" in operation:
        w = float(input("Enter with: "))
        h = float(input("Enter height: "))
        result = functions[operation](w,h)

    elif "triangle" in operation:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        result = functions[operation](b, h)

    if isinstance(result, str):
        print(result)
    else:
        print("Result:", round(result, 2))