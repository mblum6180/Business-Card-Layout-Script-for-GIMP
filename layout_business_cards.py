import gimpfu as gfu

def layout_business_cards(image, drawable, num_rows, num_cols, spacing):
    # Flatten the image to simplify the layer structure
    flattened = gfu.pdb.gimp_image_flatten(image)

    # Get card dimensions from the flattened image
    card_width = flattened.width
    card_height = flattened.height

    # Calculate the dimensions of the new image based on the number of columns, rows, and spacing
    page_width = num_cols * (card_width + spacing) - spacing
    page_height = num_rows * (card_height + spacing) - spacing

    # Create a new image for the full page layout
    page = gfu.gimp.Image(page_width, page_height, gfu.RGB)
    page.disable_undo()

    # Add a base layer to the new image
    base_layer = gfu.gimp.Layer(page, "Base Layer", page_width, page_height, gfu.RGB_IMAGE, 100, gfu.NORMAL_MODE)
    page.add_layer(base_layer, -1)
    gfu.pdb.gimp_drawable_fill(base_layer, gfu.FILL_WHITE)  # Fill with white for visibility

    # Display the new page in GIMP
    gfu.gimp.Display(page)
    gfu.gimp.displays_flush()

    # Copy the flattened image to reuse it
    gfu.pdb.gimp_edit_copy(flattened)

    # Paste the copies into the new page
    for row in range(num_rows):
        for col in range(num_cols):
            x = col * (card_width + spacing)
            y = row * (card_height + spacing)

            # Paste as a new layer
            floating_sel = gfu.pdb.gimp_edit_paste(base_layer, True)
            floating_sel.set_offsets(x, y)
            new_layer = gfu.pdb.gimp_floating_sel_to_layer(floating_sel)

# Register the script so it appears in GIMP's menus
gfu.register(
    "python_fu_layout_business_cards",
    "Layout Business Cards",
    "Automatically layouts business cards on a custom-sized page",
    "Matthew Blum",
    "Matthew Blum",
    "2024",
    "<Image>/File/Create/Layout Business Cards",
    "*",
    [
        (gfu.PF_INT, "num_rows", "Number of Rows", 5),    # Default value 5 rows
        (gfu.PF_INT, "num_cols", "Number of Columns", 2), # Default value 2 columns
        (gfu.PF_INT, "spacing", "Spacing in Pixels", 0)  # Default value 0 pixels
    ],
    [],
    layout_business_cards)

gfu.main()

