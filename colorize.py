import os

colors = {
    "white": "#FFFFFF",
    "black": "#000000",
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "gray": "#808080",
    "lightgray": "#D3D3D3",
    "darkgray": "#A9A9A9",
    "orange": "#FFA500",
    "purple": "#800080",
    "pink": "#FFC0CB",
    "brown": "#A52A2A",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "navy": "#000080",
    "teal": "#008080",
    "lime": "#00FF00",
    "indigo": "#4B0082",
    "violet": "#EE82EE",
    "beige": "#F5F5DC",
    "maroon": "#800000",
    "olive": "#808000",
}


def create_colors():
    prepare_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in prepare_colors:
        hexa_color = colors[color]
        if not os.path.exists(f"icons_{color}"):
            os.mkdir(f"icons_{color}")
        for root, dirs, files in os.walk("icons"):
            for file in files:
                with open("icons/" + file, "r") as f:
                    content = f.read()
                    content = content.replace(colors["black"], hexa_color)
                    with open(f"icons_{color}/{file}", "w") as f2:
                        f2.write(content)


if __name__ == "__main__":
    create_colors()
