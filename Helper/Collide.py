def collide(
    hit_box1: tuple[float, float, float, float], hit_box2: tuple[int, int, int, int]
):
    return (
        hit_box1[0] >= hit_box2[0]
        and hit_box1[1] >= hit_box2[1]
        and hit_box1[2] <= hit_box2[2]
        and hit_box1[3] <= hit_box2[3]
    )
