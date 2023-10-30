from paint_mass_gen import *
from paint_addons import *
from new_funk import *
import random
# os.system('resize -s 25 40' )
mass = []
mass = mass_gen_custom(5,5,' ')
paint_rectangle_nofill(5, 5, '#', 1, 1, mass)
# paint_rectangle(2, 1, '/', 2, 2, mass)
# paint_rectangle(1, 1, "/", 4, 4, mass)
paint_rectangle(1, 2, '#', 4, 2, mass)

xy = sokoban_game(2, 4, '^',mass,'*','#',[2,3,3,3,3,4],[2,2,3,2,4,4])

