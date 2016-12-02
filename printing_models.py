import printing_functions as p

unprinted = ['iphone','robot','dodecahedron']
completed = []

p.print_models(unprinted[:], completed)

p.show_lists(unprinted, completed, "after by reference")

unprinted = ['iphone','robot','dodecahedron']
completed = []

p.print_models(unprinted, completed)

p.show_lists(unprinted, completed, "after")