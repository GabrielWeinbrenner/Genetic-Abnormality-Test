from recognition import *


classifiers = Classifiers()

classifiers.add('eyes', Classifier('haarcascade_eye.xml', min_neighbors=15, min_size=(15, 15)))


def fonconi_anemia_test(image, do_draw=False):
    """fonconi_anemia_test(image, do_draw=False) -> bool"""

    eyes = classifiers.classify('eyes', image)

    assert len(eyes) == 2

    if eyes[0].position.x < eyes[1].position.x:

        left_eye, right_eye = eyes

    else:

        right_eye, left_eye = eyes

    left_eye.inflate(.88)

    right_eye.inflate(.88)

    gap = left_eye.right.distance(right_eye.left)  # get distance between eyes

    if do_draw:

        Rectangle(Vector2(gap, gap), Vector2(left_eye.right.x, (left_eye.y + right_eye.y) / 2)
                  ).draw(image, BLUE)  # draw gap between eyes

        left_eye.draw(image, RED)  # draw left eye

        right_eye.draw(image, GREEN)  # draw right eye

    min_eye_width = min(left_eye.size.x, right_eye.size.x)  # calculate minimum width of eyes

    return min_eye_width < gap  # if an eye can fit in the gap between your eyes then you have fonconi anemia

