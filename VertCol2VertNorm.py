import bpy
from mathutils import Vector

current_obj = bpy.context.active_object 
mesh = current_obj.data

normals = []
vcol_data = mesh.vertex_colors.active.data
vert_loop_map = {}

mesh.normals_split_custom_set([(0, 0, 0) for l in mesh.loops])

for l in mesh.loops:
    try:
        vert_loop_map[l.vertex_index].append(l.index)
    except KeyError:
        vert_loop_map[l.vertex_index] = [l.index]

for vertex_index in vert_loop_map:
    Tcolor = Vector()
    Tnormal = []
    print(vertex_index)
    for loop_index in vert_loop_map[vertex_index]:
        #TODO: add user selection for swizzle rather than hardcode
        Tcolor[0] = (( pow(vcol_data[loop_index].color[0], 2.2) * 2)-1)
        Tcolor[1] = -(( pow(vcol_data[loop_index].color[1], 2.2) * 2)-1)
        Tcolor[2] = (( pow(vcol_data[loop_index].color[2], 2.2) * 2)-1)
        print(Tcolor.normalized())

    normals.append( Tcolor.normalized() )

mesh.normals_split_custom_set_from_vertices(normals)
mesh.update()
