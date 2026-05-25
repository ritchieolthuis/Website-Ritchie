from PIL import Image

try:
    img = Image.open('assets/axelio.png').convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        # Check if pixel is dark (almost black) and somewhat opaque
        if item[3] > 0 and item[0] < 50 and item[1] < 50 and item[2] < 50:
            new_data.append((255, 255, 255, item[3])) # Make it white
        else:
            new_data.append(item) # Keep original color

    img.putdata(new_data)
    img.save('assets/axelio_white_text.png')
    print("Successfully created axelio_white_text.png")
except Exception as e:
    print(f"Error: {e}")
