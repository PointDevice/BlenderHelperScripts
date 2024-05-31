import bpy, re

#This script calculates the optimal eye offset for the avatar based off of arm length
#to my knowledge this uses the same math as the beta ik client
#this can be used to help proporion the height and leg lenth of the avatar
#as this gives you the eye offset from floor of real world space


########USAGE########
#T-pose the avatar in the same way it would be in unity mecanim as that is waht is used in game
#does not have to be the rest pose, as this works off of pose positions
#select the armature in object mode
#Set These Variable Names to somewhat match then names of the bones in the armature used
#This Is Case Sensative
HandBoneName = "hand"
NeckBoneName = "neck"
#click the Run script button
#if relation of neck to arms changes, delete the empty and run script again 
#it may be usefule to add a plane at world origin and then parent it to the empty created by the sctipt
#the z value of the empty location can be used in unity for the eye height of the avatar when done
#it you can get it from the object properties, or as the last value in the system console after running the script

obj = bpy.context.active_object
assert obj.type == "ARMATURE"
assert bpy.context.mode == 'OBJECT'

arm = obj.data
bpy.ops.object.mode_set(mode='POSE')
bpy.ops.pose.select_all(action='DESELECT')

for bonee in obj.pose.bones:
    if HandBoneName in bonee.name:
        bonee.bone.select = True
        WristLoc = bonee.head
    if NeckBoneName in bonee.name:
        bonee.bone.select = True
        NeckLoc = bonee.head
    bpy.ops.pose.select_all(action='DESELECT')

DistenceWristNeck = (NeckLoc - WristLoc).length

bpy.ops.object.mode_set(mode='OBJECT')

ViewPos = bpy.data.objects.new( "empty_ViewPos", None )
bpy.context.scene.collection.objects.link( ViewPos )
ViewPos.empty_draw_size = 2
ViewPos.empty_draw_type = 'PLAIN_AXES'
ViewPos.location.z = (DistenceWristNeck / .415)

print( "eye Height:" )
print( DistenceWristNeck / .415 )

