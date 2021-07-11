
def logic(src_point,dest_point,distance):
    x1,y1 = src_point
    x2,y2 = dest_point
    current_dist = ((x1-x2)**2 + (y1-y2)**2 )**0.5
    if current_dist <= distance:
        return True
    else:
        return False
    

def nearby(points_list,dest,distance):
    points_list = points_list[1:]
    atleast = 0

    for i in range(len(points_list)):
        src_point = (points_list[i][1]+220,points_list[i][2]+175)
        dest_point = (dest[i][0],dest[i][1])
        #print(src_point, dest_point)
        if logic(src_point,dest_point,distance):
            #print("logic running")
            atleast += 1

    if atleast >= 4:
        return True
    else:
        return False
    
