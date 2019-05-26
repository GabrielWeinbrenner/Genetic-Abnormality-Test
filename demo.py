from genetic_tests import load_image, fonconi_anemia_test, show, end, is_pressed, get_image


def run_test():

    image = get_image()

    try:

        results = fonconi_anemia_test(image, True)

        show(image)

        if results:

            print('You may suffer from Foconi Anemia :(')

        else:

            print('You are fine :)')

        while not is_pressed('q'):

            pass

    except AssertionError:

        print('Invalid image. \nTrying again...')

        run_test()

    finally:

        end()


run_test()
