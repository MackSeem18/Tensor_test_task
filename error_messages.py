class ErrorMessages:
    @staticmethod
    def element_is_not_presented(what, where):
        return f'Element {what} is not presented on {where}'

    @staticmethod
    def element_is_not_visible(what, where):
        return f'Element {what} is not visible on {where}'

    @staticmethod
    def cant_click_element(what, where):
        return f'Cant click element {what} on {where}'

    @staticmethod
    def cant_compare_object_locations_and_sizes(what, where):
        return f'Could not compare {what} locations and sizes on {where}.'

    @staticmethod
    def element_parameters_not_match(what, where, expected_result, actual_result):
        return f'{what} on {where} does not match the expected result. ' \
               f'{ErrorMessages.expected_actual_result(expected_result, actual_result)}'

    @staticmethod
    def wrong_url(expected_url, actual_url):
        return f'Wrong page URL, expected: {expected_url}, but got {actual_url}'

    @staticmethod
    def elements_parameters_do_not_match(parameter, first_element, second_element, value1, value2):
        return f'Parameters "{parameter}" do not match: {first_element} = {value1}, {second_element} = {value2}'

    @staticmethod
    def region_does_not_match_expected(where, expected_region, actual_region):
        return f'Incorrect region in {where}. Expected: {expected_region}, Actual: {actual_region}'
